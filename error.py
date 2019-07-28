from typing import Optional

from languageLexer import Position

class Error:
    def __init__(self, _type: str, msg: str, startPos: Optional[Position] = None, endPos: Optional[Position] = None):
        self.type = _type
        self.msg = msg
        self.startPos = startPos
        self.endPos = endPos
    
    def __repr__(self) -> str:
        return f"{self.type} in file {self.startPos.filename if self.startPos else '<undefined>'} line {self.startPos.line if self.startPos else '<undefined>'}: {self.msg}"