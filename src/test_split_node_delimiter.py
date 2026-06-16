from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


import unittest


class TestSplitNode(unittest.TestCase):
    def test_split_node_bold(self):

        node = TextNode("This is a **text node**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        print(new_nodes)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.TEXT, None),
                TextNode("text node", TextType.BOLD, None),
            ],
        )


if __name__ == "__main__":
    unittest.main()
