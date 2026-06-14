import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
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


if __name__ == "__main__":
    unittest.main()
