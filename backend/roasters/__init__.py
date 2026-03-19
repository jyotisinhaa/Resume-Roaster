"""
Roaster personalities — each file contains a unique AI persona for resume roasting.
"""

from backend.roasters.brutal_recruiter import roast as brutal_recruiter_roast
from backend.roasters.ats_scanner import roast as ats_scanner_roast
from backend.roasters.career_coach import roast as career_coach_roast
from backend.roasters.internet_troll import roast as internet_troll_roast
from backend.roasters.top_hiring_manager import roast as top_hiring_manager_roast

_ROASTERS = {
    "brutal_recruiter": brutal_recruiter_roast,
    "ats_scanner": ats_scanner_roast,
    "career_coach": career_coach_roast,
    "internet_troll": internet_troll_roast,
    "top_hiring_manager": top_hiring_manager_roast,
}


def get_roaster(personality_key: str):
    """Return the roast function for the given personality key."""
    if personality_key not in _ROASTERS:
        raise ValueError(f"Unknown personality: {personality_key}")
    return _ROASTERS[personality_key]
