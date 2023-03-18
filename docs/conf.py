from semicond import __version__

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'semicond'
copyright = '2023, Koen Van Sever'
author = 'Koen Van Sever'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks'
]

# autodoc
autodoc_typehints = 'none'
# autodoc_content = 'init'

# Napoleon
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_preprocess_types = True
napoleon_type_aliases = {
    "DataFrame": "~pandas.DataFrame",
    "Path": "~pathlib.Path",
    "Axes": "~matplotlib.axes.Axes",
    "Figure": "~matplotlib.figure.Figure",
    "heatmap": "~seaborn.heatmap",
    "array": "~numpy.ndarray",
}

# Intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
    'matplotlib': ('https://matplotlib.org', None),
    'seaborn': ('https://seaborn.pydata.org/', None),
    'xarray': ('https://docs.xarray.dev/en/stable/', None),
    'numpy': ('https://numpy.org/doc/stable', None),
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_favicon = '_static/wafer.png'
html_static_path = ['_static']
html_theme_options = {
    "icon_links": [
        {
            "name": "Github",
            "url": "https://github.com/KoenVanSever/semicond/",
            "type": "fontawesome",
            "icon": "fab fa-github-square",
        }
    ],
}
html_context = {
    "default_mode": "dark"
}
