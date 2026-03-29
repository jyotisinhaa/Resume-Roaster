"""
Theme toggle — injects the sun/moon button and handles light/dark mode switching.
"""


def get_theme_toggle_js() -> str:
    """Return the JS for the theme toggle button."""
    return """
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
        const btn = main.querySelector('.theme-toggle');
        if (btn) btn.textContent = theme === 'light' ? '🌙' : '☀️';
        localStorage.setItem(STORAGE_KEY, theme);
        // Direct style fix: file-info-name is invisible in light mode because
        // Streamlit's textColor CSS variable (#e0d5cc) overrides class-based rules.
        main.querySelectorAll('.file-info-name').forEach(function(el) {
            el.style.color = theme === 'light' ? '#111111' : '#e0d5cc';
        });
        // Fix fv-extra-line (Final Verdict supporting text) in light mode.
        main.querySelectorAll('.fv-extra-line').forEach(function(el) {
            el.style.color = theme === 'light' ? '#3d2a1a' : '#cccccc';
        });
        // Fix uploaded filename text inside the file uploader widget in light mode.
        var uploaderSelectors = [
            '[data-testid="stFileUploaderFileName"]',
            '[data-testid="stFileUploader"] section span',
            '[data-testid="stFileUploader"] section div span'
        ];
        uploaderSelectors.forEach(function(sel) {
            main.querySelectorAll(sel).forEach(function(el) {
                el.style.color = theme === 'light' ? '#111111' : '';
            });
        });
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
        const app = getApp();
        if (app) app.appendChild(btn);
    }

    function init() {
        injectToggle();
        const saved = localStorage.getItem(STORAGE_KEY) || 'dark';
        applyTheme(saved);
    }

    init();
    setInterval(init, 500);

    // Bold the roast button every 200ms — React wipes inline styles on re-render.
    // Apply to the button AND all children: Streamlit sometimes wraps text in <p>.
    function boldRoastBtn() {
        main.querySelectorAll('div[data-testid="stButton"] button').forEach(function(btn) {
            if (btn.textContent.indexOf('ROAST') === -1) return;
            [btn].concat(Array.prototype.slice.call(btn.querySelectorAll('*'))).forEach(function(el) {
                el.style.setProperty('font-weight', '900', 'important');
                el.style.setProperty('font-family', "'Arial Black', Impact, 'Helvetica Neue', sans-serif", 'important');
            });
        });
    }
    boldRoastBtn();
    setInterval(boldRoastBtn, 200);
})();
</script>
"""
