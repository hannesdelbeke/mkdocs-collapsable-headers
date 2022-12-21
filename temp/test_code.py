from mkdocs_collapsible_headings_plugin.plugin import make_headings_collapsible

# try online https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_heading
s = """
<article>
  <heading>
    <h1>HEAD1</h1>
        <p>Posted by John Doe</p>
        <p>Some additional information here</p>
        <h2>HEAD2</h2>
            <p>Posted by John Doe</p>
            <p>Some additional information here</p>
    <h1>HEAD1B</h1>
  </heading>
  <p>Lorem Ipsum dolor set amet....</p>
</article>
"""

r = make_headings_collapsible(s)
print(r)
