# import os
# import sys
# from timeit import default_timer as timer
# from datetime import datetime, timedelta
#
# from mkdocs import utils as mkdocs_utils
# from mkdocs.config import config_options, Config
# from mkdocs.plugins import BasePlugin
BasePlugin = object
config_options = object

import itertools
from bs4 import BeautifulSoup

# try online https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_header
s = """
<article>
  <header>
    <h1>HEAD1</h1>
        <p>Posted by John Doe</p>
        <p>Some additional information here</p>
        <h2>HEAD2</h2>
            <p>Posted by John Doe</p>
            <p>Some additional information here</p>
    <h1>HEAD1B</h1>
  </header>
  <p>Lorem Ipsum dolor set amet....</p>
</article>
"""

def wrap(soup, header_name):
    """wrap all headers and next siblings into sections"""
    # thanks https://stackoverflow.com/a/32290036/7924473

    headers = soup.find_all(header_name)
    for element in headers:
        els = [i for i in itertools.takewhile(
                  lambda x: x.name not in [element.name, 'script'],
                  element.next_siblings)]
        new_tag = soup.new_tag('div', class_='collapsible')
        element.insert_after(new_tag)
        for tag in els:
            new_tag.append(tag)

    return soup



def make_headers_collapsable(html_string: str) -> str:
    soup = BeautifulSoup(html_string, 'html.parser')
    for header_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        soup = wrap(soup, header_name)
    return str(soup)


r = make_headers_collapsable(s)
print(r)


class CollapsableHeaders(BasePlugin):

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
        return wrap_text_between_headers_in_collapsible_divs(html)

    # def on_page_context(self, context, page, config, nav):
    #     return context
    #
    # def on_post_page(self, output_content, page, config):
    #     return output_content

