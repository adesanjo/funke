from typing import Tuple, Optional

from languageLexer import Lexer
from languageParser import Parser
from languageInterpreter import Interpreter
from values import Value
from error import Error, RTError

from pprint import pprint

DEBUG = True

def run(code: str) -> Tuple[Optional[Value], Optional[Error]]:
    lexer = Lexer(code)
    tokens, err = lexer.makeTokens()
    if err:
        return None, err
    if DEBUG:
        print("Tokens:")
        print(tokens)
        print()
    parser = Parser(tokens)
    ast, err = parser.parseTokens()
    if err:
        return None, err
    if DEBUG:
        print("AST:")
        print(ast)
        print()
    interpreter = Interpreter(ast)
    res, err = interpreter.interpret()
    if err:
        return None, err
    return res, None