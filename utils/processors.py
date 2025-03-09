"""
# Copyright (c) 2025, Kiran Bal
# All rights reserved.

# Code written by: Kiran Bal
"""

import re
from typing import Optional


def hide_think_tags(text: str, hide: bool) -> str:
    """
    Process text to hide/show content in <think> tags.

    Args:
        text: Input text containing potential <think> tags
        hide: Boolean flag to determine visibility

    Returns:
        Processed text with <think> content hidden if required
    """
    if hide:
        return re.sub(
            r'<think>(.*?)</think>',
            r'',
            text,
            flags=re.DOTALL
        )
    return text


def format_streaming_response(chunk: str) -> Optional[str]:
    """
    Process streaming response chunks for final output.

    Args:
        chunk: Raw response chunk from LLM

    Returns:
        Formatted chunk ready for display (or None for hidden chunks)
    """
    # Filter out empty chunks and special tokens
    # if not chunk.strip() or chunk in ['<|EOT|>', '<|END_OF_TEXT|>']:
    #     return None
    return chunk