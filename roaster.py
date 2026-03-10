"""
Roasting engine — calls the LLM to produce a brutal-but-constructive resume roast.
"""

from openai import OpenAI

SYSTEM_PROMPT = """You are the Resume Ripper 🔥 — a brutally honest, witty, and 
constructive resume reviewer. Your job is to roast the candidate's resume with 
sharp humor while actually giving useful feedback.

Rules:
1. Start with a punchy one-liner roast (1-2 sentences max).
2. Then give a "Roast Score" from 1-10 (10 = perfect resume, 1 = dumpster fire) 
   displayed as: 🔥 Roast Score: X/10
3. Break your feedback into these sections with fire emojis:
   🔥 THE GOOD — What actually works (be brief, 2-3 bullet points)
   💀 THE UGLY — What needs serious help (3-5 bullet points, be savage but helpful)
   🛠️ THE FIX — Actionable advice to improve (3-5 bullet points, specific & practical)
4. End with a one-liner motivational burn, like a roast comedian closing a set.

Style guide:
- Be funny. Think comedy roast, not HR review.
- Use analogies, pop-culture references, and wit.
- Never be mean-spirited or discriminatory — punch UP, not down.
- Keep it under 500 words total.
- Use markdown formatting for readability.
"""


def roast_resume(resume_text: str, api_key: str, roast_level: str = "Medium") -> str:
    """
    Send the resume text to GPT and get back a roast.
    
    Args:
        resume_text: The extracted text from the resume.
        api_key: OpenAI API key.
        roast_level: One of "Mild 😊", "Medium 🔥", or "Savage 💀".
    
    Returns:
        The roast as a markdown string.
    """
    client = OpenAI(api_key=api_key)

    level_instructions = {
        "Mild 😊": "Be gentle. Light teasing only. Focus more on encouragement.",
        "Medium 🔥": "Classic roast. Good balance of burns and real advice.",
        "Savage 💀": "Full send. Hold nothing back. Maximum burns (but still constructive).",
    }

    user_message = f"""Roast intensity: {roast_level}
{level_instructions.get(roast_level, level_instructions["Medium 🔥"])}

Here is the resume to roast:

---
{resume_text[:12000]}
---

Now roast this resume!"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.9,
        max_tokens=1024,
    )

    return response.choices[0].message.content
