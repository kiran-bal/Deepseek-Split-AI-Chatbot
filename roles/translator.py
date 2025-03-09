"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

from typing import List

from .base_role import BaseRole


class Translator(BaseRole):
    """Multilingual translation expert supporting 50+ languages."""

    @property
    def role_name(self) -> str:
        return "🌍 Translator"

    @property
    def system_prompt(self) -> str:
        return (
            "You are a professional translator supporting 50+ languages. "
            "Maintain original meaning, adapt cultural context appropriately, "
            "and provide both formal and informal versions when relevant."
            "Your main objective is to convert english to hindi if not specified and respond the "
            "hindi version of the given input"
        )

    @property
    def capabilities(self) -> List[str]:
        return [
            "Multilingual Translation (currently eng -> hindi)",
            "Cultural Adaptation",
            "Formal/Informal Versions",
            "Idiom Handling"
        ]

    @property
    def icon(self) -> str:
        return "🌍"