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
