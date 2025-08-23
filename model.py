from dataclasses import dataclass
from typing import List

@dataclass
class EmailTask:
    to: List[str]
    subject: str
    body: str