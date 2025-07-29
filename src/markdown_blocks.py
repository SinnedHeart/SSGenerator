from enum import Enum
from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filter_block = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filter_block.append(block)
    return filter_block

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    normalized_text = " ".join(block.split())
    children = text_to_children(normalized_text)
    return HTMLNode("p", children=children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    heading_text = block[level:].strip()
    children = text_to_children(heading_text)
    return HTMLNode(f"h{level}", children=children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    code_content = block[4:-3]
    return HTMLNode("pre", children=[HTMLNode("code", value=code_content)])


def quote_to_html_node(block):
    lines = block.split("\n")
    quote_text = " ".join(line.lstrip(">").strip() for line in lines)
    children = text_to_children(quote_text)
    return HTMLNode("blockquote", children=children)    

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        dot_space_index = item.find(". ")
        text = item[dot_space_index + 2 :]
        children = text_to_children(text)
        html_items.append(HTMLNode("li", children=children))
    return HTMLNode("ol", children=html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(HTMLNode("li", children=children))
    return HTMLNode("ul", children=html_items)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            html_node = paragraph_to_html_node(block) 
        elif block_type == BlockType.HEADING:
            html_node = heading_to_html_node(block)
        elif block_type == BlockType.CODE:
            html_node = code_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            html_node = quote_to_html_node(block)
        elif block_type == BlockType.OLIST:
            html_node = olist_to_html_node(block)
        elif block_type == BlockType.ULIST:
            html_node = ulist_to_html_node(block)
        
        block_nodes.append(html_node)

    return HTMLNode("div", children=block_nodes)