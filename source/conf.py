# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
language = os.getenv("SPHINX_LANGUAGE", "en")

locale_dirs = ['locales/']      # Path to .po translation files
gettext_compact = False         # Optional: cleaner structure for .po files


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Africa Drought Bulletin'
copyright = '2025, AMHEWAS'
author = 'AMHEWAS'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

locale_dirs = ['locales/']      # Path to .po translation files
gettext_compact = False         # Optional: cleaner structure for .po files

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

"switcher": {
    "json_url": [
  { "name": "English", "url": "/en/", "lang": "en" },
  { "name": "Français", "url": "/fr/", "lang": "fr" },
  { "name": "Português", "url": "/pt/", "lang": "pt" },
  { "name": "العربية", "url": "/ar/", "lang": "ar" }
],
    "version_match": language,
},
"translations": {
    "On_this_page": "Quick Navigation",  # Replace this with your desired header
},
"external_links": [
    # {
    #     "url": "https://au.int/en/directorates/sustainable-environment#",
    #     "name": "Read More",
    # },
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
"navbar_align": "right",
"navbar_end": ["language-switcher", "navbar-icon-links"],
"navbar_persistent": ["search-button"],
"logo": {
    "image_light": "_static/images/logo.svg",
    "image_dark": "_static/images/logo.svg",
},
"secondary_sidebar_items": [],
"collapse_navigation": True,
}



