from __future__ import annotations

from typing import Optional

class Position:
    def __init__(self, idx: int, line: int, column: int, code: str):
        self.idx: int = idx
        self.line: int = line
        self.column: int = column
        self.code: str = code
    
    def advance(self, char: Optional[str] = None) -> Position:
        self.idx += 1
        self.column += 1
        if char == "\n":
            self.line += 1
            self.column = 0
        return self
    
    def copy(self) -> Position:
        return Position(self.idx, self.line, self.column, self.code)

class Error:
    def __init__(self, startPos: Position, endPos: Position, _type: str, msg: str):
        self.startPos: Position = startPos
        self.endPos: Position = endPos
        self.type: str = _type
        self.msg: str = msg
    
    def stringWithArrows(self) -> str:
        result = ""
        text = self.startPos.code
        
        # Calculate indices
        idxStart = max(text.rfind("\n", 0, self.startPos.idx), 0)
        idxEnd = text.find("\n", idxStart + 1)
        if idxEnd < 0:
            idxEnd = len(text)
        
        # Generate each line
        lineCount = self.endPos.line - self.startPos.line + 1
        for i in range(lineCount):
            # Calculate line columns
            line = text[idxStart:idxEnd]
            colStart = self.startPos.column if i == 0 else 0
            colEnd = self.endPos.column if i == lineCount - 1 else len(line) - 1
            
            # Append to result
            result += line + "\n"
            result += " " * colStart + "^" * (colEnd - colStart)
            
            # Re-calculate indices
            idxStart = idxEnd
            idxEnd = text.find("\n", idxStart + 1)
            if idxEnd < 0:
                idxEnd = len(text)
        
        return result.replace("\t", "")
    
    def __repr__(self) -> str:
        res = f"{self.type}: {self.msg}\n"
        res += f"Line {self.startPos.line + 1}\n\n"
        res += self.stringWithArrows()
        return res + "\n"

class IllegalCharacterError(Error):
    def __init__(self, charPos: Position, char: str):
        super().__init__(charPos.copy(), charPos.advance(), "IllegalCharacterError", char)