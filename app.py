"""
<APP_TITLE>
<APP_TAGLINE>
"""
import base64
from pathlib import Path

import streamlit as st

# `set_page_config` must be the first Streamlit call in the script.
st.set_page_config(
    page_title="<APP_TITLE>",
    page_icon="favicon.png",
    layout="wide",
)

# ── Home-link logo ────────────────────────────────────────────────────────────
# A 32x32 Griffith PSE blackletter G that links back to https://griffith-pse.com
# (same tab — the user is leaving the demo). Image is embedded from the local
# favicon.png as a base64 data URL — no network call when the app loads, so
# cloners running locally don't ping griffith-pse.com on every render.
#
# Two layout patterns — pick one and uncomment the matching CSS + markdown
# call below. The sidebarless variant is the default; the sidebar variant
# requires extra CSS to hide Streamlit's sticky header chrome (which
# otherwise pushes the logo 2-3rem below the top of the sidebar).
st.markdown("""
<style>
/* === Sidebarless apps (default — Knapsack, Diet pattern) ================ */
.home-logo-corner {
    position: fixed;
    top: 0.5rem;
    left: 0.75rem;
    z-index: 999999;
}
.home-logo-corner img {
    width: 32px;
    height: 32px;
    border-radius: 4px;
    display: block;
}

/* === Sidebar apps (quad-tank pattern) =================================== */
/* If you're using `st.sidebar.markdown(_HOME_LOGO_HTML, ...)` below
   instead of the main-page variant, comment out the `.home-logo-corner`
   block above and uncomment everything below. The in-flow positioning
   makes the logo sit naturally at the top of the sidebar; hiding
   `stSidebarHeader` removes Streamlit's sticky chrome (the «« collapse
   button) so nothing pushes the logo down. Trade-off: users can't
   collapse the sidebar via «« — fine if the sidebar IS the control panel. */
/*
.home-logo-corner {
    display: block;
    margin: 0 0 0.75rem;
}
.home-logo-corner img {
    width: 32px;
    height: 32px;
    border-radius: 4px;
    display: block;
}
[data-testid="stSidebarHeader"] {
    display: none !important;
}
[data-testid="stSidebarUserContent"] {
    padding-top: 0.5rem !important;
}
*/
</style>
""", unsafe_allow_html=True)

_FAVICON_DATA_URL = "data:image/png;base64," + base64.b64encode(
    (Path(__file__).parent / "favicon.png").read_bytes()
).decode()

_HOME_LOGO_HTML = (
    '<a class="home-logo-corner" href="https://griffith-pse.com" target="_self">'
    f'<img src="{_FAVICON_DATA_URL}" '
        'alt="Griffith PSE — home" />'
    '</a>'
)

# Sidebarless apps (default — Knapsack, Diet pattern):
st.markdown(_HOME_LOGO_HTML, unsafe_allow_html=True)

# Sidebar apps (quad-tank pattern) — comment out the line above, uncomment
# the line below, and swap the CSS blocks above accordingly:
# st.sidebar.markdown(_HOME_LOGO_HTML, unsafe_allow_html=True)

# ── Title block ───────────────────────────────────────────────────────────────
st.title("<APP_TITLE>")
st.caption("<APP_TAGLINE>")

# ── Sidebar inputs ────────────────────────────────────────────────────────────
# Sliders, file uploaders, model parameters, dropdowns, etc. Use a sidebar
# when the workflow is set-then-solve (configure inputs, hit a button, view
# results). Skip the sidebar when interaction is continuous and inputs are
# few — put controls inline in the main area instead.
#
# Example:
#   st.sidebar.header("Inputs")
#   x = st.sidebar.slider("x", 0.0, 10.0, 5.0)

# ── Main computation ──────────────────────────────────────────────────────────
# Build your model, call your library, run the analysis.
# Cache expensive work with @st.cache_data (for serializable returns) or
# @st.cache_resource (for solver objects, ML models, etc.).
#
# Example:
#   @st.cache_data
#   def fit_model(data):
#       return some_model(data).fit()

# ── Display ───────────────────────────────────────────────────────────────────
# Plotly / Altair charts, data tables, text output, math via st.latex, etc.

st.write("Hello, world. Replace this with your app.")
