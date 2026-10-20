# FastMCP Server Patterns

## Remote Streamable HTTP

Use environment variables for host and port:

```python
SERVER_HOST = os.getenv("MCP_HOST", "0.0.0.0").strip() or "0.0.0.0"
SERVER_PORT = _get_int_env("MCP_PORT", 16682)

mcp = FastMCP("ExampleMCPServer", host=SERVER_HOST, port=SERVER_PORT)
```

For classroom demos, defaulting to `0.0.0.0` is convenient. For local-only tools, use `127.0.0.1`.

## Host / Origin Protection

FastMCP accepts `transport_security=TransportSecuritySettings(...)`.

```python
from mcp.server.transport_security import TransportSecuritySettings

def _transport_security_settings() -> TransportSecuritySettings:
    return TransportSecuritySettings(
        enable_dns_rebinding_protection=_get_bool_env("MCP_ENABLE_DNS_REBINDING_PROTECTION"),
        allowed_hosts=_get_list_env("MCP_ALLOWED_HOSTS"),
        allowed_origins=_get_list_env("MCP_ALLOWED_ORIGINS"),
    )
```

If users see `421 Misdirected Request` and `Invalid Host header`, either:

- Add the exact `Host` value from logs to the allowed hosts list, or
- For trusted demos, disable DNS rebinding protection by default and document the risk.

## Controlled Uvicorn Startup

FastMCP's `run()` is concise, but does not expose uvicorn shutdown settings. Use explicit uvicorn startup when Ctrl+C hangs or keep-alive tuning matters:

```python
async def _run_streamable_http_async() -> None:
    import uvicorn

    config = uvicorn.Config(
        mcp.streamable_http_app(),
        host=mcp.settings.host,
        port=mcp.settings.port,
        log_level=mcp.settings.log_level.lower(),
        timeout_keep_alive=_get_int_env("MCP_UVICORN_TIMEOUT_KEEP_ALIVE", 1, minimum=0),
        timeout_graceful_shutdown=_get_int_env(
            "MCP_UVICORN_TIMEOUT_GRACEFUL_SHUTDOWN",
            2,
            minimum=0,
        ),
    )
    server = uvicorn.Server(config)
    await server.serve()


def run_server() -> None:
    import anyio

    try:
        anyio.run(_run_streamable_http_async)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run_server()
```

## Environment Helpers

Use small helpers rather than repeatedly parsing env vars:

```python
def _get_int_env(name: str, default: int, minimum: int = 1) -> int:
    value = os.getenv(name, "").strip()
    if not value:
        return default
    try:
        parsed = int(value)
    except ValueError:
        return default
    return max(minimum, parsed)


def _get_bool_env(name: str, default: bool = False) -> bool:
    value = os.getenv(name, "").strip().lower()
    if not value:
        return default
    return value in {"1", "true", "yes", "on"}


def _get_list_env(name: str) -> list[str]:
    value = os.getenv(name, "").strip()
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]
```

## Diagnostic Tools

Add or maintain a `ping()` tool that returns operational state:

```python
@mcp.tool()
def ping() -> dict[str, Any]:
    security_settings = _transport_security_settings()
    return {
        "ok": True,
        "server": "ExampleMCPServer",
        "platform": platform.system(),
        "host": SERVER_HOST,
        "port": SERVER_PORT,
        "dns_rebinding_protection_enabled": security_settings.enable_dns_rebinding_protection,
        "allowed_hosts": security_settings.allowed_hosts,
        "allowed_origins": security_settings.allowed_origins,
    }
```

For API-backed MCPs, add `check_config()` that reports whether secrets are configured without returning the secret value.

## README Security Language

Describe the actual defaults plainly:

- "Default listens on `0.0.0.0`" if true.
- "Default has no built-in authentication" if true.
- "Default does not restrict file roots" if true.
- "This is trusted classroom/internal demo configuration, not production-safe" when remote and unauthenticated.

For file MCPs, always state: MCP paths are resolved on the server machine, not the user's local client machine.
