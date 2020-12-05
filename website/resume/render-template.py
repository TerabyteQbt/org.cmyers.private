#!/usr/bin/env python3

import sys
import jinja2


vardict = {
        'short':
            {
                'SHORT_RESUME': True,
            },
        'long':
            {
                'LONG_RESUME': True,
            },
        }

vartype = sys.argv[1]
filepath = sys.argv[2]
revision = 'unknown-revision'
if len(sys.argv) > 2:
    revision = sys.argv[3]

if not vardict[vartype]:
    print("Unknown type {}".format(vartype))
    sys.exit(1)


# slurp file
content = None
with open(filepath, 'r') as fd:
    content = fd.read()

# set revision
vardict[vartype]['REVISION'] = revision

template = jinja2.Template(content)
print(template.render(**vardict[vartype]))
