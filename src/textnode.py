from enum import Enum


class TextType(Enum):
    BOLD_TEXT = "**Bold text**"
    TEXT = "text(plain)"
    ITALIC_TEXT = "_Italic text_"
    CODE_TEXT = "'Code text"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        if url:
            self.url = url

    def __eg__(self, other):
        if self.TextNode == other.TextNode:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}"


def main():
    New_node = TextNode("blablabla", "**Bold text**", "https://xd123.com")
    print(New_node)
    print("xd")

