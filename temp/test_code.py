from mkdocs_collapsible_headings_plugin.plugin import make_headings_collapsible

from bs4 import BeautifulSoup
# try online https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_heading
s = """
<article>
  <heading>
    <h2>HEAD1</h2>
        <p>Posted by John Doe</p>
        <p>Some additional information here</p>
        <h3>HEAD2</h3>
            <p>Posted by John Doe</p>
            <p>Some additional information here</p>
    <h2>HEAD1B</h2>
  </heading>
  <p>Lorem Ipsum dolor set amet....</p>
</article>
"""

r = make_headings_collapsible(s)
r = str(BeautifulSoup(r, 'html.parser').prettify())
print(r)
