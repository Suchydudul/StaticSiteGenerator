import unittest
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "Test",
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        node2 = HTMLNode(
            "Test",
            None,
            None,
            None,
        )
        node3 = HTMLNode(
            "Test",
            None,
            None,
            "",
        )
        node4 = HTMLNode(
            "Test",
            None,
            None,
            {},
        )
        node5 = HTMLNode(
            "Test",
            None,
            None,
            {"href": "https://www.duckduckgo.com"},
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )
        self.assertEqual(node2.props_to_html(), node3.props_to_html())
        self.assertEqual(node2.props_to_html(), "")
        self.assertEqual(node4.props_to_html(), "")
        self.assertEqual(node5.props_to_html(), ' href="https://www.duckduckgo.com"')


if __name__ == "__main__":
    unittest.main()
