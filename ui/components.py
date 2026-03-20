"""
Reusable UI components — hero, steps, upload JS, personality cards, footer.
"""

import streamlit as st
import streamlit.components.v1 as components


# ═══════════════════════════════════════════════════════════════════════════════
#  HERO SECTION
# ═══════════════════════════════════════════════════════════════════════════════
def render_hero():
    """Render the hero banner."""
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
    st.markdown('<div class="section-label" style="font-size:2.2rem;font-weight:900;letter-spacing:2.5px;margin-bottom:2.2rem;margin-top:2.7rem;">How It Works</div>', unsafe_allow_html=True)
    st.markdown("""
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
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes pop {
        0% { transform: scale(1); }
        100% { transform: scale(1.18); }
    }
    .step-card:hover {
        transform: translateY(-10px) scale(1.04);
        box-shadow: 0 12px 40px #FF8C0033, 0 2px 0 #FF8C00 inset;
        border-color: #FF8C00;
    }
    </style>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  UPLOAD ZONE JS — hides default Streamlit text, injects supported-formats line
# ═══════════════════════════════════════════════════════════════════════════════
def render_upload_zone_js():
    """Inject JS to clean up the Streamlit file uploader and add supported formats text."""
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

    # Initialize personality selection
    if "selected_personality" not in st.session_state:
        st.session_state["selected_personality"] = "brutal_recruiter"

    persona_keys = list(PERSONALITIES.keys())
    selected_key = st.session_state["selected_personality"]

    # Build card grid HTML
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

                    // Visual feedback: re-query ALL cards fresh to deselect everything
                    main.querySelectorAll('.persona-card[data-persona]').forEach(c => c.classList.remove('selected'));
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

        // Enforce single-selection: only one card should be .selected
        function enforceSingleSelect() {{
            const allCards = main.querySelectorAll('.persona-card[data-persona]');
            const selected = main.querySelectorAll('.persona-card.selected');
            if (selected.length > 1) {{
                // Find which radio is actually checked
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

    # Show selected personality banner
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
#  ROAST RESULTS
# ═══════════════════════════════════════════════════════════════════════════════
def render_roast_results(roast_result: str, score_breakdown: dict, sel: dict, elapsed: float):
    """Render the roast results card + share/download section."""

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

    # Split roast_result into lines for custom rendering
    if sel.get("name", "").lower() == "ats scanner" and score_breakdown:
        lines = roast_result.split('\n')
        # Find SCAN COMPLETE and ATS COMPATIBILITY SCORE lines
        scan_idx = next((i for i, l in enumerate(lines) if l.strip().upper().startswith("SCAN COMPLETE")), None)
        score_idx = next((i for i, l in enumerate(lines) if l.strip().upper().startswith("ATS COMPATIBILITY SCORE")), None)
        # Print up to SCORE BREAKDOWN (exclusive)
        breakdown_idx = next((i for i, l in enumerate(lines) if l.strip().upper().startswith("SCORE BREAKDOWN")), None)
        # Render up to and including SCORE BREAKDOWN header
        if scan_idx is not None and score_idx is not None and breakdown_idx is not None:
            for i in range(scan_idx, breakdown_idx+1):
                st.markdown(lines[i])
            # Skip all horizontal rules and empty lines after SCORE BREAKDOWN
            next_content_idx = breakdown_idx + 1
            import re as _re
            while next_content_idx < len(lines):
                line = lines[next_content_idx].strip().lower()
                # Skip empty lines, markdown HR, <hr> tags, or empty <div> tags
                if (
                    line == ''
                    or all(c in '-_—―' for c in line)
                    or line == '<hr>'
                    or line == '<hr/>'
                    or line == '<hr />'
                    or _re.match(r'<div[^>]*>[\s\u200b\u200c\u200d\uFEFF]*</div>', line)
                ):
                    next_content_idx += 1
                else:
                    break
            # Now render colored bars
            st.markdown('<div class="ats-score-breakdown">', unsafe_allow_html=True)
            desired_order = [
                "Keyword Coverage",
                "Impact Metrics",
                "Action Verbs",
                "ATS Formatting",
                "Skills Coverage",
            ]
            label_to_item = {item.get("label", ""): item for item in score_breakdown}
            for label in desired_order:
                item = label_to_item.get(label)
                if not item:
                    continue
                score = item.get("score", 0)
                if score >= 85:
                    color = "#22C55E"
                    strength = "STRONG"
                elif score >= 70:
                    color = "#F59E0B"
                    strength = "GOOD"
                else:
                    color = "#EF4444"
                    strength = "NEEDS WORK"
                bar_blocks = int(score / 10)
                bar = "█" * bar_blocks + "▓" * (1 if score % 10 >= 5 else 0) + "░" * (10 - bar_blocks - (1 if score % 10 >= 5 else 0))
                st.markdown(
                    f'<div style="display:flex;align-items:center;margin-bottom:0.3rem;gap:0.7em;">'
                    f'<span style="min-width:140px;">{label}:</span>'
                    f'<span style="min-width:80px;">{score} / 100</span>'
                    f'<span style="font-family:monospace;font-size:1.1em;color:{color};">[{bar}]</span>'
                    f'<span style="font-weight:700;color:{color};margin-left:0.7em;">{strength}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            st.markdown('</div>', unsafe_allow_html=True)
            # Skip original score breakdown lines (e.g., "- Keyword Coverage: 90 / 100")
            metric_labels = [
                "Keyword Coverage:",
                "Impact Metrics:",
                "Action Verbs:",
                "ATS Formatting:",
                "Skills Coverage:",
            ]
            i = next_content_idx
            while i < len(lines):
                line = lines[i].strip()
                # Skip lines that are just the metric labels (with or without dash/bullet)
                if any(line.lstrip('-•* ').startswith(label) for label in metric_labels):
                    i += 1
                    continue
                st.markdown(lines[i])
                i += 1
        else:
            # Fallback: just print everything as before
            st.markdown(roast_result)
    else:
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
def render_footer():
    """Render the app footer."""
    st.markdown(
        '<div class="footer">'
        '🔥 <b>Roasted with love by Resume Ripper AI</b><br>'
        'Your resume is processed in memory and never stored. We only roast, never save. 🤝'
        '</div>',
        unsafe_allow_html=True,
    )
