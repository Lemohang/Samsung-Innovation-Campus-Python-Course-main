def is_matching_html(html):
    import re
    stack = []
    
    # Regex to find tags like <html>, </html>
    tags = re.findall(r'</?[^>]+>', html)

    for tag in tags:
        if not tag.startswith('</'):
            # It's an opening tag
            tag_name = tag[1:-1].strip()
            stack.append(tag_name)
        else:
            # It's a closing tag
            tag_name = tag[2:-1].strip()
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()
    
    return len(stack) == 0


# Example HTML content from the screenshot
html_code = """
<html>
  <body>
    <h1>Hello, World!</h1>
    <p>We are learning the art of coding with Python programming language.
    Here we are learning ... </p>
    <ul>
      <li> Data Structures, </li>
      <li> Algorithms, </li>
      <li> and Computational Thinking, eventually. </li>
    </ul>
  </body>
</html>
"""

# Run the check
if is_matching_html(html_code):
    print("✅ HTML tags are properly matched.")
else:
    print("❌ HTML tags are not properly matched.")
