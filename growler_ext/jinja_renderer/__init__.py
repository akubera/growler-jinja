#
# growler_ext/jinja_renderer.py
#
"""
Loader script for the growler_jinja package.
"""

import sys
import growler_jinja

sys.modules[__name__] = growler_jinja
