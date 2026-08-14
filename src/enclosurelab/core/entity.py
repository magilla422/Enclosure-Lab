"""
Enclosure Lab

entity.py

Defines the base Entity class used throughout Enclosure Lab.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass(slots=True)
class Entity:
    """
    Base class for all major Enclosure Lab objects.

    Provides a unique identity and common metadata shared
    by every engineering object.
    """

    name: str

    id: UUID = field(default_factory=uuid4, init=False)

    created: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        init=False,
    )

    modified: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        init=False,
    )

    description: str = ""

    notes: str = ""

    tags: list[str] = field(default_factory=list)

    def touch(self) -> None:
        """Updates the modified timestamp."""
        self.modified = datetime.now(UTC)