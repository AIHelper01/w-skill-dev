#!/usr/bin/env python3
"""Heuristic PPT source-text coverage and DOCX bold check.

Run: python check_source_coverage.py --pptx input.pptx --docx output.docx --json report.json
Requires python-pptx, python-docx. Does not inspect text embedded in images.
"""
import argparse
import json
import re
from pathlib import Path


def norm(s):
    return ' '.join(re.sub(r'\s+', ' ', s).split()).casefold().strip()


def source_fragments(shape, group_shape_type):
    out = []
    if shape.shape_type == group_shape_type:
        for sub in shape.shapes:
            out.extend(source_fragments(sub, group_shape_type))
    if shape.has_text_frame:
        out.extend(p.text.strip() for p in shape.text_frame.paragraphs if p.text.strip())
    if shape.has_table:
        for row in shape.table.rows:
            for cell in row.cells:
                out.extend(p.text.strip() for p in cell.text_frame.paragraphs if p.text.strip())
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pptx',required=True)
    ap.add_argument('--docx',required=True)
    ap.add_argument('--json')
    args=ap.parse_args()
    try:
        from pptx import Presentation
        from pptx.enum.shapes import MSO_SHAPE_TYPE
        from docx import Document
    except ModuleNotFoundError as exc:
        ap.error(
            f"missing Python package '{exc.name}'. Run this script in the document "
            "artifact environment with python-pptx and python-docx available."
        )
    ppt=Presentation(args.pptx)
    doc=Document(args.docx)
    # Only inspect the matching slide section, never unrelated slides.
    sections = {}
    current = None
    duplicates = []
    for para in doc.paragraphs:
        m = re.match(r'^\s*Slide\s+(\d+)\s*[-—–:]', para.text, re.I)
        if m:
            current = int(m.group(1))
            if current in sections:
                duplicates.append(current)
            sections.setdefault(current, [])
        if current is not None:
            sections[current].append(para)
    slides=[]
    for i,slide in enumerate(ppt.slides,1):
        paras = sections.get(i, [])
        all_text = norm(' '.join(p.text for p in paras))
        # Insert boundaries at non-bold text to prevent artificial matches.
        bold_text = norm(' '.join(''.join(r.text if r.bold else ' | ' for r in p.runs) for p in paras))
        images = sum(len(p._p.xpath('.//a:blip')) for p in paras)
        items=[]
        for shape in slide.shapes:
            items.extend(source_fragments(shape, MSO_SHAPE_TYPE.GROUP))
        checks=[]
        for s in items:
            n=norm(s)
            if not n: continue
            present=n in all_text
            in_bold=n in bold_text
            checks.append({'source':s, 'present_exact':present,'bold_exact':in_bold})
        slides.append({'slide':i, 'section_found':bool(paras), 'embedded_image_count':images,
                       'source_items':len(checks),'missing_exact':[c for c in checks if not c['present_exact']],
                       'not_bold_exact':[c for c in checks if not c['bold_exact']]})
    report={'pptx':Path(args.pptx).name, 'docx':Path(args.docx).name,'slides':slides, 'duplicate_sections':duplicates, 'unexpected_sections':sorted(set(sections)-set(range(1,len(ppt.slides)+1))),
            'summary':{'slides':len(slides), 'missing_sections':sum(not x['section_found'] for x in slides), 'sections_without_images':sum(x['embedded_image_count']==0 for x in slides),'source_items':sum(x['source_items'] for x in slides),
                       'missing_exact':sum(len(x['missing_exact']) for x in slides),
                       'not_bold_exact':sum(len(x['not_bold_exact']) for x in slides)}}
    print(json.dumps(report['summary'], indent=2))
    print('NOTE: Slide-local heuristic: inspect all misses and intentional exceptions manually (inactive repeated contents, code formatting, title runs, etc.). Does not prove semantic order, verify image identity, resolve inherited bold, or parse image text.')
    if args.json:Path(args.json).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__':main()
