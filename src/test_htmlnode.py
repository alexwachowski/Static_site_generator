import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType, BlockType
from functions import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes, markdown_to_blocks, block_to_block_type, markdown_to_html, copy_to_public, extract_title, generate_page, get_md_files


class TestHTMLNode(unittest.TestCase):
    # def test_print(self):
    #     node = HTMLNode("p", "this is a test", None, None)
    #     print("Test 1: ", node)

    # def test_none_values(self):
    #     node = HTMLNode()
    #     print("Test 2:")
    #     print(node)
    
    # def test_props_to_html(self):
    #     test_prop = {
    #         "href": "https://www.google.com",
    #         "target": "_blank",
    #     }
    #     node = HTMLNode("p", "this is a test", "Something", test_prop)
    #     print("Test 3: ")
    #     print (node.props_to_html())



    # def test_leaf_to_html_p(self):
    #     node = LeafNode("p", "Hello, world!")
    #     print("Test 4")
    #     self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    # def test_print_leafnode(self):
    #     node = LeafNode("h1", "Hello, Alex!")
    #     print(node)

    # def test_to_html_with_children(self):
    #     child_node = LeafNode("span", "child")
    #     parent_node = ParentNode("div", [child_node])
    #     self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    # def test_to_html_with_grandchildren(self):
    #     grandchild_node = LeafNode("b", "grandchild")
    #     child_node = ParentNode("span", [grandchild_node])
    #     parent_node = ParentNode("div", [child_node])
    #     self.assertEqual(
    #         parent_node.to_html(),
    #         "<div><span><b>grandchild</b></span></div>",
    #     )

    
    


    # def test_text(self):
    #     node = TextNode("This is a text node", TextType.TEXT)
    #     html_node = text_node_to_html_node(node)
    #     self.assertEqual(html_node.tag, None)
    #     self.assertEqual(html_node.value, "This is a text node")

    # def test_markdown_images(self):
    #     matches = extract_markdown_images(
    #     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    #     )
    #     self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    # def test_markdown_links(self):
    #     matches = extract_markdown_links(
    #     "This is text with a link [to boot dev](https://www.boot.dev)"
    #     )
    #     self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    # def test_markdown_multi_links(self):
    #     matches = extract_markdown_links(
    #     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #     )
    #     self.assertListEqual([("to boot dev", "https://www.boot.dev"),("to youtube", "https://www.youtube.com/@bootdotdev")], matches)


    # def test_split_images(self):
    #     node = TextNode(
    #         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #         TextType.TEXT,
    #     )
    #     new_nodes = split_nodes_image([node])
    #     self.assertListEqual(
    #         [
    #             TextNode("This is text with an ", TextType.TEXT),
    #             TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
    #             TextNode(" and another ", TextType.TEXT),
    #             TextNode(
    #                 "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
    #             ),
    #         ],
    #         new_nodes,
    #     )

    # def test_split_single_image(self):
    #     node = TextNode(
    #         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
    #         TextType.TEXT,
    #     )
    #     new_nodes = split_nodes_image([node])
    #     self.assertListEqual(
    #         [
    #             TextNode("This is text with an ", TextType.TEXT),
    #             TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
    #         ],
    #         new_nodes,
    #     )

    # def test_split_link(self):
    #     node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #     TextType.TEXT,
    #     )
    #     new_nodes = split_nodes_link([node])
    #     self.assertEqual(
    #     [
    #         TextNode("This is text with a link ", TextType.TEXT),
    #         TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    #         TextNode(" and ", TextType.TEXT),
    #         TextNode(
    #             "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
    #         ),
    #     ], 
    #     new_nodes,
    #     )

    # def test_split_single_link(self):
    #     node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev)",
    #     TextType.TEXT,
    #     )
    #     new_nodes = split_nodes_link([node])
    #     self.assertEqual(
    #     [
    #         TextNode("This is text with a link ", TextType.TEXT),
    #         TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    #     ], 
    #     new_nodes,
    #     )


    # def test_text_to_nodes(self):
    #     node = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
    #                     TextType.TEXT,
    #                     )
    #     new_nodes = text_to_textnodes(node)
    #     self.assertEqual([
    #         TextNode("This is ", TextType.TEXT),
    #         TextNode("text", TextType.BOLD),
    #         TextNode(" with an ", TextType.TEXT),
    #         TextNode("italic", TextType.ITALIC),
    #         TextNode(" word and a ", TextType.TEXT),
    #         TextNode("code block", TextType.CODE),
    #         TextNode(" and an ", TextType.TEXT),
    #         TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    #         TextNode(" and a ", TextType.TEXT),
    #         TextNode("link", TextType.LINK, "https://boot.dev"),
    #     ], new_nodes
    #     )


    # def test_text_to_nodes_multiple_formats(self):
    #     node = TextNode(
    #         "Start with **bold** then _italic_ then `code` and finally a [site](https://example.com)",
    #         TextType.TEXT,
    #     )
    #     new_nodes = text_to_textnodes(node)
    #     self.assertEqual([
    #         TextNode("Start with ", TextType.TEXT),
    #         TextNode("bold", TextType.BOLD),
    #         TextNode(" then ", TextType.TEXT),
    #         TextNode("italic", TextType.ITALIC),
    #         TextNode(" then ", TextType.TEXT),
    #         TextNode("code", TextType.CODE),
    #         TextNode(" and finally a ", TextType.TEXT),
    #         TextNode("site", TextType.LINK, "https://example.com"),
    #     ], new_nodes
    #     )


    # def test_text_to_nodes_image_and_code(self):
    #     node = TextNode(
    #         "Here is an ![alt text](https://example.com/image.png) and some `inline code` with **bold text**",
    #         TextType.TEXT,
    #     )
    #     new_nodes = text_to_textnodes(node)
    #     self.assertEqual([
    #         TextNode("Here is an ", TextType.TEXT),
    #         TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
    #         TextNode(" and some ", TextType.TEXT),
    #         TextNode("inline code", TextType.CODE),
    #         TextNode(" with ", TextType.TEXT),
    #         TextNode("bold text", TextType.BOLD),
    #     ], new_nodes
    #     )

    # def test_text_to_nodes_starting_with_markdown(self):
    #     node = TextNode(
    #         "**Bold start** followed by normal text",
    #         TextType.TEXT,
    #     )
    #     new_nodes = text_to_textnodes(node)
    #     self.assertEqual([
    #         TextNode("Bold start", TextType.BOLD),
    #         TextNode(" followed by normal text", TextType.TEXT),
    #     ], new_nodes
    #     )

    # def test_text_to_nodes_multiple_links_and_images(self):
    #     node = TextNode(
    #         "An ![img1](https://example.com/1.png) then a [link1](https://a.com) and another ![img2](https://example.com/2.png)",
    #         TextType.TEXT,
    #     )
    #     new_nodes = text_to_textnodes(node)
    #     self.assertEqual([
    #         TextNode("An ", TextType.TEXT),
    #         TextNode("img1", TextType.IMAGE, "https://example.com/1.png"),
    #         TextNode(" then a ", TextType.TEXT),
    #         TextNode("link1", TextType.LINK, "https://a.com"),
    #         TextNode(" and another ", TextType.TEXT),
    #         TextNode("img2", TextType.IMAGE, "https://example.com/2.png"),
    #     ], new_nodes
    #     )

#     def test_markdown_to_blocks(self):
#         md = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

# - This is a list
# - with items
# """
#         blocks = markdown_to_blocks(md)
#         self.assertEqual(
#             blocks,
#             [
#             "This is **bolded** paragraph",
#             "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
#             "- This is a list\n- with items",
#             ],
#         )

#     def test_multiple_paragraphs(self):
#         md = """
# Paragraph one.

# Paragraph two.

# Paragraph three.
# """
#         blocks = markdown_to_blocks(md)
#         self.assertEqual(
#             blocks,
#             [
#                 "Paragraph one.",
#                 "Paragraph two.",
#                 "Paragraph three.",
#             ],
#         )

#     def test_multiline_paragraph(self):
#         md = """
# This is a paragraph
# that continues
# across multiple lines.

# This is another paragraph.
# """
#         blocks = markdown_to_blocks(md)
#         self.assertEqual(
#             blocks,
#             [
#                 "This is a paragraph\nthat continues\nacross multiple lines.",
#                 "This is another paragraph.",
#             ],
#         )

#     def test_list_then_paragraph(self):
#         md = """
# - Item one
# - Item two
# - Item three

# This is a paragraph after the list.
# """
#         blocks = markdown_to_blocks(md)
#         self.assertEqual(
#             blocks,
#             [
#                 "- Item one\n- Item two\n- Item three",
#                 "This is a paragraph after the list.",
#             ],
#         )

#     def test_extra_blank_lines(self):
#         md = """
# Paragraph one.


# Paragraph two.



# Paragraph three.
# """
#         blocks = markdown_to_blocks(md)
#         self.assertEqual(
#             blocks,
#             [
#                 "Paragraph one.",
#                 "Paragraph two.",
#                 "Paragraph three.",
#             ],
#         )

#     def test_leading_and_trailing_whitespace(self):
#         md = """


# First paragraph.


# Second paragraph.


# """
#         blocks = markdown_to_blocks(md)
#         self.assertEqual(
#             blocks,
#             [
#                 "First paragraph.",
#                 "Second paragraph.",
#             ],
#         )

    # def test_heading_block(self):
    #     block = "# Heading text"
    #     test_block = block_to_block_type(block)
    #     self.assertEqual(test_block, BlockType.HEADING)


    # def test_code_block(self):
    #     block = "```python"
    #     test_block = block_to_block_type(block)
    #     self.assertEqual(test_block, BlockType.CODE)


    # def test_quote_block(self):
    #     block = "> quoted text"
    #     test_block = block_to_block_type(block)
    #     self.assertEqual(test_block, BlockType.QUOTE)


    # def test_unordered_list_block(self):
    #     block = "- list item"
    #     test_block = block_to_block_type(block)
    #     self.assertEqual(test_block, BlockType.UNORDERED_LIST)


    # def test_ordered_list_block(self):
    #     block = ". list item"
    #     test_block = block_to_block_type(block)
    #     self.assertEqual(test_block, BlockType.ORDERED_LIST)


    # def test_paragraph_block(self):
    #     block = "This is a normal paragraph."
    #     test_block = block_to_block_type(block)
    #     self.assertEqual(test_block, BlockType.PARAGRAPH)


    # def test_plain_text_defaults_to_paragraph(self):
    #     block = "Hello world"
    #     test_block = block_to_block_type(block)
    #     self.assertEqual(test_block, BlockType.PARAGRAPH)

#     def test_paragraphs(self):
#         md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """

#         node = markdown_to_html(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#         )

# def test_codeblock(self):
#     md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """

#     node = markdown_to_html(md)
#     html = node.to_html()
#     self.assertEqual(
#         html,
#         "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
#     )

    # def test_copy_to_public(self):
    #     print(copy_to_public())

#     def test_extract_title(self):
#         markdown = """
# # Sample Title

# This is a short markdown file.
# It is used for unit testing."""
#         node = extract_title(markdown)
#         self.assertEqual("Sample Title", node)

    def test_generate_page(self):
        generate_page("./content", "template.html", "./public")

    # def test_get_md_file_path(self):
    #     files = get_md_files("./content")
    #     print("files: ", files)