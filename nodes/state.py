"""
State definition for test_github_only
"""

from typing import Dict, Any, TypedDict


class State(TypedDict):
    """State for the test_github_only workflow."""
    # Define your state fields here
    input: str
    output: Any