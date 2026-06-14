class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"htmlnode ({self.tag, self.value, self.children, self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or self.props == "":
            return ""
        new_prop = ""
        for prop in self.props:
            part = f' {prop}="{self.props[prop]}"'
            new_prop += part
        return new_prop


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value)
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None or self.tag == "":
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
