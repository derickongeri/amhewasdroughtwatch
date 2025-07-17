# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Africa Drought Bulletin'
copyright = '2025, AMHEWAS'
author = 'AMHEWAS'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_css_files = ['custom.css']
html_context = {
   # ...
   "default_mode": "light"
}

html_sidebars = {
    "**": ["search-field.html","sidebar-nav-bs", "page-toc"]
}

html_theme_options = {
"external_links": [
    {
        "url": "https://au.int/en/directorates/sustainable-environment#",
        "name": "Read More",
    },
    # {
    #     "url": "https://numfocus.org/",
    #     "name": "NumFocus",
    # },
    # {
    #     "url": "https://numfocus.org/donate",
    #     "name": "Donate to NumFocus",
    # },
],
"navbar_start": ["navbar-logo"],
"navbar_center": ["navbar-nav"],
"navbar_align": "content",
"navbar_end": ["navbar-icon-links"],
"navbar_persistent": ["search-button"],
"logo": {
    "image_light": "_static/images/logodefault.svg",
    "image_dark": "_static/images/logodefault.svg",
},
"secondary_sidebar_items": [],
"collapse_navigation": True,
}

