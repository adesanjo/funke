from typing import Optional, Union

from error import Position

class Value:
    def __init__(self, startPos: Optional[Position] = None, endPos: Optional[Position] = None, value: Union[int,float, str, None] = None):
        self.startPos: Optional[Position] = startPos
        self.endPos: Optional[Position] = endPos
        self.value: Union[int, float, str, None] = value
    
    def __repr__(self) -> str:
        return str(self.value)

class IntValue(Value):
    def __init__(self, startPos: Optional[Position] = None, endPos: Optional[Position] = None, value: int = 0):
        super().__init__(startPos, endPos, value)