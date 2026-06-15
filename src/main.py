from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


def main():

    New_node = TextNode("blablabla", TextType.TEXT, "https://xd123.com")
    print(New_node)
    print(text_node_to_html_node(New_node).to_html())


if __name__ == "__main__":
    main()
