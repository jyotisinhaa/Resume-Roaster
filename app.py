"""
🔥 Resume Ripper AI — Upload your resume, get brutally honest feedback.
"""

import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv
import os
import time
import tempfile
import logging

from parser import extract_text, validate_file

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
    /* Hide the SVG cloud icon — keep in DOM for drag events */
    [data-testid="stFileUploaderDropzone"] svg {
        visibility: hidden !important;
        height: 0 !important;
        width: 0 !important;
        overflow: hidden !important;
        position: absolute !important;
    }
    /* Hide the "Drag and drop" text and "Limit 200MB" text — keep in DOM */
    [data-testid="stFileUploaderDropzone"] > div > div:first-child > div,
    [data-testid="stFileUploaderDropzone"] > div > div:first-child > span,
    [data-testid="stFileUploaderDropzone"] > div > div:first-child > small,
    [data-testid="stFileUploaderDropzone"] > div > small,
    [data-testid="stFileUploader"] small {
        visibility: hidden !important;
        height: 0 !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
        font-size: 0 !important;
        line-height: 0 !important;
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

    /* ── Personality Cards ── */
    .persona-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
        margin-bottom: 1rem;
    }
    .persona-grid-row2 {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin-bottom: 1.5rem;
        max-width: 67%;
        margin-left: auto;
        margin-right: auto;
    }
    .persona-card {
        background: #15100c;
        border: 2px solid #2a1f18;
        border-radius: 16px;
        padding: 1.5rem 1.2rem 1.3rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        user-select: none;
    }
    .persona-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: var(--accent-grad);
        opacity: 0;
        transition: opacity 0.3s;
    }
    .persona-card:hover {
        transform: translateY(-5px);
        border-color: var(--accent-color, #FF8C0055);
        box-shadow: 0 12px 40px var(--accent-glow, rgba(255,140,0,0.12));
    }
    .persona-card:hover::before { opacity: 1; }
    .persona-card.selected {
        border-color: var(--accent-color, #FF8C00);
        box-shadow: 0 0 30px var(--accent-glow, rgba(255,140,0,0.2)),
                    inset 0 0 25px var(--accent-glow-inner, rgba(255,140,0,0.04));
        background: #1a120c;
    }
    .persona-card.selected::before { opacity: 1; }
    .persona-card.selected .persona-icon {
        transform: scale(1.15);
    }
    .persona-card.selected .persona-name {
        color: var(--accent-color, #FF8C00);
    }
    .persona-icon {
        font-size: 2.6rem;
        margin-bottom: 0.7rem;
        transition: transform 0.3s;
        filter: drop-shadow(0 0 10px var(--accent-glow, rgba(255,140,0,0.2)));
    }
    .persona-name {
        font-weight: 800;
        font-size: 1rem;
        color: #e0d5cc;
        margin-bottom: 0.4rem;
        letter-spacing: 0.5px;
        transition: color 0.3s;
    }
    .persona-tagline {
        font-size: 0.78rem;
        color: #7a6e64;
        line-height: 1.45;
        font-style: italic;
    }
    .persona-check {
        position: absolute;
        top: 10px;
        right: 12px;
        font-size: 0.85rem;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .persona-card.selected .persona-check {
        opacity: 1;
    }
    .persona-selected-banner {
        text-align: center;
        padding: 0.7rem 1.2rem;
        border-radius: 12px;
        background: #1a130d;
        border: 1px solid #FF8C0033;
        margin-bottom: 1.2rem;
    }
    .persona-selected-banner .sel-icon { font-size: 1.4rem; }
    .persona-selected-banner .sel-name {
        font-weight: 700;
        color: #FF8C00;
        font-size: 0.92rem;
    }
    .persona-selected-banner .sel-tag {
        color: #7a6e64;
        font-size: 0.8rem;
        font-style: italic;
    }
    /* Hide the radio widget used for state management */
    div[data-testid="stRadio"].persona-radio-hidden {
        position: absolute;
        opacity: 0;
        height: 0;
        overflow: hidden;
        pointer-events: none;
    }

    /* ── Theme Toggle Button ── */
    .theme-toggle {
        position: fixed;
        top: 14px;
        right: 120px;
        z-index: 999999;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        border: 2px solid #2a1f18;
        background: #15100c;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 12px rgba(0,0,0,0.4);
        line-height: 1;
        padding: 0;
    }
    .theme-toggle:hover {
        transform: scale(1.12);
        border-color: #FF8C00;
        box-shadow: 0 4px 20px rgba(255,140,0,0.25);
    }

    /* ══════════════════════════════════════════════════════════
       LIGHT MODE OVERRIDES
       ══════════════════════════════════════════════════════════ */
    .stApp.light-mode {
        background: radial-gradient(ellipse at top, #fefcfa 0%, #f5f0eb 40%, #f0ebe5 100%) !important;
        color: #2d2420 !important;
    }
    .stApp.light-mode .stMarkdown,
    .stApp.light-mode .stMarkdown p,
    .stApp.light-mode .stMarkdown li,
    .stApp.light-mode .stMarkdown h1,
    .stApp.light-mode .stMarkdown h2,
    .stApp.light-mode .stMarkdown h3,
    .stApp.light-mode .stMarkdown h4 {
        color: #2d2420 !important;
    }
    /* Hero */
    .stApp.light-mode .hero-subtitle { color: #8a7e74 !important; }
    /* Step cards */
    .stApp.light-mode .step-card {
        background: #ffffff;
        border-color: #e8e0d8;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    }
    .stApp.light-mode .step-card:hover {
        box-shadow: 0 8px 30px rgba(255,140,0,0.08);
        border-color: #FF8C0055;
    }
    .stApp.light-mode .step-num { color: #e8e0d8; }
    .stApp.light-mode .step-title { color: #2d2420; }
    .stApp.light-mode .step-desc { color: #8a7e74; }
    /* Upload zone */
    .stApp.light-mode [data-testid="stFileUploader"] {
        background: #fdfcfb !important;
        border-color: #FF8C0055 !important;
    }
    .stApp.light-mode [data-testid="stFileUploader"]:hover {
        border-color: #FF8C0088 !important;
        box-shadow: 0 0 40px rgba(255,140,0,0.06), inset 0 0 30px rgba(255,140,0,0.01) !important;
    }
    .stApp.light-mode [data-testid="stFileUploader"] label p {
        color: #2d2420 !important;
    }
    /* File info card */
    .stApp.light-mode .file-info-card {
        background: #ffffff;
        border-color: #FF8C0022;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }
    .stApp.light-mode .file-info-name { color: #2d2420; }
    .stApp.light-mode .file-info-meta { color: #8a7e74; }
    /* Persona cards */
    .stApp.light-mode .persona-card {
        background: #ffffff;
        border-color: #e8e0d8;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }
    .stApp.light-mode .persona-card:hover {
        background: #fffcf9;
    }
    .stApp.light-mode .persona-card.selected {
        background: #fffaf5;
    }
    .stApp.light-mode .persona-name { color: #2d2420; }
    .stApp.light-mode .persona-card.selected .persona-name {
        color: var(--accent-color, #FF8C00);
    }
    .stApp.light-mode .persona-tagline { color: #8a7e74; }
    .stApp.light-mode .persona-selected-banner {
        background: #fffaf5;
        border-color: #FF8C0033;
    }
    /* Roast result */
    .stApp.light-mode .roast-result {
        background: #ffffff;
        border-color: #FF8C0033;
        box-shadow: 0 4px 30px rgba(255,140,0,0.04);
        color: #2d2420;
    }
    /* Buttons */
    .stApp.light-mode .stButton > button {
        background: #ffffff !important;
        color: #2d2420 !important;
        border-color: #e8e0d8 !important;
    }
    .stApp.light-mode .stButton > button:hover {
        border-color: #FF8C00 !important;
        box-shadow: 0 4px 20px rgba(255,140,0,0.1) !important;
    }
    /* Footer & divider */
    .stApp.light-mode .footer { color: #8a7e74; }
    .stApp.light-mode .footer b { color: #5a4e44; }
    .stApp.light-mode hr { border-color: #e8e0d8 !important; }
    /* Streamlit code blocks */
    .stApp.light-mode .stCode,
    .stApp.light-mode [data-testid="stCode"] {
        background: #faf7f4 !important;
        color: #2d2420 !important;
    }
    /* Section label line */
    .stApp.light-mode .section-label::after {
        background: linear-gradient(90deg, #FF8C0044, transparent);
    }
    /* Toggle button in light mode */
    .stApp.light-mode .theme-toggle {
        background: #ffffff;
        border-color: #e8e0d8;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }
    .stApp.light-mode .theme-toggle:hover {
        border-color: #FF8C00;
        box-shadow: 0 4px 20px rgba(255,140,0,0.15);
    }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  THEME TOGGLE (top-right sun/moon icon)
# ═══════════════════════════════════════════════════════════════════════════════
components.html("""
<script>
(function() {
    const main = window.parent.document;
    const STORAGE_KEY = 'resume_roaster_theme';

    function getApp() {
        return main.querySelector('[data-testid="stAppViewContainer"]')?.closest('.stApp')
            || main.querySelector('.stApp');
    }

    function applyTheme(theme) {
        const app = getApp();
        if (!app) return;
        if (theme === 'light') {
            app.classList.add('light-mode');
        } else {
            app.classList.remove('light-mode');
        }
        // Update toggle icon
        const btn = main.querySelector('.theme-toggle');
        if (btn) btn.textContent = theme === 'light' ? '🌙' : '☀️';
        localStorage.setItem(STORAGE_KEY, theme);
    }

    function injectToggle() {
        if (main.querySelector('.theme-toggle')) return;
        const btn = document.createElement('div');
        btn.className = 'theme-toggle';
        const saved = localStorage.getItem(STORAGE_KEY) || 'dark';
        btn.textContent = saved === 'light' ? '🌙' : '☀️';
        btn.title = 'Toggle light/dark mode';
        btn.addEventListener('click', function() {
            const app = getApp();
            if (!app) return;
            const isLight = app.classList.contains('light-mode');
            applyTheme(isLight ? 'dark' : 'light');
        });
        // Append to stApp so CSS scoping works
        const app = getApp();
        if (app) app.appendChild(btn);
    }

    function init() {
        injectToggle();
        const saved = localStorage.getItem(STORAGE_KEY) || 'dark';
        applyTheme(saved);
    }

    // Run on load and re-check periodically (Streamlit re-renders)
    init();
    setInterval(init, 500);
})();
</script>
""", height=0)

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
            el.style.visibility = 'hidden';
            el.style.height = '0';
            el.style.overflow = 'hidden';
            el.style.margin = '0';
            el.style.padding = '0';
        });
        dz.querySelectorAll('small').forEach(s => {
            s.style.visibility = 'hidden';
            s.style.height = '0';
            s.style.overflow = 'hidden';
        });

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
    main.querySelectorAll('[data-testid="stFileUploader"] small').forEach(s => {
        s.style.visibility = 'hidden';
        s.style.height = '0';
        s.style.overflow = 'hidden';
    });
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
#  CHOOSE YOUR ROASTER  (only shown when file is valid)
# ═══════════════════════════════════════════════════════════════════════════════

# Personality definitions
PERSONALITIES = {
    "brutal_recruiter": {
        "icon": "😤",
        "name": "Brutal Recruiter",
        "tagline": "No mercy. Your resume has 6 seconds.",
        "accent_from": "#FF4B4B",
        "accent_to": "#CC0000",
    },
    "ats_scanner": {
        "icon": "🤖",
        "name": "ATS Scanner",
        "tagline": "Beep boop. Scanning for red flags.",
        "accent_from": "#00C9FF",
        "accent_to": "#0066FF",
    },
    "career_coach": {
        "icon": "🧑‍🏫",
        "name": "Career Coach",
        "tagline": "Tough love with a growth mindset.",
        "accent_from": "#22C55E",
        "accent_to": "#16A34A",
    },
    "internet_troll": {
        "icon": "🧌",
        "name": "Internet Troll",
        "tagline": "Maximum sarcasm. Zero chill.",
        "accent_from": "#A855F7",
        "accent_to": "#7C3AED",
    },
    "faang_manager": {
        "icon": "👔",
        "name": "FAANG Manager",
        "tagline": "Big Tech bar raiser. Show me impact.",
        "accent_from": "#F59E0B",
        "accent_to": "#D97706",
    },
}

if st.session_state.get("file_valid", False):
    st.markdown('<div class="section-label">Choose Your Roaster</div>', unsafe_allow_html=True)

    # Initialize personality selection
    if "selected_personality" not in st.session_state:
        st.session_state["selected_personality"] = "brutal_recruiter"

    # Build HTML card grid
    persona_keys = list(PERSONALITIES.keys())
    selected_key = st.session_state["selected_personality"]

    def _card_html(key, p, is_selected):
        sel_cls = " selected" if is_selected else ""
        return (
            f'<div class="persona-card{sel_cls}" data-persona="{key}" '
            f'style="--accent-grad: linear-gradient(90deg, {p["accent_from"]}, {p["accent_to"]}); '
            f'--accent-color: {p["accent_from"]}; '
            f'--accent-glow: {p["accent_from"]}33; '
            f'--accent-glow-inner: {p["accent_from"]}0a;">'
            f'  <div class="persona-check">✓</div>'
            f'  <div class="persona-icon">{p["icon"]}</div>'
            f'  <div class="persona-name">{p["name"]}</div>'
            f'  <div class="persona-tagline">{p["tagline"]}</div>'
            f'</div>'
        )

    row1_html = '<div class="persona-grid">' + ''.join(
        _card_html(k, PERSONALITIES[k], k == selected_key) for k in persona_keys[:3]
    ) + '</div>'

    row2_html = '<div class="persona-grid-row2">' + ''.join(
        _card_html(k, PERSONALITIES[k], k == selected_key) for k in persona_keys[3:]
    ) + '</div>'

    st.markdown(row1_html + row2_html, unsafe_allow_html=True)

    # Hidden radio for state management
    persona_labels = [f"{PERSONALITIES[k]['icon']} {PERSONALITIES[k]['name']}" for k in persona_keys]
    default_idx = persona_keys.index(selected_key)
    chosen_label = st.radio(
        "roaster_pick",
        options=persona_labels,
        index=default_idx,
        horizontal=True,
        label_visibility="collapsed",
        key="persona_radio",
    )
    # Sync radio → session state
    chosen_idx = persona_labels.index(chosen_label)
    st.session_state["selected_personality"] = persona_keys[chosen_idx]
    selected_key = st.session_state["selected_personality"]
    sel = PERSONALITIES[selected_key]

    # JS: clicking a card triggers the corresponding radio option
    components.html(f"""
    <script>
    (function() {{
        const main = window.parent.document;
        const KEYS = {persona_keys};
        const LABELS = {persona_labels};

        function setupCardClicks() {{
            const cards = main.querySelectorAll('.persona-card[data-persona]');
            if (!cards.length) return;

            cards.forEach(card => {{
                if (card.dataset.clickBound) return;
                card.dataset.clickBound = 'true';
                card.addEventListener('click', function() {{
                    const key = this.dataset.persona;
                    const idx = KEYS.indexOf(key);
                    if (idx === -1) return;

                    // Find the radio widget and click the right option
                    const radios = main.querySelectorAll('[data-testid="stRadio"] input[type="radio"]');
                    if (radios[idx]) {{
                        radios[idx].click();
                    }}

                    // Visual feedback: update selected state immediately
                    cards.forEach(c => c.classList.remove('selected'));
                    this.classList.add('selected');
                }});
            }});
        }}

        // Also hide the radio widget visually
        function hideRadio() {{
            const radios = main.querySelectorAll('[data-testid="stRadio"]');
            radios.forEach(r => {{
                if (r.querySelector('input[type="radio"]')) {{
                    r.style.position = 'absolute';
                    r.style.opacity = '0';
                    r.style.height = '0';
                    r.style.overflow = 'hidden';
                    r.style.pointerEvents = 'none';
                }}
            }});
        }}

        setInterval(() => {{ setupCardClicks(); hideRadio(); }}, 300);
        setupCardClicks();
        hideRadio();
    }})();
    </script>
    """, height=0)

    # Show selected personality banner
    st.markdown(
        f'<div class="persona-selected-banner">'
        f'  <span class="sel-icon">{sel["icon"]}</span> '
        f'  <span class="sel-name">{sel["name"]}</span> — '
        f'  <span class="sel-tag">{sel["tagline"]}</span>'
        f'</div>',
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

        # Import the correct roaster based on personality
        from roasters import get_roaster
        roaster_fn = get_roaster(selected_key)

        with st.spinner(f"{sel['icon']} {sel['name']} is reviewing your resume..."):
            start_time = time.time()
            try:
                roast_result = roaster_fn(resume_text, api_key)
                elapsed = time.time() - start_time
                logger.info(f"✅ Roast complete in {elapsed:.1f}s")
                logger.info(f"📋 Roast result length: {len(roast_result):,} characters")
            except Exception as e:
                logger.error(f"❌ Roast API call failed: {e}")
                st.error(f"❌ Roasting failed: {e}")
                st.stop()

        # Display results
        st.markdown('<div class="section-label">Your Roast</div>', unsafe_allow_html=True)

        badge_text = f"{sel['icon']} {sel['name']}"

        st.markdown(
            f'<div class="roast-result"><span class="roast-badge">{badge_text}</span>',
            unsafe_allow_html=True,
        )
        st.markdown(roast_result)
        st.markdown(
            f'<br><div style="color:#5a4e44; font-size:0.75rem; margin-top:1rem;">'
            f'{sel["icon"]} <i>Roasted by {sel["name"]} · Resume Ripper AI · {elapsed:.1f}s</i></div>',
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # Save to session for sharing
        st.session_state["last_roast"] = roast_result

        # Share section
        st.markdown("")
        col1, col2 = st.columns(2)
        with col1:
            share_text = f"I just got my resume roasted by the {sel['name']} 🔥\nWould you survive the roast? 😅\n#ResumeRoaster #AI #CareerTips"
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
