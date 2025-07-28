from typing import Optional

class HTMLNode:
    def __init__(self, 
                 tag: Optional[str] = None, 
                 value: Optional[str] = None, 
                 children: Optional[list["HTMLNode"]] = None, 
                 props: Optional[dict] = None):
        
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
             return " " + " ".join([f'{key}="{value}"'for key, value in self.props.items()])
        return ""
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'