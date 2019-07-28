from typing import Tuple, Optional

from languageParser import Node
from values import Value
from error import Error

class Interpreter:
    def __init__(self, ast: Node):
        pass
    
    def interpret(self) -> Tuple[Optional[Value], Optional[Error]]:
        return None, None