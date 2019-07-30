from typing import Tuple, Optional

from languageLexer import Lexer
from languageParser import Parser
from languageInterpreter import Interpreter
from values import Value
from error import Error

from pprint import pprint

def run(code: str) -> Tuple[Optional[Value], Optional[Error]]:
    lexer = Lexer(code)
    tokens, err = lexer.makeTokens()
    if err:
        return None, err
    print(tokens)
    print()
    parser = Parser(tokens)
    ast, err = parser.parseTokens()
    if err:
        return None, err
    print(ast)
    interpreter = Interpreter(ast)
    res, err = interpreter.interpret()
    return res, err