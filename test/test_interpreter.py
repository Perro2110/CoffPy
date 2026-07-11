from src.coffpy.tokenizer import Tokenizer
from src.coffpy.parser import Parser
from src.coffpy.compiler import Compiler
from src.coffpy.interpreter import Interpreter

import pytest

@pytest.mark.parametrize(
    ["code", "result"],
    [
        ("3 + 5", 8),
        ("5 - 2", 3),
        ("1 + 2", 3),
        ("1 - 9", -8),
    ],
)
def test_simple_arithmetic(code: str, result: int):
    tokens = list(Tokenizer(code))
    tree = Parser(tokens).parse()
    bytecode = list(Compiler(tree).compile())
    interpreter = Interpreter(bytecode)
    interpreter.interpret()
    assert interpreter.stack.pop() == result