import ipaddress


def is_valid_ipv4(value: str) -> bool:
    try:
        ipaddress.IPv4Address(value.strip())
        return True
    except (ValueError, AttributeError):
        return False


def is_valid_subnet_mask(value: str) -> bool:
    try:
        ipaddress.IPv4Network(f"0.0.0.0/{value.strip()}", strict=False)
        parts = [int(p) for p in value.strip().split(".")]
        binary = "".join(f"{p:08b}" for p in parts)
        return "01" not in binary
    except (ValueError, AttributeError):
        return False


def is_valid_gateway(value: str) -> bool:
    return value.strip() == "" or is_valid_ipv4(value)
