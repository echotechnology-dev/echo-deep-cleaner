from dataclasses import dataclass

@dataclass
class ScanResult:
    type: str
    path: str
    size: int
    risk: str
