
html_title = 'DarrowTools'

html_short_title = "DarrowTools"

html_theme_options = {
    'style_external_links': False,
    'navigation_depth': -1,
    'sticky_navigation' : True,
    'prev_next_buttons_location' : "none",
    }

project = 'DarrowTools'
copyright = '2022, Blake Darrow'
author = 'Blake Darrow'

extensions = [
    'sphinx_rtd_dark_mode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosectionlabel',
]

templates_path = ['_templates']

exclude_patterns = []

html_show_sourcelink = False

language = None

html_link_suffix = ""

html_static_path = [
    '_static',
]

html_js_files = [
    'logo_link.js',
]

html_css_files = [
    'css/custom.css',
]

html_show_sphinx = False

html_theme = 'rtd'

default_dark_mode = True
