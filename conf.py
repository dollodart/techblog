import sys

sys.path.append('.')

extensions = [
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.graphviz',
              ]
source_suffix = '.rst'
master_doc = 'index'
project = 'blog'
authors = 'david ollodart'
html_theme = 'alabaster'
html_static_path = ['_static/', ]
html_css_files = ['css/kbd.css',]
