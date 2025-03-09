"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

from abc import ABC, abstractmethod
from typing import List, Dict


class BaseRole(ABC):
    """Abstract base class for all chat roles."""

    @property
    @abstractmethod
    def role_name(self) -> str:
        """Return the display name of the role."""
        pass

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        """Return the system prompt for this role."""
        pass

    @property
    def capabilities(self) -> List[str]:
        """Return list of role capabilities."""
        return []

    @property
    def icon(self) -> str:
        """Return emoji icon for the role."""
        return "🤖"