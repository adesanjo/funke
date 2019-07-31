from __future__ import annotations
from typing import Optional, Union, Tuple, List

from error import Position, RTError, Error
from languageParser import Node
import languageInterpreter as li

class Value:
    def __init__(self, value: Union[int,float, str, None, List[Node]] = None, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        self.value: Union[int, float, str, None, List[Node]] = value
        self.startPos: Optional[Position] = startPos
        self.endPos: Optional[Position] = endPos
    
    def add(self, other: Value) -> Tuple[Optional[Value], Optional[Error]]:
        return None, RTError(self.startPos, other.endPos, f"Addition not implemented for {self} and {other}")
    
    def sub(self, other: Value) -> Tuple[Optional[Value], Optional[Error]]:
        return None, RTError(self.startPos, other.endPos, f"Subtraction not implemented for {self} and {other}")
    
    def mul(self, other: Value) -> Tuple[Optional[Value], Optional[Error]]:
        return None, RTError(self.startPos, other.endPos, f"Multiplication not implemented for {self} and {other}")
    
    def div(self, other: Value) -> Tuple[Optional[Value], Optional[Error]]:
        return None, RTError(self.startPos, other.endPos, f"Division not implemented for {self} and {other}")
    
    def mod(self, other: Value) -> Tuple[Optional[Value], Optional[Error]]:
        return None, RTError(self.startPos, other.endPos, f"Modulo not implemented for {self} and {other}")
    
    def eq(self, other: Value) -> bool:
        return type(self).__name__ == type(other).__name__ and self.value == other.value
    
    def lt(self, other: Value) -> bool:
        if self.value is None or other.value is None:
            return False
        if isinstance(self.value, int) and isinstance(other.value, int):
            return self.value < other.value
        if isinstance(self.value, float) and isinstance(other.value, float):
            return self.value < other.value
        if isinstance(self.value, str) and isinstance(other.value, str):
            return self.value < other.value
        return False
    
    def gt(self, other: Value) -> bool:
        if self.value is None or other.value is None:
            return False
        if isinstance(self.value, int) and isinstance(other.value, int):
            return self.value > other.value
        if isinstance(self.value, float) and isinstance(other.value, float):
            return self.value > other.value
        if isinstance(self.value, str) and isinstance(other.value, str):
            return self.value > other.value
        return False
    
    def ne(self, other: Value) -> bool:
        return type(self).__name__ != type(other).__name__ or self.value != other.value
    
    def call(self, params: List[Value], context: li.Context) -> Tuple[Optional[Value], Optional[Error]]:
        return None, RTError(self.startPos, self.endPos, f"Call not implemented for {self}")
    
    def __repr__(self) -> str:
        return repr(self.value)
    
    def __str__(self) -> str:
        return str(self.value)

class IntValue(Value):
    def __init__(self, value: int = 0, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        super().__init__(value, startPos, endPos)
    
    def add(self, other: IntValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, int) and isinstance(other.value, int))
        return IntValue(self.value + other.value), None
    
    def sub(self, other: IntValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, int) and isinstance(other.value, int))
        return IntValue(self.value - other.value), None
    
    def mul(self, other: IntValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, int) and isinstance(other.value, int))
        return IntValue(self.value * other.value), None
    
    def div(self, other: IntValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, int) and isinstance(other.value, int))
        if other.value == 0:
            return None, RTError(self.startPos, other.endPos, "Division by zero")
        return IntValue(self.value // other.value), None
    
    def mod(self, other: IntValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, int) and isinstance(other.value, int))
        if other.value == 0:
            return None, RTError(self.startPos, other.endPos, "Modulo by zero")
        return IntValue(self.value % other.value), None

class FloatValue(Value):
    def __init__(self, value: float = 0.0, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        super().__init__(value, startPos, endPos)
    
    def add(self, other: FloatValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, float) and isinstance(other.value, float))
        return FloatValue(self.value + other.value), None
    
    def sub(self, other: FloatValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, float) and isinstance(other.value, float))
        return FloatValue(self.value - other.value), None
    
    def mul(self, other: FloatValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, float) and isinstance(other.value, float))
        return FloatValue(self.value * other.value), None
    
    def div(self, other: FloatValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, float) and isinstance(other.value, float))
        if other.value == 0.0:
            return None, RTError(self.startPos, other.endPos, "Division by zero")
        return FloatValue(self.value / other.value), None
    
    def mod(self, other: FloatValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, float) and isinstance(other.value, float))
        if other.value == 0.0:
            return None, RTError(self.startPos, other.endPos, "Modulo by zero")
        return FloatValue(self.value % other.value), None

class StringValue(Value):
    def __init__(self, value: str = "", startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        super().__init__(value, startPos, endPos)
    
    def add(self, other: StringValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, str) and isinstance(other.value, str))
        return StringValue(self.value + other.value), None
    
    def mul(self, other: IntValue) -> Tuple[Optional[Value], Optional[Error]]:
        assert(isinstance(self.value, str) and isinstance(other.value, int))
        return StringValue(self.value * other.value), None

class FunctionValue(Value):
    def __init__(self, value: List[Node], paramNames: List[str], startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        super().__init__(value, startPos, endPos)
        self.paramNames: List[str] = paramNames
    
    def call(self, params: List[Value], context: li.Context) -> Tuple[Optional[Value], Optional[Error]]:
        for i in range(len(self.paramNames)):
            context.setVar(self.paramNames[i], params[i])
        interpreter = li.Interpreter()
        assert(isinstance(self.value, list) and len(self.value) > 0 and isinstance(self.value[0], Node))
        res = None
        for node in self.value:
            result, err = interpreter.visit(node, context)
            if err:
                return None, err
            if result is not None:
                res = result
        return res, None