# compiler.py
from dataclasses import dataclass
from enum import auto, StrEnum
from typing import Any

class BytecodeType(StrEnum):
    BINOP = auto()
    PUSH = auto()

@dataclass
class Bytecode:
    type: BytecodeType
    value: Any = None

class Compiler:
    def __init__(self, tree: BinOp) -> None:
        self.tree = tree

    def compile(self) -> Generator[Bytecode, None, None]:
        left = self.tree.left
        yield Bytecode(BytecodeType.PUSH, left.value)

        right = self.tree.right
        yield Bytecode(BytecodeType.PUSH, right.value)

        yield Bytecode(BytecodeType.BINOP, self.tree.op)
        