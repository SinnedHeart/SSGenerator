from typing import Optional
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, 
                 tag: Optional[str], 
                 value: str = "", 
                 props: Optional[dict] = None):
        
        super().__init__(tag=tag, value=value, props=props)

    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return str(self.value)
        props_str = ""
        if self.props:
            props_str = " " + " ".join([f'{key}="{value}"'for key, value in self.props.items()])
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    