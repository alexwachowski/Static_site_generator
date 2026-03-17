from textnode import TextNode, TextType, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode, text_node_to_html_node
import re
import os
import shutil
from pathlib import Path
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        string = old_node.text
        if delimiter in string:
            split_string = string.split(delimiter)

            if len(split_string)%2 == 0:
                raise Exception("invalid markdown")    

            for i in range(0,len(split_string)):
                if split_string[i]=='':
                    continue
                if i%2==0:
                    result.append(TextNode(split_string[i], TextType.TEXT))
                else:
                    result.append(TextNode(split_string[i], text_type))
        else:
            result.append(old_node)
        
    return result


def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    result = []
    alt_text = None
    url = None
    for old_node in old_nodes:
        if old_node.text == None:
            break
        matches = extract_markdown_images(old_node.text)
        if len(matches)==0:
            result.append(old_node)
            continue

        alt_text = matches[0][0]
        url = matches[0][1]
        sections = old_node.text.split(f"![{alt_text}]({url})") 
        node1 = TextNode(sections[0], TextType.TEXT)
        result.append(node1)
        node2 =  TextNode(alt_text, TextType.IMAGE, url)
        result.append(node2)

        if sections[1]:
            recurs_node = TextNode(sections[1], TextType.TEXT)
            recurs = split_nodes_image([recurs_node])
            result.extend(recurs)
    
    return result

def split_nodes_link(old_nodes):
    # print("old_nodes: ", old_nodes)
    result = []
    link_text = None
    url = None
    for old_node in old_nodes:
        if old_node.text == None:
            break
        matches = extract_markdown_links(old_node.text)
        # print('matches: ', matches)
        if len(matches)==0:
            result.append(old_node)
            continue

        link_text = matches[0][0]
        url = matches[0][1]
        sections = old_node.text.split(f"[{link_text}]({url})") 
        node1 = TextNode(sections[0], TextType.TEXT)
        result.append(node1)
        node2 =  TextNode(link_text, TextType.LINK, url)
        result.append(node2)

        if sections[1]:
            recurs_node = TextNode(sections[1], TextType.TEXT)
            recurs = split_nodes_link([recurs_node])
            result.extend(recurs)
    
    return result

def text_to_textnodes(text):
   result = []

   bold_text = split_nodes_delimiter([text], '**', TextType.BOLD)
   italic_text= split_nodes_delimiter(bold_text, '_', TextType.ITALIC)
   code_text = split_nodes_delimiter(italic_text, '`', TextType.CODE)
   image_split = split_nodes_image(code_text)
   link_split = split_nodes_link(image_split)
   result.extend(link_split)

   
#    print('result: ', result)
   return result

def markdown_to_blocks(markdown):
    blocks = markdown.strip().split('\n\n')
    cleaned_blocks = []
    for block in blocks: 
        stripped_block = block.strip()
        if stripped_block != '':
            cleaned_blocks.append(stripped_block)
    # print("cleaned_blocks: ", cleaned_blocks)
    return cleaned_blocks

def is_ordered_list(block):
    lines = block.split("\n")
    for line in lines:
        if not re.match(r"\d+\.\s", line):
            return False
    return True

def block_to_block_type(block):
    match block:
        case b if b.startswith('#'):
            return BlockType.HEADING
        case b if b.startswith('```'):
            return BlockType.CODE
        case b if b.startswith('>'):
            return BlockType.QUOTE
        case b if b.startswith('- '):
            return BlockType.UNORDERED_LIST
        case b if is_ordered_list(b):
            return BlockType.ORDERED_LIST
        
        case _:
            return BlockType.PARAGRAPH
        
def get_heading_level(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    return count
        
def block_to_html(block, block_type):
    # block = block.replace("\n", " ")
    # block_node = TextNode(block, TextType.TEXT)
    # children = text_to_textnodes(block_node)
    # child_nodes = []
    # for child in children:
    #     child_node = text_node_to_html_node(child)
    #     child_nodes.append(child_node)

    if block_type == BlockType.HEADING:
        level = get_heading_level(block)
        text = block[level+1:]  # remove "# "
        node = TextNode(text, TextType.TEXT)
        children = text_to_textnodes(node)
        html_children = [text_node_to_html_node(c) for c in children]
        return ParentNode(f"h{level}", html_children)
    
    elif block_type == BlockType.CODE:
        code = block.replace("```", '')
        node = (TextNode(code, TextType.CODE))
        return text_node_to_html_node(node)
    
    elif block_type == BlockType.PARAGRAPH:
        block = block.replace("\n", " ")
        block_node = TextNode(block, TextType.TEXT)
        children = text_to_textnodes(block_node)
        child_nodes = []
        for child in children:
            child_node = text_node_to_html_node(child)
            child_nodes.append(child_node)
        return (ParentNode("p", child_nodes))
    
    elif block_type == BlockType.QUOTE:
        quote = block.replace("> ", '')
        node = TextNode(f"{quote}", TextType.TEXT)
        children = text_to_textnodes(node)
        html_children = [text_node_to_html_node(c) for c in children]
        return (ParentNode("blockquote", html_children))
    
    elif block_type == BlockType.UNORDERED_LIST:
        items = block.split("\n")
        li_nodes = []

        for item in items:
            text = item.replace("- ", "", 1)
            text_nodes = text_to_textnodes(TextNode(text, TextType.TEXT))
            html_nodes = [text_node_to_html_node(n) for n in text_nodes]

            li_nodes.append(ParentNode("li", html_nodes))

        return ParentNode("ul", li_nodes)
    elif block_type == BlockType.ORDERED_LIST:
        items = block.split("\n")
        li_nodes = []

        for item in items:
            text = item.split(". ", 1)[1]
            text_nodes = text_to_textnodes(TextNode(text, TextType.TEXT))
            html_nodes = [text_node_to_html_node(n) for n in text_nodes]

            li_nodes.append(ParentNode("li", html_nodes))

    return ParentNode("ol", li_nodes)

def markdown_to_html(markdown):
    children = []
    final_string = ParentNode("div", children)
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        # print('block: ', block)
        block_type = block_to_block_type(block)
        # print('block_type: ', block_type)
        block_nodes = block_to_html(block, block_type)
        # print("block_nodes: ", block_nodes)
        children.append(block_nodes)
    # print("children: ", children)
    return final_string

def copy_to_public():
    if os.path.exists("./static") != True:
        raise Exception("No static directory exists")
    if os.path.exists("./public") == True:
        shutil.rmtree("./public")

    os.mkdir("./public")
    in_static = os.listdir("./static")

    for item in in_static:
        is_dir = os.path.isdir(f"./static/{item}")
        if is_dir == True:
            os.mkdir(f"./public/{item}")
            dir_list = os.listdir(f"./static/{item}")
            for file in dir_list:
                # print("file: ", file)
                if os.path.isfile(f"./static/{item}/{file}") == True:
                    shutil.copy(f"./static/{item}/{file}", f"./public/{item}")
        is_file = os.path.isfile(f"./static/{item}")
        if is_file == True:
            shutil.copy(f"./static/{item}", f"./public/{item}")
        

def extract_title(markdown):
    result = ""
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        # print("block: ", block)
        if "# " in block:
            block = block.replace("# ", "")
            result += block
            # print("result: ", result)
            return result
        else:
            continue

    raise Exception("No title found")

def get_md_files(path):
    paths = []

    for dir in os.listdir(path):
        full_path = os.path.join(path, dir)

        if os.path.isdir(full_path):
            paths.extend(get_md_files(full_path))
        elif os.path.isfile(full_path) is True and full_path.endswith('.md'):
            paths.append(full_path)

    return paths

def generate_page(from_path, template_path, dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")

    if os.path.exists('./public') !=True:
        os.mkdir("./public")
    file = None
    g = open(template_path)
    # temp_file = g.read()

    if os.path.isfile(from_path) == True:
        f = open(from_path)
        temp_file = g.read()
        html_file = f.replace(".md", ".html")
        public_html = Path(html_file.replace("content", "public"))
        public_html.parent.mkdir(parents=True, exist_ok=True)
        md_file = f.read()
        md_node = markdown_to_html(md_file)
        md_html = md_node.to_html()
        title = extract_title(md_file)
        temp_file = temp_file.replace("{{ Title }}", title)
        temp_file = temp_file.replace("{{ Content }}", md_html)
        d = open(html_file, "w")
        d.write(temp_file)
        d.close()
        g.seek(0)

        
    else:

        files = get_md_files(from_path)
        print("files: ", files)
        for file in files:
            temp_file = g.read()
            html_file = file.replace(".md", ".html")
            public_html = Path(html_file.replace("content", "public"))
            public_html.parent.mkdir(parents=True, exist_ok=True)
            f = open(file)
            md_file = f.read()
            md_node = markdown_to_html(md_file)
            md_html = md_node.to_html()
            title = extract_title(md_file)
            temp_file = temp_file.replace("{{ Title }}", title)
            temp_file = temp_file.replace("{{ Content }}", md_html)
            d = open(public_html, "w")
            d.write(temp_file)
            d.close()
            g.seek(0)
            
    f.close()
    g.close()
        

