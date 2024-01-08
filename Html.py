# html - HyperText Markup Language Support
# https://docs.python.org/3/library/html.html

import html

# html.escape() converts &, <, and > to HTML-safe sequences
def escape():
    s = '1 < 2 && 3 > 2'
    result = html.escape(s)
    assert result == '1 &lt; 2 &amp;&amp; 3 &gt; 2'

# html.unescape() converts html codes (ex: &gt;) to their ascii value
def unescape():
    s = '1 < 2 && 3 > 2'
    escaped = html.escape(s)
    result = html.unescape(escaped)
    assert s == result

def main():
    escape()
    unescape()

if __name__ == '__main__':
    main()
    print('Tests passed!')
