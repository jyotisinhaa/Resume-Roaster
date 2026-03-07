"""
🔥 Resume Ripper AI — Upload your resume, get brutally honest feedback.
"""

import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
import os
import time
import tempfile

from parser import extract_text, validate_file
from roaster import roast_resume

# ── Load env ──────────────────────────────────────────────────────────────────
load_dotenv()

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Resume Ripper 🔥",
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

    /* ── Upload Zone ── */
    [data-testid="stFileUploader"] {
        background: #110c08 !important;
        border: 2px dashed #FF8C0044 !important;
        border-radius: 20px !important;
        padding: 2.5rem 2rem 3.5rem !important;
        transition: border-color 0.3s, box-shadow 0.3s !important;
        text-align: center !important;
        max-width: 100% !important;
        width: calc(100% + 4rem) !important;
        margin-left: -2rem !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #FF8C0077 !important;
        box-shadow: 0 0 40px rgba(255,140,0,0.08), inset 0 0 30px rgba(255,140,0,0.02) !important;
    }

    /* Label as big centered heading with folder icon */
    [data-testid="stFileUploader"] label {
        width: 100% !important;
        text-align: center !important;
        display: block !important;
    }
    [data-testid="stFileUploader"] label p {
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        color: #e0d5cc !important;
        text-align: center !important;
    }
    /* Help text as subtitle */
    [data-testid="stFileUploader"] [data-testid="stTooltipHoverTarget"] {
        display: none !important;
    }

    /* Remove inner section borders */
    [data-testid="stFileUploader"] section {
        border: none !important;
        background: transparent !important;
    }

    /* Dropzone styling */
    [data-testid="stFileUploaderDropzone"] {
        background: transparent !important;
        border: none !important;
        padding: 0.5rem 0 !important;
        text-align: center !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }
    [data-testid="stFileUploaderDropzone"] > div {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
    }
    /* Hide the SVG cloud icon */
    [data-testid="stFileUploaderDropzone"] svg {
        display: none !important;
    }
    /* Hide the "Drag and drop" text and "Limit 200MB" text */
    [data-testid="stFileUploaderDropzone"] > div > div:first-child > div,
    [data-testid="stFileUploaderDropzone"] > div > div:first-child > span,
    [data-testid="stFileUploaderDropzone"] > div > div:first-child > small,
    [data-testid="stFileUploaderDropzone"] > div > small,
    [data-testid="stFileUploader"] small {
        display: none !important;
    }
    /* KEEP the Browse button visible and centered */
    [data-testid="stFileUploaderDropzone"] button,
    [data-testid="stBaseButton-secondary"] {
        display: inline-flex !important;
        margin: 0 auto !important;
    }

    /* Browse button */
    [data-testid="stFileUploaderDropzone"] button,
    [data-testid="stFileUploader"] [data-testid="stBaseButton-secondary"] {
        background: linear-gradient(135deg, #FF6B35, #FF8C00) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        padding: 0.55rem 2rem !important;
        font-size: 0.88rem !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 4px 18px rgba(255,107,53,0.25) !important;
        transition: transform 0.2s, box-shadow 0.2s !important;
    }
    [data-testid="stFileUploaderDropzone"] button:hover,
    [data-testid="stFileUploader"] [data-testid="stBaseButton-secondary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(255,107,53,0.35) !important;
    }

    /* Upload subtitle inside card */
    .upload-subtitle {
        text-align: center;
        color: #7a6e64;
        font-size: 0.82rem;
        margin: 0.2rem 0 0;
        padding-bottom: 0.5rem;
    }

    /* ── Uploaded file info card ── */
    .file-info-card {
        background: #1a130d;
        border: 1px solid #FF8C0022;
        border-radius: 12px;
        padding: 0.8rem 1.2rem;
        margin-top: 1rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }
    .file-info-icon {
        font-size: 1.8rem;
        filter: drop-shadow(0 0 6px rgba(255,140,0,0.2));
    }
    .file-info-details {
        flex: 1;
        text-align: left;
    }
    .file-info-name {
        font-weight: 700;
        color: #e0d5cc;
        font-size: 0.88rem;
    }
    .file-info-meta {
        color: #665c52;
        font-size: 0.75rem;
        margin-top: 2px;
    }
    .file-info-check {
        color: #22c55e;
        font-size: 1.1rem;
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

    /* (file-info-card styles are defined above) */

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

uploaded_file = st.file_uploader(
    "📂 Upload Your Resume",
    type=["pdf", "docx", "txt"],
    help="Supports PDF, DOCX & TXT · Max 10MB · Your file stays private",
)

# JS to hide default Streamlit dropzone text & inject supported-formats line
components.html("""
<script>
function cleanUploader() {
    const main = window.parent.document;
    main.querySelectorAll('[data-testid="stFileUploaderDropzone"]').forEach(dz => {
        const inner = dz.querySelector(':scope > div');
        if (!inner) return;
        Array.from(inner.children).forEach(el => {
            if (el.tagName === 'BUTTON' || el.querySelector('button')) return;
            if (el.classList && el.classList.contains('supported-formats-line')) return;
            el.style.display = 'none';
        });
        dz.querySelectorAll('small').forEach(s => s.style.display = 'none');

        // Inject supported-formats text if not already there
        if (!dz.querySelector('.supported-formats-line')) {
            const info = document.createElement('div');
            info.className = 'supported-formats-line';
            info.innerHTML = '📎 Supported formats: <b style="color:#FF8C00;">PDF</b>, <b style="color:#FF8C00;">DOCX</b>, <b style="color:#FF8C00;">TXT</b> · Max 10 MB';
            info.style.cssText = 'text-align:center;color:#8a7e74;font-size:0.8rem;margin-bottom:0.8rem;order:-1;';
            // Insert before the Browse button
            const btn = dz.querySelector('button');
            if (btn && btn.parentElement) {
                btn.parentElement.insertBefore(info, btn);
            } else {
                dz.prepend(info);
            }
        }
    });
    main.querySelectorAll('[data-testid="stFileUploader"] small').forEach(s => s.style.display = 'none');
}
setInterval(cleanUploader, 300);
cleanUploader();
</script>
""", height=0)

# Track whether a valid file is ready
if "file_valid" not in st.session_state:
    st.session_state["file_valid"] = False

# Show uploaded file info card + validate + save temp
if uploaded_file:
    file_bytes = uploaded_file.getvalue()
    size_kb = len(file_bytes) / 1024
    ext = uploaded_file.name.rsplit('.', 1)[-1].upper()
    icon = "📄" if ext == "PDF" else ("📝" if ext == "DOCX" else "📝")

    # Validate file type & size
    try:
        validate_file(file_bytes, uploaded_file.name)
        st.session_state["file_valid"] = True
    except ValueError as e:
        st.session_state["file_valid"] = False
        st.error(f"❌ {e}")

    if st.session_state["file_valid"]:
        # Save to temp directory
        temp_dir = tempfile.mkdtemp(prefix="resume_roaster_")
        temp_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(file_bytes)
        st.session_state["temp_resume_path"] = temp_path

        st.markdown(
            f'<div class="file-info-card">'
            f'  <div class="file-info-icon">{icon}</div>'
            f'  <div class="file-info-details">'
            f'    <div class="file-info-name">{uploaded_file.name}</div>'
            f'    <div class="file-info-meta">{ext} · {size_kb:.1f} KB · Ready to roast</div>'
            f'  </div>'
            f'  <div class="file-info-check">✓</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
else:
    st.session_state["file_valid"] = False


# ═══════════════════════════════════════════════════════════════════════════════
#  SELECT ROAST INTENSITY  (only shown when file is valid)
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.get("file_valid", False):
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

    # ═══════════════════════════════════════════════════════════════════════════
    #  ROAST BUTTON
    # ═══════════════════════════════════════════════════════════════════════════
    roast_clicked = st.button("🔥 ROAST MY RESUME", use_container_width=True, key="roast_btn")

    # ═══════════════════════════════════════════════════════════════════════════
    #  ROAST RESULTS
    # ═══════════════════════════════════════════════════════════════════════════
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
            f'🔥 <i>Roasted with love by Resume Ripper AI · {elapsed:.1f}s</i></div>',
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
    '🔥 <b>Roasted with love by Resume Ripper AI</b><br>'
    'Your resume is processed in memory and never stored. We only roast, never save. 🤝'
    '</div>',
    unsafe_allow_html=True,
)
