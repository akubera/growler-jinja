# -*- coding: utf-8 -*-
"""
growler_jinja/jinja_renderer


Growler middleware for Jinja2 templates

jinja: http://jinja.pocoo.org/
growler: https://github.com/pyGrowler/

"""

import logging
from jinja2 import Environment, FileSystemLoader
from growler.middleware.renderer import RenderEngine

class JinjaRenderer(RenderEngine):
    """
    Renderer middleware for jinja2 templates
    """

    default_file_extensions = [ '.html' ]

    def __init__(self, path):
        super(JinjaRenderer, self).__init__(path)
        self.log = logging.getLogger(__name__)

        # Create the Jinja Environment
        self.env = Environment(loader=FileSystemLoader(path))

    def render_source(self, filename, obj):
        self.log.info('Template %s with %s', filename, obj)
        return self.env.get_template(filename, **obj)

    @staticmethod
    def register_engine():
        import growler.middleware.renderer
        growler.middleware.renderer.render_engine_map['jinja'] = JinjaRenderer
