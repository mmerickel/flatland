project = u'flatland'
copyright = u'2008-2011, the flatland authors and contributors'

version = '0.0'
release = '0.0.hg-tip'


master_doc = 'index'
add_module_names = False
default_role = 'py:obj'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
]


intersphinx_mapping = {
    'http://docs.python.org/': None,
    'http://discorporate.us/projects/Blinker/docs/tip/': None,
}
