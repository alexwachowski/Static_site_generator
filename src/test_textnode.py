# import unittest

# from textnode import TextNode, TextType
# from functions import split_nodes_delimiter


# class TestTextNode(unittest.TestCase):
#     def test_eq(self):
#         node = TextNode("This is a text node", TextType.BOLD)
#         node2 = TextNode("This is a text node", TextType.BOLD)
#         self.assertEqual(node, node2)

#     def test_not_eq(self):
#         node = TextNode("This is a text node", TextType.ITALIC, "placeholder.com")
#         node2 = TextNode("This is a text node", TextType.BOLD, "placeholder.com")
#         self.assertNotEqual(node, node2)

#     def test_url(self):
#         node = TextNode("This is a text node", TextType.ITALIC, None)
#         node2 = TextNode("This is a text node", TextType.ITALIC, None)
#         self.assertEqual(node, node2)

#     def test_delimiter_split(self):
#         node = TextNode("This is text with a `code block` word", TextType.TEXT)
#         new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
#         expected = [
#             TextNode("This is text with a ", TextType.TEXT),
#             TextNode("code block", TextType.CODE),
#             TextNode(" word", TextType.TEXT),
#         ]   
#         self.assertEqual(new_nodes, expected)

#     def test_delimiter_split_bold(self):
#         node = TextNode("This is text with a **bold** word", TextType.TEXT)
#         new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
#         expected = [
#             TextNode("This is text with a ", TextType.TEXT),
#             TextNode("bold", TextType.BOLD),
#             TextNode(" word", TextType.TEXT),
#         ]   
#         self.assertEqual(new_nodes, expected)

#     def test_delimiter_split_italic(self):
#         node = TextNode("This is text with a _italic_ word", TextType.TEXT)
#         new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
#         expected = [
#             TextNode("This is text with a ", TextType.TEXT),
#             TextNode("italic", TextType.ITALIC),
#             TextNode(" word", TextType.TEXT),
#         ]   
#         self.assertEqual(new_nodes, expected)



# if __name__ == "__main__":
#     unittest.main()