# auto launches on startup before any other modules
# see https://stackoverflow.com/questions/10693706

# create an empty json in this location
import os
import json
data = {}
with open(os.path.join(os.path.dirname(__file__), 'data.json'), 'w') as f:
    json.dump(data, f)
print("TESTSSTS sitecustomize.py")

import mkdocs.plugins
import mkdocs_collapsible_headings
mkdocs.plugins.collapsible_headings = mkdocs_collapsible_headings.plugin.Collapsibleheadings


import site
site.main()