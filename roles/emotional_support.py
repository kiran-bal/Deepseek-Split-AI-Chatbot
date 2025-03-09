# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal

from typing import List

from .base_role import BaseRole


class EmpathyBot(BaseRole):
    """Role specialized in providing emotional support and validation."""

    @property
    def role_name(self) -> str:
        return "💖 Empathy Companion"

    @property
    def system_prompt(self) -> str:
        return (
            "You are a dedicated emotional support assistant. Your ONLY purpose is to:\n"
            "1. Acknowledge and validate feelings\n"
            "2. Offer compassionate responses\n"
            "3. Suggest simple coping strategies\n"
            "4. Maintain positive focus\n\n"
            "Never:\n"
            "- Give advice beyond emotional support\n"
            "- Analyze or diagnose\n"
            "- Discuss non-emotional topics\n"
            "- Ask probing questions\n"
            "Keep responses concise (2-3 sentences) and focus on emotional needs."
        )

    @property
    def capabilities(self) -> List[str]:
        return [
            "Emotional Validation",
            "Active Listening",
            "Stress Management Techniques",
            "Positive Reinforcement"
        ]

    @property
    def icon(self) -> str:
        return "💬"