#!/usr/bin/env python
#! /usr/bin/env python

import os
import re
import sys

# determine value of n in the current block of ngrams by parsing the filename
input_file = os.environ['map_input_file']
expected_tokens = int(re.findall(r'([\d]+)gram', os.path.basename(input_file))[0])
print input_file
print expected_tokens