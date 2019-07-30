from __future__ import annotations
from typing import Tuple, Optional, NoReturn, Dict

import random

from languageParser import Node, ProgramNode, AssignNode, VarAssignNode, VarAccessNode, IntNode, FloatNode, StringNode, InputNode, PrintNode, PlusNode, MinusNode, MulNode, DivNode, ModNode, EqualNode, LessThanNode, GreaterThanNode, NotEqualNode, CallNode, RandNode
from values import Value, IntValue, FloatValue, StringValue, FunctionValue
from error import Error, RTError

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
    
    def __repr__(self) -> str:
        res = f"{self.symbolTable}"
        if self.parent:
            res += "\n" + str(self.parent)
        return res

class Interpreter:
    def __init__(self, ast: Optional[Node] = None):
        self.ast = ast
    
    def interpret(self) -> RuntimeResult:
        if not self.ast:
            return None, RTError(None, None, "No AST generated")
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
        f = FunctionValue(node.exprNodes, node.params, node.startPos, node.endPos)
        context.setVar(node.funcName, f)
        return f, None
    
    def visitVarAssignNode(self, node: VarAssignNode, context: Context) -> RuntimeResult:
        varName = node.varName
        value, err = self.visit(node.value, context)
        if value:
            context.setVar(varName, value)
        return value, err
    
    def visitVarAccessNode(self, node: VarAccessNode, context: Context) -> RuntimeResult:
        value = context.getVar(node.varName)
        if value:
            return value, None
        return None, RTError(node.startPos, node.endPos, f"Name '{node.varName}' is not defined")
    
    def visitIntNode(self, node: IntNode, context: Context) -> RuntimeResult:
        return IntValue(node.value, node.startPos, node.endPos), None
    
    def visitFloatNode(self, node: FloatNode, context: Context) -> RuntimeResult:
        return FloatValue(node.value, node.startPos, node.endPos), None
    
    def visitStringNode(self, node: StringNode, context: Context) -> RuntimeResult:
        return StringValue(node.value, node.startPos, node.endPos), None
    
    def visitInputNode(self, node: InputNode, context: Context) -> RuntimeResult:
        val = input("> ")
        if val.isdigit():
            return IntValue(int(val), node.startPos, node.endPos), None
        if val.replace(".", "", 1).isdigit():
            return FloatValue(float(val), node.startPos, node.endPos), None
        return StringValue(val, node.startPos, node.endPos), None
    
    def visitPrintNode(self, node: PrintNode, context: Context) -> RuntimeResult:
        res, err = self.visit(node.node, context)
        if err:
            return None, err
        print(res)
        return res, err
    
    def visitPlusNode(self, node: PlusNode, context: Context) -> RuntimeResult:
        left, err = self.visit(node.leftNode, context)
        if err:
            return None, err
        right, err = self.visit(node.rightNode, context)
        if err:
            return None, err
        assert(left is not None and right is not None)
        res, err = left.add(right)
        return res, err
    
    def visitMinusNode(self, node: MinusNode, context: Context) -> RuntimeResult:
        left, err = self.visit(node.leftNode, context)
        if err:
            return None, err
        right, err = self.visit(node.rightNode, context)
        if err:
            return None, err
        assert(left is not None and right is not None)
        res, err = left.sub(right)
        return res, err
    
    def visitMulNode(self, node: MulNode, context: Context) -> RuntimeResult:
        left, err = self.visit(node.leftNode, context)
        if err:
            return None, err
        right, err = self.visit(node.rightNode, context)
        if err:
            return None, err
        assert(left is not None)
        assert(right is not None)
        res, err = left.mul(right)
        return res, err
    
    def visitDivNode(self, node: DivNode, context: Context) -> RuntimeResult:
        left, err = self.visit(node.leftNode, context)
        if err:
            return None, err
        right, err = self.visit(node.rightNode, context)
        if err:
            return None, err
        assert(left is not None and right is not None)
        res, err = left.div(right)
        return res, err
    
    def visitModNode(self, node: ModNode, context: Context) -> RuntimeResult:
        left, err = self.visit(node.leftNode, context)
        if err:
            return None, err
        right, err = self.visit(node.rightNode, context)
        if err:
            return None, err
        assert(left is not None and right is not None)
        res, err = left.mod(right)
        return res, err
    
    def visitEqualNode(self, node: EqualNode, context: Context) -> RuntimeResult:
        left, err = self.visit(node.leftNode, context)
        if err:
            return None, err
        right, err = self.visit(node.rightNode, context)
        if err:
            return None, err
        assert(left is not None and right is not None)
        res = None
        if left.eq(right):
            for inst in node.exprNodes:
                res, err = self.visit(inst, context)
        return res, None
    
    def visitLessThanNode(self, node: LessThanNode, context: Context) -> RuntimeResult:
        left, err = self.visit(node.leftNode, context)
        if err:
            return None, err
        right, err = self.visit(node.rightNode, context)
        if err:
            return None, err
        assert(left is not None and right is not None)
        res = None
        if left.lt(right):
            for inst in node.exprNodes:
                res, err = self.visit(inst, context)
        return res, None
    
    def visitGreaterThanNode(self, node: GreaterThanNode, context: Context) -> RuntimeResult:
        left, err = self.visit(node.leftNode, context)
        if err:
            return None, err
        right, err = self.visit(node.rightNode, context)
        if err:
            return None, err
        assert(left is not None and right is not None)
        res = None
        if left.gt(right):
            for inst in node.exprNodes:
                res, err = self.visit(inst, context)
        return res, None
    
    def visitNotEqualNode(self, node: NotEqualNode, context: Context) -> RuntimeResult:
        left, err = self.visit(node.leftNode, context)
        if err:
            return None, err
        right, err = self.visit(node.rightNode, context)
        if err:
            return None, err
        assert(left is not None and right is not None)
        res = None
        if left.ne(right):
            for inst in node.exprNodes:
                res, err = self.visit(inst, context)
        return res, None
    
    def visitCallNode(self, node: CallNode, context: Context) -> RuntimeResult:
        res, err = None, None
        func = context.getVar(node.funcName)
        if not func:
            return None, RTError(node.startPos, node.endPos, f"Function {node.funcName} is not defined")
        params = []
        for param in node.params:
            value, err = self.visit(param, context)
            if err:
                return None, err
            params.append(value)
        res, err = func.call(params, context)
        if err:
            return None, err
        return res, None
    
    def visitRandNode(self, node: RandNode, context: Context) -> RuntimeResult:
        fromVal, err = self.visit(node.fromNode, context)
        if err:
            return None, err
        toVal, err = self.visit(node.toNode, context)
        if err:
            return None, err
        assert(isinstance(fromVal.value, int) and isinstance(toVal.value, int))
        return IntValue(random.randint(fromVal.value, toVal.value), node.startPos, node.endPos), None