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
    paras=[(norm(p.text), any(bool(r.bold) and r.text.strip() for r in p.runs)) for p in doc.paragraphs]
    all_text=' '.join(x for x,_ in paras)
    bold_text=' '.join(norm(r.text) for p in doc.paragraphs for r in p.runs if r.bold and r.text.strip())
    slides=[]
    for i,slide in enumerate(ppt.slides,1):
        items=[]
        for shape in slide.shapes:
            items.extend(source_fragments(shape, MSO_SHAPE_TYPE.GROUP))
        checks=[]
        for s in items:
            n=norm(s)
            if not n:continue
            # Exact fragment test; formatting splits or a long text box with line breaks may yield false negatives.
            present=n in all_text
            in_bold=n in bold_text
            checks.append({'source':s[:250], 'present_exact':present,'bold_exact':in_bold})
        slides.append({'slide':i, 'source_items':len(checks),'missing_exact':[c for c in checks if not c['present_exact']], 'not_bold_exact':[c for c in checks if not c['bold_exact']]})
    report={'pptx':Path(args.pptx).name, 'docx':Path(args.docx).name,'slides':slides,
            'summary':{'slides':len(slides),'source_items':sum(x['source_items'] for x in slides),
                       'missing_exact':sum(len(x['missing_exact']) for x in slides),
                       'not_bold_exact':sum(len(x['not_bold_exact']) for x in slides)}}
    print(json.dumps(report['summary'], indent=2))
    print('NOTE: Heuristic exact match is conservative and may flag false negatives. Review per-slide output manually. It does not parse text in images.')
    if args.json:Path(args.json).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__':main()
