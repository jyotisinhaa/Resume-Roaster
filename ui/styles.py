"""
All CSS styles for the Resume Roaster app — dark mode base + light mode overrides.
"""


def get_css() -> str:
    return """
<style>
    /* ── Hero Description ── */
    .stApp:not(.light-mode) .hero-desc {
        color: #bdbdbd !important;
    }
    /* ── Dark Mode Hero Text ── */
    .stApp:not(.light-mode) .hero-main-text {
        color: #fff !important;
    }
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
        font-size: 2.2rem;
        font-weight: 900;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        color: #FF8C00;
        margin-bottom: 2.2rem;
        margin-top: 4rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        line-height: 1.08;
        width: 100%;
        box-sizing: border-box;
    }
        /* Upload Zone Customization */
        [data-testid="stFileUploader"] {
            background: #1a1207 !important;
            border: 3px solid #FF8C00 !important;
            border-radius: 22px !important;
            box-shadow: 0 6px 32px #ff8c0033, 0 2px 0 #FF8C00 inset !important;
            padding: 2.2rem 2.2rem 1.7rem 2.2rem !important;
            margin-bottom: 2.2rem !important;
            margin-top: 1.2rem !important;
            font-size: 1.25rem !important;
            font-weight: 800 !important;
            color: #FF8C00 !important;
            text-align: center !important;
            transition: box-shadow 0.18s, border 0.18s;
        }
        [data-testid="stFileUploader"]:hover {
            box-shadow: 0 12px 40px #FF8C0033, 0 2px 0 #FF8C00 inset !important;
            border-color: #FF8C00 !important;
        }
        [data-testid="stFileUploader"] .supported-formats-line {
            font-size: 1.08rem !important;
            color: #FF8C00 !important;
            margin-bottom: 1.1rem !important;
            font-weight: 700 !important;
        }
        [data-testid="stFileUploader"] button, [data-testid="stFileUploader"] .css-1cpxqw2 {
            font-size: 1.15rem !important;
            font-weight: 900 !important;
            padding: 0.7em 2.2em !important;
            border-radius: 1.5em !important;
            background: linear-gradient(90deg,#FF8C00,#FF6B35) !important;
            color: #fff !important;
            border: none !important;
            box-shadow: 0 2px 8px #FF8C0033 !important;
            margin-top: 0.7em !important;
            text-transform: uppercase !important;
            letter-spacing: 1.2px !important;
            transition: background 0.18s;
        }
        [data-testid="stFileUploader"] button:hover, [data-testid="stFileUploader"] .css-1cpxqw2:hover {
            background: linear-gradient(90deg,#FF6B35,#FF8C00) !important;
            color: #fff !important;
        }
    .section-label::after {
        content: '';
        flex: 1;
        height: 2px;
        border-radius: 2px;
        background: linear-gradient(90deg, #FF8C00aa, transparent);
        min-width: 0;
    }
    /* Ensure Streamlit's markdown container doesn't shrink-wrap the section label */
    [data-testid="stMarkdownContainer"]:has(.section-label) {
        width: 100% !important;
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
        width: 100% !important;
        margin-left: 0 !important;
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
        font-weight: 900 !important;
        font-family: 'Arial Black', Impact, 'Helvetica Neue', sans-serif !important;
        font-size: 1.15rem !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 1rem 2rem !important;
        width: 100% !important;
        box-shadow: 0 6px 30px rgba(255, 75, 75, 0.3) !important;
    }
    /* Target any child elements (p, span, div) Streamlit wraps button text in */
    div[data-testid="stButton"] > button[kind="secondary"]:last-of-type *,
    button[key="roast_btn"] * {
        font-weight: 900 !important;
        font-family: 'Arial Black', Impact, 'Helvetica Neue', sans-serif !important;
        color: white !important;
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
        margin-top: 2.8rem;
        box-shadow: 0 4px 30px rgba(255, 140, 0, 0.06);
        color: #e0d5cc;
    }
    .roast-badge {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: linear-gradient(90deg, #FF6B35, #FF8C00);
        color: white;
        padding: 0.7rem 1.5rem 0.9rem 1.5rem;
        border-radius: 22px;
        margin: 0 auto 1.5rem auto;
        box-shadow: 0 2px 12px #ff8c0033;
        width: fit-content;
    }
    .roast-badge-icon {
        font-size: 2.1rem;
        margin-bottom: 0.2rem;
    }
    .roast-badge-name {
        font-size: 1.08rem;
        font-weight: 700;
        letter-spacing: 0.01em;
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
    .pc-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 1rem;
        margin-bottom: 1.4rem;
        width: 100%;
    }
    .persona-card {
        background: linear-gradient(160deg, #1c1610 0%, #141009 100%);
        border: 1.5px solid #3a2a1e;
        border-radius: 20px;
        padding: 1.4rem 0.85rem 1.3rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.28s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        user-select: none;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    /* Gradient top accent bar */
    .persona-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: var(--accent-grad);
        opacity: 0.5;
        transition: opacity 0.25s, height 0.25s;
        border-radius: 20px 20px 0 0;
    }
    /* Bottom inner glow */
    .persona-card::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 55%;
        background: linear-gradient(to top, var(--accent-glow-inner, transparent), transparent);
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .persona-card:hover {
        transform: translateY(-7px);
        border-color: var(--accent-color);
        box-shadow: 0 18px 48px var(--accent-glow), 0 0 0 1px var(--accent-color);
        background: linear-gradient(160deg, #221a12 0%, #18110a 100%);
    }
    .persona-card:hover::before { opacity: 1; height: 4px; }
    .persona-card:hover::after  { opacity: 1; }
    .persona-card.selected {
        border-color: var(--accent-color);
        box-shadow: 0 0 0 2px var(--accent-color), 0 10px 44px var(--accent-glow);
        background: linear-gradient(160deg, #201810 0%, #160e08 100%);
    }
    .persona-card.selected::before { opacity: 1; height: 4px; }
    .persona-card.selected::after  { opacity: 1; }
    .persona-card.selected .persona-name { color: var(--accent-color); }
    .persona-card.selected .persona-tagline { color: #c8bdb5; }
    .persona-card.selected .pc-icon-ring {
        box-shadow: 0 6px 24px var(--accent-glow);
    }
    /* Selected check badge */
    .persona-check {
        position: absolute;
        top: 10px; right: 10px;
        width: 22px; height: 22px;
        border-radius: 50%;
        background: var(--accent-color, #FF8C00);
        color: #fff;
        font-size: 0.72rem;
        font-weight: 900;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.2s;
        box-shadow: 0 2px 8px var(--accent-glow, rgba(255,140,0,0.4));
    }
    .persona-card.selected .persona-check { opacity: 1; }
    /* Badge chip */
    .pc-badge {
        font-size: 0.6rem;
        font-weight: 800;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        padding: 4px 10px;
        border-radius: 20px;
        margin-bottom: 0.9rem;
        opacity: 0.85;
        transition: opacity 0.25s;
        white-space: nowrap;
    }
    .persona-card:hover .pc-badge,
    .persona-card.selected .pc-badge { opacity: 1; }
    /* Icon ring */
    .pc-icon-ring {
        width: 72px; height: 72px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        transition: transform 0.28s, box-shadow 0.28s;
    }
    .persona-card:hover .pc-icon-ring { transform: scale(1.1); }
    .persona-card.selected .pc-icon-ring { transform: scale(1.12); }
    .persona-icon {
        font-size: 2.6rem;
        line-height: 1;
        display: block;
        filter: drop-shadow(0 2px 10px var(--accent-glow, rgba(255,140,0,0.25)));
    }
    /* Name */
    .persona-name {
        font-weight: 900;
        font-size: 0.95rem;
        color: #f0e8e0 !important;
        margin-bottom: 0.4rem;
        letter-spacing: 0.2px;
        transition: color 0.25s;
        line-height: 1.2;
    }
    /* Tagline */
    .persona-tagline {
        font-size: 0.7rem;
        color: #c8beb6 !important;
        line-height: 1.5;
        font-style: italic;
    }
    /* ── Selected Banner ── */
    .persona-selected-banner {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1.1rem 1.5rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #1e1510 0%, #160f08 100%);
        border: 1.5px solid #FF8C0044;
        margin-bottom: 1.5rem;
        gap: 1rem;
        box-shadow: 0 6px 28px rgba(255,140,0,0.1);
    }
    .psb-left {
        display: flex;
        align-items: center;
        gap: 1rem;
        flex: 1;
        min-width: 0;
    }
    .psb-icon {
        width: 54px; height: 54px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        flex-shrink: 0;
    }
    .psb-info { text-align: left; flex: 1; min-width: 0; }
    .psb-label {
        font-size: 0.62rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #a09890 !important;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .psb-name {
        font-weight: 900;
        font-size: 1.1rem;
        color: #f0e8e0 !important;
        margin-bottom: 0.15rem;
        line-height: 1.2;
    }
    .psb-tag {
        font-size: 0.78rem;
        color: #c8beb6 !important;
        font-style: italic;
        margin-bottom: 0.25rem;
    }
    .psb-desc {
        font-size: 0.78rem;
        color: #ddd5cc !important;
        line-height: 1.55;
    }
    .psb-pill {
        font-size: 0.66rem;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: #fff;
        padding: 7px 16px;
        border-radius: 20px;
        white-space: nowrap;
        flex-shrink: 0;
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

    /* ── Background & Global ── */
    .stApp.light-mode {
        background: linear-gradient(160deg, #fff9f3 0%, #fdf4ea 45%, #f8ede0 100%) !important;
        color: #111111 !important;
    }
    /* ── Dark text for Streamlit native widgets + custom classes ── */
    /* Only targets block-level/label elements — never spans (roast results use inline-colored spans) */
    .stApp.light-mode p,
    .stApp.light-mode label,
    .stApp.light-mode h1, .stApp.light-mode h2,
    .stApp.light-mode h3, .stApp.light-mode h4,
    .stApp.light-mode li,
    .stApp.light-mode [data-testid="stWidgetLabel"],
    .stApp.light-mode [data-testid="stWidgetLabel"] *,
    .stApp.light-mode [data-baseweb="radio"] label,
    .stApp.light-mode [data-baseweb="radio"] div,
    .stApp.light-mode .stMarkdown,
    .stApp.light-mode .stMarkdown p,
    .stApp.light-mode .stMarkdown li,
    .stApp.light-mode .stMarkdown h1,
    .stApp.light-mode .stMarkdown h2,
    .stApp.light-mode .stMarkdown h3,
    .stApp.light-mode .stMarkdown h4 { color: #111111 !important; }

    /* Our custom classes that have hardcoded light colors in base CSS */
    .stApp.light-mode .persona-name,
    .stApp.light-mode .file-info-name,
    .stApp.light-mode .file-info-card .file-info-name,
    .stApp.light-mode .psb-name { color: #111111 !important; }

    /* Roast result section headers (white text, visible on dark bg in dark mode) */
    .stApp.light-mode .rsh { color: #111111 !important; }

    /* ── Persona note cards (Gut Reaction, First Impression, Coach's Note, Hiring Signal etc.) ── */
    .stApp.light-mode .persona-note {
        background: #ffffff !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.07) !important;
        /* border preserved from inline style so accent color stays */
    }
    .stApp.light-mode .persona-note-text {
        color: #111111 !important;
    }
    .stApp.light-mode .persona-note-subtext {
        color: #3d2b1a !important;
    }
    /* Keep accent label color visible */
    .stApp.light-mode .persona-note-label {
        opacity: 1 !important;
    }

    /* ── Final Verdict light mode: extra lines ── */
    .stApp.light-mode .fv-extra-line { color: #3d2a1a !important; }

    /* HM Verdict / Interview decision cards — light mode */
    .stApp.light-mode .hm-decision-card {
        background: #ffffff !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08) !important;
        border-width: 2px !important;
        /* border-color preserved from inline so accent color stays */
    }

    /* Muted gray inline text on light backgrounds — force darker */
    .stApp.light-mode [style*="color:#9CA3AF"],
    .stApp.light-mode [style*="color:#6B7280"],
    .stApp.light-mode [style*="color:#9ca3af"],
    .stApp.light-mode [style*="color:#6b7280"] { color: #4a3828 !important; }

    /* Accent/muted colors */
    .stApp.light-mode .section-label { color: #E65C00 !important; }
    .stApp.light-mode .hero-ai-badge { color: #E65C00 !important; }
    .stApp.light-mode .file-info-check { color: #22c55e !important; }
    .stApp.light-mode .persona-card.selected .persona-name { color: var(--accent-color) !important; }
    .stApp.light-mode .persona-card:hover .pc-desc,
    .stApp.light-mode .persona-card.selected .pc-desc { color: var(--accent-color) !important; opacity: 0.9 !important; }
    /* Muted secondary text */
    .stApp.light-mode .hero-subtitle,
    .stApp.light-mode .hero-desc,
    .stApp.light-mode .upload-subtitle,
    .stApp.light-mode .step-desc,
    .stApp.light-mode .file-info-meta,
    .stApp.light-mode .footer { color: #3d2b1a !important; }
    /* Persona card text — needs higher contrast on white */
    .stApp.light-mode .persona-name { color: #111111 !important; }
    .stApp.light-mode .persona-tagline { color: #4a3828 !important; }
    .stApp.light-mode .psb-label { color: #6a5244 !important; }
    .stApp.light-mode .psb-tag { color: #4a3828 !important; }
    .stApp.light-mode .psb-desc { color: #3a2a18 !important; }
    .stApp.light-mode .persona-card { background: #ffffff !important; border-color: #e8d8c4 !important; }
    .stApp.light-mode .persona-card.selected .persona-name { color: var(--accent-color) !important; }
    .stApp.light-mode .persona-card.selected .persona-tagline { color: #3a2a18 !important; }

    /* ── Hero ── */
    .stApp.light-mode .hero-main-text { color: #111111 !important; }
    .stApp.light-mode .hero-desc { color: #5a4030 !important; }
    .stApp.light-mode .hero-subtitle { color: #9a8878 !important; }
    /* Fix hardcoded dark hero badge pill */
    .stApp.light-mode .hero-ai-badge {
        background: #fff3e0 !important;
        color: #E65C00 !important;
        border: 1.5px solid #FF8C0040 !important;
        box-shadow: 0 2px 10px rgba(255,140,0,0.12) !important;
    }

    /* ── Section Labels ── */
    .stApp.light-mode .section-label { color: #E65C00 !important; }
    .stApp.light-mode .section-label::after {
        background: linear-gradient(90deg, #FF8C0088, transparent) !important;
    }

    /* ── Step Cards ── */
    .stApp.light-mode .step-card {
        background: #ffffff !important;
        border: 1.5px solid #ffd49a !important;
        box-shadow: 0 4px 20px rgba(255,140,0,0.09) !important;
    }
    .stApp.light-mode .step-card:hover {
        box-shadow: 0 10px 32px rgba(255,140,0,0.16) !important;
        border-color: #FF8C0077 !important;
    }
    /* ── Upload Zone ── */
    .stApp.light-mode [data-testid="stFileUploader"] {
        background: #fffdf8 !important;
        border: 2px dashed #FF8C0066 !important;
        box-shadow: 0 2px 18px rgba(255,140,0,0.07) !important;
    }
    .stApp.light-mode [data-testid="stFileUploader"]:hover {
        border-color: #FF8C00aa !important;
        box-shadow: 0 4px 30px rgba(255,140,0,0.13) !important;
    }
    /* Uploaded filename text inside the uploader widget */
    .stApp.light-mode [data-testid="stFileUploader"] span,
    .stApp.light-mode [data-testid="stFileUploader"] p,
    .stApp.light-mode [data-testid="stFileUploaderFileName"],
    .stApp.light-mode [data-testid="stFileUploaderFileName"] span,
    .stApp.light-mode [data-testid="stFileUploader"] section span,
    .stApp.light-mode [data-testid="stFileUploader"] section div span { color: #111111 !important; }

    /* ── File Info Card ── */
    .stApp.light-mode .file-info-card {
        background: #ffffff !important;
        border: 1.5px solid #ffd49a !important;
        box-shadow: 0 4px 16px rgba(255,140,0,0.08) !important;
    }

    /* ── Persona Cards ── */
    .stApp.light-mode .persona-card {
        background: #ffffff !important;
        border: 1.5px solid #e8d8c4 !important;
        box-shadow: 0 2px 14px rgba(0,0,0,0.07) !important;
    }
    .stApp.light-mode .persona-card:hover {
        background: #fffcf8 !important;
        box-shadow: 0 10px 36px var(--accent-glow), 0 0 0 1.5px var(--accent-color) !important;
    }
    .stApp.light-mode .persona-card.selected {
        background: #fffaf4 !important;
        box-shadow: 0 0 0 2px var(--accent-color), 0 10px 36px var(--accent-glow) !important;
    }

    /* ── Selected Banner ── */
    .stApp.light-mode .persona-selected-banner {
        background: #ffffff !important;
        border-color: #ffd49a !important;
        box-shadow: 0 4px 20px rgba(255,140,0,0.1) !important;
    }

    /* ── ATS Score Breakdown ── */
    .stApp.light-mode .ats-score-breakdown {
        background: #ffffff !important;
        border: 1px solid #edddc8 !important;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05) !important;
    }

    /* ── Roast Result — keep dark bg so light text stays readable ── */
    .stApp.light-mode .roast-result {
        background: #15100c !important;
        border-color: #FF8C0033 !important;
        box-shadow: 0 4px 30px rgba(255,140,0,0.12) !important;
    }

    /* ── Buttons ── */
    .stApp.light-mode .stButton > button {
        background: #ffffff !important;
        color: #111111 !important;
        border: 1.5px solid #edddc8 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
    }
    .stApp.light-mode .stButton > button:hover {
        border-color: #FF8C00 !important;
        box-shadow: 0 4px 20px rgba(255,140,0,0.15) !important;
    }

    /* ── Footer & Divider ── */
    .stApp.light-mode .footer { color: #9a8878 !important; }
    .stApp.light-mode .footer b { color: #6a5844 !important; }
    .stApp.light-mode hr { border-color: #edddc8 !important; }

    /* ── Code Blocks ── */
    .stApp.light-mode .stCode,
    .stApp.light-mode [data-testid="stCode"] {
        background: #faf6f0 !important;
        color: #111111 !important;
    }

    /* ── Theme Toggle ── */
    .stApp.light-mode .theme-toggle {
        background: #ffffff !important;
        border-color: #edddc8 !important;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08) !important;
    }
    .stApp.light-mode .theme-toggle:hover {
        border-color: #FF8C00 !important;
        box-shadow: 0 4px 20px rgba(255,140,0,0.2) !important;
    }

    /* ── Final Verdict ── */
    .final-verdict-card { }
    .fv-extra-line { color: #cccccc; }
</style>
"""
