"""
🔥 Resume Ripper AI — Upload your resume, get brutally honest feedback.

This is the main entry point. All UI lives in ui/, all backend in backend/.
"""

import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
import os
import time
import tempfile
import logging

from backend.parser import extract_text, validate_file
from backend.roasters import get_roaster, get_roaster_stream, get_score_extractor
from ui.styles import get_css
from ui.theme import get_theme_toggle_js
from ui.components import (
    PERSONALITIES,
    render_hero,
    render_how_it_works,
    render_upload_zone_js,
    render_file_info_card,
    render_personality_selector,
    render_roast_results,
    render_footer,
)

# ── Logging setup ─────────────────────────────────────────────────────────────
logger = logging.getLogger("ResumeRoaster")

# ── Load env ──────────────────────────────────────────────────────────────────
load_dotenv()

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Resume Ripper 🔥",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Inject CSS ────────────────────────────────────────────────────────────────
st.markdown(get_css(), unsafe_allow_html=True)

# ── Theme toggle ──────────────────────────────────────────────────────────────
components.html(get_theme_toggle_js(), height=0)

# ── Hero ──────────────────────────────────────────────────────────────────────
render_hero()

# ── How It Works ──────────────────────────────────────────────────────────────
render_how_it_works()

# ═══════════════════════════════════════════════════════════════════════════════
#  UPLOAD YOUR RESUME
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="section-label">Upload Your Resume</div>', unsafe_allow_html=True)

api_key = os.getenv("OPENAI_API_KEY", "")

uploaded_file = st.file_uploader(
    "📂 Upload Your Resume",
    help="Supports PDF, DOCX & TXT · Max 10MB · Your file stays private",
)

render_upload_zone_js()

# Track whether a valid file is ready
if "file_valid" not in st.session_state:
    st.session_state["file_valid"] = False

if uploaded_file:
    file_bytes = uploaded_file.getvalue()
    size_kb = len(file_bytes) / 1024
    ext = uploaded_file.name.rsplit('.', 1)[-1].upper()

    logger.info(f"📤 File uploaded: {uploaded_file.name} ({size_kb:.1f} KB)")

    # Validate file type & size
    try:
        validate_file(file_bytes, uploaded_file.name)
        st.session_state["file_valid"] = True
    except ValueError as e:
        st.session_state["file_valid"] = False
        logger.warning(f"❌ Validation failed for {uploaded_file.name}: {e}")
        st.error(
            f"⚠️ **Invalid file format** — You uploaded a `.{ext.lower()}` file.\n\n"
            f"Supported formats: **PDF**, **DOCX**, **TXT** only.\n\n"
            f"Please upload a valid resume file and try again."
        )

    if st.session_state["file_valid"]:
        # Save to temp directory
        temp_dir = tempfile.mkdtemp(prefix="resume_roaster_")
        temp_path = os.path.join(temp_dir, uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(file_bytes)
        st.session_state["temp_resume_path"] = temp_path
        logger.info(f"💾 File saved to temp: {temp_path}")

        render_file_info_card(uploaded_file.name, ext, size_kb)
else:
    st.session_state["file_valid"] = False


# ═══════════════════════════════════════════════════════════════════════════════
#  CHOOSE YOUR ROASTER + ROAST  (only shown when file is valid)
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.get("file_valid", False):
    selected_key, sel = render_personality_selector()

    # ── Roast Button ──────────────────────────────────────────────────────────
    roast_clicked = st.button("🔥 ROAST MY RESUME", use_container_width=True, key="roast_btn")

    # ── Roast Flow ────────────────────────────────────────────────────────────
    if roast_clicked:
        logger.info(f"🔥 ROAST BUTTON CLICKED — Personality: {sel['name']}")

        if not uploaded_file:
            st.warning("📄 Please upload your resume first!")
            st.stop()

        # Extract text first (before API key check so logs always show)
        with st.spinner("📖 Reading your resume..."):
            try:
                file_bytes = uploaded_file.getvalue()
                resume_text = extract_text(file_bytes, uploaded_file.name)
            except Exception as e:
                logger.error(f"❌ Text extraction failed: {e}")
                st.error(f"❌ Failed to read file: {e}")
                st.stop()

        logger.info(f"📝 Extracted text length: {len(resume_text):,} characters")

        if len(resume_text.strip()) < 50:
            logger.warning("⚠️ Resume text too short (< 50 chars)")
            st.error("📄 Your resume seems empty or too short. Is this really a resume?")
            st.stop()

        # Now check API key
        if not api_key or api_key == "sk-your-key-here":
            logger.error("❌ No API key set")
            st.error("🔑 OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")
            st.stop()

        # Roast it with the selected personality!
        logger.info(f"🔥 Sending to OpenAI (personality: {sel['name']})...")
        logger.info(f"📨 TEXT BEING SENT TO AI ({len(resume_text[:12000]):,} chars):\n{'─'*60}\n{resume_text[:12000]}\n{'─'*60}")

        stream_fn = get_roaster_stream(selected_key)
        score_extractor = get_score_extractor(selected_key)

        # ── Stream response into a live placeholder ────────────────────────────
        stream_placeholder = st.empty()
        roast_result = ""
        start_time = time.time()
        last_render = start_time

        try:
            for chunk in stream_fn(resume_text, api_key):
                roast_result += chunk
                now = time.time()
                # Throttle UI updates to ~20fps to avoid hammering Streamlit
                if now - last_render >= 0.05:
                    stream_placeholder.markdown(roast_result + " ▌")
                    last_render = now
        except Exception as e:
            logger.error(f"❌ Roast stream failed: {e}")
            st.error(f"❌ Roasting failed: {e}")
            st.stop()

        elapsed = time.time() - start_time
        stream_placeholder.empty()

        score_breakdown = score_extractor(roast_result)
        logger.info(f"✅ Roast complete in {elapsed:.1f}s — {len(roast_result):,} chars")

        render_roast_results(roast_result, score_breakdown, sel, elapsed)


# ── Footer ────────────────────────────────────────────────────────────────────
render_footer()
