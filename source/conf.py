
import sphinx_rtd_theme

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosectionlabel',
]

html_theme = "sphinx_rtd_theme"

project = 'DarrowTools'
copyright = '2022, Blake Darrow'
author = 'Blake Darrow'

templates_path = ['_templates']

exclude_patterns = []

html_theme = 'sphinx_rtd_theme'

html_show_sourcelink = False

language = None
html_static_path = ['_static']

htmlhelp_basename = 'DarrowTools'