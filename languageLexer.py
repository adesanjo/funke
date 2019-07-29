from typing import List, Optional, Union, Tuple

import string

from tokens import *
from error import Position, Error, IllegalCharacterError

DIGITS = "1234567890"
LETTERS = string.ascii_letters + "_"
LETTERS_DIGITS = LETTERS + DIGITS

class Token:
    def __init__(self, _type: str, value: Union[str, int, float, None], startPos: Position, endPos: Optional[Position] = None):
        self.type: str = _type
        self.value: Union[str, int, float, None] = value
        self.startPos: Position = startPos.copy()
        if endPos:
            self.endPos: Position = endPos.copy()
        else:
            self.endPos: Position = startPos.copy()
    
    def __repr__(self) -> str:
        if self.value is not None:
            return f"{self.type}: {self.value}"
        return f"{self.type}"

class Lexer:
    def __init__(self, code: str):
        self.code: str = code
        self.pos: Position = Position(-1, 0, -1, self.code)
        self.char: Optional[str] = None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.char)
        if self.pos.idx < len(self.code):
            self.char = self.code[self.pos.idx]
        else:
            self.char = None
    
    def makeTokens(self) -> Tuple[List[Token], Optional[Error]]:
        tokens = []
        
        while self.char is not None:
            if self.char in " \n\r\t":
                self.advance()
            elif self.char in DIGITS:
                tokens.append(self.makeNumber())
            elif self.char in LETTERS:
                tokens.append(self.makeIdentifier())
            elif self.char == "\"":
                tokens.append(self.makeString())
            elif self.char == "=":
                tokens.append(Token(TT_EQUAL, None, self.pos))
                self.advance()
            elif self.char == "(":
                tokens.append(Token(TT_LPAREN, None, self.pos))
                self.advance()
            elif self.char == ")":
                tokens.append(Token(TT_RPAREN, None, self.pos))
                self.advance()
            elif self.char == ",":
                tokens.append(Token(TT_COMMA, None, self.pos))
                self.advance()
            elif self.char == "+":
                tokens.append(Token(TT_COMMA, None, self.pos))
                self.advance()
            elif self.char == "-":
                tokens.append(Token(TT_COMMA, None, self.pos))
                self.advance()
            else:
                return [], IllegalCharacterError(self.pos, f"'{self.char}'")
        
        tokens.append(Token(TT_EOF, None, self.pos))
        return tokens, None
    
    def makeNumber(self) -> Token:
        numStr = ""
        hasDot = False
        startPos = self.pos.copy()
        
        while self.char is not None and self.char in DIGITS + "_.":
            if self.char == ".":
                if hasDot:
                    break
                hasDot = True
            if self.char != "_":
                numStr += self.char
            self.advance()

        if hasDot:
            return Token(TT_FLOAT, float(numStr), startPos, self.pos)
        return Token(TT_INT, int(numStr), startPos, self.pos)

    def makeIdentifier(self) -> Token:
        idStr = ""
        startPos = self.pos.copy()

        while self.char is not None and self.char in LETTERS_DIGITS:
            idStr += self.char
            self.advance()

        return Token(TT_IDENTIFIER, idStr, startPos, self.pos)
    
    def makeString(self) -> Token:
        string = ""
        startPos = self.pos.copy()
        
        escapeChars = {
            "n": "\n",
            "t": "\t",
            "r": "\r"
        }
        
        self.advance()
        while self.char is not None and self.char != "\"":
            if self.char == "\\":
                self.advance()
                if self.char in escapeChars:
                    string += escapeChars[self.char]
                elif self.char == "x":
                    self.advance()
                    a = self.char
                    self.advance()
                    b = self.char
                    if a in DIGITS + "abcdef" and b in DIGITS + "abcdef":
                        string += chr(int(a + b, 16))
                    else:
                        string += "?"
                else:
                    string += self.char
            else:
                string += self.char
            self.advance()
        self.advance()
        
        return Token(TT_STRING, string, startPos, self.pos)