import os
import sys
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin

# from unittest.mock import MagicMock
# BasePlugin = MagicMock()
# config_options = MagicMock()

import itertools
from bs4 import BeautifulSoup


def wrap(soup, heading_name):
    """wrap all headings and next siblings into sections"""
    # thanks https://stackoverflow.com/a/32290036/7924473

    headings = soup.find_all(heading_name)
    for element in headings:
        els = [i for i in itertools.takewhile(
                  lambda x: x.name not in [element.name, 'script'],
                  element.next_siblings)]

        # all classes start with md- to avoid conflicts with other plugins
        # md : makedocs
        tag_toggle = soup.new_tag('input type="checkbox"', class_='md-nav__toggle md-toggle')
        # tag_toggle_icon = soup.new_tag('span', class_='md-nav__icon md-icon')
        tag_div = soup.new_tag('tr', class_='md-heading__content')

        # element.insert(0, tag_toggle)
        # element.insert_before(tag_toggle)
        element.append(tag_toggle)
        element.insert_after(tag_div)

        for tag in els:
            tag_div.append(tag)

    return soup


def make_headings_collapsible(html_string: str) -> str:
    soup = BeautifulSoup(html_string, 'html.parser')
    # skip h1 since h1 in markdown is h2 in html
    # when updating this, also update in javascript
    for heading_name in [ 'h2', 'h3', 'h4', 'h5', 'h6']:
        soup = wrap(soup, heading_name)
    return str(soup)


class Collapsibleheadings(BasePlugin):

    config_scheme = (
        ('param', config_options.Type(str, default='')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0

    # def on_serve(self, server):
    #     return server
    #
    # def on_pre_build(self, config):
    #     return
    #
    # def on_files(self, files, config):
    #     return files
    #
    # def on_nav(self, nav, config, files):
    #     return nav
    #
    # def on_env(self, env, config, files):
    #     return env
    #
    # def on_config(self, config):
    #     return config
    #
    # def on_post_build(self, config):
    #     return
    #
    # def on_pre_template(self, template, template_name, config):
    #     return template
    #
    # def on_template_context(self, context, template_name, config):
    #     return context
    #
    # def on_post_template(self, output_content, template_name, config):
    #     return output_content
    #
    # def on_pre_page(self, page, config, files):
    #     return page
    #
    # def on_page_read_source(self, page, config):
    #     return ""
    #
    # def on_page_markdown(self, markdown, page, config, files):
    #     return markdown

    def on_page_content(self, html, page, config, files):
        """The page_content event is called after the Markdown text is rendered to HTML
        (but before being passed to a template) and can be used to alter the HTML body of the page."""
        return make_headings_collapsible(html)

    # def on_page_context(self, context, page, config, nav):
    #     return context
    #
    # def on_post_page(self, output_content, page, config):
    #     return output_content

