import subprocess
import sys
from typing import List, Dict

CREATE_NO_WINDOW = 0x08000000


def _run(cmd: List[str]) -> subprocess.CompletedProcess:
    flags = CREATE_NO_WINDOW if sys.platform == "win32" else 0
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        creationflags=flags,
    )


def list_adapters() -> List[str]:
    result = _run(["netsh", "interface", "show", "interface"])
    lines = result.stdout.splitlines()
    adapters = []
    header_found = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("---"):
            header_found = True
            continue
        if not header_found:
            continue
        parts = line.split()
        if len(parts) >= 4:
            adapters.append(" ".join(parts[3:]))
    return adapters


def show_config() -> str:
    return _run(["netsh", "interface", "ip", "show", "config"]).stdout


def show_address(adapter: str) -> str:
    return _run(["netsh", "interface", "ip", "show", "address", adapter]).stdout


def set_static(adapter: str, ip: str, mask: str, gateway: str = "") -> Dict:
    cmd = ["netsh", "interface", "ip", "set", "address", adapter, "static", ip, mask]
    if gateway.strip():
        cmd.append(gateway.strip())
    r = _run(cmd)
    return {"ok": r.returncode == 0, "out": r.stdout + r.stderr}


def set_dhcp(adapter: str) -> Dict:
    a = _run(["netsh", "interface", "ip", "set", "address", adapter, "dhcp"])
    b = _run(["netsh", "interface", "ip", "set", "dns", adapter, "dhcp"])
    return {
        "ok": a.returncode == 0 and b.returncode == 0,
        "out": (a.stdout + a.stderr + b.stdout + b.stderr).strip(),
    }