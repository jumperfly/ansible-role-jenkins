#!/usr/bin/env python
import sys
import yaml

if len(sys.argv) == 3:
    meta_file = sys.argv[1]
    out_file = sys.argv[2]
else:
    print("Usage: requirements-gen.py <path to meta/main.yml file> <output file>")
    sys.exit(1)

with open(meta_file, 'r') as stream:
    meta = yaml.load(stream)
if 'dependencies' in meta:
    with open(out_file, 'w') as stream:
        yaml.dump(meta['dependencies'], stream)
