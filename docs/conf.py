# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tmp'
copyright = '2023, syl'
author = 'syl'
release = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark',
'sphinx_markdown_tables',
'sphinx.ext.mathjax',
'sphinx_math_dollar',
# 'sphinx-mathjax-offline'
]


# Optional: Customize MathJax options
# mathjax_config = {
#     'TeX': {'extensions': ['AMSmath.js', 'AMSsymbols.js', 'noErrors.js', 'noUndefined.js']}
# }

mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3.0.0/es5/tex-svg.js'

mathjax3_config = {
    'TeX': {
    'extensions': ['AMSmath.js', 'AMSsymbols.js', 'noErrors.js', 'noUndefined.js']
    },

  'tex': {
    'inlineMath': [['$','$'], ['\\(','\\)']],
    'processEscapes': True
  }
}


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []
