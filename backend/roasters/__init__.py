"""
Roaster personalities — each file contains a unique AI persona for resume roasting.
"""

from backend.roasters.brutal_recruiter import roast as brutal_recruiter_roast, roast_stream as brutal_recruiter_stream, _extract_score as brutal_recruiter_extract
from backend.roasters.ats_scanner import roast as ats_scanner_roast, roast_stream as ats_scanner_stream, _add_visual_bars as ats_scanner_extract
from backend.roasters.career_coach import roast as career_coach_roast, roast_stream as career_coach_stream, _extract_score as career_coach_extract
from backend.roasters.internet_troll import roast as internet_troll_roast, roast_stream as internet_troll_stream, _extract_score as internet_troll_extract
from backend.roasters.top_hiring_manager import roast as top_hiring_manager_roast, roast_stream as top_hiring_manager_stream, _extract_score as top_hiring_manager_extract

_ROASTERS = {
    "brutal_recruiter": brutal_recruiter_roast,
    "ats_scanner": ats_scanner_roast,
    "career_coach": career_coach_roast,
    "internet_troll": internet_troll_roast,
    "top_hiring_manager": top_hiring_manager_roast,
}

_STREAMERS = {
    "brutal_recruiter": brutal_recruiter_stream,
    "ats_scanner": ats_scanner_stream,
    "career_coach": career_coach_stream,
    "internet_troll": internet_troll_stream,
    "top_hiring_manager": top_hiring_manager_stream,
}

_EXTRACTORS = {
    "brutal_recruiter": brutal_recruiter_extract,
    "ats_scanner": ats_scanner_extract,
    "career_coach": career_coach_extract,
    "internet_troll": internet_troll_extract,
    "top_hiring_manager": top_hiring_manager_extract,
}


def get_roaster(personality_key: str):
    """Return the roast function for the given personality key."""
    if personality_key not in _ROASTERS:
        raise ValueError(f"Unknown personality: {personality_key}")
    return _ROASTERS[personality_key]


def get_roaster_stream(personality_key: str):
    """Return the streaming roast generator function for the given personality key."""
    if personality_key not in _STREAMERS:
        raise ValueError(f"Unknown personality: {personality_key}")
    return _STREAMERS[personality_key]


def get_score_extractor(personality_key: str):
    """Return the score extraction function for the given personality key."""
    if personality_key not in _EXTRACTORS:
        raise ValueError(f"Unknown personality: {personality_key}")
    return _EXTRACTORS[personality_key]
