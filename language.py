from typing import Tuple, Optional

from languageLexer import Lexer
from languageParser import Parser
from languageInterpreter import Interpreter
from values import Value
from error import Error

def run(filename: str, code: str) -> Tuple[Optional[Value], Optional[Error]]:
    lexer = Lexer(filename, code)
    tokens = lexer.makeTokens()
    parser = Parser(tokens)
    ast = parser.parseTokens()
    interpreter = Interpreter(ast)
    res, err = interpreter.interpret()
    return res, err