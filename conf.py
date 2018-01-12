# -*- coding: utf-8 -*-

import os
import sys
import glob
import time

try:
    exec(open('BioNetGen/docs/conf.py').read())
except IOError:
    exec(open('../../manual/conf.py').read())

sys.path.append(os.path.abspath('manual/sphinxext'))
              #'sphinxcontrib.googleanalytics',
              #'ipython_console_highlighting',
              #'ipython_directive']
extensions = [ 'sphinx.ext.todo',
               'sphinx.ext.autodoc',
               'sphinx.ext.doctest',
               'sphinx.ext.coverage',
               'sphinx.ext.extlinks',
               'sphinx.ext.graphviz',
               'sphinx.ext.ifconfig',
               'sphinx.ext.viewcode',
               #'sphinx.ext.intersphinx',
               'sphinx.ext.inheritance_diagram',
               'matplotlib.sphinxext.mathmpl',
               'matplotlib.sphinxext.only_directives',
	       'IPython.sphinxext.ipython_directive' ,
	       'IPython.sphinxext.ipython_console_highlighting',
	       'googleanalytics']

exclude_patterns.append('RuleBender')
exclude_patterns.append('tutorials/template')
exclude_patterns.extend(glob.glob('tutorials/**/acknowledgments.rst'))
templates_path = ['_template']
source_suffix = '.rst'
master_doc = 'contents'

# not needed when building the full website
intersphinx_mapping.pop('prodywebsite')

project = u'RuleBender'
copyright = u'2007-2018, University of Pittsburgh'

# -- Options for HTML output ---------------------------------------------------

html_favicon = 'manual/_static/favicon.ico'

html_additional_pages = {
    'index': 'rulebender.html',
    'downloads/index': 'downloads.html',
    'tutorials/index': 'tutorials.html',
    'statistics/index': 'statistics.html',
}

html_sidebars = {
    '**': ['toolbox.html', 'releasenotes.html', 'howtocite.html'],
}

# -- Options for LaTeX output --------------------------------------------------
#latex_logo = 'manual/_static/logo.png'

lines = (line for line in rst_epilog.split('\n')
         if ('_Tut' not in line and '_NMW' not in line))
rst_epilog = '\n'.join(lines)

