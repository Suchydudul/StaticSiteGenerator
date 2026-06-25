from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextType, TextNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown: str):
    markdown_block = markdown_to_blocks(markdown)
    for block in markdown_block:
        blocktype = block_to_block_type(block)
        print(block)
        block, tag = get_block_tag(blocktype, block)
        print(block, tag)
        list_of_nodes = text_to_textnodes(block)
        print(list_of_nodes)
        list_of_leafnodes = []
        for node in list_of_nodes:
            list_of_leafnodes.append(text_node_to_html_node(node))
        print(list_of_leafnodes)
        parentnode = ParentNode(tag, list_of_leafnodes)
        print(parentnode.to_html())
        list_of_parent_nodes = []
        list_of_parent_nodes.append(parentnode)
    print(ParentNode("div", list_of_parent_nodes).to_html())


def get_block_tag(blocktype: BlockType, block: str) -> str:
    match blocktype.value:
        case "paragraph":
            print("para")
            return block.replace("\n", " "), "p"
        case "quote":
            print("head")
        case "code":
            return
        case "heading":
            return
        case "unordered_list":
            return
        case "ordered_list":
            return


md = """
This is **bolded** paragraph
text in a p
tag here


"""

markdown_to_html_node(md)
