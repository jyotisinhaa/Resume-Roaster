"""
Reusable UI components — hero, steps, upload JS, personality cards, footer.
"""
import streamlit as st
import streamlit.components.v1 as components

# ═══════════════════════════════════════════════════════════════════════════════
#  UPLOAD ZONE JS
# ═══════════════════════════════════════════════════════════════════════════════
def render_upload_zone_js():
    """Inject JS to clean up the Streamlit file uploader and add supported formats text."""
    import streamlit.components.v1 as components
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
            if (!dz.querySelector('.supported-formats-line')) {
                const info = document.createElement('div');
                info.className = 'supported-formats-line';
                info.innerHTML = '📎 Supported formats: <b style="color:#FF8C00;">PDF</b>, <b style="color:#FF8C00;">DOCX</b>, <b style="color:#FF8C00;">TXT</b> · Max 10 MB';
                info.style.cssText = 'text-align:center;color:#8a7e74;font-size:0.8rem;margin-bottom:0.8rem;order:-1;';
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


# ═══════════════════════════════════════════════════════════════════════════════
#  HERO SECTION
# ═══════════════════════════════════════════════════════════════════════════════
def render_hero():
    """Render the hero banner."""
    st.markdown("""
    <style>
    @keyframes growBar {
        from { width: 0%; }
        to { width: var(--target-width); }
    }
    @keyframes glowPulse {
        0% { box-shadow: 0 0 0px transparent; }
        100% { box-shadow: 0 0 8px var(--bar-color); }
    }
    @keyframes shimmerFlow {
        0% { background-position-x: -120px; }
        100% { background-position-x: 100%; }
    }
    .animated-bar {
        height: 6px;
        border-radius: 6px;
        position: relative;
        overflow: hidden;
        animation: growBar 1.2s cubic-bezier(.77,0,.18,1) forwards, glowPulse 0.8s ease-in-out forwards;
        background: var(--bar-color, #FF8C00);
    }
    .animated-bar.shimmer::before {
        content: '';
        position: absolute;
        left: 0; top: 0; bottom: 0;
        width: 100%;
        z-index: 2;
        background: linear-gradient(120deg, transparent 0%, rgba(255,255,255,0.38) 30%, rgba(255,255,255,0.85) 55%, transparent 100%);
        background-size: 120px 100%;
        background-repeat: no-repeat;
        animation: shimmerFlow 1.5s cubic-bezier(.77,0,.18,1) infinite;
        pointer-events: none;
        mix-blend-mode: lighten;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="hero" style="margin-top:2.5rem;">
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;margin-bottom:2.2rem;width:100%;">
            <span style="font-size:6.5rem;font-weight:900;letter-spacing:1.5px;text-align:center;line-height:1.02;" class="hero-main-text">Resume<span style="color:#FF8C00;">Ripper</span></span>
            <span style="display:inline-block;background:#2a1f18;padding:0.5em 1.2em;border-radius:2em;font-weight:700;color:#FF8C00;font-size:1.15rem;letter-spacing:1px;margin-top:0.7em;">🔥 AI-Powered Resume Feedback</span>
        </div>
        <div class="hero-main-text" style="font-size:2.8rem;font-weight:900;line-height:1.08;margin-bottom:0.5rem;">
            Get your resume<br><span style="color:#FF8C00;">brutally roasted</span><br>by 5 AI experts
        </div>
        <div class="hero-desc" style="font-size:1.15rem;font-weight:400;max-width:700px;margin-bottom:2.2rem;text-align:center;margin-left:auto;margin-right:auto;">
            Upload your resume and let our AI panel of an ATS Scanner, Brutal Recruiter, Career Coach, Internet Troll, and Top Hiring Manager tear it apart — so real interviewers don't have to.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  HOW IT WORKS SECTION
# ═══════════════════════════════════════════════════════════════════════════════
def render_how_it_works():
    """Render the 3-step how-it-works cards."""
    st.markdown("""
    <div class="section-label" style="font-size:2.2rem;font-weight:900;letter-spacing:2.5px;margin-bottom:2.2rem;margin-top:2.7rem;">How It Works</div>
    <div class="steps-row" style="display:flex;flex-wrap:wrap;justify-content:center;gap:2.5rem;margin:2.8rem 0;">
        <div class="step-card" style="background:linear-gradient(135deg,#fff7e6 0%,#ffe0b2 100%);border-radius:22px;box-shadow:0 6px 32px #ff8c0033,0 2px 0 #FF8C00 inset;padding:2.3rem 2.3rem 1.7rem 2.3rem;min-width:270px;max-width:340px;flex:1 1 270px;display:flex;flex-direction:column;align-items:center;transition:transform 0.18s,box-shadow 0.18s;border:2px solid #FF8C00;position:relative;overflow:hidden;">
            <div class="step-num" style="font-size:1.2rem;font-weight:900;color:#fff;background:linear-gradient(90deg,#FF8C00,#FF6B35);border-radius:50%;width:2.5em;height:2.5em;display:flex;align-items:center;justify-content:center;margin-bottom:0.8em;box-shadow:0 2px 8px #FF8C0033;">01</div>
            <div class="step-icon" style="font-size:2.7rem;margin-bottom:0.6em;color:#FF8C00;animation:pulse 1.5s infinite alternate;">📄</div>
            <div class="step-title" style="font-size:1.35rem;font-weight:800;margin-bottom:0.5em;color:#FF8C00;text-align:center;letter-spacing:1.5px;">Upload Your Resume</div>
            <div class="step-desc" style="font-size:1.08rem;color:#6d4c1b;text-align:center;margin-bottom:0.2em;font-weight:400;line-height:1.6;">Drag and drop or browse for your PDF, DOCX, or TXT file. We accept the good, the bad, and the catastrophically over-formatted.</div>
        </div>
        <div class="step-card" style="background:linear-gradient(135deg,#fbead1 0%,#fff7e6 100%);border-radius:22px;box-shadow:0 6px 32px #ff8c0033,0 2px 0 #FF8C00 inset;padding:2.3rem 2.3rem 1.7rem 2.3rem;min-width:270px;max-width:340px;flex:1 1 270px;display:flex;flex-direction:column;align-items:center;transition:transform 0.18s,box-shadow 0.18s;border:2px solid #FF8C00;position:relative;overflow:hidden;">
            <div class="step-num" style="font-size:1.2rem;font-weight:900;color:#fff;background:linear-gradient(90deg,#FF8C00,#FF6B35);border-radius:50%;width:2.5em;height:2.5em;display:flex;align-items:center;justify-content:center;margin-bottom:0.8em;box-shadow:0 2px 8px #FF8C0033;">02</div>
            <div class="step-icon" style="font-size:2.7rem;margin-bottom:0.6em;color:#FF8C00;animation:spin 2.5s linear infinite;">🤖</div>
            <div class="step-title" style="font-size:1.35rem;font-weight:800;margin-bottom:0.5em;color:#FF8C00;text-align:center;letter-spacing:1.5px;">AI Panel Review</div>
            <div class="step-desc" style="font-size:1.08rem;color:#6d4c1b;text-align:center;margin-bottom:0.2em;font-weight:400;line-height:1.6;">Your resume is reviewed from every angle—ATS Scanner, Brutal Recruiter, Career Coach, Internet Troll, and Top Hiring Manager.</div>
        </div>
        <div class="step-card" style="background:linear-gradient(135deg,#fff7e6 0%,#ffe0b2 100%);border-radius:22px;box-shadow:0 6px 32px #ff8c0033,0 2px 0 #FF8C00 inset;padding:2.3rem 2.3rem 1.7rem 2.3rem;min-width:270px;max-width:340px;flex:1 1 270px;display:flex;flex-direction:column;align-items:center;transition:transform 0.18s,box-shadow 0.18s;border:2px solid #FF8C00;position:relative;overflow:hidden;">
            <div class="step-num" style="font-size:1.2rem;font-weight:900;color:#fff;background:linear-gradient(90deg,#FF8C00,#FF6B35);border-radius:50%;width:2.5em;height:2.5em;display:flex;align-items:center;justify-content:center;margin-bottom:0.8em;box-shadow:0 2px 8px #FF8C0033;">03</div>
            <div class="step-icon" style="font-size:2.7rem;margin-bottom:0.6em;color:#FF8C00;animation:pop 1.2s infinite alternate;">💡</div>
            <div class="step-title" style="font-size:1.35rem;font-weight:800;margin-bottom:0.5em;color:#FF8C00;text-align:center;letter-spacing:1.5px;">Get Actionable Feedback</div>
            <div class="step-desc" style="font-size:1.08rem;color:#6d4c1b;text-align:center;margin-bottom:0.2em;font-weight:400;line-height:1.6;">Get expert feedback and practical tips from multiple perspectives—instantly improve your resume with actionable insights.</div>
        </div>
    </div>
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.12); }
    }
    .ats-score-breakdown {
        background: linear-gradient(120deg, #18120b 80%, #2a1f18 100%);
        border-radius: 18px;
        border: 1.5px solid #3B2C1A;
        box-shadow: 0 4px 32px #ff8c0022, 0 1.5px 0 #FF8C00 inset;
        padding: 1.5rem 2rem 1.2rem 2rem;
        margin-bottom: 2.2rem;
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
    }
    .animated-bar {
        height: 10px;
        border-radius: 8px;
        position: relative;
        overflow: hidden;
        animation: growBar 1.2s cubic-bezier(.77,0,.18,1) forwards, glowPulse 0.8s ease-in-out forwards;
        background: var(--bar-color, #FF8C00);
        box-shadow: 0 0 12px 0 var(--bar-color, #FF8C00), 0 2px 12px #0002;
        transition: width 1.2s cubic-bezier(.77,0,.18,1), background 0.4s;
    }
    .animated-bar.shimmer::before {
        content: '';
        position: absolute;
        left: 0; top: 0; bottom: 0;
        width: 100%;
        z-index: 2;
        background: linear-gradient(120deg,
            rgba(255,255,255,0.0) 0%,
            #fffbe6 10%,
            #ffe0b2 20%,
            #FF8C00 40%,
            #FF6B35 60%,
            #22C55E 80%,
            rgba(255,255,255,0.0) 100%
        );
        background-size: 160px 100%;
        background-repeat: no-repeat;
        animation: shimmerFlow 1.6s cubic-bezier(.77,0,.18,1) infinite;
        pointer-events: none;
        mix-blend-mode: lighten;
        opacity: 0.85;
    }
    .score-label {
        font-size: 1.05rem;
        color: #f3e7d1;
        font-weight: 700;
        letter-spacing: 0.5px;
        padding-left: 2px;
    }
    .score-strength {
        font-size: 0.92rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        text-shadow: 0 1px 4px #000a;
    }
    </style>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  FILE INFO CARD
# ═══════════════════════════════════════════════════════════════════════════════
def render_file_info_card(file_name: str, ext: str, size_kb: float):
    """Render the uploaded file info card."""
    icon = "📄" if ext == "PDF" else ("📝" if ext == "DOCX" else "📝")
    st.markdown(
        f'<div class="file-info-card">'
        f'  <div class="file-info-icon">{icon}</div>'
        f'  <div class="file-info-details">'
        f'    <div class="file-info-name">{file_name}</div>'
        f'    <div class="file-info-meta">{ext} · {size_kb:.1f} KB · Ready to roast</div>'
        f'  </div>'
        f'  <div class="file-info-check">✓</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ═══════════════════════════════════════════════════════════════════════════════
#  PERSONALITY CARD GRID
# ═══════════════════════════════════════════════════════════════════════════════

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
    "top_hiring_manager": {
        "icon": "👔",
        "name": "Top Hiring Manager",
        "tagline": "Seasoned leader. Seeks excellence in any industry.",
        "accent_from": "#F59E0B",
        "accent_to": "#D97706",
    },
}


def _card_html(key: str, p: dict, is_selected: bool) -> str:
    """Generate HTML for a single personality card."""
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


def render_personality_selector() -> tuple[str, dict]:
    """
    Render the personality card grid + hidden radio + JS sync.
    Returns (selected_key, selected_personality_dict).
    """
    st.markdown('<div class="section-label">Choose Your Roaster</div>', unsafe_allow_html=True)

    if "selected_personality" not in st.session_state:
        st.session_state["selected_personality"] = "brutal_recruiter"

    persona_keys = list(PERSONALITIES.keys())
    selected_key = st.session_state["selected_personality"]

    row1_html = '<div class="persona-grid">' + ''.join(
        _card_html(k, PERSONALITIES[k], k == selected_key) for k in persona_keys[:3]
    ) + '</div>'

    row2_html = '<div class="persona-grid-row2">' + ''.join(
        _card_html(k, PERSONALITIES[k], k == selected_key) for k in persona_keys[3:]
    ) + '</div>'

    st.markdown(row1_html + row2_html, unsafe_allow_html=True)

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
    chosen_idx = persona_labels.index(chosen_label)
    st.session_state["selected_personality"] = persona_keys[chosen_idx]
    selected_key = st.session_state["selected_personality"]
    sel = PERSONALITIES[selected_key]

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
                    const radios = main.querySelectorAll('[data-testid="stRadio"] input[type="radio"]');
                    if (radios[idx]) {{
                        radios[idx].click();
                    }}
                    main.querySelectorAll('.persona-card[data-persona]').forEach(c => c.classList.remove('selected'));
                    this.classList.add('selected');
                }});
            }});
        }}

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

        function enforceSingleSelect() {{
            const allCards = main.querySelectorAll('.persona-card[data-persona]');
            const selected = main.querySelectorAll('.persona-card.selected');
            if (selected.length > 1) {{
                const radios = main.querySelectorAll('[data-testid="stRadio"] input[type="radio"]');
                let checkedIdx = -1;
                radios.forEach((r, i) => {{ if (r.checked) checkedIdx = i; }});
                const activeKey = checkedIdx >= 0 ? KEYS[checkedIdx] : KEYS[0];
                allCards.forEach(c => {{
                    if (c.dataset.persona === activeKey) {{
                        c.classList.add('selected');
                    }} else {{
                        c.classList.remove('selected');
                    }}
                }});
            }}
        }}

        setInterval(() => {{ setupCardClicks(); hideRadio(); enforceSingleSelect(); }}, 300);
        setupCardClicks();
        hideRadio();
    }})();
    </script>
    """, height=0)

    st.markdown(
        f'<div class="persona-selected-banner">'
        f'  <span class="sel-icon">{sel["icon"]}</span> '
        f'  <span class="sel-name">{sel["name"]}</span> — '
        f'  <span class="sel-tag">{sel["tagline"]}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    return selected_key, sel


# ═══════════════════════════════════════════════════════════════════════════════
#  LINKEDIN SHARE CARD
# ═══════════════════════════════════════════════════════════════════════════════
def _render_linkedin_card(score_breakdown: list, overall_score: int, ov_label: str, ov_grade: str, ov_color: str):
    """Render a screenshot-ready LinkedIn share card."""
    import streamlit as st

    desired_order = ["Keyword Coverage", "Impact Metrics", "Action Verbs", "ATS Formatting", "Skills Coverage"]
    label_to_item = {item.get("label", ""): item for item in score_breakdown}

    def score_color(s):
        if s >= 85: return "#22C55E"
        if s >= 70: return "#3B82F6"
        if s >= 50: return "#EAB308"
        return "#EF4444"

    metrics_html = ""
    for label in desired_order:
        item = label_to_item.get(label)
        if not item:
            continue
        s = item.get("score", 0)
        c = score_color(s)
        short = label.replace(" Coverage", "").replace(" Metrics", "").replace(" Verbs", " V.").replace("Formatting", "Format")
        metrics_html += f"""
        <div style="background:#0d1b2a;border-radius:10px;padding:10px 12px;border-top:2px solid {c};flex:1;min-width:80px;text-align:center;">
            <div style="font-size:1.4rem;font-weight:900;color:{c};line-height:1;">{s}</div>
            <div style="font-size:0.65rem;color:#6B7280;margin-top:3px;white-space:nowrap;">{short}</div>
        </div>"""

    circumference = round(2 * 3.14159 * 40, 1)
    dash = round(overall_score / 100 * circumference, 1)

    st.markdown('<div style="font-size:1.1rem;font-weight:800;color:#FF8C00;margin:24px 0 8px 0;letter-spacing:0.5px;font-family:inherit;">🔥 Share Your Results</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.82rem;color:#6B7280;margin-bottom:10px;">Screenshot this card or use the buttons below to share on LinkedIn.</div>', unsafe_allow_html=True)
    components.html(f"""
    <style>
    .li-card {{
        background:linear-gradient(135deg,#0a0f1e 0%,#0d1b2a 60%,#091422 100%);
        border:1px solid #1e3a5f;
        border-radius:18px;
        padding:22px 20px 18px 20px;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
        max-width:520px;
        margin:0 auto;
        position:relative;
        overflow:hidden;
        box-shadow:0 8px 40px #00C9FF18;
    }}
    .li-card::before {{
        content:'';
        position:absolute;
        top:0;left:0;right:0;height:2px;
        background:linear-gradient(90deg,transparent,{ov_color},{ov_color}88,transparent);
    }}
    .li-header {{
        display:flex;justify-content:space-between;align-items:center;margin-bottom:18px;
    }}
    .li-brand {{
        font-size:0.7rem;color:#6B7280;letter-spacing:2px;font-weight:700;text-transform:uppercase;
    }}
    .li-badge {{
        font-size:0.7rem;color:#00C9FF;font-weight:800;letter-spacing:1px;
        background:#00C9FF18;border:1px solid #00C9FF44;border-radius:20px;padding:3px 10px;
    }}
    .li-hero {{
        display:flex;align-items:center;gap:20px;margin-bottom:20px;
    }}
    .li-metrics {{
        display:flex;gap:8px;margin-bottom:18px;flex-wrap:wrap;
    }}
    .li-footer {{
        border-top:1px solid #1e3a5f;
        padding-top:12px;
        display:flex;
        justify-content:space-between;
        align-items:center;
    }}
    .li-cta {{
        font-size:0.78rem;color:#FF8C00;font-weight:700;
    }}
    .li-sub {{
        font-size:0.72rem;color:#374151;
    }}
    </style>
    <div class="li-card">
        <div class="li-header">
            <div class="li-brand">🔥 Resume Ripper AI</div>
            <div class="li-badge">🤖 ATS Scanner</div>
        </div>
        <div class="li-hero">
            <div style="position:relative;width:90px;height:90px;flex-shrink:0;">
                <svg width="90" height="90" viewBox="0 0 90 90">
                    <circle cx="45" cy="45" r="40" fill="none" stroke="#1e2d3d" stroke-width="9"/>
                    <circle cx="45" cy="45" r="40" fill="none" stroke="{ov_color}" stroke-width="9"
                        stroke-dasharray="{dash} {circumference}" stroke-linecap="round"
                        transform="rotate(-90 45 45)"
                        style="filter:drop-shadow(0 0 6px {ov_color});"/>
                </svg>
                <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;line-height:1;">
                    <div style="font-size:1.7rem;font-weight:900;color:{ov_color};line-height:1;">{overall_score}</div>
                    <div style="font-size:0.52rem;color:#6B7280;letter-spacing:1px;">/ 100</div>
                </div>
            </div>
            <div>
                <div style="font-size:1.8rem;font-weight:900;color:{ov_color};letter-spacing:2px;line-height:1;">{ov_label}</div>
                <div style="font-size:0.82rem;color:#9CA3AF;margin-top:4px;">ATS Compatibility</div>
                <div style="margin-top:6px;">
                    <span style="background:{ov_color}22;color:{ov_color};border:1px solid {ov_color}55;border-radius:20px;padding:3px 12px;font-size:0.78rem;font-weight:800;">Grade {ov_grade}</span>
                </div>
            </div>
        </div>
        <div class="li-metrics">{metrics_html}</div>
        <div class="li-footer">
            <div class="li-cta">🔥 Try Resume Ripper AI — it's free!</div>
            <div class="li-sub">Would your resume survive?</div>
        </div>
    </div>
    """, height=340)


# ═══════════════════════════════════════════════════════════════════════════════
#  SHARE BOX
# ═══════════════════════════════════════════════════════════════════════════════
def _render_share_box(share_text: str, roast_result: str, sel_name: str):
    """Render share buttons: LinkedIn, Copy text, Download report."""
    import json

    share_text_json = json.dumps(share_text)
    roast_json = json.dumps(roast_result)
    file_name_json = json.dumps(f"resume_roast_{sel_name.lower().replace(' ', '_')}.txt")

    components.html(f"""
    <style>
    .sb-actions {{
        display:flex;
        gap:0.7rem;
        margin-top:12px;
    }}
    .sb-btn {{
        flex:1;
        padding:0.7rem 0.8rem;
        border-radius:10px;
        font-size:0.88rem;
        font-weight:700;
        cursor:pointer;
        border:none;
        text-align:center;
        display:inline-flex;
        align-items:center;
        justify-content:center;
        gap:6px;
        transition:opacity 0.15s,transform 0.1s;
        text-decoration:none;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    }}
    .sb-btn:hover {{ opacity:0.88; transform:translateY(-1px); }}
    .sb-li   {{ background:#0A66C2; color:#fff; }}
    .sb-copy {{ background:#FF8C00; color:#fff; }}
    .sb-dl   {{ background:#1e1e1e; color:#FF8C00; border:1.5px solid #FF8C00; }}
    .sb-feedback {{
        display:none;
        font-size:0.76rem;
        color:#22C55E;
        margin-top:0.55rem;
        text-align:center;
        font-weight:700;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    }}
    </style>
    <div class="sb-actions">
        <button class="sb-btn sb-li"   onclick="sbLinkedIn()">💼 Post on LinkedIn</button>
        <button class="sb-btn sb-copy" onclick="sbCopyText()">📋 Copy Text</button>
        <button class="sb-btn sb-dl"   onclick="sbDownload()">📥 Download</button>
    </div>
    <div class="sb-feedback" id="sb-fb">✅ Copied to clipboard!</div>
    <script>
    const SB_SHARE = {share_text_json};
    const SB_ROAST = {roast_json};
    const SB_FILE  = {file_name_json};

    function sbLinkedIn() {{
        const url = 'https://www.linkedin.com/feed/?shareActive=true&text=' + encodeURIComponent(SB_SHARE);
        window.open(url, '_blank');
    }}

    function sbShowFeedback() {{
        const el = document.getElementById('sb-fb');
        el.style.display = 'block';
        setTimeout(() => {{ el.style.display = 'none'; }}, 2200);
    }}

    function sbCopyText() {{
        try {{
            window.parent.navigator.clipboard.writeText(SB_SHARE).then(sbShowFeedback, sbFallback);
        }} catch(e) {{ sbFallback(); }}
    }}

    function sbFallback() {{
        try {{
            const ta = window.parent.document.createElement('textarea');
            ta.value = SB_SHARE;
            ta.style.cssText = 'position:fixed;opacity:0;top:0;left:0;';
            window.parent.document.body.appendChild(ta);
            ta.focus(); ta.select();
            window.parent.document.execCommand('copy');
            window.parent.document.body.removeChild(ta);
            sbShowFeedback();
        }} catch(e) {{
            alert('Copy failed — please copy manually.');
        }}
    }}

    function sbDownload() {{
        const blob = new Blob([SB_ROAST], {{type:'text/plain;charset=utf-8'}});
        const url  = URL.createObjectURL(blob);
        const a    = window.parent.document.createElement('a');
        a.href = url; a.download = SB_FILE;
        window.parent.document.body.appendChild(a);
        a.click();
        window.parent.document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }}
    </script>
    """, height=90)


# ═══════════════════════════════════════════════════════════════════════════════
#  ROAST RESULTS
# ═══════════════════════════════════════════════════════════════════════════════
def render_roast_results(roast_result: str, score_breakdown: dict, sel: dict, elapsed: float):
    """Render the roast results card + share/download section."""
    st.markdown("""
    <div style="font-size:0.75rem;color:#9CA3AF;margin-bottom:6px;">
    Analyzing resume signals...
    </div>
    """, unsafe_allow_html=True)

    if sel.get("name", "").lower() == "ats scanner" and score_breakdown:
        import re
        lines = roast_result.split('\n')

        def find_section(header):
            for i, l in enumerate(lines):
                if l.strip().upper().startswith(header.upper()):
                    return i
            return None

        scan_idx = find_section("SCAN COMPLETE")
        score_idx = find_section("ATS COMPATIBILITY SCORE")
        breakdown_idx = find_section("SCORE BREAKDOWN")
        match_idx = find_section("MATCH PROBABILITY")
        detected_idx = find_section("KEYWORDS DETECTED")
        missing_idx = find_section("KEYWORDS MISSING")
        weak_idx = find_section("WEAK BULLETS DETECTED")
        parsing_idx = find_section("SECTION PARSING CHECK")
        structure_idx = find_section("STRUCTURE ANALYSIS")
        warnings_idx = find_section("ATS PARSING WARNINGS")
        formatting_idx = find_section("FORMATTING OBSERVATIONS")
        recruiter_idx = find_section("RECRUITER SCAN RESULT")
        signals_idx = find_section("EXPERIENCE SIGNALS")
        protocol_idx = find_section("OPTIMIZATION PROTOCOL")
        density_idx = find_section("KEYWORD DENSITY")
        roast_idx = find_section("🔥 ROAST LEVEL")
        final_idx = find_section("FINAL RECOMMENDATION")

        # Overall ATS Score Hero
        total_scores = [item.get("score", 0) for item in score_breakdown if item.get("score")]
        overall_score = round(sum(total_scores) / len(total_scores)) if total_scores else 0
        if overall_score >= 85:
            ov_color = "#22C55E"; ov_grade = "A"; ov_label = "EXCELLENT"
        elif overall_score >= 70:
            ov_color = "#3B82F6"; ov_grade = "B"; ov_label = "STRONG"
        elif overall_score >= 50:
            ov_color = "#EAB308"; ov_grade = "C"; ov_label = "AVERAGE"
        else:
            ov_color = "#EF4444"; ov_grade = "D"; ov_label = "WEAK"

        circumference = round(2 * 3.14159 * 54, 1)
        dash = round(overall_score / 100 * circumference, 1)

        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#0a0f1e 0%,#0d1b2a 60%,#091422 100%);
            border:1px solid {ov_color}33;
            border-radius:20px;
            padding:28px 24px 22px 24px;
            margin:16px 0 20px 0;
            text-align:center;
            position:relative;
            overflow:hidden;
        ">
            <div style="position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,{ov_color},{ov_color}88,transparent);"></div>
            <div style="font-size:0.75rem;color:#00C9FF;letter-spacing:3px;font-weight:800;margin-bottom:16px;">🤖 ATS SCAN COMPLETE</div>
            <div style="position:relative;width:150px;height:150px;margin:0 auto 14px auto;">
                <svg width="150" height="150" viewBox="0 0 150 150">
                    <circle cx="75" cy="75" r="54" fill="none" stroke="#1e2d3d" stroke-width="12"/>
                    <circle cx="75" cy="75" r="54" fill="none" stroke="{ov_color}" stroke-width="12"
                        stroke-dasharray="{dash} {circumference}" stroke-linecap="round"
                        transform="rotate(-90 75 75)"
                        style="filter:drop-shadow(0 0 8px {ov_color});"
                    />
                </svg>
                <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;line-height:1;">
                    <div style="font-size:2.8rem;font-weight:900;color:{ov_color};line-height:1;">{overall_score}</div>
                    <div style="font-size:0.6rem;color:#6B7280;letter-spacing:1px;margin-top:3px;">OUT OF 100</div>
                </div>
            </div>
            <div style="font-size:1.5rem;font-weight:900;color:{ov_color};letter-spacing:3px;margin-bottom:4px;">{ov_label}</div>
            <div style="font-size:0.8rem;color:#6B7280;">ATS Compatibility Score &nbsp;·&nbsp; Grade <b style="color:{ov_color};">{ov_grade}</b></div>
        </div>
        """, unsafe_allow_html=True)

        # Score Breakdown
        st.markdown(f"""
        <div style="display:flex;align-items:center;justify-content:space-between;margin:18px 0 12px 0;">
            <div style="font-size:1.1rem;font-weight:800;letter-spacing:0.5px;color:#ffffff;font-family:inherit;">📊 Score Breakdown</div>
            <div style="height:1px;flex:1;margin-left:12px;background:linear-gradient(90deg,#00C9FF,transparent);opacity:0.4;"></div>
        </div>
        """, unsafe_allow_html=True)

        desired_order = [
            "Keyword Coverage",
            "Impact Metrics",
            "Action Verbs",
            "ATS Formatting",
            "Skills Coverage",
        ]
        label_to_item = {item.get("label", ""): item for item in score_breakdown}
        for i, label in enumerate(desired_order):
            item = label_to_item.get(label)
            if not item:
                continue
            score = item.get("score", 0)
            if score >= 85:
                color = "#22C55E"; strength = "EXCELLENT"; grade = "A"
            elif score >= 70:
                color = "#3B82F6"; strength = "STRONG"; grade = "B"
            elif score >= 50:
                color = "#EAB308"; strength = "AVG"; grade = "C"
            else:
                color = "#EF4444"; strength = "WEAK"; grade = "D"
            st.markdown(f"""
            <div style="display:flex;align-items:center;margin-bottom:10px;gap:10px;background:#0d1117;border-radius:10px;padding:9px 12px;border-left:3px solid {color};">
                <div style="width:140px;font-size:0.88rem;color:#cfcfcf;font-weight:500;">{label}</div>
                <div style="width:34px;font-weight:900;font-size:1rem;color:{color};">{score}</div>
                <div style="flex:1;height:10px;background:#1a1a2e;border-radius:8px;overflow:hidden;">
                    <div class="animated-bar shimmer" style="
                        --target-width:{score}%;
                        --bar-color:{color};
                        height:100%;
                        width:0%;
                        animation-delay:{i * 0.15}s;
                        background:linear-gradient(90deg,{color},{color}77);"
                    ></div>
                </div>
                <div style="width:34px;text-align:center;font-size:0.95rem;font-weight:900;color:{color};background:{color}22;border-radius:6px;padding:2px 0;">{grade}</div>
            </div>
            """, unsafe_allow_html=True)

        def parse_weak_bullets(section_lines):
            import re
            bullets = []
            current = {"Original": "", "Issue": "", "Improved Version": ""}
            current_key = None
            for line in section_lines:
                line = line.strip()
                if re.match(r'^Original\s*:', line, re.IGNORECASE):
                    if any(current.values()):
                        bullets.append(current)
                        current = {"Original": "", "Issue": "", "Improved Version": ""}
                    current_key = "Original"
                    current["Original"] = line.split(":", 1)[1].strip()
                elif re.match(r'^Issue\s*:', line, re.IGNORECASE):
                    current_key = "Issue"
                    current["Issue"] = line.split(":", 1)[1].strip()
                elif re.match(r'^Improved Version\s*:', line, re.IGNORECASE):
                    current_key = "Improved Version"
                    current["Improved Version"] = line.split(":", 1)[1].strip()
                else:
                    if current_key:
                        current[current_key] += " " + line
            if any(current.values()):
                bullets.append(current)
            return bullets

        def render_section(title, icon, idx, next_idx, color=None, bg=None):
            if idx is None:
                return
            import re
            section_lines = lines[idx+1:next_idx] if next_idx else lines[idx+1:]
            st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
            st.markdown(f"""
            <div style="
                margin:16px 0 6px 0;
                font-size:1.1rem;
                font-weight:800;
                color:#ffffff;
                display:flex;
                align-items:center;
                gap:8px;
                font-family:inherit;
                letter-spacing:0.5px;
            ">
                <span>{icon}</span> {title}
            </div>
            """, unsafe_allow_html=True)
            if title == "Weak Bullets Detected":
                st.markdown(f"<div style='border-radius:8px;padding:8px 0 2px 0;margin-bottom:2px;'>", unsafe_allow_html=True)
                bullets = parse_weak_bullets(section_lines)
                for b in bullets:
                    st.markdown(f"""
                    <div style="
                        background:#111;
                        border:1px solid #2a2a2a;
                        border-radius:10px;
                        padding:14px;
                        margin-bottom:12px;
                    ">
                        <div style="color:#9CA3AF;font-size:0.8rem;margin-bottom:4px;">ORIGINAL</div>
                        <div style="color:#E5E7EB;margin-bottom:10px;">
                            {b.get("Original") or "<i>Missing</i>"}
                        </div>
                        <div style="color:#F87171;font-size:0.8rem;margin-bottom:4px;">ISSUE</div>
                        <div style="margin-bottom:10px;color:#FCA5A5;">
                            {b.get("Issue") or "<i>Missing</i>"}
                        </div>
                        <div style="color:#34D399;font-size:0.8rem;margin-bottom:4px;">IMPROVED</div>
                        <div style="color:#6EE7B7;">
                            {b.get("Improved Version") or "<i>Missing</i>"}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            elif title in ("Keywords Detected", "Keywords Missing"):
                pill_color = "#22C55E" if title == "Keywords Detected" else "#EF4444"
                pill_bg = "#0d2a1a" if title == "Keywords Detected" else "#2a0d0d"
                pill_border = "#22C55E44" if title == "Keywords Detected" else "#EF444444"
                all_pills_html = ""
                for l in section_lines:
                    line = l.strip()
                    if not line:
                        continue
                    if re.fullmatch(r'[-_*\s]{3,}', line):
                        continue
                    if line.endswith(':') and not line.startswith(('-', '•', '*')):
                        if all_pills_html:
                            st.markdown(f"<div style='display:flex;flex-wrap:wrap;gap:7px;margin-bottom:12px;'>{all_pills_html}</div>", unsafe_allow_html=True)
                            all_pills_html = ""
                        cat = line.rstrip(':')
                        st.markdown(f"<div style='font-size:0.7rem;color:#6B7280;letter-spacing:2px;margin:10px 0 6px 0;font-weight:700;'>{cat.upper()}</div>", unsafe_allow_html=True)
                    elif line.startswith(('-', '•', '*')):
                        keyword = re.sub(r'^[-•*]\s*', '', line).strip()
                        if keyword:
                            all_pills_html += f'<span style="background:{pill_bg};color:{pill_color};border:1px solid {pill_border};border-radius:20px;padding:4px 13px;font-size:0.82rem;font-weight:600;white-space:nowrap;">{keyword}</span>'
                    else:
                        if all_pills_html:
                            st.markdown(f"<div style='display:flex;flex-wrap:wrap;gap:7px;margin-bottom:12px;'>{all_pills_html}</div>", unsafe_allow_html=True)
                            all_pills_html = ""
                        st.markdown(f"<div style='font-size:0.85rem;color:#9CA3AF;margin:4px 0;'>{line}</div>", unsafe_allow_html=True)
                if all_pills_html:
                    st.markdown(f"<div style='display:flex;flex-wrap:wrap;gap:7px;margin-bottom:8px;'>{all_pills_html}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='border-radius:8px;padding:4px 0 2px 0;margin-bottom:2px;'>", unsafe_allow_html=True)
                for l in section_lines:
                    line = l.strip()
                    if not line:
                        continue
                    if re.fullmatch(r'[-_*\s]{3,}', line):
                        continue
                    st.markdown(l)
                st.markdown("</div>", unsafe_allow_html=True)
            if next_idx is not None:
                st.markdown("<div style='height:1px;background:#222;margin:10px 0 6px 0;opacity:0.5;'></div>", unsafe_allow_html=True)

        render_section("Match Probability", "🎯", match_idx, detected_idx, color="#00C9FF")
        render_section("Keywords Detected", "✅", detected_idx, missing_idx, color="#22C55E", bg="#172a1a")
        render_section("Keywords Missing", "⚠️", missing_idx, weak_idx, color="#EF4444", bg="#2a1818")
        render_section("Weak Bullets Detected", "📝", weak_idx, parsing_idx, color="#F59E0B", bg="#2a1f18")
        render_section("Section Parsing Check", "📑", parsing_idx, structure_idx, color="#00C9FF")
        render_section("Structure Analysis", "🧩", structure_idx, warnings_idx, color="#00C9FF")
        render_section("ATS Parsing Warnings", "⚠️", warnings_idx, formatting_idx, color="#EF4444")
        render_section("Formatting Observations", "🖋️", formatting_idx, recruiter_idx, color="#F59E0B")
        render_section("Recruiter Scan Result", "🔍", recruiter_idx, signals_idx, color="#FF8C00")
        render_section("Experience Signals", "🚩", signals_idx, protocol_idx, color="#A855F7")
        render_section("Optimization Protocol", "🛠️", protocol_idx, density_idx, color="#22C55E")
        render_section("Keyword Density", "📊", density_idx, roast_idx, color="#00C9FF")
        render_section("Roast Level", "🔥", roast_idx, final_idx, color="#FF8C00")

        # Final Recommendation
        if final_idx is not None:
            rec_lines = lines[final_idx+1:]
            VALID_VERDICTS = {"optimize", "reformat", "critical rewrite"}
            PROMPT_LEAK_SIGNALS = {
                "tone:", "analytical", "robotic", "diagnostic",
                "sound like", "maximum 600", "be concise", "no filler",
                "every sentence must", "choose one:",
            }
            verdict = None
            clean_content = []
            for l in rec_lines:
                stripped = l.strip()
                if not stripped:
                    continue
                lower = stripped.lower()
                if lower in VALID_VERDICTS and verdict is None:
                    verdict = stripped.upper()
                    continue
                if any(signal in lower for signal in PROMPT_LEAK_SIGNALS) and len(stripped) < 80:
                    continue
                clean_content.append(stripped)
            display_verdict = verdict or "OPTIMIZE"
            st.markdown(f"""
            <div style="background:linear-gradient(90deg,#FF8C00,#FF6B35);color:#fff;padding:18px 22px;border-radius:12px;margin:18px 0 0 0;box-shadow:0 2px 12px #FF8C0033;">
                <div style="font-size:1.3em;font-weight:900;margin-bottom:10px;">⭐ FINAL RECOMMENDATION</div>
                <div style="font-size:1.6rem;font-weight:900;letter-spacing:2px;margin-bottom:12px;border-bottom:1px solid rgba(255,255,255,0.3);padding-bottom:10px;">{display_verdict}</div>
                {''.join(f'<div style="margin-top:6px;font-size:1rem;font-weight:400;line-height:1.6;">{line}</div>' for line in clean_content)}
            </div>
            """, unsafe_allow_html=True)

        # Footer
        st.markdown(f"""
        <div style="text-align:right;font-size:12px;color:#777;margin-top:18px;">
            {sel["icon"]} Generated by {sel["name"]} · {elapsed:.1f}s
        </div>
        """, unsafe_allow_html=True)

        st.session_state["last_roast"] = roast_result
        _render_linkedin_card(score_breakdown, overall_score, ov_label, ov_grade, ov_color)
        share_text = f"I just scored {overall_score}/100 on the ATS Scanner 🤖\nHere's my resume breakdown — would yours survive? 👀\n🔥 Try it free → Resume Ripper AI\n#ResumeRoaster #ATSTips #JobSearch #CareerTips #AI"
        _render_share_box(share_text, roast_result, sel["name"])

    else:
        # Fallback: original rendering for other personas
        st.markdown('<div class="section-label">Your Roast</div>', unsafe_allow_html=True)
        badge_html = (
            f'<div class="roast-result">'
            f'  <div class="roast-badge">'
            f'    <div class="roast-badge-icon">{sel["icon"]}</div>'
            f'    <div class="roast-badge-name">{sel["name"]}</div>'
            f'  </div>'
            f'  <div style="height: 1.2rem;"></div>'
        )
        st.markdown(badge_html, unsafe_allow_html=True)
        st.markdown(roast_result)
        st.markdown(
            f'<br><div style="color:#5a4e44; font-size:0.75rem; margin-top:1rem;">'
            f'{sel["icon"]} <i>Roasted by {sel["name"]} · Resume Ripper AI · {elapsed:.1f}s</i></div>',
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)
        st.session_state["last_roast"] = roast_result
        share_text = f"I just got my resume roasted by the {sel['name']} 🔥\nWould you survive the roast? 😅\n#ResumeRoaster #AI #CareerTips"
        _render_share_box(share_text, roast_result, sel["name"])


# ═══════════════════════════════════════════════════════════════════════════════
#  FOOTER
# ═══════════════════════════════════════════════════════════════════════════════
def render_footer():
    """Render the app footer."""
    st.markdown(
        '<div class="footer">'
        '🔥 <b>Roasted with love by Resume Ripper</b><br>'
        'Your resume is processed in memory and never stored. We only roast, never save. 🤝'
        '</div>',
        unsafe_allow_html=True,
    )