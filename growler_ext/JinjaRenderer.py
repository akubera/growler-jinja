#
# growler_ext/JinjaRenderer.py
#
"""
Loader script for the JinjaRenderer class.

This script overloads the expected module object with the class JinjaRenderer.
"""

import sys
from growler_jinja.jinja_renderer import JinjaRenderer

sys.modules[__name__] = JinjaRenderer
