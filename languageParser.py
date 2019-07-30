from __future__ import annotations
from typing import List, Optional, Tuple, Union

from tokens import *
from languageLexer import Position, Token
from error import Error, InvalidSyntaxError

class Node:
    def __init__(self, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        self.startPos: Optional[Position] = startPos
        self.endPos: Optional[Position] = endPos
    
    def __repr__(self) -> str:
        return "Node"

class ProgramNode(Node):
    def __init__(self, startPos: Position, endPos: Position, nodes: List[Node]):
        super().__init__(startPos, endPos)
        self.nodes: List[Node] = nodes
    
    def __repr__(self) -> str:
        s = ",\n"
        return f"ProgramNode: [\n{s.join(str(node) for node in self.nodes)}\n]"

class AssignNode(Node):
    def __init__(self, startPos: Position, endPos: Position, funcName: str, params: List[str], exprNodes: List[Node]):
        super().__init__(startPos, endPos)
        self.funcName: str = funcName
        self.params: List[str] = params
        self.exprNodes: List[Node] = exprNodes
    
    def __repr__(self) -> str:
        return f"AssignNode [{self.funcName}, {self.params}, {', '.join(str(node) for node in self.exprNodes)}]"

class VarAssignNode(Node):
    def __init__(self, startPos: Position, endPos: Position, varName: str, value: Node):
        super().__init__(startPos, endPos)
        self.varName: str = varName
        self.value: Node = value
    
    def __repr__(self) -> str:
        return f"VarAssignNode [{self.varName}, {str(self.value)}]"

class VarAccessNode(Node):
    def __init__(self, startPos: Position, endPos: Position, varName: str):
        super().__init__(startPos, endPos)
        self.varName: str = varName
    
    def __repr__(self) -> str:
        return f"VarAccessNode [{self.varName}]"

class IntNode(Node):
    def __init__(self, startPos: Position, endPos: Position, value: int):
        super().__init__(startPos, endPos)
        self.value: int = value
    
    def __repr__(self) -> str:
        return f"IntNode [{self.value}]"

class FloatNode(Node):
    def __init__(self, startPos: Position, endPos: Position, value: float):
        super().__init__(startPos, endPos)
        self.value: float = value
    
    def __repr__(self) -> str:
        return f"FloatNode [{self.value}]"

class StringNode(Node):
    def __init__(self, startPos: Position, endPos: Position, value: str):
        super().__init__(startPos, endPos)
        self.value: str = value
    
    def __repr__(self) -> str:
        return f"StringNode [{self.value}]"

class InputNode(Node):
    def __init__(self, startPos: Position, endPos: Position):
        super().__init__(startPos, endPos)
    
    def __repr__(self) -> str:
        return f"InputNode"

class PrintNode(Node):
    def __init__(self, startPos: Position, endPos: Position, node: Node):
        super().__init__(startPos, endPos)
        self.node: Node = node
    
    def __repr__(self) -> str:
        return f"PrintNode [{str(self.node)}]"

class PlusNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
    
    def __repr__(self) -> str:
        return f"PlusNode [{str(self.leftNode)}, {str(self.rightNode)}]"

class MinusNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
    
    def __repr__(self) -> str:
        return f"MinusNode [{str(self.leftNode)}, {str(self.rightNode)}]"

class MulNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
    
    def __repr__(self) -> str:
        return f"MulNode [{str(self.leftNode)}, {str(self.rightNode)}]"

class DivNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
    
    def __repr__(self) -> str:
        return f"DivNode [{str(self.leftNode)}, {str(self.rightNode)}]"

class ModNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
    
    def __repr__(self) -> str:
        return f"ModNode [{str(self.leftNode)}, {str(self.rightNode)}]"

class EqualNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node, exprNodes: List[Node]):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
        self.exprNodes: List[Node] = exprNodes
    
    def __repr__(self) -> str:
        return f"EqualNode [{str(self.leftNode)}, {str(self.rightNode)}, {', '.join(str(node) for node in self.exprNodes)}]"

class LessThanNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node, exprNodes: List[Node]):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
        self.exprNodes: List[Node] = exprNodes
    
    def __repr__(self) -> str:
        return f"LessThanNode [{str(self.leftNode)}, {str(self.rightNode)}, {', '.join(str(node) for node in self.exprNodes)}]"

class GreaterThanNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node, exprNodes: List[Node]):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
        self.exprNodes: List[Node] = exprNodes
    
    def __repr__(self) -> str:
        return f"GreaterThanNode [{str(self.leftNode)}, {str(self.rightNode)}, {', '.join(str(node) for node in self.exprNodes)}]"

class NotEqualNode(Node):
    def __init__(self, startPos: Position, endPos: Position, leftNode: Node, rightNode: Node, exprNodes: List[Node]):
        super().__init__(startPos, endPos)
        self.leftNode: Node = leftNode
        self.rightNode: Node = rightNode
        self.exprNodes: List[Node] = exprNodes
    
    def __repr__(self) -> str:
        return f"NotEqualNode [{str(self.leftNode)}, {str(self.rightNode)}, {', '.join(str(node) for node in self.exprNodes)}]"

class CallNode(Node):
    def __init__(self, startPos: Position, endPos: Position, funcName: str, params: List[Node]):
        super().__init__(startPos, endPos)
        self.funcName: str = funcName
        self.params: List[Node] = params
    
    def __repr__(self) -> str:
        return f"CallNode [{self.funcName}, {', '.join(str(node) for node in self.params)}]"

class RandNode(Node):
    def __init__(self, startPos: Position, endPos: Position, fromNode: Node, toNode: Node):
        super().__init__(startPos, endPos)
        self.fromNode: Node = fromNode
        self.toNode: Node = toNode
    
    def __repr__(self) -> str:
        return f"RandNode [{str(self.fromNode)}, {str(self.toNode)}]"

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
            return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected Identifier. Error id: 0")
        funcName = self.token.value
        assert(isinstance(funcName, str))
        self.advance()
        
        if self.token.type != TT_LPAREN:
            return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 1")
        self.advance()
        
        params = []
        if self.token.type == TT_IDENTIFIER:
            params.append(self.token.value)
            self.advance()
            while self.token.type == TT_COMMA:
                self.advance()
                if self.token.type != TT_IDENTIFIER:
                    return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected identifier. Error id: 2")
                params.append(self.token.value)
                self.advance()
        if self.token.type != TT_RPAREN:
            return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 3")
        self.advance()
        
        if self.token.type != TT_EQUAL:
            return Node(), Error(self.token.startPos, self.token.endPos, "NotAssign", "Expected '='. Error id: 4")
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
        if self.token.type == TT_EOF:
            return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Unexpected EOF. Error id: 5")
        if self.token.type == TT_INT:
            startPos = self.token.startPos
            endPos = self.token.endPos
            value = self.token.value
            self.advance()
            assert(isinstance(value, int))
            return IntNode(startPos, endPos, value), None
        if self.token.type == TT_FLOAT:
            startPos = self.token.startPos
            endPos = self.token.endPos
            value = self.token.value
            self.advance()
            assert(isinstance(value, float))
            return FloatNode(startPos, endPos, value), None
        if self.token.type == TT_STRING:
            startPos = self.token.startPos
            endPos = self.token.endPos
            value = self.token.value
            self.advance()
            assert(isinstance(value, str))
            return StringNode(startPos, endPos, value), None
        if self.token.type == TT_POUND:
            startPos = self.token.startPos
            endPos = self.token.endPos
            self.advance()
            return InputNode(startPos, endPos), None
        if self.token.type == TT_DOLLAR:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 6")
            self.advance()
            basicExpr, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 7")
            endPos = self.token.endPos
            self.advance()
            return PrintNode(startPos, endPos, basicExpr), None
        if self.token.type == TT_PLUS:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 8")
            self.advance()
            leftNode, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 9")
            self.advance()
            rightNode, err = self.makeBasicExpr()
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 10")
            endPos = self.token.endPos
            self.advance()
            return PlusNode(startPos, endPos, leftNode, rightNode), None
        if self.token.type == TT_MINUS:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 11")
            self.advance()
            leftNode, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 12")
            self.advance()
            rightNode, err = self.makeBasicExpr()
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 13")
            endPos = self.token.endPos
            self.advance()
            return MinusNode(startPos, endPos, leftNode, rightNode), None
        if self.token.type == TT_MUL:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 14")
            self.advance()
            leftNode, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 15")
            self.advance()
            rightNode, err = self.makeBasicExpr()
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 16")
            endPos = self.token.endPos
            self.advance()
            return MulNode(startPos, endPos, leftNode, rightNode), None
        if self.token.type == TT_DIV:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 17")
            self.advance()
            leftNode, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 18")
            self.advance()
            rightNode, err = self.makeBasicExpr()
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 19")
            endPos = self.token.endPos
            self.advance()
            return DivNode(startPos, endPos, leftNode, rightNode), None
        if self.token.type == TT_MOD:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 20")
            self.advance()
            leftNode, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 21")
            self.advance()
            rightNode, err = self.makeBasicExpr()
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 22")
            endPos = self.token.endPos
            self.advance()
            return ModNode(startPos, endPos, leftNode, rightNode), None
        if self.token.type == TT_AT:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 23")
            self.advance()
            fromNode, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 24")
            self.advance()
            toNode, err = self.makeBasicExpr()
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 25")
            endPos = self.token.endPos
            self.advance()
            return RandNode(startPos, endPos, fromNode, toNode), None
        if self.token.type == TT_EQUAL:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 26")
            self.advance()
            leftNode, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 27")
            self.advance()
            rightNode, err = self.makeBasicExpr()
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 28")
            self.advance()
            exprNodes, err = self.makeExprs()
            if err:
                return Node(), err
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 29")
            endPos = self.token.endPos
            self.advance()
            return EqualNode(startPos, endPos, leftNode, rightNode, exprNodes), None
        if self.token.type == TT_LESSTHAN:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 30")
            self.advance()
            leftNode, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 31")
            self.advance()
            rightNode, err = self.makeBasicExpr()
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 32")
            self.advance()
            exprNodes, err = self.makeExprs()
            if err:
                return Node(), err
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 33")
            endPos = self.token.endPos
            self.advance()
            return LessThanNode(startPos, endPos, leftNode, rightNode, exprNodes), None
        if self.token.type == TT_GREATERTHAN:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 34")
            self.advance()
            leftNode, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 35")
            self.advance()
            rightNode, err = self.makeBasicExpr()
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 36")
            self.advance()
            exprNodes, err = self.makeExprs()
            if err:
                return Node(), err
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 37")
            endPos = self.token.endPos
            self.advance()
            return GreaterThanNode(startPos, endPos, leftNode, rightNode, exprNodes), None
        if self.token.type == TT_NOTEQUAL:
            startPos = self.token.startPos
            self.advance()
            if self.token.type != TT_LPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected '('. Error id: 38")
            self.advance()
            leftNode, err = self.makeBasicExpr()
            if err:
                return Node(), err
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 39")
            self.advance()
            rightNode, err = self.makeBasicExpr()
            if self.token.type != TT_COMMA:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ','. Error id: 40")
            self.advance()
            exprNodes, err = self.makeExprs()
            if err:
                return Node(), err
            if self.token.type != TT_RPAREN:
                return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 41")
            endPos = self.token.endPos
            self.advance()
            return NotEqualNode(startPos, endPos, leftNode, rightNode, exprNodes), None
        if self.token.type == TT_IDENTIFIER:
            varName = self.token.value
            assert(isinstance(varName, str))
            startPos = self.token.startPos
            endPos = self.token.endPos
            self.advance()
            if self.token.type == TT_LPAREN:
                self.advance()
                params = []
                if self.token.type != TT_RPAREN:
                    basicExpr, err = self.makeBasicExpr()
                    if err:
                        return Node(), err
                    params.append(basicExpr)
                    while self.token.type == TT_COMMA:
                        self.advance()
                        basicExpr, err = self.makeBasicExpr()
                        if err:
                            return Node(), err
                        params.append(basicExpr)
                if self.token.type != TT_RPAREN:
                    return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected ')'. Error id: 42")
                endPos = self.token.endPos
                self.advance()
                return CallNode(startPos, endPos, varName, params), None
            return VarAccessNode(startPos, endPos, varName), None
        return Node(), InvalidSyntaxError(self.token.startPos, self.token.endPos, "Expected valid basic expression. Error id: 43")