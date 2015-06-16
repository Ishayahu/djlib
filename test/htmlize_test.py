__author__ = 'Ishayahu'

import unittest
from text_utils import htmlize
__version__ = '0.0.1'

class MyTestCase(unittest.TestCase):
    def test_bold (self):
        self.assertEqual( htmlize("*bold*"), "<b>bold</b>")
    def test_italic (self):
        self.assertEqual( htmlize("**bold**"), "<i>bold</i>")
    def test_link_http (self):
        self.assertEqual( htmlize("http://site.com"), '<a href="http://site.com">http://site.com</a>')
    def test_link_https (self):
        self.assertEqual( htmlize("https://site.com"), '<a href="https://site.com">https://site.com</a>')
    def test_basic_1(self):
        self.assertEqual( htmlize("*bold* **italic** http://site.com https://site.com https://site.com/page.php"),
                          u'<b>bold</b> <i>italic</i> <a href="http://site.com">http://site.com</a> <a href="https://site.com">https://site.com</a> <a href="https://site.com/page.php">https://site.com/page.php</a>')
    def test_basic_2(self):
        a=r'*bold* **italic** < http://site.com \\ https://site.com &>\* ' \
    '**sdfadf** *dfs* https://site.com/page.php ' \
    'https://site.com/page.php&got=cot'
        b = r'<b>bold</b> <i>italic</i> &lt <a href="http://site.com">http://site.com</a> \ <a href="https://site.com">https://site.com</a> &amp&gt* <i>sdfadf</i> <b>dfs</b> <a href="https://site.com/page.php">https://site.com/page.php</a> <a href="https://site.com/page.php&got=cot">https://site.com/page.php&got=cot</a>'
        self.assertEqual(htmlize(a),b)
    def test_winpath(self):
        a=r'C:\\Documents and Settings\\mira.MEOC0>dir \\\\docsrv\\secretar-test'
        self.assertEqual(htmlize(a),
                         ur'C:\Documents and Settings\mira.MEOC0&gtdir \\docsrv\secretar-test')
    def test_table(self):
        a="""||h1||h2||
            ||r1||r2||

            neflsflk

            ||h1||h2||h1||h2||
            ||r1||r2||r1||r2||"""

        self.assertEqual(htmlize(a),
                         u'<table border=1><tr><td>h1</td><td>h2</td></tr><tr><td>r1</td><td>r2</td></tr></table>neflsflk<table border=1><tr><td>h1</td><td>h2</td><td>h1</td><td>h2</td></tr><tr><td>r1</td><td>r2</td><td>r1</td><td>r2</td></tr></table>')
    def test_escape(self):
        a=r"""\*bold\* \\backslash\\ {yesterday}"""

        self.assertEqual(htmlize(a),
                         r'*bold* \backslash\ {yesterday}')

if __name__ == '__main__':
    unittest.main()
