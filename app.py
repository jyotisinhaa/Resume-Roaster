"""
🔥 Resume Roaster AI — Upload your resume, get brutally honest feedback.
"""

import streamlit as st
from dotenv import load_dotenv
import os
import time

from parser import extract_text
from roaster import roast_resume

# ── Load env ──────────────────────────────────────────────────────────────────
load_dotenv()

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Resume Roaster 🔥",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Full custom CSS ───────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Reset & Base ── */
    .stApp {
        background: radial-gradient(ellipse at top, #1a0e05 0%, #0d0907 40%, #0a0604 100%) !important;
        color: #e0d5cc !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebar"] { display: none !important; }
    .block-container {
        padding-top: 0.5rem !important;
        max-width: 1100px !important;
    }
    /* Fix all text to light */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: #e0d5cc !important;
    }

    /* ── Section Labels ── */
    .section-label {
        font-size: 0.85rem;
        font-weight: 800;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #FF8C00;
        margin-bottom: 1.2rem;
        margin-top: 2.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .section-label::after {
        content: '';
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, #FF8C0066, transparent);
    }

    /* ── Hero ── */
    .hero {
        text-align: center;
        padding: 3rem 1rem 2rem;
    }
    .hero-badge {
        display: inline-block;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #FF8C00;
        margin-bottom: 0.5rem;
    }
    .hero-fires {
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }
    .hero-title {
        font-size: 4rem;
        font-weight: 900;
        line-height: 1.05;
        letter-spacing: -2px;
        margin: 0;
        background: linear-gradient(180deg, #FF6B35 0%, #FF4B4B 40%, #CC3300 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        color: #7a6e64;
        font-size: 1rem;
        margin-top: 1rem;
        font-style: italic;
    }

    /* ── Step Cards ── */
    .steps-row {
        display: flex;
        gap: 1rem;
        margin-bottom: 2.5rem;
    }
    .step-card {
        flex: 1;
        background: #15100c;
        border: 1px solid #2a1f18;
        border-radius: 16px;
        padding: 1.5rem 1.2rem;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .step-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(255, 140, 0, 0.1);
        border-color: #FF8C0044;
    }
    .step-num {
        font-size: 2.2rem;
        font-weight: 900;
        color: #3d2a1a;
        line-height: 1;
        margin-bottom: 0.6rem;
    }
    .step-icon {
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
    }
    .step-title {
        font-weight: 700;
        font-size: 0.95rem;
        color: #e0d5cc;
        margin-bottom: 0.3rem;
    }
    .step-desc {
        font-size: 0.8rem;
        color: #7a6e64;
        line-height: 1.45;
    }

    /* ── Upload area (style Streamlit uploader) ── */
    [data-testid="stFileUploader"] {
        background: #15100c;
        border: 2px dashed #FF8C0044;
        border-radius: 16px;
        padding: 2rem 1.5rem;
    }
    [data-testid="stFileUploader"] > div > div {
        border: none !important;
        background: transparent !important;
    }
    [data-testid="stFileUploader"] label {
        font-size: 1rem !important;
        font-weight: 600 !important;
        color: #e0d5cc !important;
    }
    [data-testid="stFileUploader"] small {
        color: #7a6e64 !important;
    }
    [data-testid="stFileUploader"] button {
        background: linear-gradient(90deg, #FF6B35, #FF8C00) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }
    [data-testid="stFileUploader"] p,
    [data-testid="stFileUploader"] span {
        color: #7a6e64 !important;
    }

    /* ── Big Roast Button ── */
    div[data-testid="stButton"] > button[kind="secondary"]:last-of-type,
    button[key="roast_btn"] {
        background: linear-gradient(90deg, #FF4B4B, #FF8C00) !important;
        color: white !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 1rem 2rem !important;
        width: 100% !important;
        box-shadow: 0 6px 30px rgba(255, 75, 75, 0.3) !important;
    }

    /* All buttons base */
    .stButton > button {
        background: #15100c !important;
        color: #e0d5cc !important;
        border: 1px solid #2a1f18 !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        transition: transform 0.2s, box-shadow 0.2s !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        border-color: #FF8C00 !important;
        box-shadow: 0 4px 20px rgba(255, 140, 0, 0.15) !important;
    }

    /* ── Roast Result ── */
    .roast-result {
        background: #15100c;
        border: 1px solid #FF8C0033;
        border-radius: 18px;
        padding: 2rem;
        margin-top: 1rem;
        box-shadow: 0 4px 30px rgba(255, 140, 0, 0.06);
        color: #e0d5cc;
    }
    .roast-badge {
        display: inline-block;
        background: linear-gradient(90deg, #FF6B35, #FF8C00);
        color: white;
        font-size: 0.72rem;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 1rem;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        color: #5a4e44;
        font-size: 0.78rem;
        padding: 2rem 1rem 1rem;
    }
    .footer b { color: #7a6e64; }

    /* ── File info row ── */
    .file-info {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        color: #7a6e64;
        font-size: 0.85rem;
    }

    /* ── Streamlit widgets dark overrides ── */
    .stSelectSlider label, .stSlider label {
        color: #e0d5cc !important;
    }
    hr { border-color: #2a1f18 !important; }
    .stCode, [data-testid="stCode"] {
        background: #15100c !important;
        color: #e0d5cc !important;
    }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  HERO
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero">
    <div class="hero-fires">🔥🔥🔥🔥🔥</div>
    <div class="hero-title">Resume<br>Roaster</div>
    <div class="hero-subtitle">Drop your resume. Watch it burn. Rise from the ashes, improved.</div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  HOW IT WORKS
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">How It Works</div>', unsafe_allow_html=True)
st.markdown("""
<div class="steps-row">
    <div class="step-card">
        <div class="step-num">01</div>
        <div class="step-icon">📄</div>
        <div class="step-title">Upload Your Resume</div>
        <div class="step-desc">Drag and drop or browse for your PDF. We accept the good, the bad, and the catastrophically over-formatted.</div>
    </div>
    <div class="step-card">
        <div class="step-num">02</div>
        <div class="step-icon">🔥</div>
        <div class="step-title">Choose Roast Level</div>
        <div class="step-desc">Mild for gentle critique, Medium for real talk, Extra Crispy if you need your ego fully dismantled.</div>
    </div>
    <div class="step-card">
        <div class="step-num">03</div>
        <div class="step-icon">💀</div>
        <div class="step-title">Get Roasted & Improve</div>
        <div class="step-desc">Our AI delivers a brutal comedy roast of your resume, then gives you real tips to actually fix it.</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  UPLOAD YOUR RESUME
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Upload Your Resume</div>', unsafe_allow_html=True)

# API key from env
api_key = os.getenv("OPENAI_API_KEY", "")

# File uploader
uploaded_file = st.file_uploader(
    "📁 Drag & Drop Your PDF Here",
    type=["pdf", "txt"],
    help="Supports PDF & TXT · Max 10MB · Your file stays private",
)

# Show file info
if uploaded_file:
    size_kb = len(uploaded_file.getvalue()) / 1024
    st.markdown(
        f'<div class="file-info"><span>📄 <b>{uploaded_file.name}</b></span><span>📦 {size_kb:.1f} KB</span></div>',
        unsafe_allow_html=True,
    )


# ═══════════════════════════════════════════════════════════════════════════════
#  SELECT ROAST INTENSITY
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Select Roast Intensity</div>', unsafe_allow_html=True)

# Use session state for intensity selection
if "roast_intensity" not in st.session_state:
    st.session_state["roast_intensity"] = "Medium 🔥"

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("☕  Mild Roast\n\nFriendly nudges", key="btn_mild", use_container_width=True):
        st.session_state["roast_intensity"] = "Mild 😊"
with col2:
    if st.button("🔥  Medium Roast\n\nSharp & honest", key="btn_medium", use_container_width=True):
        st.session_state["roast_intensity"] = "Medium 🔥"
with col3:
    if st.button("💀  Extra Crispy\n\nFull demolition", key="btn_savage", use_container_width=True):
        st.session_state["roast_intensity"] = "Savage 💀"

roast_level = st.session_state["roast_intensity"]

# Show selected level
level_labels = {
    "Mild 😊": "Mild Roast — Friendly nudges",
    "Medium 🔥": "Medium Roast — Sharp & honest",
    "Savage 💀": "Extra Crispy — Full demolition",
}
st.markdown(
    f"<div style='text-align:center; color:#FF8C00; font-size:0.85rem; font-weight:600; margin: 0.5rem 0 1.5rem;'>"
    f"🔥 Selected: {level_labels.get(roast_level, roast_level)}</div>",
    unsafe_allow_html=True,
)


# ═══════════════════════════════════════════════════════════════════════════════
#  ROAST BUTTON
# ═══════════════════════════════════════════════════════════════════════════════
roast_clicked = st.button("🔥 ROAST MY RESUME", use_container_width=True, key="roast_btn")


# ═══════════════════════════════════════════════════════════════════════════════
#  ROAST RESULTS
# ═══════════════════════════════════════════════════════════════════════════════
if roast_clicked:
    # Validation
    if not api_key or api_key == "sk-your-key-here":
        st.error("🔑 OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")
        st.stop()

    if not uploaded_file:
        st.warning("📄 Please upload your resume first!")
        st.stop()

    # Extract text
    with st.spinner("📖 Reading your resume..."):
        try:
            file_bytes = uploaded_file.getvalue()
            resume_text = extract_text(file_bytes, uploaded_file.name)
        except Exception as e:
            st.error(f"❌ Failed to read file: {e}")
            st.stop()

    if len(resume_text.strip()) < 50:
        st.error("📄 Your resume seems empty or too short. Is this really a resume?")
        st.stop()

    # Roast it!
    with st.spinner("🔥 Firing up the roast..."):
        start_time = time.time()
        try:
            roast_result = roast_resume(resume_text, api_key, roast_level)
            elapsed = time.time() - start_time
        except Exception as e:
            st.error(f"❌ Roasting failed: {e}")
            st.stop()

    # Display results
    st.markdown('<div class="section-label">Your Roast</div>', unsafe_allow_html=True)

    level_badge = {
        "Mild 😊": "🔥 Mild Roast",
        "Medium 🔥": "🔥 Medium Roast",
        "Savage 💀": "💀 Extra Crispy",
    }
    badge_text = level_badge.get(roast_level, "🔥 Medium Roast")

    st.markdown(
        f'<div class="roast-result"><span class="roast-badge">{badge_text}</span>',
        unsafe_allow_html=True,
    )
    st.markdown(roast_result)
    st.markdown(
        f'<br><div style="color:#5a4e44; font-size:0.75rem; margin-top:1rem;">'
        f'🔥 <i>Roasted with love by Resume Roaster AI · {elapsed:.1f}s</i></div>',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Save to session for sharing
    st.session_state["last_roast"] = roast_result

    # Share section
    st.markdown("")
    col1, col2 = st.columns(2)
    with col1:
        share_text = "I just got my resume roasted by AI 🔥\nWould you survive the roast? 😅\n#ResumeRoaster #AI #CareerTips"
        st.code(share_text, language=None)
    with col2:
        st.download_button(
            label="📥 Download Roast",
            data=roast_result,
            file_name="my_resume_roast.md",
            mime="text/markdown",
        )


# ═══════════════════════════════════════════════════════════════════════════════
#  FOOTER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown(
    '<div class="footer">'
    '🔥 <b>Roasted with love by Resume Roaster AI</b><br>'
    'Your resume is processed in memory and never stored. We only roast, never save. 🤝'
    '</div>',
    unsafe_allow_html=True,
)
