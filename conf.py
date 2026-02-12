project = 'Quicken Help Guide'
author = 'Independent Documentation'
release = '1.0'

extensions = []

templates_path = []

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]

html_theme = 'alabaster'

html_static_path = ['_static']

# IMPORTANT: serve existing HTML files
html_extra_path = ['.']

master_doc = 'index'

html_show_sphinx = False
html_show_copyright = True

html_theme_options = {
    'description': 'Independent step-by-step Quicken help documentation',
    'show_powered_by': False,
    'show_related': True,
}
