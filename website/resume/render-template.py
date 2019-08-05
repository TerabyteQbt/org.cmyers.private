#!/usr/bin/env python

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

if not vardict[vartype]:
    print "Unknown type {}".format(vartype)
    sys.exit(1)


# slurp file
content = None
with open(filepath, 'r') as fd:
    content = fd.read()

template = jinja2.Template(content)
print template.render(**vardict[vartype])
