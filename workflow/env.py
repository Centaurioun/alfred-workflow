#!/usr/bin/env python
# encoding: utf-8
#
# Copyright © 2015 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2015-01-24
#

"""
"""

from __future__ import print_function, unicode_literals, absolute_import

import sys

from workflow.base import get_logger
from workflow._env import WorkflowEnvironment

log = get_logger(__name__)

# Some questionable magic ...
# Replace this module in the namespace with a WorkflowEnvironment instance
# From outside, the methods and attributes of WorkflowEnvironment are
# the attributes and functions of this module
sys.modules[__name__] = WorkflowEnvironment()
