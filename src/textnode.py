from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    BOLD = "bold"
    TEXT = "text"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode{self.text}, {self.text_type.value}, {self.url}"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    text = text_node.text
    url = text_node.url
    text_type = text_node.text_type.value
    match text_type:
        case "text":
            return LeafNode(None, text, None)
        case "bold":
            return LeafNode("b", text, None)
        case "italic":
            return LeafNode("i", text, None)

        case "code":
            return LeafNode("code", text, None)

        case "link":
            return LeafNode("a", text, {"href": url})

        case "image":
            return LeafNode("img", "", {"src": url, "alt": text})
        case _:
            raise Exception("invalid node text type")
