from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any
from string import digits

class TokenType(StrEnum):
    INT = auto()
    PLUS = auto()
    MINUS = auto()
    EOF = auto()

    def __repr__(self):
        return f"TokenType.{self.name}"

@dataclass
class Token:
    type: TokenType
    value: Any = None

    def __repr__(self):
        return f"Token({self.type}) {self.value!r}" if self.value is not None else f"Token({self.type})"


"""
we want to be able to turn a string like

"3 + 5" into the stream [Token(INT, 3), Token(PLUS), Token(INT, 5), Token(EOF)];
"6 - 3" into the stream [Token(INT, 6), Token(MINUS), Token(INT, 3), Token(EOF)]; and
"1 + 2 + 3 + 4 - 5 - 6 + 7 - 8" into the stream [Token(INT, 1), Token(PLUS), Token(INT, 2), Token(PLUS), Token(INT, 3), Token(PLUS), Token(INT, 4), Token(MINUS), Token(INT, 5), Token(MINUS), Token(INT, 6), Token(PLUS), Token(INT, 7), Token(MINUS), Token(INT, 8), Token(EOF)].
"""
class Tokenizer:
    def __init__(self, code: str) -> None:
        self.code = code
        self.ptr: int = 0

    def next_token(self) -> Token:
        while self.ptr < len(self.code) and self.code[self.ptr] == " ":
            self.ptr += 1

        if self.ptr == len(self.code):
            return Token(TokenType.EOF)

        char = self.code[self.ptr]
        self.ptr += 1
        if char == "+":
            return Token(TokenType.PLUS)
        elif char == "-":
            return Token(TokenType.MINUS)
        elif char in digits:
            return Token(TokenType.INT, int(char))
        else:
            raise RuntimeError(f"Can't tokenize {char!r}.")

    def __iter__(self) -> Generator[Token, None, None]:
        while (token := self.next_token()).type != TokenType.EOF:
            yield token
        yield token  # Yield the EOF token too.