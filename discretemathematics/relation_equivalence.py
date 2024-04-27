from typing import Tuple, TypeAlias, Set, List

from itertools import product

BinaryRelation: TypeAlias = Set[Tuple[int, int]]
UnderlyingSet: TypeAlias = Set[int]


def isReflexive(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x in X:
        if (x, x) not in R:
            return False

    return True


def isSymmetric(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x, y in R:
        if (y, x) not in R:
            return False
    return True


def isTransitive(X: UnderlyingSet, R: BinaryRelation) -> bool:
    for x, y in R:
        for z in X:
            if (x, y) in R and (y, z) in R and (x, z) not in R:
                return False

    return True


def isEquivalence(X: UnderlyingSet, R: BinaryRelation) -> bool:
    return isReflexive(X, R) and isSymmetric(X, R) and isTransitive(X, R)


def getPartition(X: UnderlyingSet, R: BinaryRelation) -> List[Set[int]]:
    partition: List[Set[int]] = []
    for x, y in product(X, X):
        if (x, y) in R:
            for subset in partition:
                if x in subset:
                    subset.add(y)
                    break
            else:
                partition.append({x, y})
    return partition


def main() -> None:
    # Configure binary relations here :)

    A: UnderlyingSet = {1, 2, 3, 4, 5}
    R: BinaryRelation = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (1, 2), (2, 1)}
    # R: BinaryRelation = {(1, 3), (2, 4), (5, 5)}

    print(f"Equivalence: {isEquivalence(A, R)}")

    if isEquivalence(A, R):
        print(f"Partition: {getPartition(A, R)}")


if __name__ == "__main__":
    main()
