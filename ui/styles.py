"""
All CSS styles for the Resume Roaster app — dark mode base + light mode overrides.
"""


def get_css() -> str:
    """Return the complete CSS stylesheet as a string."""
    return """
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

        /* ATS Score Breakdown */
        .ats-score-breakdown {
            margin: 1.2rem 0 1.5rem 0;
            padding: 1rem 1.2rem 0.5rem 1.2rem;
            background: #18120b;
            border-radius: 12px;
            border: 1px solid #2a1f18;
            max-width: 480px;
            margin-left: auto;
            margin-right: auto;
            box-shadow: 0 2px 12px #00000022;
        }
        /* Hide empty score breakdown divs (no bars) */
        .ats-score-breakdown:empty {
            display: none !important;
            background: none !important;
            border: none !important;
            box-shadow: none !important;
            padding: 0 !important;
            margin: 0 !important;
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
"""
