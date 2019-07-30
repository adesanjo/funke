from __future__ import annotations
from typing import List, Optional, Tuple, Union

from tokens import *
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

class GreaterThanNode(Node):
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
        self.nextToken: Optional[Token] = None
        self.advance()
    
    def advance(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
        else:
            self.token = None
        if self.idx + 1 < len(self.tokens):
            self.nextToken = self.tokens[self.idx + 1]
        else:
            self.nextToken = None
    
    def parseTokens(self) -> Tuple[Node, Optional[Error]]:
        return self.makeProgram()
    
    def makeProgram(self) -> Tuple[Node, Optional[Error]]:
        nodes = []
        startPos = self.token.startPos
        idx = self.idx
        assign, err = self.makeAssign()
        while not err:
            nodes.append(assign)
            idx = self.idx
            assign, err = self.makeAssign()
        if err.type != "NotAssign":
            return Node(), err
        self.idx = idx - 1
        self.advance()
        basicExpr, err = self.makeBasicExpr()
        if err:
            return Node(), err
        nodes.append(basicExpr)
        endPos = self.token.endPos
        return ProgramNode(startPos, endPos, nodes), None
    
    def makeAssign(self) -> Tuple[Node, Optional[Error]]:
        startPos = self.token.startPos
        if self.token.type != TT_IDENTIFIER:
            return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected Identifier")
        funcName = self.token.value
        assert(isinstance(funcName, str))
        self.advance()
        
        if self.token.type != TT_LPAREN:
            return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('")
        self.advance()
        
        params = []
        if self.token.type == TT_IDENTIFIER:
            params.append(self.token.value)
            self.advance()
            while self.token.type == TT_COMMA:
                self.advance()
                if self.token.type != TT_IDENTIFIER:
                    return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected identifier")
                params.append(self.token.value)
                self.advance()
        if self.token.type != TT_RPAREN:
            return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'")
        self.advance()
        
        if self.token.type != TT_EQUAL:
            return Node(), Error(self.token.startPos, self.token.endPos, "NotAssign", "Expected '='")
        self.advance()
        
        exprNodes, err = self.makeExprs()
        if err:
            return Node(), err
        endPos = exprNodes[-1].endPos
        assert(endPos is not None)
        return AssignNode(startPos, endPos, funcName, params, exprNodes), None
    
    def makeExprs(self) -> Tuple[List[Node], Optional[Error]]:
        exprs = []
        expr, err = self.makeExpr()
        if err:
            return [], err
        while self.token.type == TT_COMMA:
            self.advance()
            expr, err = self.makeExpr()
            if err:
                return [], err
        exprs.append(expr)
        return exprs, None
    
    def makeExpr(self) -> Tuple[Node, Optional[Error]]:
        if self.token.type == TT_IDENTIFIER and self.nextToken.type == TT_EQUAL:
            startPos = self.token.startPos
            varName = self.token.value
            assert(isinstance(varName, str))
            self.advance()
            self.advance()
            basicExpr, err = self.makeBasicExpr()
            if err:
                return Node(), err
            endPos = basicExpr.endPos
            assert(endPos is not None)
            return VarAssignNode(startPos, endPos, varName, basicExpr), None
        basicExpr, err = self.makeBasicExpr()
        if err:
            return Node(), err
        return basicExpr, None
    
    def makeBasicExpr(self) -> Tuple[Node, Optional[Error]]:
        return Node(), None