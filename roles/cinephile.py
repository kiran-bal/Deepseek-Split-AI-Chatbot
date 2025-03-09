"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

from typing import List

from .base_role import BaseRole


class Cinephile(BaseRole):
    """Movie expert with deep knowledge of global cinema."""

    @property
    def role_name(self) -> str:
        return "🎬 Cinephile"

    @property
    def system_prompt(self) -> str:
        return (
            "You are a film expert with knowledge of global cinema history. "
            "Give only film related answers and present it in a precise and structured manner to read easily"
        )

    @property
    def capabilities(self) -> List[str]:
        return [
            "Movie Recommendations",
            "Film Analysis",
            "Historical Context",
            "Crew Insights"
        ]

    @property
    def icon(self) -> str:
        return "🎬"