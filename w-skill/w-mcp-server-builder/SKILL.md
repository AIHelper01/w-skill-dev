---
name: w-mcp-server-builder
description: Build, improve, or review Python FastMCP / MCP server examples, especially Streamable HTTP servers. Use when Codex needs to create or harden MCP tools, add remote access, configure Host/Origin protection, improve Ctrl+C shutdown behavior, design file/API tools, validate tool behavior, or update README documentation for MCP demos.
---

# MCP Server Builder

Use this skill to implement or improve small Python MCP servers in educational or internal-tooling repositories. Prefer the repository's existing MCP SDK style and keep changes tightly scoped.

## Workflow

1. Inspect the existing server entrypoint and README.
2. Identify transport, host, port, security, and shutdown behavior.
3. Preserve the existing business tools unless the user asks to change them.
4. Add remote access support deliberately:
   - Default for trusted classroom demos may be `0.0.0.0`.
   - Keep env vars for host and port.
   - Make Host/Origin DNS rebinding protection configurable.
5. Replace bare `mcp.run(transport="streamable-http")` only when shutdown or uvicorn settings need control.
6. Validate by importing the module, calling diagnostic tools, compiling Python, and briefly starting/stopping the server if feasible.
7. Update README with exact client URL, env vars, risks, validation steps, and troubleshooting.

For reusable implementation patterns, read [references/fastmcp-patterns.md](references/fastmcp-patterns.md).

## Code Review Checklist

- Confirm whether the server should be local-only or remote-accessible.
- Confirm whether the server is trusted-demo code or production-like code.
- For remote access, expose host/port through environment variables.
- For Streamable HTTP behind IP/domain access, handle `421 Misdirected Request` from Host header checks.
- For Ctrl+C hangs, configure uvicorn `timeout_keep_alive` and `timeout_graceful_shutdown`, and catch `KeyboardInterrupt`.
- For file tools, document that paths refer to the server machine, not the MCP client machine.
- For API tools, avoid leaking API keys; expose `check_config()` style diagnostics that report presence, not secrets.
- For tools that mutate state, return structured JSON with `ok`, `error`, `message`, and target paths or identifiers.
- Do not claim an MCP operation succeeded unless a tool call or local verification confirms it.

## README Requirements

When updating README for an MCP server, include:

- Entry script and MCP URL.
- Required env vars and optional env vars.
- Remote access section with `<服务器IP>` examples.
- Host/Origin / DNS rebinding behavior and 421 troubleshooting.
- Shutdown / Ctrl+C behavior if uvicorn settings are customized.
- Tool list with parameters and success/error response shape.
- Security section that names the real default behavior.
- Validation commands, at minimum `python -m py_compile <server>.py` and diagnostic tool calls.

## Validation

Always run:

```bash
python -m py_compile <server>.py
```

Prefer also running:

```bash
python -c 'import <module> as s; print(s.ping())'
```

If shutdown behavior changed, briefly start the server and send one `Ctrl+C`; confirm it exits without traceback. If binding is blocked by sandboxing, request escalation rather than skipping silently.
