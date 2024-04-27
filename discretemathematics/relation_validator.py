from typing import Tuple, TypeAlias, Set

from itertools import product

BinaryRelation: TypeAlias = Set[Tuple[int, int]]
UnderlyingSet: TypeAlias = Set[int]


def isReflexive(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x in X:
        if (x, x) not in R:
            return False

    return True


def isIrreflexive(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x in X:
        if (x, x) in R:
            return False
    return True


def isSymmetric(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x, y in R:
        if (y, x) not in R:
            return False
    return True


def isAsymmetric(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x, y in R:
        if (y, x) in R and x != y:
            return False
    return True


def isStrictAntisymmetric(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x, y in R:
        if (y, x) in R:
            return False
    return True


def isDichotomous(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x, y in product(X, X):
        if (x, y) not in R and (y, x) not in R:
            return False

    return True


def isTrichotomous(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x, y in product(X, X):
        if (x, y) not in R and (y, x) not in R and x != y:
            return False

    return True


def isTransitive(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x, y in R:
        for z in X:
            if (x, y) in R and (y, z) in R and (x, z) not in R:
                return False

    return True


def main() -> None:
    # Configure binary relations here :)

    A: UnderlyingSet = {1, 2, 3, 4, 5}
    # R: BinaryRelation = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)}
    R: BinaryRelation = {(1, 3), (2, 4), (5, 5)}

    print(f"Reflexive: {isReflexive(A, R)}")
    print(f"Irreflexive: {isIrreflexive(A, R)}")
    print(f"Symmetric: {isSymmetric(A, R)}")
    print(f"Asymmetric: {isAsymmetric(A, R)}")
    print(f"Strict Antisymmetric: {isStrictAntisymmetric(A, R)}")
    print(f"Dichotomous: {isDichotomous(A, R)}")
    print(f"Trichotomous: {isTrichotomous(A, R)}")
    print(f"Transitive: {isTransitive(A, R)}")


if __name__ == "__main__":
    main()
