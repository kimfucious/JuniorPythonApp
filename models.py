from dataclasses import dataclass
from enums import WishStatus
from typing import Optional


@dataclass
class Wish:
    description: str
    status: WishStatus
    id: str
    created_at: str
    updated_at: str


@dataclass
class PartialWish(Wish):
    description: str
    status: WishStatus
    id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
