from typing import List

#from tokens import *

class Position:
    def __init__(self, filename: str, line: int, column: int, characterPos: int):
        self.filename = filename
        self.line = line
        self.column = column
        self.characterPos = characterPos

class Token:
    def __init__(self, _type: str, value: str):
        self.type = _type
        self.value = value

class Lexer:
    def __init__(self, filename: str, code: str):
        pass
    
    def makeTokens(self) -> List[Token]:
        return []