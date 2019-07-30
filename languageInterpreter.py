from __future__ import annotations
from typing import Tuple, Optional, NoReturn, Dict

from languageParser import Node, ProgramNode, AssignNode, VarAssignNode, VarAccessNode, IntNode, FloatNode, StringNode, InputNode, PrintNode, PlusNode, MinusNode, MulNode, DivNode, ModNode, EqualNode, LessThanNode, GreaterThanNode, NotEqualNode, CallNode, RandNode
from values import Value
from error import Error

RuntimeResult = Tuple[Optional[Value], Optional[Error]]

class Context:
    def __init__(self, symbolTable: Optional[Dict[str, Value]] = None, parent: Optional[Context] = None):
        if symbolTable is not None:
            self.symbolTable: Dict[str, Value] = symbolTable
        else:
            self.symbolTable: Dict[str, Value] = {}
        self.parent: Optional[Context] = parent
    
    def getVar(self, varName: str) -> Optional[Value]:
        if varName in self.symbolTable:
            return self.symbolTable[varName]
        if self.parent:
            return self.parent.getVar(varName)
        return None
    
    def setVar(self, varName: str, value: Value):
        self.symbolTable[varName] = value

class Interpreter:
    def __init__(self, ast: Node):
        self.ast = ast
    
    def interpret(self) -> RuntimeResult:
        return self.visit(self.ast, Context())
    
    def visit(self, node: Node, context: Context) -> RuntimeResult:
        methodName = f"visit{type(node).__name__}"
        method = getattr(self, methodName, self.noVisitMethod)
        return method(node, context)

    def noVisitMethod(self, node, context) -> NoReturn:
        raise Exception(f"No visit{type(node).__name__} method defined")
    
    def visitProgramNode(self, node: ProgramNode, context: Context) -> RuntimeResult:
        res, err = None, None
        for inst in node.nodes:
            res, err = self.visit(inst, context)
        return res, err
    
    def visitAssignNode(self, node: AssignNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitVarAssignNode(self, node: VarAssignNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitVarAccessNode(self, node: VarAccessNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitIntNode(self, node: IntNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitFloatNode(self, node: FloatNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitStringNode(self, node: StringNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitInputNode(self, node: InputNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitPrintNode(self, node: PrintNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitPlusNode(self, node: PlusNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitMinusNode(self, node: MinusNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitMulNode(self, node: MulNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitDivNode(self, node: DivNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitModNode(self, node: ModNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitEqualNode(self, node: EqualNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitLessThanNode(self, node: LessThanNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitGreaterThanNode(self, node: GreaterThanNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitNotEqualNode(self, node: NotEqualNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitCallNode(self, node: CallNode, context: Context) -> RuntimeResult:
        return None, None
    
    def visitRandNode(self, node: RandNode, context: Context) -> RuntimeResult:
        return None, None