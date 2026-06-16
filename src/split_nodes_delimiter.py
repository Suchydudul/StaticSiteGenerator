from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            pass
        splitted_nodes = node.text.split(delimiter)
        print(splitted_nodes)
        for splitted_node in splitted_nodes:
            if len(splitted_node) == 0:
                pass

            elif splitted_node == splitted_nodes[1]:
                new_text_node = TextNode(splitted_node, text_type)
                new_nodes.append(new_text_node)
            else:
                new_text_node = TextNode(splitted_node, TextType.TEXT)
                new_nodes.append(new_text_node)

        # cooler way to split but may implement l8r idk
        # for splitted_node in splitted_nodes:
        # if splitted_node.startswith(delimiter) & splitted_node.endswith(delimiter):
        # new_text_node = TextNode(splitted_node[1 : len(splitted_node) - 1])
        #   new_nodes.extend(new_text_node)
        #
    return new_nodes


node = TextNode("This is a **text node**", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
__import__("pprint").pprint(new_nodes)
