#!/usr/bin/env python
# mypy: ignore-errors
# spapros documentation build configuration file
#
# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys
from pathlib import Path

from nbconvert.preprocessors import TagRemovePreprocessor
from sphinx.ext.napoleon.docstring import GoogleDocstring

HERE = Path(__file__).parent
#sys.path[:0] = [str(HERE.parent), str(HERE / "_extensions")]
sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("../.."))
sys.path.append(os.path.abspath("../spapros"))
#sys.path.append(os.path.abspath("../spapros/evaluation"))
#sys.path.append(os.path.abspath("../spapros/selection"))
#sys.path.append(os.path.abspath("./_tutorials"))


# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

# Add 'sphinx_automodapi.automodapi' if you want to build modules
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx_click",
    "sphinx_rtd_dark_mode",
    "nbsphinx",
    "sphinx_gallery.load_style",
    "nbsphinx_link",
    # "jupyter_sphinx.embed_widgets",
    #*[p.stem for p in (HERE / "_extensions").glob("*.py")],
]


# nbsphinx setup (for tutorial gallery)

# this doesn't work since we only use extension "sphinx_gallery.load_style" and not 'sphinx_gallery.gen_gallery'
# --> instead we add a custom css files
#sphinx_gallery_conf = { 
#    "thumbnail_size": (250, 250),
#}

nbsphinx_timeout = -1

# html_show_sourcelink = True
# html_sourcelink_suffix = ""
# suppress_warnings = [
#     'nbsphinx',
# ]
# nbsphinx_execute = "never"
TagRemovePreprocessor.remove_input_tags = {"remove_input"}

autosummary_generate = True
autodoc_member_order = "groupwise"
autodoc_typehints = "signature"
autodoc_docstring_signature = True
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
napoleon_use_rtype = True
napoleon_use_param = True
napoleon_custom_sections = [("Params", "Parameters")]  # ('Returns', 'params_style')]
# napoleon_use_ivar = True # Displays class attributes like class parameters. Even better solved with extra code below.

todo_include_todos = False

default_dark_mode = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = [".rst"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "spapros"
copyright = "2021, Lukas Heumos"
author = "Lukas Heumos"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = "0.1.1"
# The full version, including alpha/beta/rc tags.
release = "0.1.1"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "plot_examples", "readme.rst"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#

# colors from spapros logo:
# brigth_blue = '#8dcaff'
# purple = '#a55fc1'
# darker_blue = '#1761a0'
# darker_purple = '##6360b2'
# green = '#4cc61e'
# brighter_green = '#99c712'
# html_theme_options = {
#     "style_nav_header_background": "black",
# }

home_page_in_toc = True
html_logo = "_static/logo.png"
html_favicon = "_static/logo.png"
html_title = "spapros docs"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "spaprosdoc"


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ("letterpaper" or "a4paper").
    #
    # "papersize": "letterpaper",
    # The font size ("10pt", "11pt" or "12pt").
    #
    # "pointsize": "10pt",
    # Additional stuff for the LaTeX preamble.
    #
    # "preamble": "",
    # Latex figure (float) alignment
    #
    # "figure_align": "htbp",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "spapros.tex",
        "spapros Documentation",
        "Lukas Heumos",
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "spapros",
        "spapros Documentation",
        [author],
        1,
    )
]

autodoc_typehints = "description"


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "spapros",
        "spapros Documentation",
        author,
        "spapros",
        "One line description of project.",
        "Miscellaneous",
    ),
]

html_css_files = [
    "custom_cookietemple.css",
]

suppress_warnings = [
    "nbsphinx",
]


#def setup(app):
#    app.add_css_file("custom_cookietemple.css")


# -- Extensions to the  Napoleon GoogleDocstring class ---------------------
# setting napoleon_use_ivar = True (see above) will create the correct formatting
# for class attributes. However the attribute section has then the title "Variables".
# The following lines fix that issue and additionally distinguish class vs instance attrs.
# see https://michaelgoerz.net/notes/extending-sphinx-napoleon-docstring-sections.html
# and https://github.com/sphinx-doc/sphinx/issues/2115

# first, we define new methods for any new sections and add them to the class


def parse_keys_section(self, section):
    return self._format_fields("Keys", self._consume_fields())


GoogleDocstring._parse_keys_section = parse_keys_section


def parse_attributes_section(self, section):
    return self._format_fields("Attributes", self._consume_fields())


GoogleDocstring._parse_attributes_section = parse_attributes_section


def parse_class_attributes_section(self, section):
    return self._format_fields("Class Attributes", self._consume_fields())


GoogleDocstring._parse_class_attributes_section = parse_class_attributes_section

# we now patch the parse method to guarantee that the the above methods are
# assigned to the _section dict


def patched_parse(self):
    self._sections["keys"] = self._parse_keys_section
    self._sections["class attributes"] = self._parse_class_attributes_section
    self._unpatched_parse()


GoogleDocstring._unpatched_parse = GoogleDocstring._parse
GoogleDocstring._parse = patched_parse

# --------------------------------------------------------------------------
