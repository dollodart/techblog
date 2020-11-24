import sys
import sphinx_rtd_theme

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
#html_theme = 'sphinx_rtd_theme'
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
