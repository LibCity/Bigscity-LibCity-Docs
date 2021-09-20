# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
import sphinx_rtd_theme
from recommonmark.parser import CommonMarkParser
# -- Project information -----------------------------------------------------

project = 'Bigscity-LibCity'
copyright = '2020, aptx1231'
author = 'aptx1231'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'recommonmark',
'sphinx_markdown_tables',
'sphinx_rtd_theme',
'sphinx.ext.autodoc',
'sphinx.ext.todo',
'sphinx.ext.napoleon',
'sphinx.ext.doctest',
'sphinx.ext.autosummary',
'sphinx.ext.githubpages',
'sphinx.ext.mathjax',
'sphinx.ext.intersphinx',
'sphinx.ext.viewcode',
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['.DS_Store']

autodoc_mock_imports = ["torch"]
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

napoleon_include_private_with_doc = True

latex_elements={
    'papersize':'a4paper',
    'pointsize':'12pt','classoptions':',oneside','babel':'',
    'inputenc':'',
    'utf8extra':'',
    'preamble': r"""
    \usepackage{xeCJK}
    \usepackage{indentfirst}
    \setlength{\parindent}{2em}
    \setCJKmainfont{WenQuanYi Micro Hei}
    \setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
    \setCJKfamilyfont{song}{WenQuanYi Micro Hei}
    \setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
    \XeTeXlinebreaklocale "zh"
    \XeTeXlinebreakskip = 0pt plus 1pt
    """
}
