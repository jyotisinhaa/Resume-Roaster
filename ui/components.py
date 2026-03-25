"""
Reusable UI components — hero, steps, upload JS, personality cards, footer.
"""

import streamlit as st
import streamlit.components.v1 as components

# ═══════════════════════════════════════════════════════════════════════════════
#  UPLOAD ZONE JS — hides default Streamlit text, injects supported-formats line
# ═══════════════════════════════════════════════════════════════════════════════
def render_upload_zone_js():
    """Inject JS to clean up the Streamlit file uploader and add supported formats text."""
    import streamlit.components.v1 as components
    components.html("""
    <script>
    function cleanUploader() {
        const main = window.parent.document;
        main.querySelectorAll('[data-testid=\"stFileUploaderDropzone\"]').forEach(dz => {
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
                info.innerHTML = '📎 Supported formats: <b style=\"color:#FF8C00;\">PDF</b>, <b style=\"color:#FF8C00;\">DOCX</b>, <b style=\"color:#FF8C00;\">TXT</b> · Max 10 MB';
                info.style.cssText = 'text-align:center;color:#8a7e74;font-size:0.8rem;margin-bottom:0.8rem;order:-1;';
                const btn = dz.querySelector('button');
                if (btn && btn.parentElement) {
                    btn.parentElement.insertBefore(info, btn);
                } else {
                    dz.prepend(info);
                }
            }
        });
        main.querySelectorAll('[data-testid=\"stFileUploader\"] small').forEach(s => {
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
    # Add global animation CSS for animated bars and shimmer effect (only once, at top of app)
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
    @keyframes shimmerFlow {
        0% { background-position-x: -160px; }
        100% { background-position-x: 100%; }
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
    # ...existing code...
    # Bonus: show 'Analyzing resume signals...' above bars
    st.markdown("""
    <div style="font-size:0.75rem;color:#9CA3AF;margin-bottom:6px;">
    Analyzing resume signals...
    </div>
    """, unsafe_allow_html=True)

    if sel.get("name", "").lower() == "ats scanner" and score_breakdown:
        # Parse the roast_result into sections
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

        # Score Breakdown (dashboard style, animated, only once)
        # NOTE: Move the animation CSS to your main app file for global effect!
        st.markdown(f"""
        <div style="
            display:flex;
            align-items:center;
            justify-content:space-between;
            margin:18px 0 10px 0;
        ">
            <div style="
                font-size:1.15rem;
                font-weight:800;
                letter-spacing:0.5px;
                color:#ffffff;
            ">
                📊 Score Breakdown
            </div>
            <div style="
                height:1px;
                flex:1;
                margin-left:12px;
                background:linear-gradient(90deg,#FF8C00,transparent);
                opacity:0.6;
            "></div>
        </div>
        """, unsafe_allow_html=True)

        # Animated bars (staggered, correct color logic, only once)
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
            # Unified color/label logic
            if score >= 85:
                color = "#22C55E"   # green
                strength = "EXCELLENT"
            elif score >= 70:
                color = "#3B82F6"   # blue
                strength = "STRONG"
            elif score >= 50:
                color = "#EAB308"   # yellow
                strength = "AVERAGE"
            else:
                color = "#EF4444"   # red
                strength = "WEAK"
            st.markdown(f"""
            <div style="display:flex;align-items:center;margin-bottom:8px;gap:10px;">
                <div style="width:150px;font-size:0.9rem;color:#cfcfcf;">{label}</div>
                <div style="width:60px;font-weight:600;">{score}</div>
                <div style="flex:1;height:6px;background:#1e1e1e;border-radius:6px;overflow:hidden;">
                    <div class="animated-bar shimmer" style="
                        --target-width:{score}%;
                        --bar-color:{color};
                        width:0%;
                        animation-delay:{i * 0.15}s;
                        background:linear-gradient(90deg,{color},{color}AA);"
                    ></div>
                </div>
                <div style="width:80px;text-align:right;font-size:0.8rem;font-weight:700;color:{color};">{strength}</div>
            </div>
            """, unsafe_allow_html=True)


        # Section rendering helper (premium style)
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
            # Add subtle spacing before each section
            st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
            # Standardized section header
            st.markdown(f"""
            <div style="
                margin:16px 0 6px 0;
                font-size:1rem;
                font-weight:700;
                color:#ffffff;
                display:flex;
                align-items:center;
                gap:8px;
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
            else:
                st.markdown(f"<div style='border-radius:8px;padding:4px 0 2px 0;margin-bottom:2px;'>", unsafe_allow_html=True)
                for l in section_lines:
                    line = l.strip()
                    # Skip markdown horizontal rules and empty lines
                    if not line:
                        continue
                    if re.fullmatch(r'[-_*\\s]{3,}', line):
                        continue
                    st.markdown(l)
                st.markdown("</div>", unsafe_allow_html=True)
            # Add a subtle divider after each section except the last
            if next_idx is not None:
                st.markdown("<div style='height:1px;background:#222;margin:10px 0 6px 0;opacity:0.5;'></div>", unsafe_allow_html=True)

        # Render sections as cards/boxes
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

        # Final Recommendation as a banner
        if final_idx is not None:
            rec_lines = lines[final_idx+1:]

            # Only allow valid recommendation words
            VALID_VERDICTS = {"optimize", "reformat", "critical rewrite"}
            verdict = None
            clean_content = []
            for l in rec_lines:
                stripped = l.strip()
                if not stripped:
                    continue
                lower = stripped.lower()
                # Capture verdict
                if lower in VALID_VERDICTS and verdict is None:
                    verdict = stripped.upper()
                    continue
                # Remove prompt leakage
                if stripped.startswith("Tone:") or "analytical" in lower:
                    continue
                clean_content.append(stripped)
            display_verdict = verdict or "OPTIMIZE"
            st.markdown(f"""
            <div style="background:linear-gradient(90deg,#FF8C00,#FF6B35);color:#fff;padding:18px 22px;border-radius:12px;font-size:1.18rem;font-weight:900;margin:18px 0 0 0;box-shadow:0 2px 12px #FF8C0033;">
                <div style="font-size:1.3em;font-weight:900;margin-bottom:10px;">⭐ FINAL RECOMMENDATION</div>
                <div style="font-size:1.6rem;font-weight:900;letter-spacing:2px;margin-bottom:12px;">{display_verdict}</div>
                {''.join(f'<div style="margin-top:6px;">{line}</div>' for line in clean_content)}
            </div>
            """, unsafe_allow_html=True)

        # Footer
        st.markdown(f"""
        <div style="text-align:right;font-size:12px;color:#777;margin-top:18px;">
            {sel["icon"]} Generated by {sel["name"]} · {elapsed:.1f}s
        </div>
        """, unsafe_allow_html=True)

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
        '🔥 <b>Roasted with love by Resume Ripper</b><br>'
        'Your resume is processed in memory and never stored. We only roast, never save. 🤝'
        '</div>',
        unsafe_allow_html=True,
    )
