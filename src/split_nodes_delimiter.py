import re
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_urls


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted_images = extract_markdown_images(node.text)
        pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        split_node = []
        splitted_nodes = re.split(pattern, node.text)
        if len(splitted_nodes) == 0:
            raise ValueError("invalid markdown, section not closed")
        for i in range(len(splitted_nodes)):
            if len(splitted_nodes[i]) == 0:
                continue
            elif (
                len(extracted_images) != 0
                and splitted_nodes[i] == extracted_images[0][1]
            ):
                del extracted_images[0]
            elif (
                len(extracted_images) != 0 and splitted_nodes[i] in extracted_images[0]
            ):
                alt_text = extracted_images[0][0]
                url = extracted_images[0][1]
                new_text_node = TextNode(alt_text, TextType.IMAGE, url)
                split_node.append(new_text_node)
            else:
                new_text_node = TextNode(splitted_nodes[i], TextType.TEXT)
                split_node.append(new_text_node)
        new_nodes.extend(split_node)

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted_ulrs = extract_markdown_urls(node.text)
        pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
        split_node = []
        splitted_nodes = re.split(pattern, node.text)
        if len(splitted_nodes) == 0:
            raise ValueError("invalid markdown, section not closed")
        for i in range(len(splitted_nodes)):
            if len(splitted_nodes[i]) == 0:
                continue
            elif len(extracted_ulrs) != 0 and splitted_nodes[i] == extracted_ulrs[0][1]:
                del extracted_ulrs[0]
            elif len(extracted_ulrs) != 0 and splitted_nodes[i] in extracted_ulrs[0]:
                alt_text = extracted_ulrs[0][0]
                url = extracted_ulrs[0][1]
                new_text_node = TextNode(alt_text, TextType.LINK, url)
                split_node.append(new_text_node)
            else:
                new_text_node = TextNode(splitted_nodes[i], TextType.TEXT)
                split_node.append(new_text_node)
        new_nodes.extend(split_node)

    return new_nodes


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_node = []
        splitted_nodes = node.text.split(delimiter)
        if len(splitted_nodes) == 0:
            raise ValueError("invalid markdown, section not closed")
        for i in range(len(splitted_nodes)):
            if len(splitted_nodes[i]) == 0:
                pass

            elif i % 2 == 1:
                new_text_node = TextNode(splitted_nodes[i], text_type)
                split_node.append(new_text_node)
            else:
                new_text_node = TextNode(splitted_nodes[i], TextType.TEXT)
                split_node.append(new_text_node)

        # cooler way to split but may implement l8r idk
        # for splitted_node in splitted_nodes:
        # if splitted_node.startswith(delimiter) & splitted_node.endswith(delimiter):
        # new_text_node = TextNode(splitted_node[1 : len(splitted_node) - 1])
        #   new_nodes.extend(new_text_node)
        new_nodes.extend(split_node)
    return new_nodes
