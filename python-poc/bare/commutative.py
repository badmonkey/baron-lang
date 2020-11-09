from enum import Enum, unique

from .statement import Expression


class CommutativeExpr(Expression):
    """
    for ops: + * band bor bxor
    """

    @unique
    class Op(Enum):
        ARITH_SUM = 1
        ARITH_MULT = 2
        BIN_AND = 3
        BIN_OR = 4
        BIN_XOR = 5
