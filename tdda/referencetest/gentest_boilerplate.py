HEADER = '''# -*- coding: utf-8 -*-

"""
%(SCRIPT)s: Automatically generated test code from tdda gentest.

Generation command:

  %(GEN_COMMAND)s
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import os
import sys
import tempfile

from tdda.referencetest import ReferenceTestCase
from tdda.referencetest.gentest import exec_command

COMMAND = %(COMMAND)s
CWD = os.path.abspath(os.path.dirname(__file__))
REFDIR = os.path.join(CWD, 'ref', %(NAME)s)
%(SET_TMPDIR)s
%(GENERATED_FILES)s


class TestAnalysis(ReferenceTestCase):
    @classmethod
    def setUpClass(cls):
        (cls.output,
         cls.error,
         cls.exc,
         cls.exit_code,
         cls.duration) = exec_command(COMMAND, CWD)
        %(REMOVE_PREVIOUS_OUTPUTS)s

    def test_no_exception(self):
        msg = 'No exception should be generated'
        self.assertEqual((str(self.exc), msg), ('None', msg))

    def test_exit_code(self):
        self.assertEqual(self.exit_code, %(EXIT_CODE)d)
'''


TAIL = '''
if __name__ == '__main__':
    ReferenceTestCase.main()
'''
