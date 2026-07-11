from dataclasses import dataclass

@dataclass
class TreeNode:
    pass

@dataclass
class BinOp(TreeNode):
    op: str
    left: "Int"
    right: "Int"

@dataclass
class Int(TreeNode):
    value: int

class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.next_token_index: int = 0
        """Points to the next token to be consumed."""

    def eat(self, expected_token_type: TokenType) -> Token:
        """Returns the next token if it is of the expected type.

        If the next token is not of the expected type, this raises an error.
        """
        next_token = self.tokens[self.next_token_index]
        self.next_token_index += 1
        if next_token.type != expected_token_type:
            raise RuntimeError(f"Expected {expected_token_type}, ate {next_token!r}.")
        return next_token

    def peek(self, skip: int = 0) -> TokenType | None:
        """Checks the type of an upcoming token without consuming it."""
        peek_at = self.next_token_index + skip
        return self.tokens[peek_at].type if peek_at < len(self.tokens) else None