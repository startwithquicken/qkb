project = 'Quicken Desktop Guide'
author = 'Quicken Desktop Team'
release = '1.0'

extensions = []

# Templates directory (safe to keep empty)
templates_path = ['_templates']

exclude_patterns = [
    '_build',
    '.git',
    '.github',
    '.readthedocs.yaml',
    'Thumbs.db',
    '.DS_Store',
]

# Use Read the Docs theme
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_title = "Quicken Desktop Download | Install, Activate & Update"

html_show_sphinx = False
html_show_copyright = True
