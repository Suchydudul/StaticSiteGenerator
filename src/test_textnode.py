import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq_nodes(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a node", TextType.TEXT)
        node4 = TextNode("This is a text node", TextType.BOLD, None)
        node5 = TextNode("This is a text node", TextType.BOLD, "https:sxxdsa")
        node6 = TextNode("This is a text node", TextType.BOLD, False)
        node7 = TextNode("This is a text node", TextType.BOLD, "none")

        self.assertEqual(node, node2)
        self.assertEqual(node, node4)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node7)
        self.assertNotEqual(node5, node6)

    def test_text_types(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node_code = TextNode("This is a code node", TextType.CODE)
        node_bold = TextNode("This is a BOLD node", TextType.BOLD)
        node_italic = TextNode("This is a ITALIC node", TextType.ITALIC)
        node_image = TextNode("This is a IMAGE node", TextType.IMAGE, "www.text.com")
        node_link = TextNode("This is a LINK node", TextType.LINK, "www.text.com")
        html_node_code = text_node_to_html_node(node_code)
        html_node_bold = text_node_to_html_node(node_bold)
        html_node_italic = text_node_to_html_node(node_italic)
        html_node_link = text_node_to_html_node(node_link)
        html_node = text_node_to_html_node(node)
        html_node_image = text_node_to_html_node(node_image)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node_bold.tag, "b")
        self.assertEqual(html_node_italic.tag, "i")
        self.assertEqual(html_node_code.tag, "code")
        self.assertEqual(html_node_link.tag, "a")
        self.assertEqual(html_node_image.tag, "img")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node_link.props, {"href": "www.text.com"})
        self.assertEqual(
            html_node_image.props,
            {"src": "www.text.com", "alt": "This is a IMAGE node"},
        )

        self.assertEqual(html_node_image.value, "")


if __name__ == "__main__":
    unittest.main()
