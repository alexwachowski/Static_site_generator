from textnode import TextType

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result_list = []
        if self.props == None:
            return ""
        
        for prop in self.props:
            result_list.append(f" {prop}={self.props[prop]}")

        return ''.join(result_list)

    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode: no value")
        
        if self.tag == None:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag!r}, value={self.value!r}, props={self.props!r})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode: no tag")
        if self.children == None:
            raise ValueError("ParentNode: no children")
        
        result = ''
        for child in self.children:
            result += child.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"
    
def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.BOLD:
                return LeafNode('b', text_node.text)
            case TextType.ITALIC:
                return LeafNode('i', text_node.text)
            case TextType.CODE:
                return LeafNode('code', text_node.text)
            case TextType.LINK:
                return LeafNode(f'a href="{text_node.url}"', text_node.text)
            case TextType.IMAGE:
                return LeafNode('img', '', {
                "src": text_node.url,
                "alt": text_node.text
            })
            
            case _:
                return LeafNode(None, text_node.text)