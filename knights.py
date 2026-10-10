from logic import *

# Puzzle 0: A says, "I am both a knight and a knave."
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

statement = And(AKnight, AKnave)

knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, statement),
    Implication(AKnave, Not(statement))
)

print("Puzzle 0")
for symbol in (AKnight, AKnave):
    if model_check(knowledge0, symbol):
        print(symbol)

# Puzzle 1: A says, "We are both knaves." B says nothing.
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

statement1 = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, statement1),
    Implication(AKnave, Not(statement1))
)

print("\nPuzzle 1")
for symbol in (AKnight, AKnave, BKnight, BKnave):
    if model_check(knowledge1, symbol):
        print(symbol)

# Puzzle 2: A says "We are the same kind."
# B says "We are of different kinds."
same_kind = Or(And(AKnight, BKnight), And(AKnave, BKnave))
different_kind = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, same_kind),
    Implication(AKnave, Not(same_kind)),
    Implication(BKnight, different_kind),
    Implication(BKnave, Not(different_kind))
)

print("\nPuzzle 2")
for symbol in (AKnight, AKnave, BKnight, BKnave):
    if model_check(knowledge2, symbol):
        print(symbol)

# Puzzle 3 (Bonus): A said one of two possible statements.
# A said "I am a knight" iff ASaidKnight is true.
ASaidKnight = Symbol("A said 'I am a knight'")
ASaidKnave = Symbol("A said 'I am a knave'")
CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledge3 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave), Not(And(CKnight, CKnave)),
    Or(ASaidKnight, ASaidKnave), Not(And(ASaidKnight, ASaidKnave)),
    # A's actual utterance must match A's truthfulness.
    Implication(ASaidKnight, Implication(AKnight, AKnight)),
    Implication(ASaidKnight, Implication(AKnave, Not(AKnight))),
    Implication(ASaidKnave, Implication(AKnight, AKnave)),
    Implication(ASaidKnave, Implication(AKnave, Not(AKnave))),
    # B makes two separate claims, both subject to B's truthfulness.
    Implication(BKnight, ASaidKnave),
    Implication(BKnave, Not(ASaidKnave)),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    # C says A is a knight.
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)

print("\nPuzzle 3 (Bonus)")
for symbol in (AKnight, AKnave, BKnight, BKnave, CKnight, CKnave):
    if model_check(knowledge3, symbol):
        print(symbol)
print("A's statement:")
for symbol in (ASaidKnight, ASaidKnave):
    if model_check(knowledge3, symbol):
        print(symbol)
