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
            <span class="hero-ai-badge" style="display:inline-block;background:#2a1f18;padding:0.5em 1.2em;border-radius:2em;font-weight:700;color:#FF8C00;font-size:1.15rem;letter-spacing:1px;margin-top:0.7em;">🔥 AI-Powered Resume Feedback</span>
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
    <div class="section-label" style="margin-top:2rem;">How It Works</div>
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
        "tagline": "I've trashed 50,000+ resumes. Is yours next?",
        "description": "The unfiltered truth recruiters think but never say out loud.",
        "badge": "Most Direct",
        "accent_from": "#FF4B4B",
        "accent_to": "#CC0000",
    },
    "ats_scanner": {
        "icon": "🤖",
        "name": "ATS Scanner",
        "tagline": "90% of resumes never reach a human. Will yours?",
        "description": "Algorithm-grade scan — find every keyword gap before a bot kills your application.",
        "badge": "Data-Driven",
        "accent_from": "#00C9FF",
        "accent_to": "#0066FF",
    },
    "career_coach": {
        "icon": "🧑‍🏫",
        "name": "Career Coach",
        "tagline": "Your potential is real. Your resume isn't showing it.",
        "description": "Honest, actionable fixes that turn a forgettable resume into an interview magnet.",
        "badge": "Most Encouraging",
        "accent_from": "#22C55E",
        "accent_to": "#16A34A",
    },
    "internet_troll": {
        "icon": "🧌",
        "name": "Internet Troll",
        "tagline": "Sir, this is a resume — not a cry for help.",
        "description": "The most savage feedback you'll actually learn from. Roast-proof your resume.",
        "badge": "Most Entertaining",
        "accent_from": "#A855F7",
        "accent_to": "#7C3AED",
    },
    "top_hiring_manager": {
        "icon": "👔",
        "name": "Top Hiring Manager",
        "tagline": "I make $500K hiring calls. Earn your callback.",
        "description": "C-suite lens on whether you'd even get a callback — no corporate fluff.",
        "badge": "Most Authoritative",
        "accent_from": "#F59E0B",
        "accent_to": "#D97706",
    },
}


def _card_html(key: str, p: dict, is_selected: bool) -> str:
    """Generate HTML for a single personality card."""
    sel_cls = " selected" if is_selected else ""
    af, at = p["accent_from"], p["accent_to"]
    badge = p.get("badge", "")
    return (
        f'<div class="persona-card{sel_cls}" data-persona="{key}" '
        f'style="--accent-grad:linear-gradient(135deg,{af},{at});'
        f'--accent-color:{af};--accent-glow:{af}55;--accent-glow-inner:{af}14;">'
        f'<div class="persona-check">✓</div>'
        f'<div class="pc-badge" style="color:{af};background:{af}22;border:1px solid {af}55;">{badge}</div>'
        f'<div class="pc-icon-ring" style="background:linear-gradient(135deg,{af}22,{at}11);border:2px solid {af}44;">'
        f'<span class="persona-icon">{p["icon"]}</span>'
        f'</div>'
        f'<div class="persona-name">{p["name"]}</div>'
        f'<div class="persona-tagline">{p["tagline"]}</div>'
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

    grid_html = '<div class="pc-grid">' + ''.join(
        _card_html(k, PERSONALITIES[k], k == selected_key) for k in persona_keys
    ) + '</div>'

    st.markdown(grid_html, unsafe_allow_html=True)

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

    af, at = sel["accent_from"], sel["accent_to"]
    _ar = int(af[1:3], 16); _ag = int(af[3:5], 16); _ab = int(af[5:7], 16)
    st.markdown(
        f'<div class="persona-selected-banner" style="border-color:{af}66;box-shadow:0 0 32px rgba({_ar},{_ag},{_ab},0.18);">'
        f'  <div class="psb-left">'
        f'    <div class="psb-icon" style="background:linear-gradient(135deg,{af}2a,{at}18);border:2px solid {af}55;box-shadow:0 4px 20px rgba({_ar},{_ag},{_ab},0.25);">{sel["icon"]}</div>'
        f'    <div class="psb-info">'
        f'      <div class="psb-label">✦ Selected Roaster</div>'
        f'      <div class="psb-name" style="color:{af};">{sel["name"]}</div>'
        f'      <div class="psb-tag">{sel["tagline"]}</div>'
        f'      <div class="psb-desc">{sel.get("description","")}</div>'
        f'    </div>'
        f'  </div>'
        f'  <div class="psb-pill" style="background:linear-gradient(135deg,{af},{at});box-shadow:0 4px 14px rgba({_ar},{_ag},{_ab},0.4);">{sel.get("badge","")}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    return selected_key, sel


# ═══════════════════════════════════════════════════════════════════════════════
#  LINKEDIN SHARE CARD
# ═══════════════════════════════════════════════════════════════════════════════
def _render_linkedin_card(score_breakdown: list, overall_score: int, ov_label: str, ov_grade: str, ov_color: str,
                          roast_line: str = "", match_prob: str = "", recommendation: str = "",
                          copy_text: str = "", roast_result: str = ""):
    """Render a screenshot-ready LinkedIn share card."""
    import streamlit as st
    import json as _json

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

    # Build sub-score lines
    sub_scores = ""
    for label in desired_order:
        item = label_to_item.get(label)
        if item:
            sub_scores += f"  • {label}: {item.get('score', 0)}/100\n"

    roast_snippet = f'\n🔥 "{roast_line[:110]}{"…" if len(roast_line) > 110 else ""}"\n' if roast_line else ""
    match_line    = f"\n{match_prob}" if match_prob else ""
    rec_line      = f"\nFinal Recommendation: {recommendation}" if recommendation else ""

    li_text = (
        f"I just scanned my resume with the ATS Scanner on Resume Ripper AI 🤖\n\n"
        f"ATS Score: {overall_score}/100 — {ov_label} (Grade {ov_grade})\n"
        f"{match_line}\n"
        f"\nScore Breakdown:\n{sub_scores}"
        f"{roast_snippet}"
        f"{rec_line}\n\n"
        f"Would your resume survive the scan? 👀\n"
        f"#ResumeRipper #ATSTips #JobSearch #CareerTips #AI"
    )
    li_text_json = _json.dumps(li_text)
    copy_text_json = _json.dumps(copy_text or li_text)
    roast_text_json = _json.dumps(roast_result)

    st.markdown('<div style="font-size:1.1rem;font-weight:800;color:#00C9FF;margin:24px 0 8px 0;letter-spacing:0.5px;font-family:inherit;">🤖 Share Your Results</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.82rem;color:#6B7280;margin-bottom:6px;">Save the card as an image, then attach it to your LinkedIn post.</div>', unsafe_allow_html=True)
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

    <div style="display:flex;gap:10px;margin-top:14px;max-width:520px;margin-left:auto;margin-right:auto;">
        <button onclick="saveATSCard()" style="
            flex:1;padding:10px 0;border-radius:10px;border:none;cursor:pointer;
            background:#00C9FF;color:#000;font-size:0.88rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1">📸 Save Card as Image</button>
        <button onclick="postATSLinkedIn()" style="
            flex:1;padding:10px 0;border-radius:10px;border:none;cursor:pointer;
            background:#0A66C2;color:#fff;font-size:0.88rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">💼 Post on LinkedIn</button>
    </div>
    <div id="ats-hint" style="
        display:none;max-width:520px;margin:8px auto 0 auto;
        font-size:0.75rem;color:#22C55E;text-align:center;font-weight:600;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    ">✅ Card saved! Attach the image to your LinkedIn post.</div>

    <div style="display:flex;flex-direction:column;gap:8px;margin-top:8px;max-width:520px;margin-left:auto;margin-right:auto;">
        <button onclick="atsCopyText()" style="
            width:100%;padding:12px 0;border-radius:10px;border:none;cursor:pointer;
            background:#FF8C00;color:#fff;font-size:0.92rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1">📋 Copy Text</button>
        <button onclick="atsDownload()" style="
            width:100%;padding:12px 0;border-radius:10px;border:1.5px solid #FF8C00;cursor:pointer;
            background:#1e1e1e;color:#FF8C00;font-size:0.92rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1">📥 Download</button>
    </div>
    <div id="ats-copy-fb" style="
        display:none;max-width:520px;margin:6px auto 0 auto;
        font-size:0.75rem;color:#22C55E;text-align:center;font-weight:600;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    ">✅ Copied to clipboard!</div>

    <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
    <script>
    const ATS_LI_TEXT = {li_text_json};
    const ATS_COPY_TEXT = {copy_text_json};
    const ATS_ROAST_TEXT = {roast_text_json};
    function saveATSCard() {{
        const card = document.querySelector('.li-card');
        html2canvas(card, {{ backgroundColor:'#0a0f1e', scale:2, useCORS:true, logging:false }})
        .then(canvas => {{
            const link = document.createElement('a');
            link.download = 'ats_scanner_score.png';
            link.href = canvas.toDataURL('image/png');
            link.click();
            document.getElementById('ats-hint').style.display = 'block';
            setTimeout(() => {{ document.getElementById('ats-hint').style.display = 'none'; }}, 4000);
        }});
    }}
    function postATSLinkedIn() {{
        window.open('https://www.linkedin.com/feed/?shareActive=true&text=' + encodeURIComponent(ATS_LI_TEXT), '_blank');
    }}
    function atsCopyText() {{
        var show = function() {{
            var fb = document.getElementById('ats-copy-fb');
            fb.style.display = 'block';
            setTimeout(function() {{ fb.style.display = 'none'; }}, 2200);
        }};
        var fallback = function() {{
            try {{
                var ta = window.parent.document.createElement('textarea');
                ta.value = ATS_COPY_TEXT; ta.style.cssText = 'position:fixed;opacity:0;top:0;left:0;';
                window.parent.document.body.appendChild(ta); ta.focus(); ta.select();
                window.parent.document.execCommand('copy');
                window.parent.document.body.removeChild(ta); show();
            }} catch(e) {{ alert('Copy failed — please copy manually.'); }}
        }};
        try {{ window.parent.navigator.clipboard.writeText(ATS_COPY_TEXT).then(show, fallback); }}
        catch(e) {{ fallback(); }}
    }}
    function atsDownload() {{
        var blob = new Blob([ATS_ROAST_TEXT], {{type:'text/plain;charset=utf-8'}});
        var url = URL.createObjectURL(blob);
        var a = window.parent.document.createElement('a');
        a.href = url; a.download = 'ats_scanner_roast.txt';
        window.parent.document.body.appendChild(a); a.click();
        window.parent.document.body.removeChild(a); URL.revokeObjectURL(url);
    }}
    </script>
    """, height=590)


# ═══════════════════════════════════════════════════════════════════════════════
#  BRUTAL RECRUITER LINKEDIN SHARE CARD
# ═══════════════════════════════════════════════════════════════════════════════
def _render_br_linkedin_card(score_val: int, sc_label: str, sc_grade: str, sc_color: str, verdict_text: str, linkedin_roast: str,
                             copy_text: str = "", roast_result_full: str = ""):
    """Render a screenshot-ready LinkedIn share card for the Brutal Recruiter."""
    import json as _json
    circumference = round(2 * 3.14159 * 54, 1)
    dash = round(score_val / 10 * circumference, 1)

    low_v = verdict_text.lower()
    if "hire" in low_v and "maybe" not in low_v and "pass" not in low_v:
        v_color = "#22C55E"; v_icon = "✅ HIRE"
        v_bg = "rgba(34,197,94,0.12)"
        v_msg = "You made it through. Don't blow the interview."
    elif "maybe" in low_v:
        v_color = "#EAB308"; v_icon = "🤔 MAYBE"
        v_bg = "rgba(234,179,8,0.12)"
        v_msg = "Borderline. One more pass and it could flip."
    else:
        v_color = "#EF4444"; v_icon = "❌ PASS"
        v_bg = "rgba(239,68,68,0.12)"
        v_msg = "Hard pass. Fix it before you apply anywhere."

    import re as _re
    def _li_clean(text: str) -> str:
        text = text.strip()
        text = _re.sub(r'^#{1,6}\s*', '', text)
        text = _re.sub(r'\*\*', '', text)
        text = _re.sub(r'\*(?!\s)', '', text)
        text = _re.sub(r'^[-–—•]\s*', '', text)
        text = _re.sub(r'(?i)^verdict\s*:\s*', '', text)
        return text.strip()

    clean_verdict = _li_clean(verdict_text)
    clean_roast   = _li_clean(linkedin_roast)
    roast_display = (clean_roast[:160] + "…") if len(clean_roast) > 160 else clean_roast
    verdict_display = (clean_verdict[:120] + "…") if len(clean_verdict) > 120 else clean_verdict

    # RGB components for rgba()
    _scr = int(sc_color[1:3], 16)
    _scg = int(sc_color[3:5], 16)
    _scb = int(sc_color[5:7], 16)

    li_text = (
        f"I just survived the Brutal Recruiter on Resume Ripper AI 😤\n\n"
        f"Recruiter Score: {score_val}/10 — {sc_label}\n"
        f"Verdict: {clean_verdict}\n\n"
        f"🔥 \"{clean_roast[:100]}{'…' if len(clean_roast) > 100 else ''}\"\n\n"
        f"Would your resume survive the roast?\n"
        f"#ResumeRoaster #BrutalRecruiter #JobSearch #CareerTips #AI"
    )
    li_text_json = _json.dumps(li_text)
    br_copy_text_json = _json.dumps(copy_text or li_text)
    br_roast_text_json = _json.dumps(roast_result_full)

    st.markdown('<div style="font-size:1.1rem;font-weight:800;color:#FF4B4B;margin:24px 0 8px 0;letter-spacing:0.5px;font-family:inherit;">😤 Share Your Results</div>', unsafe_allow_html=True)
    st.markdown(
        '<div style="font-size:0.82rem;color:#6B7280;margin-bottom:10px;">'
        'Screenshot this card and share it on LinkedIn — dare your network to beat your score.</div>',
        unsafe_allow_html=True,
    )
    components.html(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    * {{ box-sizing: border-box; }}

    .br-card {{
        background: linear-gradient(160deg, #0f0202 0%, #1e0808 40%, #120404 100%);
        border: 1.5px solid rgba({_scr},{_scg},{_scb},0.35);
        border-radius: 24px;
        padding: 32px 28px 26px 28px;
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
        max-width: 560px;
        margin: 0 auto;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 60px rgba({_scr},{_scg},{_scb},0.15), 0 20px 60px rgba(0,0,0,0.6);
    }}
    /* top accent stripe */
    .br-card::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; height: 3px;
        background: linear-gradient(90deg, transparent 0%, {sc_color} 40%, {sc_color} 60%, transparent 100%);
    }}
    /* subtle bg glow orb */
    .br-card::after {{
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 200px; height: 200px;
        background: radial-gradient(circle, rgba({_scr},{_scg},{_scb},0.12) 0%, transparent 70%);
        pointer-events: none;
    }}

    .br-toprow {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 24px;
    }}
    .br-brand {{
        font-size: 0.75rem;
        color: #6B7280;
        letter-spacing: 2.5px;
        font-weight: 700;
        text-transform: uppercase;
    }}
    .br-brand span {{ color: #FF4B4B; }}
    .br-badge {{
        font-size: 0.7rem;
        color: #FF4B4B;
        font-weight: 800;
        letter-spacing: 1px;
        background: rgba(255,75,75,0.12);
        border: 1px solid rgba(255,75,75,0.3);
        border-radius: 20px;
        padding: 4px 12px;
        text-transform: uppercase;
    }}

    /* ── Score ring + number ── */
    .br-score-section {{
        display: flex;
        align-items: center;
        gap: 24px;
        margin-bottom: 22px;
    }}
    .br-ring-wrap {{
        position: relative;
        width: 130px;
        height: 130px;
        flex-shrink: 0;
    }}
    .br-ring-inner {{
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        line-height: 1;
    }}
    .br-score-num {{
        font-size: 3rem;
        font-weight: 900;
        color: {sc_color};
        line-height: 1;
        display: block;
        filter: drop-shadow(0 0 10px {sc_color});
    }}
    .br-score-denom {{
        font-size: 0.65rem;
        color: #6B7280;
        letter-spacing: 1.5px;
        margin-top: 2px;
        display: block;
    }}
    .br-score-right {{
        flex: 1;
    }}
    .br-verdict-label {{
        font-size: 2.4rem;
        font-weight: 900;
        color: {sc_color};
        letter-spacing: 3px;
        line-height: 1;
        filter: drop-shadow(0 0 8px {sc_color});
        margin-bottom: 6px;
    }}
    .br-grade-row {{
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin-bottom: 8px;
    }}
    .br-pill {{
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0.5px;
    }}
    .br-verdict-sub {{
        font-size: 0.82rem;
        color: #9CA3AF;
        font-style: italic;
        line-height: 1.45;
    }}

    /* ── Verdict box ── */
    .br-verdict-box {{
        background: {v_bg};
        border: 1px solid rgba({_scr},{_scg},{_scb},0.3);
        border-radius: 14px;
        padding: 14px 18px;
        margin-bottom: 16px;
    }}
    .br-verdict-tag {{
        font-size: 0.62rem;
        color: {v_color};
        font-weight: 800;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 6px;
    }}
    .br-verdict-text {{
        font-size: 0.92rem;
        color: #E5E7EB;
        line-height: 1.55;
    }}

    /* ── Quote box ── */
    .br-quote {{
        background: rgba(168,85,247,0.08);
        border-left: 3px solid #A855F7;
        border-radius: 0 10px 10px 0;
        padding: 12px 16px;
        margin-bottom: 18px;
        font-size: 0.85rem;
        color: #E9D5FF;
        font-style: italic;
        line-height: 1.55;
    }}

    /* ── Footer ── */
    .br-footer {{
        border-top: 1px solid rgba(255,255,255,0.06);
        padding-top: 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .br-cta {{
        font-size: 0.8rem;
        color: #FF8C00;
        font-weight: 800;
    }}
    .br-hashtags {{
        font-size: 0.68rem;
        color: #374151;
        letter-spacing: 0.5px;
    }}
    </style>

    <div class="br-card" id="br-card">
        <!-- Top row -->
        <div class="br-toprow">
            <div class="br-brand"><span>🔥</span> Resume Ripper AI</div>
            <div class="br-badge">😤 Brutal Recruiter</div>
        </div>

        <!-- Score ring + verdict label -->
        <div class="br-score-section">
            <div class="br-ring-wrap">
                <svg width="130" height="130" viewBox="0 0 130 130">
                    <circle cx="65" cy="65" r="54" fill="none" stroke="rgba({_scr},{_scg},{_scb},0.15)" stroke-width="12"/>
                    <circle cx="65" cy="65" r="54" fill="none" stroke="{sc_color}" stroke-width="12"
                        stroke-dasharray="{dash} {circumference}" stroke-linecap="round"
                        transform="rotate(-90 65 65)"
                        style="filter:drop-shadow(0 0 10px {sc_color});"/>
                </svg>
                <div class="br-ring-inner">
                    <span class="br-score-num">{score_val}</span>
                    <span class="br-score-denom">OUT OF 10</span>
                </div>
            </div>
            <div class="br-score-right">
                <div class="br-verdict-label">{sc_label}</div>
                <div class="br-grade-row">
                    <span class="br-pill" style="background:rgba({_scr},{_scg},{_scb},0.15);color:{sc_color};border:1px solid rgba({_scr},{_scg},{_scb},0.4);">Grade {sc_grade}</span>
                    <span class="br-pill" style="background:rgba({_scr},{_scg},{_scb},0.15);color:{sc_color};border:1px solid rgba({_scr},{_scg},{_scb},0.4);">{v_icon}</span>
                </div>
                <div class="br-verdict-sub">{v_msg}</div>
            </div>
        </div>

        <!-- Verdict box -->
        <div class="br-verdict-box">
            <div class="br-verdict-tag">⚖️ Recruiter Verdict</div>
            <div class="br-verdict-text">{verdict_display}</div>
        </div>

        <!-- LinkedIn roast quote -->
        <div class="br-quote">🔥 "{roast_display}"</div>

        <!-- Footer -->
        <div class="br-footer">
            <div class="br-cta">🔥 Try Resume Ripper AI — it's free!</div>
            <div class="br-hashtags">#ResumeRoaster #JobSearch #AI</div>
        </div>
    </div>

    <div style="display:flex;gap:10px;margin-top:14px;max-width:560px;margin-left:auto;margin-right:auto;">
        <button onclick="saveCardImage()" style="
            flex:1;padding:12px 0;border-radius:12px;border:none;cursor:pointer;
            background:linear-gradient(90deg,#FF4B4B,#FF8C00);color:#fff;
            font-size:0.9rem;font-weight:800;letter-spacing:0.5px;
            font-family:'Inter','Segoe UI',Arial,sans-serif;
            box-shadow:0 4px 20px rgba(255,75,75,0.35);
            transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">
            📸 Save Card as Image
        </button>
        <button onclick="postLinkedIn()" style="
            flex:1;padding:12px 0;border-radius:12px;border:none;cursor:pointer;
            background:#0A66C2;color:#fff;font-size:0.9rem;font-weight:800;letter-spacing:0.5px;
            font-family:'Inter','Segoe UI',Arial,sans-serif;
            box-shadow:0 4px 20px rgba(10,102,194,0.35);
            transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">
            💼 Post on LinkedIn
        </button>
    </div>
    <div id="br-hint" style="
        display:none;max-width:560px;margin:8px auto 0 auto;
        font-size:0.76rem;color:#22C55E;text-align:center;font-weight:700;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    ">✅ Card saved! Attach the image to your LinkedIn post.</div>

    <div style="display:flex;flex-direction:column;gap:8px;margin-top:8px;max-width:560px;margin-left:auto;margin-right:auto;">
        <button onclick="brCopyText()" style="
            width:100%;padding:12px 0;border-radius:12px;border:none;cursor:pointer;
            background:#FF8C00;color:#fff;font-size:0.92rem;font-weight:800;letter-spacing:0.5px;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">📋 Copy Text</button>
        <button onclick="brDownload()" style="
            width:100%;padding:12px 0;border-radius:12px;border:1.5px solid #FF8C00;cursor:pointer;
            background:#1e1e1e;color:#FF8C00;font-size:0.92rem;font-weight:800;letter-spacing:0.5px;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">📥 Download</button>
    </div>
    <div id="br-copy-fb" style="
        display:none;max-width:560px;margin:6px auto 0 auto;
        font-size:0.76rem;color:#22C55E;text-align:center;font-weight:700;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    ">✅ Copied to clipboard!</div>

    <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
    <script>
    const LI_TEXT = {li_text_json};
    const BR_COPY_TEXT = {br_copy_text_json};
    const BR_ROAST_TEXT = {br_roast_text_json};

    function saveCardImage() {{
        var card = document.getElementById('br-card');
        html2canvas(card, {{
            backgroundColor: '#0f0202',
            scale: 2,
            useCORS: true,
            logging: false
        }}).then(function(canvas) {{
            var link = document.createElement('a');
            link.download = 'resume_ripper_score.png';
            link.href = canvas.toDataURL('image/png');
            link.click();
            document.getElementById('br-hint').style.display = 'block';
            setTimeout(function() {{ document.getElementById('br-hint').style.display = 'none'; }}, 4000);
        }});
    }}

    function postLinkedIn() {{
        window.open('https://www.linkedin.com/feed/?shareActive=true&text=' + encodeURIComponent(LI_TEXT), '_blank');
    }}
    function brCopyText() {{
        var show = function() {{
            var fb = document.getElementById('br-copy-fb');
            fb.style.display = 'block';
            setTimeout(function() {{ fb.style.display = 'none'; }}, 2200);
        }};
        var fallback = function() {{
            try {{
                var ta = window.parent.document.createElement('textarea');
                ta.value = BR_COPY_TEXT; ta.style.cssText = 'position:fixed;opacity:0;top:0;left:0;';
                window.parent.document.body.appendChild(ta); ta.focus(); ta.select();
                window.parent.document.execCommand('copy');
                window.parent.document.body.removeChild(ta); show();
            }} catch(e) {{ alert('Copy failed — please copy manually.'); }}
        }};
        try {{ window.parent.navigator.clipboard.writeText(BR_COPY_TEXT).then(show, fallback); }}
        catch(e) {{ fallback(); }}
    }}
    function brDownload() {{
        var blob = new Blob([BR_ROAST_TEXT], {{type:'text/plain;charset=utf-8'}});
        var url = URL.createObjectURL(blob);
        var a = window.parent.document.createElement('a');
        a.href = url; a.download = 'brutal_recruiter_roast.txt';
        window.parent.document.body.appendChild(a); a.click();
        window.parent.document.body.removeChild(a); URL.revokeObjectURL(url);
    }}
    </script>
    """, height=760)


# ═══════════════════════════════════════════════════════════════════════════════
#  CAREER COACH LINKEDIN SHARE CARD
# ═══════════════════════════════════════════════════════════════════════════════
def _render_cc_linkedin_card(score_val: int, sc_label: str, sc_grade: str, sc_color: str, closer_text: str,
                             strengths: list = None, growth: list = None, actions: list = None,
                             copy_text: str = "", roast_result_full: str = ""):
    """Render a screenshot-ready LinkedIn share card for the Career Coach."""
    import json as _json, re as _re

    circumference = round(2 * 3.14159 * 40, 1)
    dash = round(score_val / 10 * circumference, 1)

    def _cc_clean(text):
        text = _re.sub(r'^#{1,6}\s*', '', text.strip())
        text = _re.sub(r'\*\*', '', text)
        text = _re.sub(r'\*(?!\s)', '', text)
        text = _re.sub(r'^[-–—•🌟🎯🚀]\s*', '', text)
        # Strip leading name (e.g. "Anurag, ..." or "Anurag! ...")
        text = _re.sub(r'^[A-Z][a-z]+[,!]\s*', '', text)
        return text.strip()

    clean_closer = _cc_clean(closer_text)
    closer_display = (clean_closer[:120] + "…") if len(clean_closer) > 120 else clean_closer

    li_text = (
        f"Just got my resume reviewed by an AI Career Coach on Resume Ripper AI 🧑‍🏫\n\n"
        f"Resume Strength: {score_val}/10 — {sc_label} (Grade {sc_grade})\n\n"
        f"💬 \"{clean_closer}\"\n\n"
        f"Would you like a free resume review? 🚀\n"
        f"#ResumeRipper #CareerCoach #JobSearch #CareerTips #AI"
    )
    li_text_json = _json.dumps(li_text)
    cc_copy_text_json = _json.dumps(copy_text or li_text)
    cc_roast_text_json = _json.dumps(roast_result_full)

    st.markdown('<div style="font-size:1.1rem;font-weight:800;color:#22C55E;margin:24px 0 8px 0;letter-spacing:0.5px;font-family:inherit;">🧑‍🏫 Share Your Results</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.82rem;color:#6B7280;margin-bottom:6px;">Save the card as an image, then attach it to your LinkedIn post.</div>', unsafe_allow_html=True)
    components.html(f"""
    <style>
    .cc-card {{
        background:linear-gradient(135deg,#051a0a 0%,#0d2a14 60%,#051a0a 100%);
        border:1px solid #1a5a2a;
        border-radius:18px;
        padding:22px 20px 18px 20px;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
        max-width:520px;
        margin:0 auto;
        position:relative;
        overflow:hidden;
        box-shadow:0 8px 40px #22C55E18;
    }}
    .cc-card::before {{
        content:'';
        position:absolute;
        top:0;left:0;right:0;height:2px;
        background:linear-gradient(90deg,transparent,{sc_color},{sc_color}88,transparent);
    }}
    .cc-header {{ display:flex;justify-content:space-between;align-items:center;margin-bottom:18px; }}
    .cc-brand  {{ font-size:0.7rem;color:#6B7280;letter-spacing:2px;font-weight:700;text-transform:uppercase; }}
    .cc-badge  {{ font-size:0.7rem;color:#22C55E;font-weight:800;letter-spacing:1px;
                  background:#22C55E18;border:1px solid #22C55E44;border-radius:20px;padding:3px 10px; }}
    .cc-hero   {{ display:flex;align-items:center;gap:20px;margin-bottom:18px; }}
    .cc-closer-box {{
        background:#0a2a12;border-left:3px solid #22C55E;border-radius:8px;
        padding:10px 14px;margin-bottom:16px;
        font-size:0.82rem;color:#BBF7D0;font-style:italic;line-height:1.5;
    }}
    .cc-footer {{
        border-top:1px solid #1a3a22;padding-top:12px;
        display:flex;justify-content:space-between;align-items:center;
    }}
    .cc-cta {{ font-size:0.78rem;color:#FF8C00;font-weight:700; }}
    .cc-sub  {{ font-size:0.72rem;color:#374151; }}
    </style>
    <div class="cc-card">
        <div class="cc-header">
            <div class="cc-brand">🔥 Resume Ripper AI</div>
            <div class="cc-badge">🧑‍🏫 Career Coach</div>
        </div>
        <div class="cc-hero">
            <div style="position:relative;width:90px;height:90px;flex-shrink:0;">
                <svg width="90" height="90" viewBox="0 0 90 90">
                    <circle cx="45" cy="45" r="40" fill="none" stroke="#1a3a22" stroke-width="9"/>
                    <circle cx="45" cy="45" r="40" fill="none" stroke="{sc_color}" stroke-width="9"
                        stroke-dasharray="{dash} {circumference}" stroke-linecap="round"
                        transform="rotate(-90 45 45)"
                        style="filter:drop-shadow(0 0 6px {sc_color});"/>
                </svg>
                <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;line-height:1;">
                    <div style="font-size:1.7rem;font-weight:900;color:{sc_color};line-height:1;">{score_val}</div>
                    <div style="font-size:0.52rem;color:#6B7280;letter-spacing:1px;">/ 10</div>
                </div>
            </div>
            <div>
                <div style="font-size:1.8rem;font-weight:900;color:{sc_color};letter-spacing:2px;line-height:1;">{sc_label}</div>
                <div style="font-size:0.82rem;color:#9CA3AF;margin-top:4px;">Resume Strength</div>
                <div style="margin-top:8px;">
                    <span style="background:{sc_color}22;color:{sc_color};border:1px solid {sc_color}55;border-radius:20px;padding:3px 12px;font-size:0.78rem;font-weight:800;">Grade {sc_grade}</span>
                </div>
            </div>
        </div>
        <div class="cc-closer-box">💬 "{closer_display}"</div>
        <div class="cc-footer">
            <div class="cc-cta">🔥 Try Resume Ripper AI — it's free!</div>
            <div class="cc-sub">Level up your resume today.</div>
        </div>
    </div>

    <div style="display:flex;gap:10px;margin-top:14px;max-width:520px;margin-left:auto;margin-right:auto;">
        <button onclick="saveCCCard()" style="
            flex:1;padding:10px 0;border-radius:10px;border:none;cursor:pointer;
            background:#22C55E;color:#fff;font-size:0.88rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">📸 Save Card as Image</button>
        <button onclick="postCCLinkedIn()" style="
            flex:1;padding:10px 0;border-radius:10px;border:none;cursor:pointer;
            background:#0A66C2;color:#fff;font-size:0.88rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">💼 Post on LinkedIn</button>
    </div>
    <div id="cc-hint" style="
        display:none;max-width:520px;margin:8px auto 0 auto;
        font-size:0.75rem;color:#22C55E;text-align:center;font-weight:600;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    ">✅ Card saved! Attach the image to your LinkedIn post.</div>

    <div style="display:flex;flex-direction:column;gap:8px;margin-top:8px;max-width:520px;margin-left:auto;margin-right:auto;">
        <button onclick="ccCopyText()" style="
            width:100%;padding:12px 0;border-radius:10px;border:none;cursor:pointer;
            background:#FF8C00;color:#fff;font-size:0.92rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">📋 Copy Text</button>
        <button onclick="ccDownload()" style="
            width:100%;padding:12px 0;border-radius:10px;border:1.5px solid #FF8C00;cursor:pointer;
            background:#1e1e1e;color:#FF8C00;font-size:0.92rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">📥 Download</button>
    </div>
    <div id="cc-copy-fb" style="
        display:none;max-width:520px;margin:6px auto 0 auto;
        font-size:0.75rem;color:#22C55E;text-align:center;font-weight:600;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    ">✅ Copied to clipboard!</div>

    <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
    <script>
    const CC_LI_TEXT = {li_text_json};
    const CC_COPY_TEXT = {cc_copy_text_json};
    const CC_ROAST_TEXT = {cc_roast_text_json};
    function saveCCCard() {{
        const card = document.querySelector('.cc-card');
        html2canvas(card, {{ backgroundColor:'#051a0a', scale:2, useCORS:true, logging:false }})
        .then(canvas => {{
            const link = document.createElement('a');
            link.download = 'career_coach_score.png';
            link.href = canvas.toDataURL('image/png');
            link.click();
            document.getElementById('cc-hint').style.display = 'block';
            setTimeout(() => {{ document.getElementById('cc-hint').style.display = 'none'; }}, 4000);
        }});
    }}
    function postCCLinkedIn() {{
        window.open('https://www.linkedin.com/feed/?shareActive=true&text=' + encodeURIComponent(CC_LI_TEXT), '_blank');
    }}
    function ccCopyText() {{
        var show = function() {{
            var fb = document.getElementById('cc-copy-fb');
            fb.style.display = 'block';
            setTimeout(function() {{ fb.style.display = 'none'; }}, 2200);
        }};
        var fallback = function() {{
            try {{
                var ta = window.parent.document.createElement('textarea');
                ta.value = CC_COPY_TEXT; ta.style.cssText = 'position:fixed;opacity:0;top:0;left:0;';
                window.parent.document.body.appendChild(ta); ta.focus(); ta.select();
                window.parent.document.execCommand('copy');
                window.parent.document.body.removeChild(ta); show();
            }} catch(e) {{ alert('Copy failed — please copy manually.'); }}
        }};
        try {{ window.parent.navigator.clipboard.writeText(CC_COPY_TEXT).then(show, fallback); }}
        catch(e) {{ fallback(); }}
    }}
    function ccDownload() {{
        var blob = new Blob([CC_ROAST_TEXT], {{type:'text/plain;charset=utf-8'}});
        var url = URL.createObjectURL(blob);
        var a = window.parent.document.createElement('a');
        a.href = url; a.download = 'career_coach_roast.txt';
        window.parent.document.body.appendChild(a); a.click();
        window.parent.document.body.removeChild(a); URL.revokeObjectURL(url);
    }}
    </script>
    """, height=520)


# ═══════════════════════════════════════════════════════════════════════════════
#  INTERNET TROLL LINKEDIN SHARE CARD
# ═══════════════════════════════════════════════════════════════════════════════
def _render_it_linkedin_card(score_val: int, sc_label: str, sc_grade: str, sc_color: str, closing_roast: str,
                             copy_text: str = "", roast_result_full: str = ""):
    """Render a screenshot-ready LinkedIn share card for the Internet Troll."""
    import json as _json, re as _re

    circumference = round(2 * 3.14159 * 40, 1)
    dash = round(score_val / 10 * circumference, 1)

    def _it_clean(text):
        text = _re.sub(r'^#{1,6}\s*', '', text.strip())
        text = _re.sub(r'\*\*', '', text)
        text = _re.sub(r'\*(?!\s)', '', text)
        text = _re.sub(r'^[-–—•😂🤡🧠💀]\s*', '', text)
        text = _re.sub(r'^[A-Z][a-z]+[,!]\s*', '', text)
        return text.strip()

    clean_roast = _it_clean(closing_roast)
    roast_display = (clean_roast[:120] + "…") if len(clean_roast) > 120 else clean_roast

    li_text = (
        f"Just got my resume roasted by the Internet Troll on Resume Ripper AI 🧌\n\n"
        f"Cringe Score: {score_val}/10 — {sc_label}\n\n"
        f"🔥 \"{clean_roast[:110]}{'…' if len(clean_roast) > 110 else ''}\"\n\n"
        f"Would your resume survive the roast? 😂\n"
        f"#ResumeRipper #InternetTroll #JobSearch #CareerTips #AI"
    )
    li_text_json = _json.dumps(li_text)
    it_copy_text_json = _json.dumps(copy_text or li_text)
    it_roast_text_json = _json.dumps(roast_result_full)

    st.markdown('<div style="font-size:1.1rem;font-weight:800;color:#A855F7;margin:24px 0 8px 0;letter-spacing:0.5px;font-family:inherit;">🧌 Share Your Results</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.82rem;color:#6B7280;margin-bottom:6px;">Save the card as an image, then attach it to your LinkedIn post.</div>', unsafe_allow_html=True)
    components.html(f"""
    <style>
    .it-card {{
        background:linear-gradient(135deg,#0d0514 0%,#1a0a2e 60%,#0d0514 100%);
        border:1px solid #3b1a5a;
        border-radius:18px;
        padding:22px 20px 18px 20px;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
        max-width:520px;
        margin:0 auto;
        position:relative;
        overflow:hidden;
        box-shadow:0 8px 40px #A855F718;
    }}
    .it-card::before {{
        content:'';
        position:absolute;
        top:0;left:0;right:0;height:2px;
        background:linear-gradient(90deg,transparent,{sc_color},{sc_color}88,transparent);
    }}
    .it-header {{ display:flex;justify-content:space-between;align-items:center;margin-bottom:18px; }}
    .it-brand  {{ font-size:0.7rem;color:#6B7280;letter-spacing:2px;font-weight:700;text-transform:uppercase; }}
    .it-badge  {{ font-size:0.7rem;color:#A855F7;font-weight:800;letter-spacing:1px;
                  background:#A855F718;border:1px solid #A855F744;border-radius:20px;padding:3px 10px; }}
    .it-hero   {{ display:flex;align-items:center;gap:20px;margin-bottom:18px; }}
    .it-roast-box {{
        background:#1a0a2e;border-left:3px solid #A855F7;border-radius:8px;
        padding:10px 14px;margin-bottom:16px;
        font-size:0.82rem;color:#E9D5FF;font-style:italic;line-height:1.5;
    }}
    .it-footer {{
        border-top:1px solid #2a1a3a;padding-top:12px;
        display:flex;justify-content:space-between;align-items:center;
    }}
    .it-cta {{ font-size:0.78rem;color:#FF8C00;font-weight:700; }}
    .it-sub  {{ font-size:0.72rem;color:#374151; }}
    </style>
    <div class="it-card">
        <div class="it-header">
            <div class="it-brand">🔥 Resume Ripper AI</div>
            <div class="it-badge">🧌 Internet Troll</div>
        </div>
        <div class="it-hero">
            <div style="position:relative;width:90px;height:90px;flex-shrink:0;">
                <svg width="90" height="90" viewBox="0 0 90 90">
                    <circle cx="45" cy="45" r="40" fill="none" stroke="#2a1a3a" stroke-width="9"/>
                    <circle cx="45" cy="45" r="40" fill="none" stroke="{sc_color}" stroke-width="9"
                        stroke-dasharray="{dash} {circumference}" stroke-linecap="round"
                        transform="rotate(-90 45 45)"
                        style="filter:drop-shadow(0 0 6px {sc_color});"/>
                </svg>
                <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;line-height:1;">
                    <div style="font-size:1.7rem;font-weight:900;color:{sc_color};line-height:1;">{score_val}</div>
                    <div style="font-size:0.52rem;color:#6B7280;letter-spacing:1px;">/ 10</div>
                </div>
            </div>
            <div>
                <div style="font-size:1.8rem;font-weight:900;color:{sc_color};letter-spacing:2px;line-height:1;">{sc_label}</div>
                <div style="font-size:0.82rem;color:#9CA3AF;margin-top:4px;">Cringe Score</div>
                <div style="margin-top:8px;">
                    <span style="background:{sc_color}22;color:{sc_color};border:1px solid {sc_color}55;border-radius:20px;padding:3px 12px;font-size:0.78rem;font-weight:800;">Grade {sc_grade}</span>
                </div>
            </div>
        </div>
        <div class="it-roast-box">🔥 "{roast_display}"</div>
        <div class="it-footer">
            <div class="it-cta">🔥 Try Resume Ripper AI — it's free!</div>
            <div class="it-sub">Would your resume survive?</div>
        </div>
    </div>

    <div style="display:flex;gap:10px;margin-top:14px;max-width:520px;margin-left:auto;margin-right:auto;">
        <button onclick="saveITCard()" style="
            flex:1;padding:10px 0;border-radius:10px;border:none;cursor:pointer;
            background:#A855F7;color:#fff;font-size:0.88rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">📸 Save Card as Image</button>
        <button onclick="postITLinkedIn()" style="
            flex:1;padding:10px 0;border-radius:10px;border:none;cursor:pointer;
            background:#0A66C2;color:#fff;font-size:0.88rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">💼 Post on LinkedIn</button>
    </div>
    <div id="it-hint" style="
        display:none;max-width:520px;margin:8px auto 0 auto;
        font-size:0.75rem;color:#22C55E;text-align:center;font-weight:600;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    ">✅ Card saved! Attach the image to your LinkedIn post.</div>

    <div style="display:flex;flex-direction:column;gap:8px;margin-top:8px;max-width:520px;margin-left:auto;margin-right:auto;">
        <button onclick="itCopyText()" style="
            width:100%;padding:12px 0;border-radius:10px;border:none;cursor:pointer;
            background:#FF8C00;color:#fff;font-size:0.92rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">📋 Copy Text</button>
        <button onclick="itDownload()" style="
            width:100%;padding:12px 0;border-radius:10px;border:1.5px solid #FF8C00;cursor:pointer;
            background:#1e1e1e;color:#FF8C00;font-size:0.92rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">📥 Download</button>
    </div>
    <div id="it-copy-fb" style="
        display:none;max-width:520px;margin:6px auto 0 auto;
        font-size:0.75rem;color:#22C55E;text-align:center;font-weight:600;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    ">✅ Copied to clipboard!</div>

    <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
    <script>
    const IT_LI_TEXT = {li_text_json};
    const IT_COPY_TEXT = {it_copy_text_json};
    const IT_ROAST_TEXT = {it_roast_text_json};
    function saveITCard() {{
        const card = document.querySelector('.it-card');
        html2canvas(card, {{ backgroundColor:'#0d0514', scale:2, useCORS:true, logging:false }})
        .then(canvas => {{
            const link = document.createElement('a');
            link.download = 'internet_troll_score.png';
            link.href = canvas.toDataURL('image/png');
            link.click();
            document.getElementById('it-hint').style.display = 'block';
            setTimeout(() => {{ document.getElementById('it-hint').style.display = 'none'; }}, 4000);
        }});
    }}
    function postITLinkedIn() {{
        window.open('https://www.linkedin.com/feed/?shareActive=true&text=' + encodeURIComponent(IT_LI_TEXT), '_blank');
    }}
    function itCopyText() {{
        var show = function() {{
            var fb = document.getElementById('it-copy-fb');
            fb.style.display = 'block';
            setTimeout(function() {{ fb.style.display = 'none'; }}, 2200);
        }};
        var fallback = function() {{
            try {{
                var ta = window.parent.document.createElement('textarea');
                ta.value = IT_COPY_TEXT; ta.style.cssText = 'position:fixed;opacity:0;top:0;left:0;';
                window.parent.document.body.appendChild(ta); ta.focus(); ta.select();
                window.parent.document.execCommand('copy');
                window.parent.document.body.removeChild(ta); show();
            }} catch(e) {{ alert('Copy failed — please copy manually.'); }}
        }};
        try {{ window.parent.navigator.clipboard.writeText(IT_COPY_TEXT).then(show, fallback); }}
        catch(e) {{ fallback(); }}
    }}
    function itDownload() {{
        var blob = new Blob([IT_ROAST_TEXT], {{type:'text/plain;charset=utf-8'}});
        var url = URL.createObjectURL(blob);
        var a = window.parent.document.createElement('a');
        a.href = url; a.download = 'internet_troll_roast.txt';
        window.parent.document.body.appendChild(a); a.click();
        window.parent.document.body.removeChild(a); URL.revokeObjectURL(url);
    }}
    </script>
    """, height=520)


# ═══════════════════════════════════════════════════════════════════════════════
#  TOP HIRING MANAGER LINKEDIN SHARE CARD
# ═══════════════════════════════════════════════════════════════════════════════
def _render_hm_linkedin_card(score_val: int, sc_label: str, sc_grade: str, sc_color: str,
                              verdict_text: str, interview_decision: str,
                              copy_text: str = "", roast_result_full: str = ""):
    import json as _json, re as _re

    circumference = round(2 * 3.14159 * 40, 1)
    dash = round(score_val / 10 * circumference, 1)

    def _hm_clean(text):
        text = _re.sub(r'^#{1,6}\s*', '', text.strip())
        text = _re.sub(r'\*\*', '', text)
        text = _re.sub(r'\*(?!\s)', '', text)
        text = _re.sub(r'^[-–—•✔️⚠️📈💼👀🏆]\s*', '', text)
        text = _re.sub(r'^[A-Z][a-z]+[,!]\s*', '', text)
        return text.strip()

    clean_verdict = _hm_clean(verdict_text)
    clean_interview = _hm_clean(interview_decision)

    low_v = clean_verdict.lower()
    if "shortlist" in low_v:
        v_color = "#22C55E"; v_icon = "✅ SHORTLIST"
    elif "consider" in low_v:
        v_color = "#F59E0B"; v_icon = "🤔 CONSIDER"
    else:
        v_color = "#EF4444"; v_icon = "❌ PASS"

    low_i = clean_interview.lower()
    if "yes" in low_i:
        i_color = "#22C55E"; i_text = "Yes — Would Interview"
    elif "maybe" in low_i or "possibly" in low_i:
        i_color = "#F59E0B"; i_text = "Maybe"
    else:
        i_color = "#EF4444"; i_text = "No"

    li_text = (
        f"Just had my resume assessed by a Top Hiring Manager on Resume Ripper AI 🏆\n\n"
        f"Shortlist Score: {score_val}/10 — {sc_label} (Grade {sc_grade})\n"
        f"Verdict: {clean_verdict}\n"
        f"Would I be interviewed? → {clean_interview}\n\n"
        f"Would your resume make the shortlist? 👀\n"
        f"#ResumeRipper #HiringManager #JobSearch #CareerTips #AI"
    )
    li_text_json = _json.dumps(li_text)
    hm_copy_text_json = _json.dumps(copy_text or li_text)
    hm_roast_text_json = _json.dumps(roast_result_full)

    st.markdown('<div style="font-size:1.1rem;font-weight:800;color:#F59E0B;margin:24px 0 8px 0;letter-spacing:0.5px;font-family:inherit;">🏆 Share Your Results</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.82rem;color:#6B7280;margin-bottom:6px;">Save the card as an image, then attach it to your LinkedIn post.</div>', unsafe_allow_html=True)
    components.html(f"""
    <style>
    .hm-card {{
        background:linear-gradient(135deg,#0f0c00 0%,#1f1800 60%,#0f0c00 100%);
        border:1px solid #5a3a00;
        border-radius:18px;
        padding:22px 20px 18px 20px;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
        max-width:520px;
        margin:0 auto;
        position:relative;
        overflow:hidden;
        box-shadow:0 8px 40px #F59E0B18;
    }}
    .hm-card::before {{
        content:'';position:absolute;top:0;left:0;right:0;height:2px;
        background:linear-gradient(90deg,transparent,{sc_color},{sc_color}88,transparent);
    }}
    .hm-header {{ display:flex;justify-content:space-between;align-items:center;margin-bottom:18px; }}
    .hm-brand  {{ font-size:0.7rem;color:#6B7280;letter-spacing:2px;font-weight:700;text-transform:uppercase; }}
    .hm-badge  {{ font-size:0.7rem;color:#F59E0B;font-weight:800;letter-spacing:1px;
                  background:#F59E0B18;border:1px solid #F59E0B44;border-radius:20px;padding:3px 10px; }}
    .hm-hero   {{ display:flex;align-items:center;gap:20px;margin-bottom:18px; }}
    .hm-footer {{
        border-top:1px solid #2a1f00;padding-top:12px;
        display:flex;justify-content:space-between;align-items:center;
    }}
    </style>
    <div class="hm-card">
        <div class="hm-header">
            <div class="hm-brand">🔥 Resume Ripper AI</div>
            <div class="hm-badge">🏆 Top Hiring Manager</div>
        </div>
        <div class="hm-hero">
            <div style="position:relative;width:90px;height:90px;flex-shrink:0;">
                <svg width="90" height="90" viewBox="0 0 90 90">
                    <circle cx="45" cy="45" r="40" fill="none" stroke="#2a1f00" stroke-width="9"/>
                    <circle cx="45" cy="45" r="40" fill="none" stroke="{sc_color}" stroke-width="9"
                        stroke-dasharray="{dash} {circumference}" stroke-linecap="round"
                        transform="rotate(-90 45 45)"
                        style="filter:drop-shadow(0 0 6px {sc_color});"/>
                </svg>
                <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;line-height:1;">
                    <div style="font-size:1.7rem;font-weight:900;color:{sc_color};line-height:1;">{score_val}</div>
                    <div style="font-size:0.52rem;color:#6B7280;letter-spacing:1px;">/ 10</div>
                </div>
            </div>
            <div>
                <div style="font-size:1.8rem;font-weight:900;color:{sc_color};letter-spacing:2px;line-height:1;">{sc_label}</div>
                <div style="font-size:0.82rem;color:#9CA3AF;margin-top:4px;">Shortlist Score</div>
                <div style="margin-top:8px;display:flex;gap:8px;flex-wrap:wrap;">
                    <span style="background:{sc_color}22;color:{sc_color};border:1px solid {sc_color}55;border-radius:20px;padding:3px 12px;font-size:0.78rem;font-weight:800;">Grade {sc_grade}</span>
                    <span style="background:{v_color}22;color:{v_color};border:1px solid {v_color}55;border-radius:20px;padding:3px 12px;font-size:0.78rem;font-weight:800;">{v_icon}</span>
                </div>
            </div>
        </div>
        <div style="background:#1f1800;border-left:3px solid {i_color};border-radius:8px;padding:10px 14px;margin-bottom:16px;">
            <div style="font-size:0.68rem;color:{i_color};letter-spacing:1.5px;font-weight:700;margin-bottom:4px;">👀 INTERVIEW DECISION</div>
            <div style="font-size:0.92rem;color:#FEF3C7;font-weight:700;">{i_text}</div>
        </div>
        <div class="hm-footer">
            <div style="font-size:0.78rem;color:#FF8C00;font-weight:700;">🔥 Try Resume Ripper AI — it's free!</div>
            <div style="font-size:0.72rem;color:#374151;">Would you make the shortlist?</div>
        </div>
    </div>

    <div style="display:flex;gap:10px;margin-top:14px;max-width:520px;margin-left:auto;margin-right:auto;">
        <button onclick="saveHMCard()" style="
            flex:1;padding:10px 0;border-radius:10px;border:none;cursor:pointer;
            background:#F59E0B;color:#000;font-size:0.88rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1">📸 Save Card as Image</button>
        <button onclick="postHMLinkedIn()" style="
            flex:1;padding:10px 0;border-radius:10px;border:none;cursor:pointer;
            background:#0A66C2;color:#fff;font-size:0.88rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.85" onmouseout="this.style.opacity=1">💼 Post on LinkedIn</button>
    </div>
    <div id="hm-hint" style="
        display:none;max-width:520px;margin:8px auto 0 auto;
        font-size:0.75rem;color:#22C55E;text-align:center;font-weight:600;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    ">✅ Card saved! Attach the image to your LinkedIn post.</div>

    <div style="display:flex;flex-direction:column;gap:8px;margin-top:8px;max-width:520px;margin-left:auto;margin-right:auto;">
        <button onclick="hmCopyText()" style="
            width:100%;padding:12px 0;border-radius:10px;border:none;cursor:pointer;
            background:#FF8C00;color:#fff;font-size:0.92rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1">📋 Copy Text</button>
        <button onclick="hmDownload()" style="
            width:100%;padding:12px 0;border-radius:10px;border:1.5px solid #FF8C00;cursor:pointer;
            background:#1e1e1e;color:#FF8C00;font-size:0.92rem;font-weight:700;
            font-family:'Inter','Segoe UI',Arial,sans-serif;transition:opacity 0.15s;
        " onmouseover="this.style.opacity=0.8" onmouseout="this.style.opacity=1">📥 Download</button>
    </div>
    <div id="hm-copy-fb" style="
        display:none;max-width:520px;margin:6px auto 0 auto;
        font-size:0.75rem;color:#22C55E;text-align:center;font-weight:600;
        font-family:'Inter','Segoe UI',Arial,sans-serif;
    ">✅ Copied to clipboard!</div>

    <script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
    <script>
    const HM_LI_TEXT = {li_text_json};
    const HM_COPY_TEXT = {hm_copy_text_json};
    const HM_ROAST_TEXT = {hm_roast_text_json};
    function saveHMCard() {{
        const card = document.querySelector('.hm-card');
        html2canvas(card, {{ backgroundColor:'#0f0c00', scale:2, useCORS:true, logging:false }})
        .then(canvas => {{
            const link = document.createElement('a');
            link.download = 'hiring_manager_score.png';
            link.href = canvas.toDataURL('image/png');
            link.click();
            document.getElementById('hm-hint').style.display = 'block';
            setTimeout(() => {{ document.getElementById('hm-hint').style.display = 'none'; }}, 4000);
        }});
    }}
    function postHMLinkedIn() {{
        window.open('https://www.linkedin.com/feed/?shareActive=true&text=' + encodeURIComponent(HM_LI_TEXT), '_blank');
    }}
    function hmCopyText() {{
        var show = function() {{
            var fb = document.getElementById('hm-copy-fb');
            fb.style.display = 'block';
            setTimeout(function() {{ fb.style.display = 'none'; }}, 2200);
        }};
        var fallback = function() {{
            try {{
                var ta = window.parent.document.createElement('textarea');
                ta.value = HM_COPY_TEXT; ta.style.cssText = 'position:fixed;opacity:0;top:0;left:0;';
                window.parent.document.body.appendChild(ta); ta.focus(); ta.select();
                window.parent.document.execCommand('copy');
                window.parent.document.body.removeChild(ta); show();
            }} catch(e) {{ alert('Copy failed — please copy manually.'); }}
        }};
        try {{ window.parent.navigator.clipboard.writeText(HM_COPY_TEXT).then(show, fallback); }}
        catch(e) {{ fallback(); }}
    }}
    function hmDownload() {{
        var blob = new Blob([HM_ROAST_TEXT], {{type:'text/plain;charset=utf-8'}});
        var url = URL.createObjectURL(blob);
        var a = window.parent.document.createElement('a');
        a.href = url; a.download = 'hiring_manager_roast.txt';
        window.parent.document.body.appendChild(a); a.click();
        window.parent.document.body.removeChild(a); URL.revokeObjectURL(url);
    }}
    </script>
    """, height=530)


# ═══════════════════════════════════════════════════════════════════════════════
#  SHARE BOX
# ═══════════════════════════════════════════════════════════════════════════════
def _render_share_box(share_text: str, roast_result: str, sel_name: str, show_linkedin: bool = True):
    """Render share buttons: LinkedIn (optional), Copy text, Download report."""
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
        {'<button class="sb-btn sb-li" onclick="sbLinkedIn()">💼 Post on LinkedIn</button>' if show_linkedin else ''}
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
#  SHARED HERO SCORE CARD  — single source of truth for all personas
# ═══════════════════════════════════════════════════════════════════════════════
def _render_hero_score_card(
    header_icon: str,
    header_text: str,
    header_color: str,
    bg_gradient: str,
    ring_bg: str,
    sc_color: str,
    score_val,
    out_of: str,
    dash: float,
    circumference: float,
    sc_label: str,
    sc_grade: str,
    score_type_label: str,
):
    """Render the hero score card identically across all personas."""
    st.markdown(
        f'<div style="'
        f'background:{bg_gradient};'
        f'border:1.5px solid {sc_color}44;'
        f'border-radius:20px;'
        f'padding:28px 24px 22px 24px;'
        f'margin:16px 0 20px 0;'
        f'text-align:center;'
        f'position:relative;overflow:hidden;">'
        # top accent stripe
        f'<div style="position:absolute;top:0;left:0;right:0;height:3px;'
        f'background:linear-gradient(90deg,transparent,{sc_color},{sc_color}88,transparent);"></div>'
        # header label
        f'<div style="font-size:0.75rem;color:{header_color};letter-spacing:3px;font-weight:800;'
        f'text-transform:uppercase;margin-bottom:16px;">{header_icon} {header_text}</div>'
        # score ring
        f'<div style="position:relative;width:150px;height:150px;margin:0 auto 14px auto;">'
        f'<svg width="150" height="150" viewBox="0 0 150 150">'
        f'<circle cx="75" cy="75" r="54" fill="none" stroke="{ring_bg}" stroke-width="12"/>'
        f'<circle cx="75" cy="75" r="54" fill="none" stroke="{sc_color}" stroke-width="12"'
        f' stroke-dasharray="{dash} {circumference}" stroke-linecap="round"'
        f' transform="rotate(-90 75 75)"'
        f' style="filter:drop-shadow(0 0 8px {sc_color});"/>'
        f'</svg>'
        f'<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);'
        f'text-align:center;line-height:1;">'
        f'<div style="font-size:2.8rem;font-weight:900;color:{sc_color};line-height:1;">{score_val}</div>'
        f'<div style="font-size:0.6rem;color:#9CA3AF;letter-spacing:1px;margin-top:4px;">OUT OF {out_of}</div>'
        f'</div>'
        f'</div>'
        # verdict label
        f'<div style="font-size:1.5rem;font-weight:900;color:{sc_color};letter-spacing:3px;margin-bottom:6px;">{sc_label}</div>'
        # score type + grade
        f'<div style="font-size:0.8rem;color:#9CA3AF;">'
        f'{score_type_label} &nbsp;·&nbsp; Grade <b style="color:{sc_color};">{sc_grade}</b>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ═══════════════════════════════════════════════════════════════════════════════
#  ROAST RESULTS
# ═══════════════════════════════════════════════════════════════════════════════
def render_roast_results(roast_result: str, score_breakdown: dict, sel: dict, elapsed: float):
    """Render the roast results card + share/download section."""
    st.markdown('<div class="roast-area">', unsafe_allow_html=True)

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

        _render_hero_score_card(
            header_icon="🤖", header_text="ATS SCAN COMPLETE",
            header_color="#00C9FF",
            bg_gradient="linear-gradient(135deg,#0a0f1e 0%,#0d1b2a 60%,#091422 100%)",
            ring_bg="#1e2d3d",
            sc_color=ov_color, score_val=overall_score, out_of="100",
            dash=dash, circumference=circumference,
            sc_label=ov_label, sc_grade=ov_grade,
            score_type_label="ATS Compatibility Score",
        )

        # Score Breakdown
        st.markdown(f"""
        <div style="display:flex;align-items:center;justify-content:space-between;margin:18px 0 12px 0;">
            <div class="rsh" style="font-size:1.1rem;font-weight:800;letter-spacing:0.5px;color:#ffffff;font-family:inherit;">📊 Score Breakdown</div>
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
            <div class="rsh" style="
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
                bullets = parse_weak_bullets(section_lines)
                for b in bullets:
                    orig    = b.get("Original") or "<i>—</i>"
                    issue   = b.get("Issue") or "<i>—</i>"
                    improved = b.get("Improved Version") or "<i>—</i>"
                    st.markdown(
                        '<div style="'
                        'background:#13100d;'
                        'border:1px solid #2e2418;'
                        'border-radius:16px;'
                        'margin-bottom:16px;'
                        'overflow:hidden;'
                        'box-shadow:0 4px 18px rgba(0,0,0,0.25);">'

                        # ── ORIGINAL row ──────────────────────────────────────
                        '<div style="padding:14px 18px 12px 18px;border-bottom:1px solid #2e2418;">'
                        '<span style="display:inline-block;background:#374151;color:#F9FAFB;'
                        'font-size:0.62rem;font-weight:800;letter-spacing:2.5px;'
                        'padding:3px 10px;border-radius:20px;margin-bottom:8px;'
                        'text-transform:uppercase;">📄 Original</span>'
                        f'<div style="color:#CBD5E1;font-size:0.92rem;line-height:1.6;">{orig}</div>'
                        '</div>'

                        # ── ISSUE row ─────────────────────────────────────────
                        '<div style="padding:12px 18px 12px 18px;border-bottom:1px solid #2e2418;'
                        'background:rgba(239,68,68,0.07);">'
                        '<span style="display:inline-block;background:#EF4444;color:#fff;'
                        'font-size:0.62rem;font-weight:800;letter-spacing:2.5px;'
                        'padding:3px 10px;border-radius:20px;margin-bottom:8px;'
                        'text-transform:uppercase;">⚠ Issue</span>'
                        f'<div style="color:#FECACA;font-size:0.92rem;line-height:1.6;">{issue}</div>'
                        '</div>'

                        # ── IMPROVED row ──────────────────────────────────────
                        '<div style="padding:12px 18px 16px 18px;background:rgba(34,197,94,0.07);">'
                        '<span style="display:inline-block;background:#22C55E;color:#fff;'
                        'font-size:0.62rem;font-weight:800;letter-spacing:2.5px;'
                        'padding:3px 10px;border-radius:20px;margin-bottom:8px;'
                        'text-transform:uppercase;">✓ Improved</span>'
                        f'<div style="color:#BBF7D0;font-size:0.92rem;line-height:1.6;">{improved}</div>'
                        '</div>'

                        '</div>',
                        unsafe_allow_html=True,
                    )
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


        # Extract roast one-liner for share text
        ats_roast_line = ""
        if roast_idx is not None:
            roast_section = lines[roast_idx + 1: final_idx] if final_idx else lines[roast_idx + 1:]
            for l in roast_section:
                stripped = l.strip()
                if stripped and not stripped.upper().startswith("ROAST LEVEL"):
                    ats_roast_line = stripped
                    break

        # Extract match probability
        ats_match_prob = ""
        if match_idx is not None:
            match_section = lines[match_idx + 1: detected_idx] if detected_idx else lines[match_idx + 1:]
            for l in match_section:
                stripped = l.strip().lstrip("-•").strip()
                if stripped:
                    ats_match_prob = stripped
                    break

        st.session_state["last_roast"] = roast_result
        share_text = f"I just scored {overall_score}/100 on the ATS Scanner 🤖\nHere's my resume breakdown — would yours survive? 👀\n🔥 Try it free → Resume Ripper AI\n#ResumeRoaster #ATSTips #JobSearch #CareerTips #AI"
        _render_linkedin_card(score_breakdown, overall_score, ov_label, ov_grade, ov_color,
                              ats_roast_line, ats_match_prob, display_verdict,
                              copy_text=share_text, roast_result=roast_result)

    elif sel.get("name", "").lower() == "brutal recruiter":
        import re

        lines = roast_result.split('\n')

        def find_section_br(header):
            for i, l in enumerate(lines):
                stripped = re.sub(r'[^\w\s]', '', l).strip().upper()
                if header.upper() in stripped:
                    return i
            return None

        def _clean(text: str) -> str:
            """Strip markdown artifacts: headings, bold, italic, leading dashes/bullets."""
            import html as _html
            text = text.strip()
            text = re.sub(r'^#{1,6}\s*', '', text)
            text = re.sub(r'\*\*', '', text)
            text = re.sub(r'\*(?!\s)', '', text)
            text = re.sub(r'`[^`]*`', '', text)
            text = re.sub(r'^[-–—•]\s*', '', text)
            text = re.sub(r'(?i)^verdict\s*:\s*', '', text)
            return _html.escape(text.strip())

        gut_end = find_section_br("RECRUITER SCORE")
        gut_lines = lines[:gut_end] if gut_end is not None else []
        gut_text = _clean(" ".join(l.strip() for l in gut_lines if l.strip()))
        # Strip leading all-caps name (e.g. "ANURAG SINGH") and reaction label
        gut_text = re.sub(r'^[A-Z][A-Z\s]{2,30}\s+', '', gut_text)
        gut_text = re.sub(r'(?i)^(instant|gut|first)\s*(reaction|impression)\s*:\s*', '', gut_text).strip()

        score_val = None
        score_breakdown_br = score_breakdown or []
        if score_breakdown_br:
            score_val = score_breakdown_br[0].get("score", 5)
        else:
            m = re.search(r'Recruiter Score[:\s]*(\d+)\s*/\s*10', roast_result, re.IGNORECASE)
            if m:
                score_val = int(m.group(1))
        if score_val is None:
            score_val = 5

        eye_idx    = find_section_br("WHAT CAUGHT MY EYE")
        flags_idx  = find_section_br("RED FLAGS")
        rewrite_idx = find_section_br("IF I WERE REWRITING")
        verdict_idx = None
        linkedin_idx = None
        for i, l in enumerate(lines):
            low = l.strip().lower()
            if verdict_idx is None and any(v in low for v in ["hire", "maybe", "pass"]) and ("/" in low or "·" in low or "—" in low or "-" in low or len(l.strip()) < 120):
                if i > (rewrite_idx or 0):
                    verdict_idx = i
            if linkedin_idx is None and ("linkedin" in low or "screenshot" in low or "zinger" in low):
                if i > (verdict_idx or rewrite_idx or 0):
                    linkedin_idx = i

        # Score color
        if score_val >= 8:
            sc_color = "#22C55E"; sc_grade = "A"; sc_label = "STRONG"
        elif score_val >= 6:
            sc_color = "#EAB308"; sc_grade = "B"; sc_label = "DECENT"
        elif score_val >= 4:
            sc_color = "#FF8C00"; sc_grade = "C"; sc_label = "WEAK"
        else:
            sc_color = "#EF4444"; sc_grade = "D"; sc_label = "REJECTED"

        circumference_br = round(2 * 3.14159 * 54, 1)
        dash_br = round(score_val / 10 * circumference_br, 1)

        # ── Hero Score Card ──────────────────────────────────────────────────
        _render_hero_score_card(
            header_icon="😤", header_text="BRUTAL RECRUITER VERDICT",
            header_color="#FF4B4B",
            bg_gradient="linear-gradient(135deg,#1a0505 0%,#2a0d0d 60%,#1a0505 100%)",
            ring_bg="#2a1a1a",
            sc_color=sc_color, score_val=score_val, out_of="10",
            dash=dash_br, circumference=circumference_br,
            sc_label=sc_label, sc_grade=sc_grade,
            score_type_label="Recruiter Score",
        )

        # ── Gut Reaction ──────────────────────────────────────────────────────
        if gut_text:
            st.markdown(f"""
            <div class="persona-note" style="
                background:linear-gradient(135deg,#1f0707 0%,#2a0d0d 100%);
                border:1px solid #FF4B4B33;
                border-radius:14px;
                padding:20px 22px 18px 22px;
                margin:0 0 18px 0;
                position:relative;
                overflow:hidden;
            ">
                <div style="position:absolute;top:-10px;left:14px;font-size:5rem;color:#FF4B4B18;font-family:Georgia,serif;line-height:1;user-select:none;">"</div>
                <div class="persona-note-label" style="font-size:0.68rem;color:#FF4B4B;letter-spacing:3px;font-weight:800;margin-bottom:10px;text-transform:uppercase;">⚡ Gut Reaction</div>
                <div class="persona-note-text" style="font-size:1.05rem;color:#F3E7D1;line-height:1.75;font-style:italic;position:relative;z-index:1;">{gut_text}</div>
            </div>
            """, unsafe_allow_html=True)

        def render_br_section(title, icon, color, bg, start_idx, end_idx):
            if start_idx is None:
                return
            section_lines = lines[start_idx + 1: end_idx] if end_idx else lines[start_idx + 1:]
            bullets = [_clean(re.sub(r'^[✅🚩📝]\s*', '', l.strip()))
                       for l in section_lines if l.strip() and not re.fullmatch(r'[-_*\s]{2,}', l.strip())]
            bullets = [b for b in bullets if b]
            if not bullets:
                return
            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="rsh" style="margin:12px 0 6px 0;font-size:1.05rem;font-weight:800;color:#ffffff;
                        display:flex;align-items:center;gap:8px;letter-spacing:0.5px;">
                <span>{icon}</span> {title}
                <div style="height:1px;flex:1;background:linear-gradient(90deg,{color},transparent);opacity:0.5;margin-left:6px;"></div>
            </div>
            """, unsafe_allow_html=True)
            for b in bullets:
                st.markdown(f"""
                <div style="display:flex;align-items:flex-start;gap:10px;background:{bg};border-radius:8px;
                            padding:10px 14px;margin-bottom:8px;border-left:3px solid {color};">
                    <span style="color:{color};font-size:1rem;flex-shrink:0;margin-top:1px;">›</span>
                    <span style="color:#E5E7EB;font-size:0.92rem;line-height:1.55;">{b}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("<div style='height:1px;background:#2a1a1a;margin:10px 0 6px 0;'></div>", unsafe_allow_html=True)

        render_br_section("What Caught My Eye", "✅", "#22C55E", "#0d2a1a", eye_idx, flags_idx)
        render_br_section("Red Flags", "🚩", "#EF4444", "#2a0d0d", flags_idx, rewrite_idx)
        render_br_section("If I Were Rewriting This", "📝", "#FF8C00", "#2a1f18", rewrite_idx, verdict_idx)

        # Extract text for card — needed before rendering blocks
        br_verdict_text = ""
        br_roast_text = ""

        # ── Verdict ──────────────────────────────────────────────────────────
        if verdict_idx is not None:
            verdict_end = linkedin_idx if linkedin_idx else len(lines)
            verdict_lines = [l.strip() for l in lines[verdict_idx:verdict_end] if l.strip()]
            br_verdict_text = _clean(verdict_lines[0]) if verdict_lines else ""
            extra_lines = [_clean(l) for l in (verdict_lines[1:] if len(verdict_lines) > 1 else [])]
            low_v = br_verdict_text.lower()
            if "hire" in low_v and "maybe" not in low_v and "pass" not in low_v:
                v_color = "#22C55E"; v_icon = "✅"
            elif "maybe" in low_v:
                v_color = "#EAB308"; v_icon = "🤔"
            else:
                v_color = "#EF4444"; v_icon = "❌"
            # Convert hex verdict color to rgb for rgba() — avoids 8-digit hex browser quirks
            _vr = int(v_color[1:3], 16)
            _vg = int(v_color[3:5], 16)
            _vb = int(v_color[5:7], 16)

            # ── Header (separate call — avoids Markdown parser eating nested divs) ──
            st.markdown(
                f'<div class="final-verdict-header" style="margin:24px 0 10px 0;display:flex;align-items:center;gap:10px;">'
                f'<span style="font-size:1.05rem;font-weight:900;color:{v_color};letter-spacing:1px;white-space:nowrap;text-transform:uppercase;">⚖️ Final Verdict</span>'
                f'<div style="height:2px;flex:1;background:linear-gradient(90deg,rgba({_vr},{_vg},{_vb},0.7),transparent);border-radius:2px;"></div>'
                f'</div>',
                unsafe_allow_html=True,
            )

            # ── Box (separate call) ───────────────────────────────────────────────
            _sep = (
                f'<div style="height:1px;background:rgba({_vr},{_vg},{_vb},0.25);margin:12px 0 8px 0;"></div>'
                if extra_lines else ""
            )
            _extras = "".join(
                f'<div class="fv-extra-line" style="font-size:0.88rem;line-height:1.65;margin-top:4px;">{l}</div>'
                for l in extra_lines
            )
            st.markdown(
                f'<div class="final-verdict-card" style="'
                f'background:rgba({_vr},{_vg},{_vb},0.09);'
                f'border:2px solid rgba({_vr},{_vg},{_vb},0.65);'
                f'border-radius:14px;padding:22px 26px;margin:0 0 20px 0;">'
                f'<div style="font-size:1.5rem;font-weight:900;color:{v_color};'
                f'font-family:\'Arial Black\',Impact,\'Helvetica Neue\',sans-serif;line-height:1.4;">'
                f'{v_icon}&nbsp;&nbsp;{br_verdict_text}'
                f'</div>'
                f'{_sep}{_extras}'
                f'</div>',
                unsafe_allow_html=True,
            )

        # ── LinkedIn Roast ────────────────────────────────────────────────────
        if linkedin_idx is not None:
            roast_lines = [l.strip() for l in lines[linkedin_idx:] if l.strip()]
            br_roast_text = _clean(" ".join(roast_lines))
            st.markdown(f"""
            <div class="persona-note" style="background:linear-gradient(90deg,#2a0d2a,#1a0505);border:1.5px solid #A855F755;
                        border-radius:12px;padding:16px 20px;margin:12px 0 18px 0;">
                <div class="persona-note-label" style="font-size:0.72rem;color:#A855F7;letter-spacing:2px;font-weight:800;margin-bottom:8px;">🔥 LINKEDIN ROAST</div>
                <div class="persona-note-text" style="font-size:1rem;color:#E9D5FF;font-style:italic;line-height:1.6;">{br_roast_text}</div>
            </div>
            """, unsafe_allow_html=True)

        st.session_state["last_roast"] = roast_result
        share_text = f"I just got brutally roasted by the Brutal Recruiter 😤\nRecruiter Score: {score_val}/10 — {sc_label}\nWould you survive the roast? 🔥\n#ResumeRoaster #BrutalRecruiter #CareerTips #AI"
        _render_br_linkedin_card(score_val, sc_label, sc_grade, sc_color, br_verdict_text, br_roast_text,
                                 copy_text=share_text, roast_result_full=roast_result)

    elif sel.get("name", "").lower() == "career coach":
        import re

        lines = roast_result.split('\n')

        def find_section_cc(header):
            for i, l in enumerate(lines):
                if header.upper() in l.upper():
                    return i
            return None

        def _clean_cc(text: str) -> str:
            import html as _html
            text = text.strip()
            text = re.sub(r'^#{1,6}\s*', '', text)
            text = re.sub(r'\*\*', '', text)
            text = re.sub(r'\*(?!\s)', '', text)
            text = re.sub(r'`[^`]*`', '', text)          # strip inline code spans
            text = re.sub(r'^[-–—•🌟🎯🚀💪]\s*', '', text)
            text = _html.escape(text.strip())             # escape <, >, & so they never break HTML
            return text

        # Score
        score_val = None
        if score_breakdown:
            score_val = score_breakdown[0].get("score", 7)
        else:
            m = re.search(r'Resume\s+Strength\s*:\s*(\d+)\s*/\s*10', roast_result, re.IGNORECASE)
            if m:
                score_val = int(m.group(1))
        if score_val is None:
            score_val = 7

        if score_val >= 8:
            sc_color = "#22C55E"; sc_grade = "A"; sc_label = "STRONG"
        elif score_val >= 6:
            sc_color = "#3B82F6"; sc_grade = "B"; sc_label = "SOLID"
        elif score_val >= 4:
            sc_color = "#EAB308"; sc_grade = "C"; sc_label = "DEVELOPING"
        else:
            sc_color = "#EF4444"; sc_grade = "D"; sc_label = "NEEDS WORK"

        circumference_cc = round(2 * 3.14159 * 54, 1)
        dash_cc = round(score_val / 10 * circumference_cc, 1)

        # Section indices
        score_idx    = find_section_cc("RESUME STRENGTH")
        strengths_idx = find_section_cc("YOUR STRENGTHS")
        growth_idx   = find_section_cc("GROWTH AREAS")
        action_idx   = find_section_cc("ACTION PLAN")

        # Opening observation = lines before score line
        opening_lines = lines[:score_idx] if score_idx else []
        opening_text = _clean_cc(" ".join(l.strip() for l in opening_lines if l.strip()))
        opening_text = re.sub(r'^[A-Z][A-Z\s]{2,30}\s+', '', opening_text).strip()

        # Closer = lines after ACTION PLAN section
        closer_text = ""
        if action_idx is not None:
            action_lines = lines[action_idx + 1:]
            # find the last non-bullet paragraph as the closer
            closer_candidates = [
                _clean_cc(l) for l in reversed(action_lines)
                if l.strip() and not l.strip().startswith(('-', '•', '*'))
                and not re.fullmatch(r'[-_*\s]{2,}', l.strip())
            ]
            closer_text = closer_candidates[0] if closer_candidates else ""

        # ── Hero Score Card ──────────────────────────────────────────────────
        _render_hero_score_card(
            header_icon="🧑‍🏫", header_text="CAREER COACH ASSESSMENT",
            header_color="#22C55E",
            bg_gradient="linear-gradient(135deg,#051a0a 0%,#0d2a14 60%,#051a0a 100%)",
            ring_bg="#0d2a14",
            sc_color=sc_color, score_val=score_val, out_of="10",
            dash=dash_cc, circumference=circumference_cc,
            sc_label=sc_label, sc_grade=sc_grade,
            score_type_label="Resume Strength",
        )

        # ── Opening Observation ───────────────────────────────────────────────
        if opening_text:
            st.markdown(f"""
            <div class="persona-note" style="
                background:linear-gradient(135deg,#071a0a 0%,#0f2a14 100%);
                border:1px solid #22C55E33;
                border-radius:14px;
                padding:20px 22px 18px 22px;
                margin:0 0 18px 0;
                position:relative;overflow:hidden;
            ">
                <div style="position:absolute;top:-10px;left:14px;font-size:5rem;color:#22C55E14;font-family:Georgia,serif;line-height:1;user-select:none;">"</div>
                <div class="persona-note-label" style="font-size:0.68rem;color:#22C55E;letter-spacing:3px;font-weight:800;margin-bottom:10px;text-transform:uppercase;">💬 First Impression</div>
                <div class="persona-note-text" style="font-size:1.05rem;color:#D1FAE5;line-height:1.75;font-style:italic;position:relative;z-index:1;">{opening_text}</div>
            </div>
            """, unsafe_allow_html=True)

        def render_cc_section(title, icon, color, bg, start_idx, end_idx):
            if start_idx is None:
                return
            section_lines = lines[start_idx + 1: end_idx] if end_idx else lines[start_idx + 1:]

            # Parse into items: each item is a (bullet_text, [example_lines]) tuple
            items = []
            current_bullet = None
            current_examples = []
            in_example = False

            for raw in section_lines:
                line = raw.strip()
                if not line or re.fullmatch(r'[-_*\s]{2,}', line):
                    continue
                cleaned = _clean_cc(line)
                if not cleaned:
                    continue

                # Detect start of an Example block
                if re.match(r'^Example\s*:', cleaned, re.IGNORECASE):
                    in_example = True
                    example_content = re.sub(r'^Example\s*:\s*', '', cleaned, flags=re.IGNORECASE).strip()
                    if example_content:
                        current_examples.append(example_content)
                    continue

                # If line looks like a continuation of an example (indented or part of a list under Example)
                if in_example and (raw.startswith('  ') or raw.startswith('\t') or line.startswith('-')):
                    current_examples.append(cleaned)
                    continue

                # New bullet point — save the previous one
                in_example = False
                if current_bullet:
                    items.append((current_bullet, current_examples))
                current_bullet = cleaned
                current_examples = []

            if current_bullet:
                items.append((current_bullet, current_examples))

            if not items:
                return

            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="rsh" style="margin:12px 0 6px 0;font-size:1.05rem;font-weight:800;color:#ffffff;
                        display:flex;align-items:center;gap:8px;letter-spacing:0.5px;">
                <span>{icon}</span> {title}
                <div style="height:1px;flex:1;background:linear-gradient(90deg,{color},transparent);opacity:0.5;margin-left:6px;"></div>
            </div>
            """, unsafe_allow_html=True)

            for bullet, examples in items:
                example_html = ""
                if examples:
                    example_lines_html = "".join(
                        f'<div style="margin-top:4px;color:#9CA3AF;font-size:0.82rem;line-height:1.5;">{e}</div>'
                        for e in examples if e
                    )
                    example_html = f"""
                    <div style="margin-top:8px;background:#0a0a0a;border-radius:6px;padding:8px 12px;
                                border-left:2px solid {color}55;">
                        <div style="font-size:0.68rem;color:{color};letter-spacing:1.5px;font-weight:700;margin-bottom:4px;">EXAMPLE</div>
                        {example_lines_html}
                    </div>"""

                st.markdown(f"""
                <div style="background:{bg};border-radius:8px;padding:10px 14px;margin-bottom:10px;border-left:3px solid {color};">
                    <div style="display:flex;align-items:flex-start;gap:10px;">
                        <span style="color:{color};font-size:1rem;flex-shrink:0;margin-top:1px;">›</span>
                        <span style="color:#E5E7EB;font-size:0.92rem;line-height:1.55;">{bullet}</span>
                    </div>
                    {example_html}
                </div>
                """, unsafe_allow_html=True)
            st.markdown("<div style='height:1px;background:#0d2a14;margin:10px 0 6px 0;'></div>", unsafe_allow_html=True)

        render_cc_section("Your Strengths",  "🌟", "#22C55E", "#071a0a", strengths_idx, growth_idx)
        render_cc_section("Growth Areas",    "🎯", "#3B82F6", "#071522", growth_idx,    action_idx)
        render_cc_section("Action Plan",     "🚀", "#F59E0B", "#1a1507", action_idx,    None)

        # ── Motivational Closer ───────────────────────────────────────────────
        if closer_text:
            st.markdown(f"""
            <div class="persona-note" style="background:linear-gradient(90deg,#22C55E22,#071a0a);border:1.5px solid #22C55E44;
                        border-radius:12px;padding:16px 20px;margin:12px 0 18px 0;">
                <div class="persona-note-label" style="font-size:0.72rem;color:#22C55E;letter-spacing:2px;font-weight:800;margin-bottom:6px;">✨ COACH'S NOTE</div>
                <div class="persona-note-text" style="font-size:1rem;color:#D1FAE5;font-style:italic;line-height:1.6;">{closer_text}</div>
            </div>
            """, unsafe_allow_html=True)

        def _extract_cc_bullets(start, end, limit=2):
            if start is None:
                return []
            section = lines[start + 1: end] if end else lines[start + 1:]
            result = []
            for raw in section:
                line = raw.strip()
                if not line or re.fullmatch(r'[-_*\s]{2,}', line):
                    continue
                if re.match(r'^Example\s*:', line, re.IGNORECASE):
                    continue
                cleaned = _clean_cc(line)
                if cleaned and len(cleaned) > 8:
                    result.append(cleaned)
                if len(result) >= limit:
                    break
            return result

        cc_strengths = _extract_cc_bullets(strengths_idx, growth_idx)
        cc_growth    = _extract_cc_bullets(growth_idx, action_idx)
        cc_actions   = _extract_cc_bullets(action_idx, None)

        st.session_state["last_roast"] = roast_result
        share_text = (
            f"Just had my resume reviewed by an AI Career Coach 🧑‍🏫\n"
            f"Resume Strength: {score_val}/10 — {sc_label}\n"
            f"Getting actionable feedback to level up my job search! 🚀\n"
            f"#ResumeRipper #CareerCoach #JobSearch #CareerTips #AI"
        )
        _render_cc_linkedin_card(score_val, sc_label, sc_grade, sc_color,
                                 closer_text or opening_text,
                                 strengths=cc_strengths, growth=cc_growth, actions=cc_actions,
                                 copy_text=share_text, roast_result_full=roast_result)

    elif sel.get("name", "").lower() == "internet troll":
        import re

        lines = roast_result.split('\n')

        def find_section_it(header):
            for i, l in enumerate(lines):
                if header.upper() in l.upper():
                    return i
            return None

        def _clean_it(text: str) -> str:
            import html as _html
            text = text.strip()
            text = re.sub(r'^#{1,6}\s*', '', text)
            text = re.sub(r'\*\*', '', text)
            text = re.sub(r'\*(?!\s)', '', text)
            text = re.sub(r'`[^`]*`', '', text)
            text = re.sub(r'^[-–—•😂🤡🧠💀]\s*', '', text)
            text = re.sub(r'^[A-Z][a-z]+[,!]\s*', '', text)
            return _html.escape(text.strip())

        # Score
        score_val = None
        if score_breakdown:
            score_val = score_breakdown[0].get("score", 5)
        else:
            m = re.search(r'Cringe Score[:\s]*(\d+)\s*/\s*10', roast_result, re.IGNORECASE)
            if m:
                score_val = int(m.group(1))
        if score_val is None:
            score_val = 5

        # Cringe score: 10 = max cringe (inverted palette)
        if score_val >= 8:
            sc_color = "#EF4444"; sc_grade = "F"; sc_label = "MAX CRINGE"
        elif score_val >= 6:
            sc_color = "#F59E0B"; sc_grade = "D"; sc_label = "PRETTY BAD"
        elif score_val >= 4:
            sc_color = "#A855F7"; sc_grade = "C"; sc_label = "MID"
        else:
            sc_color = "#22C55E"; sc_grade = "A"; sc_label = "TOLERABLE"

        circumference_it = round(2 * 3.14159 * 54, 1)
        dash_it = round(score_val / 10 * circumference_it, 1)

        # Section indices
        score_idx   = find_section_it("CRINGE SCORE")
        memes_idx   = find_section_it("MEMES WRITE THEMSELVES")
        plots_idx   = find_section_it("PLOT HOLES")
        serious_idx = find_section_it("OK BUT SERIOUSLY")

        # Opening one-liner = lines before score
        opening_lines = lines[:score_idx] if score_idx else []
        opening_text = _clean_it(" ".join(l.strip() for l in opening_lines if l.strip()))

        # Closing roast = non-bullet lines after the last section
        closing_text = ""
        last_idx = serious_idx
        if last_idx is not None:
            for l in reversed(lines[last_idx + 1:]):
                stripped = l.strip()
                if stripped and not stripped.startswith(('-', '•', '*')) \
                        and not re.fullmatch(r'[-_*\s]{2,}', stripped):
                    closing_text = _clean_it(stripped)
                    break

        # ── Hero Score Card ──────────────────────────────────────────────────
        _render_hero_score_card(
            header_icon="🧌", header_text="INTERNET TROLL VERDICT",
            header_color="#A855F7",
            bg_gradient="linear-gradient(135deg,#0d0514 0%,#1a0a2e 60%,#0d0514 100%)",
            ring_bg="#1a0a2e",
            sc_color=sc_color, score_val=score_val, out_of="10",
            dash=dash_it, circumference=circumference_it,
            sc_label=sc_label, sc_grade=sc_grade,
            score_type_label="Cringe Score",
        )

        # ── Opening One-Liner ────────────────────────────────────────────────
        if opening_text:
            st.markdown(f"""
            <div class="persona-note" style="
                background:linear-gradient(135deg,#0d0514 0%,#1a0a2e 100%);
                border:1px solid #A855F733;
                border-radius:14px;
                padding:20px 22px 18px 22px;
                margin:0 0 18px 0;
                position:relative;overflow:hidden;
            ">
                <div style="position:absolute;top:-10px;left:14px;font-size:5rem;color:#A855F714;font-family:Georgia,serif;line-height:1;user-select:none;">"</div>
                <div class="persona-note-label" style="font-size:0.68rem;color:#A855F7;letter-spacing:3px;font-weight:800;margin-bottom:10px;">💀 OPENING ROAST</div>
                <div class="persona-note-text" style="font-size:1.05rem;color:#E9D5FF;line-height:1.75;font-style:italic;position:relative;z-index:1;">{opening_text}</div>
            </div>
            """, unsafe_allow_html=True)

        def render_it_section(title, icon, color, bg, start_idx, end_idx):
            if start_idx is None:
                return
            section_lines = lines[start_idx + 1: end_idx] if end_idx else lines[start_idx + 1:]
            bullets = [_clean_it(re.sub(r'^[😂🤡🧠💀]\s*', '', l.strip()))
                       for l in section_lines
                       if l.strip() and not re.fullmatch(r'[-_*\s]{2,}', l.strip())]
            bullets = [b for b in bullets if b and len(b) > 4]
            if not bullets:
                return
            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="rsh" style="margin:12px 0 6px 0;font-size:1.05rem;font-weight:800;color:#ffffff;
                        display:flex;align-items:center;gap:8px;letter-spacing:0.5px;">
                <span>{icon}</span> {title}
                <div style="height:1px;flex:1;background:linear-gradient(90deg,{color},transparent);opacity:0.5;margin-left:6px;"></div>
            </div>
            """, unsafe_allow_html=True)
            for b in bullets:
                st.markdown(f"""
                <div style="display:flex;align-items:flex-start;gap:10px;background:{bg};border-radius:8px;
                            padding:10px 14px;margin-bottom:8px;border-left:3px solid {color};">
                    <span style="color:{color};font-size:1rem;flex-shrink:0;margin-top:1px;">›</span>
                    <span style="color:#E5E7EB;font-size:0.92rem;line-height:1.55;">{b}</span>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("<div style='height:1px;background:#1a0a2e;margin:10px 0 6px 0;'></div>", unsafe_allow_html=True)

        render_it_section("The Memes Write Themselves", "😂", "#EF4444", "#2a0d0d",   memes_idx,  plots_idx)
        render_it_section("Plot Holes in Your Career Story", "🤡", "#F59E0B", "#1a1507", plots_idx,  serious_idx)
        render_it_section("OK But Seriously",             "🧠", "#A855F7", "#1a0a2e",  serious_idx, None)

        # ── Closing Viral Roast ──────────────────────────────────────────────
        if closing_text:
            st.markdown(f"""
            <div class="persona-note" style="background:linear-gradient(90deg,#A855F722,#0d0514);border:1.5px solid #A855F755;
                        border-radius:12px;padding:16px 20px;margin:12px 0 18px 0;">
                <div class="persona-note-label" style="font-size:0.72rem;color:#A855F7;letter-spacing:2px;font-weight:800;margin-bottom:6px;">🔥 CLOSING ROAST</div>
                <div class="persona-note-text" style="font-size:1rem;color:#E9D5FF;font-style:italic;line-height:1.6;">{closing_text}</div>
            </div>
            """, unsafe_allow_html=True)

        st.session_state["last_roast"] = roast_result
        share_text = (
            f"Just got my resume roasted by the Internet Troll 🧌\n"
            f"Cringe Score: {score_val}/10 — {sc_label}\n"
            f"Would your resume survive? 😂\n"
            f"#ResumeRipper #InternetTroll #JobSearch #CareerTips #AI"
        )
        _render_it_linkedin_card(score_val, sc_label, sc_grade, sc_color, closing_text or opening_text,
                                 copy_text=share_text, roast_result_full=roast_result)

    elif sel.get("name", "").lower() == "top hiring manager":
        import re

        lines = roast_result.split('\n')

        def find_section_hm(header):
            header_up = header.upper()
            for i, l in enumerate(lines):
                # Strip markdown/punctuation and check if this line IS the header
                stripped = re.sub(r'[^A-Z0-9\s]', '', l.upper()).strip()
                if stripped == header_up or stripped.startswith(header_up + ' ') or stripped.endswith(' ' + header_up):
                    # Guard: header lines are short (not body text containing the word)
                    if len(stripped.split()) <= len(header_up.split()) + 3:
                        return i
            return None

        def _clean_hm(text: str) -> str:
            import html as _html
            text = text.strip()
            text = re.sub(r'^#{1,6}\s*', '', text)
            text = re.sub(r'\*\*', '', text)
            text = re.sub(r'\*(?!\s)', '', text)
            text = re.sub(r'`[^`]*`', '', text)
            text = re.sub(r'^[-–—•✔️⚠️📈💼👀🏆]\s*', '', text)
            text = re.sub(r'(?i)^verdict\s*:\s*', '', text)
            text = re.sub(r'^[A-Z][a-z]+[,!]\s*', '', text)
            return _html.escape(text.strip())

        # Score
        score_val = None
        if score_breakdown:
            score_val = score_breakdown[0].get("score", 6)
        else:
            m = re.search(r'Shortlist Score[:\s]*(\d+)\s*/\s*10', roast_result, re.IGNORECASE)
            if m:
                score_val = int(m.group(1))
        if score_val is None:
            score_val = 6

        if score_val >= 8:
            sc_color = "#22C55E"; sc_grade = "A"; sc_label = "STRONG HIRE"
        elif score_val >= 6:
            sc_color = "#F59E0B"; sc_grade = "B"; sc_label = "CONSIDER"
        elif score_val >= 4:
            sc_color = "#FF8C00"; sc_grade = "C"; sc_label = "BORDERLINE"
        else:
            sc_color = "#EF4444"; sc_grade = "D"; sc_label = "PASS"

        circumference_hm = round(2 * 3.14159 * 54, 1)
        dash_hm = round(score_val / 10 * circumference_hm, 1)

        # Section indices
        score_idx    = find_section_hm("SHORTLIST SCORE")
        works_idx    = find_section_hm("WHAT WORKS")
        concerns_idx = find_section_hm("CONCERNS")
        improve_idx  = find_section_hm("IMPROVEMENT PLAN")
        signal_idx   = find_section_hm("HIRING SIGNAL")
        verdict_idx  = find_section_hm("VERDICT")
        interview_idx = find_section_hm("WOULD I INTERVIEW")

        # Instant impression = lines before score
        impression_lines = lines[:score_idx] if score_idx else []
        impression_text = _clean_hm(" ".join(l.strip() for l in impression_lines if l.strip()))
        impression_text = re.sub(r'(?i)^instant\s+impression\s*:\s*', '', impression_text).strip()

        # Verdict text
        hm_verdict_text = ""
        if verdict_idx is not None:
            end = interview_idx if interview_idx else len(lines)
            for l in lines[verdict_idx: end]:
                c = _clean_hm(l)
                if c and len(c) > 3:
                    hm_verdict_text = c
                    break

        # Interview decision
        hm_interview_text = ""
        if interview_idx is not None:
            for l in lines[interview_idx:]:
                c = _clean_hm(l)
                if c and len(c) > 2:
                    hm_interview_text = c
                    break

        # Hiring signal text
        hm_signal_text = ""
        if signal_idx is not None:
            sig_end = verdict_idx if verdict_idx else len(lines)
            sig_lines = [_clean_hm(l) for l in lines[signal_idx + 1: sig_end]
                         if l.strip() and not re.fullmatch(r'[-_*\s]{2,}', l.strip())]
            hm_signal_text = " ".join(b for b in sig_lines if b)

        # Verdict color
        low_v = hm_verdict_text.lower()
        if "shortlist" in low_v:
            v_color = "#22C55E"; v_icon = "✅ SHORTLIST"
        elif "consider" in low_v:
            v_color = "#F59E0B"; v_icon = "🤔 CONSIDER"
        else:
            v_color = "#EF4444"; v_icon = "❌ PASS"

        # Interview decision color
        low_i = hm_interview_text.lower()
        if "→ yes" in low_i or low_i.endswith("yes"):
            i_color = "#22C55E"
        elif "maybe" in low_i or "possibly" in low_i:
            i_color = "#F59E0B"
        else:
            i_color = "#EF4444"

        # ── Hero Score Card ──────────────────────────────────────────────────
        _render_hero_score_card(
            header_icon="🏆", header_text="TOP HIRING MANAGER ASSESSMENT",
            header_color="#F59E0B",
            bg_gradient="linear-gradient(135deg,#0f0c00 0%,#1f1800 60%,#0f0c00 100%)",
            ring_bg="#1f1800",
            sc_color=sc_color, score_val=score_val, out_of="10",
            dash=dash_hm, circumference=circumference_hm,
            sc_label=sc_label, sc_grade=sc_grade,
            score_type_label="Shortlist Score",
        )

        # ── Instant Impression ───────────────────────────────────────────────
        if impression_text:
            st.markdown(
                '<div style="background:linear-gradient(135deg,#0f0c00 0%,#1f1800 100%);'
                'border:1px solid rgba(245,158,11,0.2);border-radius:14px;'
                'padding:20px 22px 18px 22px;margin:0 0 18px 0;position:relative;overflow:hidden;">'
                '<div style="position:absolute;top:-10px;left:14px;font-size:5rem;color:rgba(245,158,11,0.08);font-family:Georgia,serif;line-height:1;user-select:none;">"</div>'
                '<div style="font-size:0.68rem;color:#F59E0B;letter-spacing:3px;font-weight:800;margin-bottom:10px;">⚡ INSTANT IMPRESSION</div>'
                f'<div style="font-size:1.05rem;color:#FEF3C7;line-height:1.75;font-style:italic;position:relative;z-index:1;">{impression_text}</div>'
                '</div>',
                unsafe_allow_html=True,
            )

        def render_hm_section(title, icon, color, bg, start_idx, end_idx):
            if start_idx is None:
                return
            section_lines = lines[start_idx + 1: end_idx] if end_idx else lines[start_idx + 1:]
            bullets = [_clean_hm(l) for l in section_lines
                       if l.strip() and not re.fullmatch(r'[-_*\s]{2,}', l.strip())]
            bullets = [b for b in bullets if b and len(b) > 4]
            if not bullets:
                return
            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
            st.markdown(
                f'<div class="rsh" style="margin:12px 0 6px 0;font-size:1.05rem;font-weight:800;color:#ffffff;'
                f'display:flex;align-items:center;gap:8px;letter-spacing:0.5px;">'
                f'<span>{icon}</span> {title}'
                f'<div style="height:1px;flex:1;background:linear-gradient(90deg,{color},transparent);opacity:0.5;margin-left:6px;"></div>'
                f'</div>',
                unsafe_allow_html=True,
            )
            for b in bullets:
                st.markdown(
                    f'<div style="display:flex;align-items:flex-start;gap:10px;background:{bg};border-radius:8px;'
                    f'padding:10px 14px;margin-bottom:8px;border-left:3px solid {color};">'
                    f'<span style="color:{color};font-size:1rem;flex-shrink:0;margin-top:1px;">›</span>'
                    f'<span style="color:#E5E7EB;font-size:0.92rem;line-height:1.55;">{b}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            st.markdown("<div style='height:1px;background:#1f1800;margin:10px 0 6px 0;'></div>", unsafe_allow_html=True)

        render_hm_section("What Works",       "✔️", "#22C55E", "#071a0a", works_idx,    concerns_idx)
        render_hm_section("Concerns",         "⚠️", "#EF4444", "#2a0d0d", concerns_idx, improve_idx)
        render_hm_section("Improvement Plan", "📈", "#F59E0B", "#1a1507", improve_idx,  signal_idx)

        # ── Hiring Signal ────────────────────────────────────────────────────
        if hm_signal_text:
            st.markdown(
                '<div class="persona-note" style="background:linear-gradient(90deg,rgba(245,158,11,0.09),#1a1200);'
                'border:1.5px solid rgba(245,158,11,0.4);border-radius:14px;padding:18px 20px;margin:14px 0;">'
                '<div class="persona-note-label" style="font-size:0.72rem;color:#F59E0B;letter-spacing:2px;font-weight:800;margin-bottom:8px;">💼 HIRING SIGNAL</div>'
                f'<div class="persona-note-text" style="font-size:0.95rem;color:#FEF3C7;line-height:1.7;">{hm_signal_text}</div>'
                '</div>',
                unsafe_allow_html=True,
            )

        # ── Verdict + Interview Decision ─────────────────────────────────────
        if hm_verdict_text or hm_interview_text:
            # Convert hex colors to rgb for rgba() usage
            def _hex_rgb(h):
                h = h.lstrip('#')
                return int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
            vr, vg, vb = _hex_rgb(v_color)
            ir, ig, ib = _hex_rgb(i_color)

            verdict_card = ""
            if hm_verdict_text:
                verdict_card = (
                    f'<div class="persona-note hm-decision-card" style="flex:1;min-width:180px;'
                    f'background:linear-gradient(135deg,rgba({vr},{vg},{vb},0.09),#0f0c00);'
                    f'border:2px solid rgba({vr},{vg},{vb},0.4);border-radius:14px;padding:16px 18px;">'
                    f'<div class="persona-note-label" style="font-size:0.65rem;color:{v_color};letter-spacing:2px;font-weight:800;margin-bottom:8px;">⚖️ VERDICT</div>'
                    f'<div style="font-size:1.2rem;font-weight:900;color:{v_color};margin-bottom:6px;">{v_icon}</div>'
                    f'<div class="persona-note-subtext" style="font-size:0.82rem;color:#9CA3AF;line-height:1.4;">{hm_verdict_text}</div>'
                    f'</div>'
                )
            interview_card = ""
            if hm_interview_text:
                interview_card = (
                    f'<div class="persona-note hm-decision-card" style="flex:1;min-width:180px;'
                    f'background:linear-gradient(135deg,rgba({ir},{ig},{ib},0.09),#0f0c00);'
                    f'border:2px solid rgba({ir},{ig},{ib},0.4);border-radius:14px;padding:16px 18px;">'
                    f'<div class="persona-note-label" style="font-size:0.65rem;color:{i_color};letter-spacing:2px;font-weight:800;margin-bottom:8px;">👀 WOULD I INTERVIEW?</div>'
                    f'<div class="persona-note-text" style="font-size:1rem;font-weight:800;color:{i_color};line-height:1.4;">{hm_interview_text}</div>'
                    f'</div>'
                )
            st.markdown(
                f'<div style="display:flex;gap:14px;margin:14px 0 20px 0;flex-wrap:wrap;">'
                f'{verdict_card}'
                f'{interview_card}'
                f'</div>',
                unsafe_allow_html=True,
            )

        st.session_state["last_roast"] = roast_result
        share_text = (
            f"Just had my resume assessed by a Top Hiring Manager on Resume Ripper AI 🏆\n"
            f"Shortlist Score: {score_val}/10 — {sc_label}\n"
            f"Would your resume make the shortlist? 👀\n"
            f"#ResumeRipper #HiringManager #JobSearch #CareerTips #AI"
        )
        _render_hm_linkedin_card(score_val, sc_label, sc_grade, sc_color,
                                  hm_verdict_text, hm_interview_text,
                                  copy_text=share_text, roast_result_full=roast_result)

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
    st.markdown('</div>', unsafe_allow_html=True)


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