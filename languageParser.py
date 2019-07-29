from typing import List, Optional

from languageLexer import Position, Token

class Node:
    def __init__(self, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        self.startPos: Optional[Position] = startPos
        self.endPos: Optional[Position] = endPos

class NopNode(Node):
    def __init__(self, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        super().__init__(startPos, endPos)

class Parser:
    def __init__(self, tokens: List[Token]):
        pass
    
    def parseTokens(self) -> Node:
        return Node()