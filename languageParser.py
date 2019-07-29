from __future__ import annotations
from typing import List, Optional, Tuple, Union

from languageLexer import Position, Token
from error import Error, InvalidSyntaxError

class Node:
    def __init__(self, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        self.startPos: Optional[Position] = startPos
        self.endPos: Optional[Position] = endPos

class ProgramNode(Node):
    def __init__(self, startPos: Position, endPos: Position, nodes: List[Node]):
        super().__init__(startPos, endPos)
        self.nodes: List[Node] = nodes

class AssignNode(Node):
    def __init__(self, startPos: Position, endPos: Position, funcName: str, params: List[str], exprNodes: List[Node]):
        super().__init__(startPos, endPos)
        self.funcName: str = funcName
        self.parans: List[str] = params
        self.exprNodes: List[Node] = exprNodes

class VarAssignNode(Node):
    def __init__(self, startPos: Position, endPos: Position, varName: str, value: Node):
        super().__init__(startPos, endPos)
        self.varName: str = varName
        self.value: Node = value

class VarAccessNode(Node):
    def __init__(self, startPos: Position, endPos: Position, varName: str):
        super().__init__(startPos, endPos)
        self.varName: str = varName

class IntNode(Node):
    def __init__(self, startPos: Position, endPos: Position, value: int):
        super().__init__(startPos, endPos)
        self.value: int = value

class FloatNode(Node):
    def __init__(self, startPos: Position, endPos: Position, value: float):
        super().__init__(startPos, endPos)
        self.value: float = value

class StringNode(Node):
    def __init__(self, startPos: Position, endPos: Position, value: str):
        super().__init__(startPos, endPos)
        self.value: str = value

class InputNode(Node):
    def __init__(self, startPos: Position, endPos: Position):
        super().__init__(startPos, endPos)

class PrintNode(Node):
    def __init__(self, startPos: Position, endPos: Position, node: Node):
        super().__init__(startPos, endPos)
        self.node: Node = node

class PlusNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode

class MinusNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode

class MulNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode

class DivNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode

class ModNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode

class EqualNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node, exprNodes: List[Node]):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
        self.exprNodes: List[Node] = exprNodes

class LessThanNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node, exprNodes: List[Node]):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
        self.exprNodes: List[Node] = exprNodes

class GreatrThanNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node, exprNodes: List[Node]):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
        self.exprNodes: List[Node] = exprNodes

class NotEqualNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node, exprNodes: List[Node]):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
        self.exprNodes: List[Node] = exprNodes

class CallNode(Node):
    def __init__(self, startPos: Position, endPos: Position, funcName: str, params: List[str]):
        super().__init__(startPos, endPos)
        self.funcName: str = funcName
        self.parans: List[str] = params

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens: List[Token] = tokens
        self.idx: int = -1
        self.token: Optional[Token] = None
        self.advance()
    
    def advance(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
        else:
            self.token = None
    
    def parseTokens(self) -> Tuple[Node, Optional[Error]]:
        return self.makeProgram()
    
    def makeProgram(self) -> Tuple[Node, Optional[Error]]:
        assign, err = self.makeAssign()
        return Node(), None
    
    def makeAssign(self) -> Tuple[Node, Optional[Error]]:
        return Node(), None
    
    def makeExprs(self) -> Tuple[Node, Optional[Error]]:
        return Node(), None
    
    def makeExpr(self) -> Tuple[Node, Optional[Error]]:
        return Node(), None
    
    def makeBasicExpr(self) -> Tuple[Node, Optional[Error]]:
        return Node(), None