#!/usr/bin/python3

# This script eases the work necessary to scale a repo
# Replaces YAML value

import sys
from ruamel.yaml import YAML
import pathlib

desired_replicas = sys.argv[1]
print('Setting minReplicas to: ' + desired_replicas)

yaml = YAML()
yaml.preserve_quotes = True

mf = pathlib.Path('helm/prod-ecommerce-values.yaml')
doc = yaml.load(mf)

doc['hpa']['minReplicas'] = int(desired_replicas)

yaml.dump(doc, mf)

print('Success!')
