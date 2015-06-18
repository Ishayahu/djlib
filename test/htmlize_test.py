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
                         u'<table border=1><tr><td>h1</td><td>h2</td></tr><tr><td>r1</td><td>r2</td><td><p>            neflsflk<p>            </td><td>h1</td><td>h2</td><td>h1</td><td>h2</td></tr><tr><td>r1</td><td>r2</td><td>r1</td><td>r2</td></tr></table>')
    def test_abzatz(self):
        a="""Absatz1

        Abzats2

        Abz3
        Abz3"""

        self.assertEqual(htmlize(a),
                         u'Absatz1<p>        Abzats2<p>        Abz3\n        Abz3')
    def test_lists(self):
        a="""
        Welcome to RegExr v2.0 by gskinner.com!

         -Edit the Expression & Text to see matches. Roll over matches or the expression for details.
        + Undo mistakes with ctrl-z. Save & Share expressions with friends or the Community. A full Reference & Help is available in the Library, or watch the video Tutorial

        - 12345 -98.7 3.141 .6180 9,000 +42
        - 555.123.4567	+1-(800)-555-2468

        - foo@demo.net	bar.ba@test.co.uk
         - www.demo.com	http://foo.co.uk/
        Sample text for testing:
        abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
        + 0123456789 +-.,!@#$%^&*();\/|<>"'
        + 12345 -98.7 3.141 .6180 9,000 +42
        + 555.123.4567	+1-(800)-555-2468
         + foo@demo.net	bar.ba@test.co.uk
         + www.demo.com	http://foo.co.uk/
        http://regexr.com/foo.html?q=bar
        """

        self.assertEqual(htmlize(a),
                u"""\n        Welcome to RegExr v2.0 by gskinner.com!<p>         -Edit the Expression &amp Text to see matches. Roll over matches or the expression for details.<ol><li>Undo mistakes with ctrl-z. Save &amp Share expressions with friends or the Community. A full Reference &amp Help is available in the Library, or watch the video Tutorial<p>        - 12345 -98.7 3.141 .6180 9,000 +42</li><ul><li>555.123.4567\t+1-(800)-555-2468<p>        - foo@demo.net\tbar.ba@test.co.uk</li><li>www.demo.com\t<a href="http://foo.co.uk/">http://foo.co.uk/</a></li></ul></ol>        Sample text for testing:\n        abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ<ol><li>0123456789 +-.,!@#$%^&amp*();\\/|&lt&gt"\'</li><li>12345 -98.7 3.141 .6180 9,000 +42</li><li>555.123.4567\t+1-(800)-555-2468</li><li>foo@demo.net\tbar.ba@test.co.uk</li><li>www.demo.com\t<a href="http://foo.co.uk/">http://foo.co.uk/</a></li></ol>        <a href="http://regexr.com/foo.html?q=bar">http://regexr.com/foo.html?q=bar</a>\n        """)

    def test_escape(self):
        a=r"""\*bold\* \\backslash\\ {yesterday}"""

        self.assertEqual(htmlize(a),
                         r'*bold* \backslash\ {yesterday}')

if __name__ == '__main__':
    unittest.main()
