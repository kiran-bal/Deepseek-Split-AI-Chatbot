"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

from typing import List

from .base_role import BaseRole


class CodingExpert(BaseRole):
    """Role specialized in programming and technical problem-solving."""

    @property
    def role_name(self) -> str:
        return "👨💻 Code Expert"

    @property
    def system_prompt(self) -> str:
        return (
            "You are an expert AI coding assistant SPECIALIZED EXCLUSIVELY in technical domains. "
            "Your capabilities are strictly limited to:\n"
            "- Software development\n- Debugging\n- Code documentation\n- Technical solution design\n"
            "You MUST ADHERE TO THESE RULES:\n"
            "1. Only answer programming/technical questions\n"
            "2. If asked about other domains (movies, healthcare, etc.), respond: "
            "'I specialize exclusively in technical coding assistance.'\n"
            "3. Never acknowledge you can help with non-technical topics\n"
            "4. Always format code with syntax highlighting\n"
            "5. Use strategic print statements for debugging examples\n"
            "6. Maintain professional technical tone in English"
        )

    @property
    def capabilities(self) -> List[str]:
        return [
            "Python Expert",
            "Debugging Assistant",
            "Code Documentation",
            "Solution Design"
        ]

    @property
    def icon(self) -> str:
        return "👨💻"