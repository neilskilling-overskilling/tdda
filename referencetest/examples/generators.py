# -*- coding: utf-8 -*-
"""
generators.py: Trivial result generation functions for illustrating
               tdda.referencetest

Source repository: http://github.com/tdda/tdda

License: MIT

Copyright (c) Stochastic Solutions Limited 2016
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import math

def generate_string():
    """
    Returns an HTML string that should display identically to the result
    stored in tdda/examples/reference/string_result, but which has
    four (non-semantic) differences:
        - The Copyright line is different
        - The version number line is different
        - It has a newline at the top, unlike the reference file.
        - It is missing a newline at the end of the string, which the
          reference file includes.
    """
    return """<!DOCTYPE html>
<html>
  <head>
    <!--
    Copyright (c) Stochastic Solutions, 2016
    Version 1.0.0
    -->
<meta charset="UTF-8"/>
<style type="text/css">
body {font-family: Palatino, "Palatino Linotype", Times; text-align: center}
h1 {font-size: large; text-align: center;}
div {padding: 12px 0 12px 0;}
</style>
<title>
  Python-Generated HTML Example for writabletestcase.WritableTestCase
</title>
</head>
<body>
  <h1>Python-Generated HTML Example for writabletestcase.WritableTestCase</h1>
  <div>
    This page is generated by Python (as a string).
  </div>
  %s
  <div>
    It's not terribly exciting.
    But it will serve to illustrate writabletestcase.WritableTestCase.
  </div>
</body>
</html>
""" % generate_spiral()


def generate_file(path):
    html = '''<!DOCTYPE html>
<html>
  <head>
    <!--
    Copyright (c) Stochastic Solutions, 2016
    Version 1.0.0
    -->
<meta charset="UTF-8"/>
<style type="text/css">
body {font-family: Palatino, "Palatino Linotype", Times; text-align: center;}
h1 {font-size: large; text-align: center;}
div {padding-top: 12px; padding-bottom: 12px;}
</style>
 <title>
  Python-Genel./rated HTML Example for writabletestcase.WritableTestCase
</title>
</head>
<body>
  <h1>Python-Generated HTML Example for writabletestcase.WritableTestCase</h1>
  <div>
    This page is generated by Python (as a file).
  </div>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="200" height="200">
    <style type="text/css">text { font-family: Helvetica, Verdana, Sans;}</style>

    <!-- TDDA Test Output Version 0.0.1
         Copyright (c) Stochastic Solutions Limited 2016 -->

    <rect x="0" y="0" width="96" height="96" style="fill:#C08080"/>
    <rect x="105" y="0" width="96" height="96" style="fill:#F0C080"/>
    <rect x="0" y="104" width="96" height="96" style="fill:#F0C080"/>
    <rect x="104" y="104" width="96" height="96" style="fill:#C08080"/>
    <text x="50" y="78" font-size="80" text-anchor="middle">T</text>
    <text x="150" y="78" font-size="80" text-anchor="middle">D</text>
    <text x="50" y="178" font-size="80" text-anchor="middle">D</text>
    <text x="150" y="178" font-size="80" text-anchor="middle">A</text>
  </svg>

  <div>
    It will serve to illustrate writabletestcase.WritableTestCase.
  </div>
</body>
</html>
'''
    with open(path, 'w') as f:
        f.write(html)


def generate_spiral():
    return '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100" height="100">
    <g transform="translate(50,50)">
        <path d="M 0 0 %s z" stroke="red" fill="none"/>
    </g>
</svg>''' % ' '.join('%d %d L' % (t / 20 * math.cos(t * 2 * math.pi / 100),
                                  t / 20 * math.sin(t * 2 * math.pi / 100))
                     for t in range(1000))



