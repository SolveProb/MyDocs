# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Personal Docs'
copyright = '2023, syl'
author = 'Song Yalong'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark',
'sphinx_markdown_tables',
'sphinx.ext.mathjax',
'sphinx_math_dollar',
'sphinx-mathjax-offline'
]


# mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js'
# mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML'


# Optional: Customize MathJax options

mathjax_config = {
    'tex2jax': {
        'inlineMath': [['$','$'],  ["\\(","\\)"] ],
        'displayMath': [["\\[","\\]"] , ['$$','$$']],
    },
}

mathjax3_config = {
  "tex": {
    "inlineMath": [['$','$'], ['\\(', '\\)']],
    "displayMath": [["\\[", "\\]"], ['$$','$$']],
  }
}


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []
