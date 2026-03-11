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
})();
</script>
"""
