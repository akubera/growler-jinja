"""
tests/test_renderer

Test for the growler-jinja mostly copied from
pyGrowler/growler-mako and pyGrowler/growler-jade
"""
import pytest

import growler_jinja
import growler_jinja.jinja_renderer
from growler_jinja.jinja_renderer import JinjaRenderer


@pytest.fixture
def renderer():
    return JinjaRenderer('./tests/templates')


def test_renderer(renderer):
    assert isinstance(renderer, growler_jinja.jinja_renderer.JinjaRenderer)


def test_imports():
    growler_ext = pytest.importorskip('growler.ext')

    assert growler_ext.JinjaRenderer is JinjaRenderer
    assert growler_ext.jinja_renderer is growler_jinja


# def xtest_render_html(renderer, tmpdir):
#     fname = tmpdir + "/file"
#     print(fname)
#     with open(fname, 'w') as f:
#         f.write("""#vid\n  color blue""")
#     m = mock.Mock()
#     renderer.render_source(fname, m)

#     assert None
