project = 'Quicken Help Guide'
author = 'Independent Documentation'
release = '1.0'

extensions = []

exclude_patterns = [
    '_build',
    '.git',
    '.github',
    '.readthedocs.yaml',
    'Thumbs.db',
    '.DS_Store',
]

html_theme = 'alabaster'

html_static_path = ['_static']

master_doc = 'index'

html_show_sphinx = False
html_show_copyright = True

html_theme_options = {
    'description': 'Independent step-by-step Quicken help documentation',
    'show_powered_by': False,
    'show_related': True,
}
