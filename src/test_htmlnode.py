import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_htmlnode(self):
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

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode(None, "Hello, world!")
        node3 = LeafNode("", "Hello, world!")
        node4 = LeafNode("p", "Hello, world!", None)
        node5 = LeafNode("p", "Hello, world!", {"href": "www.test2137.pl"})

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), node3.to_html())
        self.assertEqual(node.to_html(), node4.to_html())
        self.assertEqual(node5.to_html(), '<p href="www.test2137.pl">Hello, world!</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
