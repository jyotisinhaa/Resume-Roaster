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
    /* Neutralize any outer container border Streamlit may inject (e.g. stVerticalBlockBorderWrapper) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: none !important;
        box-shadow: none !important;
        background: transparent !important;
    }

    [data-testid="stFileUploader"] {
        background: #110c08 !important;
        border: 2px dashed #FF8C0055 !important;
        border-radius: 20px !important;
        padding: 2.5rem 2rem 3.5rem !important;
        transition: border-color 0.3s, box-shadow 0.3s !important;
        text-align: center !important;
        width: 100% !important;
        margin-left: 0 !important;
        /* Override any default Streamlit blue/cyan borders */
        outline: none !important;
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
        text-transform: uppercase !important;
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
        margin-bottom: 1.8rem;
        width: 100%;
    }
    .persona-card {
        background: linear-gradient(160deg, #1f1812 0%, #140f08 60%, #0e0b06 100%);
        border: 1.5px solid #3a2a1a;
        border-radius: 22px;
        padding: 1.5rem 0.9rem 1.4rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        user-select: none;
        display: flex;
        flex-direction: column;
        align-items: center;
        min-height: 270px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.04);
    }
    /* Gradient top accent bar */
    .persona-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: var(--accent-grad);
        opacity: 0.55;
        transition: opacity 0.28s, height 0.28s;
        border-radius: 22px 22px 0 0;
    }
    /* Bottom inner glow */
    .persona-card::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 50%;
        background: linear-gradient(to top, var(--accent-glow-inner, transparent), transparent);
        pointer-events: none;
        opacity: 0.25;
        transition: opacity 0.3s;
    }
    /* Shimmer sweep */
    .pc-shimmer {
        position: absolute;
        top: 0; left: -120%; bottom: 0;
        width: 55%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
        transform: skewX(-18deg);
        transition: left 0.6s ease;
        pointer-events: none;
        z-index: 1;
    }
    .persona-card:hover .pc-shimmer { left: 170%; }
    .persona-card:hover {
        transform: translateY(-8px) scale(1.025);
        border-color: var(--accent-color);
        box-shadow: 0 20px 50px var(--accent-glow), 0 0 0 1px var(--accent-color), 0 4px 24px rgba(0,0,0,0.5);
        background: linear-gradient(160deg, #271e14 0%, #1a1209 60%, #110d07 100%);
    }
    .persona-card:hover::before { opacity: 1; height: 4px; }
    .persona-card:hover::after  { opacity: 0.65; }
    .persona-card.selected {
        border-color: var(--accent-color);
        box-shadow: 0 0 0 2px var(--accent-color), 0 12px 48px var(--accent-glow), 0 4px 24px rgba(0,0,0,0.5);
        background: linear-gradient(160deg, #241a11 0%, #180e08 60%, #100b06 100%);
    }
    .persona-card.selected::before { opacity: 1; height: 4px; }
    .persona-card.selected::after  { opacity: 0.8; }
    .persona-card.selected .persona-name { color: var(--accent-color); }
    .persona-card.selected .persona-tagline { color: #e0d8d0; }
    /* Selected check badge */
    .persona-check {
        position: absolute;
        top: 11px; right: 11px;
        width: 22px; height: 22px;
        border-radius: 50%;
        background: var(--accent-color, #FF8C00);
        color: #fff;
        font-size: 0.68rem;
        font-weight: 900;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.22s, transform 0.22s;
        box-shadow: 0 2px 12px var(--accent-glow, rgba(255,140,0,0.5));
        z-index: 2;
        transform: scale(0.7);
    }
    .persona-card.selected .persona-check {
        opacity: 1;
        transform: scale(1);
    }
    /* Icon wrap + conic-gradient outer ring */
    .pc-icon-wrap {
        margin-bottom: 0.9rem;
        transition: transform 0.3s cubic-bezier(0.4,0,0.2,1);
    }
    .persona-card:hover .pc-icon-wrap  { transform: scale(1.08); }
    .persona-card.selected .pc-icon-wrap { transform: scale(1.1); }
    .pc-icon-outer {
        border-radius: 50%;
        transition: box-shadow 0.3s;
    }
    .persona-card.selected .pc-icon-outer,
    .persona-card:hover .pc-icon-outer {
        box-shadow: 0 0 24px var(--accent-glow);
    }
    .pc-icon-ring {
        width: 74px; height: 74px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .persona-icon {
        font-size: 2.7rem;
        line-height: 1;
        display: block;
        filter: drop-shadow(0 2px 8px var(--accent-glow, rgba(255,140,0,0.25)));
        transition: filter 0.3s;
    }
    .persona-card:hover .persona-icon,
    .persona-card.selected .persona-icon {
        filter: drop-shadow(0 4px 16px var(--accent-glow, rgba(255,140,0,0.6)));
    }
    /* Thin accent divider */
    .pc-divider {
        width: 48%;
        height: 1px;
        margin: 0 auto 0.8rem;
        border-radius: 2px;
        opacity: 0.6;
        transition: width 0.3s, opacity 0.3s;
    }
    .persona-card:hover .pc-divider,
    .persona-card.selected .pc-divider { width: 72%; opacity: 1; }
    /* Name */
    .persona-name {
        font-weight: 900;
        font-size: 0.97rem;
        color: #f2eae2 !important;
        margin-bottom: 0.28rem;
        letter-spacing: 0.3px;
        transition: color 0.25s;
        line-height: 1.2;
    }
    /* Badge chip */
    .pc-badge {
        font-size: 0.58rem;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
        padding: 3px 11px;
        border-radius: 20px;
        margin-bottom: 0.7rem;
        opacity: 0.85;
        transition: opacity 0.25s, transform 0.22s;
        white-space: nowrap;
        z-index: 2;
    }
    .persona-card:hover .pc-badge,
    .persona-card.selected .pc-badge { opacity: 1; transform: scale(1.05); }
    /* Tagline */
    .persona-tagline {
        font-size: 0.7rem;
        color: #9e968e !important;
        line-height: 1.55;
        font-style: italic;
        transition: color 0.25s;
        z-index: 2;
        padding: 0 0.1rem;
    }
    /* Description — fades in when selected */
    .pc-desc {
        font-size: 0.65rem;
        color: #8a8280 !important;
        line-height: 1.5;
        margin-top: 0.55rem;
        opacity: 0;
        max-height: 0;
        overflow: hidden;
        transition: opacity 0.35s ease, max-height 0.38s ease;
        z-index: 2;
        padding: 0 0.1rem;
    }
    .persona-card.selected .pc-desc {
        opacity: 1;
        max-height: 80px;
        color: #c8c0b8 !important;
    }
    /* ── Selected Banner ── */
    .persona-selected-banner {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1.3rem 1.8rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #201813 0%, #160e08 100%);
        border: 1.5px solid #FF8C0033;
        margin-bottom: 1.5rem;
        gap: 1.2rem;
        box-shadow: 0 8px 40px rgba(0,0,0,0.4), 0 0 0 1px rgba(255,140,0,0.06), inset 0 1px 0 rgba(255,255,255,0.05);
        position: relative;
        overflow: hidden;
    }
    .persona-selected-banner::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent 0%, var(--psb-accent, #FF8C00) 40%, var(--psb-accent, #FF8C00) 60%, transparent 100%);
        opacity: 0.55;
    }
    .psb-left {
        display: flex;
        align-items: center;
        gap: 1.2rem;
        flex: 1;
        min-width: 0;
    }
    .psb-icon {
        width: 62px; height: 62px;
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        flex-shrink: 0;
        box-shadow: 0 4px 18px rgba(0,0,0,0.3);
    }
    .psb-info { text-align: left; flex: 1; min-width: 0; }
    .psb-label {
        font-size: 0.6rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #a09890 !important;
        font-weight: 700;
        margin-bottom: 0.25rem;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    .psb-label::before {
        content: '';
        display: inline-block;
        width: 6px; height: 6px;
        border-radius: 50%;
        background: var(--psb-accent, #FF8C00);
        flex-shrink: 0;
    }
    .psb-name {
        font-weight: 900;
        font-size: 1.28rem;
        color: var(--psb-accent, #f0e8e0) !important;
        margin-bottom: 0.3rem;
        line-height: 1.15;
        letter-spacing: 0.2px;
    }
    .psb-tag {
        font-size: 0.88rem;
        color: #e8e0d8 !important;
        font-style: normal;
        font-weight: 600;
        margin-bottom: 0.4rem;
        line-height: 1.4;
    }
    .psb-desc {
        font-size: 0.8rem;
        color: #a8a098 !important;
        line-height: 1.6;
        padding-left: 0.7rem;
        border-left: 2px solid var(--psb-accent, #FF8C0066);
    }
    .psb-pill {
        font-size: 0.66rem;
        font-weight: 800;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        color: #fff;
        padding: 8px 18px;
        border-radius: 20px;
        white-space: nowrap;
        flex-shrink: 0;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3);
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

    /* ── Consistent result section label ── */
    .result-label {
        font-size: 1.05rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.5px !important;
        text-transform: none !important;
        margin-bottom: 8px !important;
        display: block;
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
    .stApp.light-mode .psb-tag { color: #2a1a0a !important; font-weight: 600 !important; }
    .stApp.light-mode .psb-desc { color: #5a4030 !important; }
    .stApp.light-mode .persona-card { background: #ffffff !important; border-color: #e8d8c4 !important; }
    .stApp.light-mode .persona-card:hover { background: #fffaf5 !important; }
    .stApp.light-mode .persona-card.selected { background: #fffaf5 !important; }
    .stApp.light-mode .persona-card.selected .persona-name { color: var(--accent-color) !important; }
    .stApp.light-mode .persona-card.selected .persona-tagline { color: #3a2a18 !important; }
    .stApp.light-mode .pc-icon-ring { background: #f5efe8 !important; }
    .stApp.light-mode .pc-desc { color: #6a5244 !important; }
    .stApp.light-mode .persona-card.selected .pc-desc { color: #3a2a18 !important; }

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
    /* Score breakdown rows — dark background → light */
    .stApp.light-mode .ats-breakdown-row {
        background: #f5f0ea !important;
        background-color: #f5f0ea !important;
    }
    /* Bar track — dark navy → warm light gray */
    .stApp.light-mode .ats-bar-track {
        background: #ddd5cc !important;
    }
    /* Label text — light gray → near-black */
    .stApp.light-mode .ats-breakdown-label {
        color: #1a1008 !important;
    }

    /* ── ATS Scanner — Weak Bullets card ── */
    .stApp.light-mode .ats-wb-card {
        background: #f5f0ea !important;
        border-color: #e0d0c0 !important;
        box-shadow: 0 2px 12px rgba(0,0,0,0.07) !important;
    }
    .stApp.light-mode .ats-wb-row-orig {
        border-bottom-color: #e0d0c0 !important;
    }
    .stApp.light-mode .ats-wb-row-issue {
        background: rgba(239,68,68,0.06) !important;
        border-bottom-color: #e0d0c0 !important;
    }
    .stApp.light-mode .ats-wb-row-imp {
        background: rgba(34,197,94,0.06) !important;
    }
    .stApp.light-mode .ats-wb-text {
        color: #1a1008 !important;
    }
    .stApp.light-mode .ats-wb-badge-orig {
        background: #d0c8c0 !important;
        color: #1a1008 !important;
    }

    /* ── ATS Scanner — Keyword pills ── */
    .stApp.light-mode .ats-kw-pill {
        background: #f0ebe4 !important;
    }
    /* ── ATS Scanner — Keyword category headers & fallback text ── */
    .stApp.light-mode .ats-kw-cat,
    .stApp.light-mode .ats-kw-text {
        color: #4a3828 !important;
    }

    /* ── ATS Scanner — section divider line ── */
    .stApp.light-mode [style*="background:#222"] {
        background: #e0d5cc !important;
    }

    /* ── Roast Result — light background in light mode ── */
    .stApp.light-mode .roast-result {
        background: #faf7f2 !important;
        border-color: #e0cdb8 !important;
        box-shadow: 0 4px 30px rgba(255,140,0,0.08) !important;
    }

    /* ── Section headers (.rsh) — override inline white color in light mode ──
       (The base .rsh color rule is already at line ~716 above)              ── */
    .stApp.light-mode .rsh [style*="color:#ffffff"],
    .stApp.light-mode .rsh [style*="color:#fff"],
    .stApp.light-mode .rsh [style*="color: #fff"] { color: #111111 !important; }

    /* ── Hero score card — light background in light mode ── */
    .stApp.light-mode .hero-score-card {
        background: #faf7f2 !important;
        box-shadow: 0 2px 16px rgba(0,0,0,0.07) !important;
    }
    /* Ring track circle: was dark (e.g. #2a1a1a) — make it a soft warm gray on light bg */
    .stApp.light-mode .hero-score-card .ring-track {
        stroke: #ddd5cc !important;
    }

    /* ── Result item boxes (bullet cards across all personas) ──
       NOTE: not using .roast-area ancestor selector — Streamlit wraps each
       st.markdown() in its own div, so descendant selectors across calls fail. ── */
    .stApp.light-mode .result-item-box {
        background: #f0ebe4 !important;
        background-color: #f0ebe4 !important;
    }
    .stApp.light-mode .result-item-box .rib-text,
    .stApp.light-mode .result-item-box [style*="color:#E5E7EB"],
    .stApp.light-mode .result-item-box [style*="color:#cfcfcf"],
    .stApp.light-mode .result-item-box [style*="color:#CBD5E1"] {
        color: #1a1008 !important;
    }
    .stApp.light-mode .result-item-box [style*="color:#9CA3AF"] {
        color: #5a4030 !important;
    }
    /* inline dark label text inside result-item-box (e.g. ATS score labels #cfcfcf) */
    .stApp.light-mode .result-item-box [style*="color:#cfcfcf"],
    .stApp.light-mode .result-item-box [style*="color:#ffffff"],
    .stApp.light-mode .result-item-box [style*="color:#fff"] {
        color: #1a1008 !important;
    }

    /* ── ATS score breakdown: progress bar track ── */
    .stApp.light-mode .ats-bar-track {
        background: #ddd5cc !important;
    }

    /* ── ATS Weak Bullets card ── */
    .stApp.light-mode .ats-wb-card {
        background: #faf7f2 !important;
        border-color: #e0cdb8 !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06) !important;
    }
    .stApp.light-mode .ats-wb-row-orig {
        border-bottom-color: #e0cdb8 !important;
    }
    .stApp.light-mode .ats-wb-row-issue {
        background: rgba(239,68,68,0.06) !important;
        border-bottom-color: #e0cdb8 !important;
    }
    .stApp.light-mode .ats-wb-row-imp {
        background: rgba(34,197,94,0.06) !important;
    }
    .stApp.light-mode .ats-wb-text {
        color: #1a1008 !important;
    }
    /* Original badge (gray bg + white text) → light on light bg */
    .stApp.light-mode .ats-wb-badge-orig {
        background: #c8bdb0 !important;
        color: #1a1008 !important;
    }

    /* ── ATS keyword pills (detected=green bg, missing=red bg) ── */
    .stApp.light-mode .ats-kw-pill {
        background: #f0ebe4 !important;
    }

    /* ── HM Instant Impression box ── */
    .stApp.light-mode .hm-instant-impression {
        background: rgba(245,158,11,0.06) !important;
        border-color: rgba(245,158,11,0.25) !important;
    }
    .stApp.light-mode .hm-impression-text {
        color: #1a1008 !important;
    }

    /* ── Internet Troll roast box ── */
    .stApp.light-mode .it-roast-box {
        background: #f0ebe4 !important;
        border-color: #A855F755 !important;
    }
    .stApp.light-mode .it-roast-box * { color: #1a1008 !important; }

    /* ── Persona note cards — override inline light colors on light bg ── */
    .stApp.light-mode .persona-note [style*="color:#ffffff"],
    .stApp.light-mode .persona-note [style*="color:#fff"],
    .stApp.light-mode .persona-note [style*="color:#E5E7EB"],
    .stApp.light-mode .persona-note [style*="color:#cfcfcf"],
    .stApp.light-mode .persona-note [style*="color:#CBD5E1"],
    .stApp.light-mode .persona-note [style*="color:#e0d5cc"] { color: #1a1008 !important; }
    .stApp.light-mode .persona-note [style*="color:#9CA3AF"],
    .stApp.light-mode .persona-note [style*="color:#6B7280"],
    .stApp.light-mode .persona-note [style*="color:#9ca3af"] { color: #5a4030 !important; }

    /* ── Text Inputs / Text Areas / Select boxes ── */
    .stApp.light-mode [data-baseweb="input"],
    .stApp.light-mode [data-baseweb="input"] input,
    .stApp.light-mode [data-baseweb="textarea"],
    .stApp.light-mode [data-baseweb="textarea"] textarea,
    .stApp.light-mode [data-testid="stTextInput"] input,
    .stApp.light-mode [data-testid="stTextArea"] textarea,
    .stApp.light-mode [data-baseweb="select"] [data-baseweb="popover"],
    .stApp.light-mode [data-baseweb="select"] > div:first-child {
        background: #ffffff !important;
        background-color: #ffffff !important;
        color: #111111 !important;
        border-color: #e0cdb8 !important;
    }
    .stApp.light-mode [data-baseweb="input"]:focus-within,
    .stApp.light-mode [data-baseweb="textarea"]:focus-within,
    .stApp.light-mode [data-testid="stTextInput"] input:focus,
    .stApp.light-mode [data-testid="stTextArea"] textarea:focus {
        border-color: #FF8C00 !important;
        box-shadow: 0 0 0 2px rgba(255,140,0,0.15) !important;
    }
    /* Placeholder text */
    .stApp.light-mode [data-baseweb="input"] input::placeholder,
    .stApp.light-mode [data-baseweb="textarea"] textarea::placeholder,
    .stApp.light-mode [data-testid="stTextInput"] input::placeholder,
    .stApp.light-mode [data-testid="stTextArea"] textarea::placeholder {
        color: #a08878 !important;
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

    /* ══════════════════════════════════════════
       RESPONSIVE BREAKPOINTS
       ══════════════════════════════════════════ */

    /* ── Tablet / iPad (601px – 1024px) ── */
    @media (max-width: 1024px) {
        .block-container { max-width: 100% !important; padding-left: 1.5rem !important; padding-right: 1.5rem !important; }

        /* Hero */
        .hero { padding: 0 0.5rem !important; }

        /* Section labels */
        .section-label { font-size: 1.7rem !important; margin-top: 2.5rem !important; margin-bottom: 1.4rem !important; }

        /* Persona grid — 3 cols on tablet */
        .pc-grid { grid-template-columns: repeat(3, 1fr) !important; }
        .persona-card { min-height: 220px !important; padding: 1.2rem 0.8rem !important; }
        .persona-icon { font-size: 2rem !important; }
        .persona-name { font-size: 0.88rem !important; }
        .persona-tagline { font-size: 0.72rem !important; }
        .pc-desc { font-size: 0.7rem !important; }

        /* How it works — 2 cols on tablet */
        .steps-row { gap: 1.2rem !important; }
        .step-card { min-width: 200px !important; flex: 1 1 42% !important; padding: 1.8rem 1.4rem !important; }

        /* File info */
        .file-info-name { font-size: 0.82rem !important; }
    }

    /* ── Mobile (max 600px) ── */
    @media (max-width: 600px) {
        /* Streamlit core containers — prevent clipping */
        .stApp { overflow-x: hidden !important; }
        .block-container {
            padding-left: 0.8rem !important;
            padding-right: 0.8rem !important;
            padding-bottom: 2rem !important;
            max-width: 100vw !important;
            overflow-x: hidden !important;
            box-sizing: border-box !important;
        }
        [data-testid="stMarkdownContainer"],
        [data-testid="stVerticalBlock"],
        [data-testid="stColumn"],
        .stMarkdown {
            max-width: 100% !important;
            overflow-x: hidden !important;
            box-sizing: border-box !important;
            word-break: break-word !important;
        }

        /* Hero */
        .hero { padding: 0 !important; }
        .hero-main-text { text-align: center !important; }
        .hero-ai-badge { font-size: 0.78rem !important; padding: 0.35em 0.8em !important; letter-spacing: 0.5px !important; }
        .roast-counter-badge { padding: 0.45em 1rem !important; }

        /* Section labels */
        .section-label {
            font-size: 1.35rem !important;
            margin-top: 2rem !important;
            margin-bottom: 1rem !important;
            letter-spacing: 1.5px !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }

        /* How it works — single column on mobile */
        .steps-row { flex-direction: column !important; align-items: stretch !important; gap: 0.9rem !important; }
        .step-card {
            min-width: unset !important;
            max-width: 100% !important;
            flex: 1 1 100% !important;
            padding: 1.4rem 1.1rem !important;
            box-sizing: border-box !important;
        }
        .step-title { font-size: 1.1rem !important; }
        .step-desc { font-size: 0.95rem !important; }

        /* Persona grid — 2 cols on mobile */
        .pc-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 0.6rem !important; }
        .persona-card {
            min-height: 190px !important;
            padding: 1rem 0.6rem !important;
            border-radius: 14px !important;
            box-sizing: border-box !important;
            overflow: hidden !important;
        }
        .persona-icon { font-size: 1.7rem !important; }
        .persona-name { font-size: 0.8rem !important; }
        .persona-tagline {
            font-size: 0.65rem !important;
            display: -webkit-box !important;
            -webkit-line-clamp: 3 !important;
            -webkit-box-orient: vertical !important;
            overflow: hidden !important;
        }
        .pc-desc { display: none !important; }
        .pc-badge { font-size: 0.6rem !important; padding: 0.15em 0.5em !important; }
        .persona-check { font-size: 0.75rem !important; padding: 0.15em 0.4em !important; }

        /* Upload zone */
        [data-testid="stFileUploader"] { padding: 1rem 0.8rem !important; }
        [data-testid="stFileUploaderDropzone"] { padding: 0.8rem !important; }
        .supported-formats-line {
            font-size: 0.72rem !important;
            white-space: normal !important;
            word-break: break-word !important;
        }
        .file-info-card {
            padding: 0.8rem 1rem !important;
            gap: 0.6rem !important;
            flex-wrap: wrap !important;
        }
        .file-info-name {
            font-size: 0.78rem !important;
            word-break: break-all !important;
            overflow-wrap: anywhere !important;
        }
        .file-info-icon { font-size: 1.4rem !important; }

        /* Roast button */
        [data-testid="stButton"] > button { font-size: 1rem !important; padding: 0.7rem 1rem !important; }

        /* Results — tighten padding, prevent overflow */
        .result-item-box {
            padding: 1rem !important;
            word-break: break-word !important;
            overflow-wrap: break-word !important;
            overflow-x: hidden !important;
        }
        .score-label { font-size: 0.88rem !important; }
        pre, code { white-space: pre-wrap !important; word-break: break-word !important; }
    }
</style>
"""
