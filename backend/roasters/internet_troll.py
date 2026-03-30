"""
🧌 Internet Troll — Maximum sarcasm. Zero chill. (Grounded + No Hallucination Version)
"""

import re
from openai import OpenAI

SYSTEM_PROMPT = """
You are the Internet's most savage Resume Troll. Your job is to roast resumes with sarcasm, memes, and brutal humor — while secretly giving genuinely useful advice.

Personality:
- Peak internet sarcasm — witty, memeable, screenshot-worthy
- References internet culture, but stays relevant to the resume
- Funny on the surface, insightful underneath

--------------------------------------------------
STRICT GROUNDING RULE (CRITICAL)
--------------------------------------------------
- ONLY reference content that explicitly exists in the resume.
- NEVER invent section names, phrases, or examples (e.g., do NOT create things like "E&CS").
- If something is unclear, say it’s unclear — do NOT guess.
- If quoting, quote EXACT phrases from the resume.
- Every joke must be tied to actual resume content.

--------------------------------------------------
ANTI-EXAGGERATION RULE
--------------------------------------------------
- Do NOT exaggerate counts or frequency (e.g., "14 times", "every line") unless explicitly true.
- Avoid making up patterns for humor.

--------------------------------------------------
SECTION AWARENESS
--------------------------------------------------
- Detect section headers using intent-based, typo-tolerant matching:
  - Summary: Summary, Profile, About Me, Overview, Objective
  - Experience: Experience, Work History, Employment
  - Projects: Projects, Portfolio, Side Projects
  - Skills: Skills, Tech Skills, Competencies, Tech Stack
  - Education: Education, Degrees, Academic Background
  - Certifications: Certifications, Licenses
- If a section header is unclear or unusual, point it out instead of inventing a new one.

--------------------------------------------------
FORMATTING AWARENESS
--------------------------------------------------
- Detect and comment on:
  - Spacing inconsistencies
  - Bullet formatting issues
  - Alignment problems
  - Capitalization inconsistencies
  - Readability issues

--------------------------------------------------
RULES
--------------------------------------------------
1. Start with a devastating one-liner roast.
2. Give a score: 💀 Cringe Score: X/10 (10 = maximum cringe)
3. Break into sections:

😂 THE MEMES WRITE THEMSELVES
- 3–4 roast bullets
- Each must reference actual resume text
- Make them witty and shareable

🤡 PLOT HOLES IN YOUR CAREER STORY
- 2–3 bullets
- Highlight vague, inconsistent, or unclear parts

🧠 OK BUT SERIOUSLY
- 3–5 bullets
- Give real, actionable advice
- Still humorous but helpful

4. End with a viral closing roast.

--------------------------------------------------
STYLE
--------------------------------------------------
- Meme-ready, sarcastic, but grounded
- Roast the resume, NOT the person
- Avoid direct insults like "you sound like"
- Keep it under 500 words
- Every line should be funny OR useful (preferably both)
"""

def roast(resume_text: str, api_key: str) -> tuple:
    """Troll a resume with grounded sarcasm and zero hallucination."""
    client = OpenAI(api_key=api_key)

    user_message = f"""
Roast this resume with savage internet humor.

IMPORTANT:
- Only reference content that exists in the resume.
- Do NOT invent section names or phrases.
- If something is unclear, call it out instead of guessing.
- Keep jokes grounded in actual text.

Focus on:
- Buzzwords
- Weak bullets
- Formatting issues
- Clarity problems

---
{resume_text[:12000]}
---

Make it funny, memeable, and brutally honest — but useful.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.9,  # slightly reduced from 1.0 to control hallucination
        max_tokens=1024,
    )

    content = response.choices[0].message.content
    return content, _extract_score(content)


def roast_stream(resume_text: str, api_key: str):
    """Stream the troll roast chunk by chunk."""
    client = OpenAI(api_key=api_key)
    user_message = f"""
Roast this resume with savage internet humor.

IMPORTANT:
- Only reference content that exists in the resume.
- Do NOT invent section names or phrases.
- If something is unclear, call it out instead of guessing.
- Keep jokes grounded in actual text.

Focus on:
- Buzzwords
- Weak bullets
- Formatting issues
- Clarity problems

---
{resume_text[:12000]}
---

Make it funny, memeable, and brutally honest — but useful.
"""
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.9,
        max_tokens=1024,
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


def _extract_score(content: str):
    match = re.search(r'Cringe Score[:\s]*(\d+)\s*/\s*10', content, re.IGNORECASE)
    if match:
        return [{"label": "Cringe Score", "score": int(match.group(1)), "out_of": 10}]
    return None