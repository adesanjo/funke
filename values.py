from typing import Optional, Union

from error import Position

class Value:
    def __init__(self, value: Union[int,float, str, None] = None, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        self.value: Union[int, float, str, None] = value
        self.startPos: Optional[Position] = startPos
        self.endPos: Optional[Position] = endPos
    
    def __repr__(self) -> str:
        return str(self.value)

class IntValue(Value):
    def __init__(self, value: int = 0, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        super().__init__(value, startPos, endPos)

class FloatValue(Value):
    def __init__(self, value: float = 0.0, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        super().__init__(value, startPos, endPos)

class StringValue(Value):
    def __init__(self, value: str = "", startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        super().__init__(value, startPos, endPos)