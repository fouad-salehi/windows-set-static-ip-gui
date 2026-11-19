import subprocess
from typing import List, Dict


def _run(cmd: List[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )


def list_adapters() -> List[str]:
    result = _run(["netsh", "interface", "show", "interface"])
    adapters = []
    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 5 and parts[0] in ("Enabled", "Disabled"):
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
