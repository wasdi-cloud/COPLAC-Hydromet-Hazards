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
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Hydromet Hazards'
copyright = 'CopernicusLAC - 2025'
author = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinxemoji.sphinxemoji']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_theme_options = {
    "sidebar_hide_name": False,  # keep section title visible
    "navigation_with_keys": True,  # optional keyboard nav
    "light_css_variables": {
        "color-brand-primary": "#0f294f",
        "color-brand-content": "#0f294f",
        "color-foreground-primary" : "#000",
    },
     "dark_css_variables": {
        "color-brand-primary": "#50f3fd",
        "color-brand-content": "#0c64d0",
        "color-foreground-primary" : "#FFFFFF",
    }
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_favicon = 'favicon.ico'

html_logo = '_static/coplac-3.png'

## Remove source button 
html_copy_source = False
html_show_sourcelink = False


import os
import sys
#print(sys.path)

rst_prolog = """
.. role:: raw-html(raw)
   :format: html
"""