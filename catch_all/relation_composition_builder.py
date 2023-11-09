from typing import Tuple, TypeAlias, Set

BinaryRelation: TypeAlias = Set[Tuple[int, int]]


def compose_binary_relation(
    relations: Tuple[BinaryRelation, BinaryRelation]
) -> Tuple[BinaryRelation, BinaryRelation]:
    R, S = relations

    S_composition_R: BinaryRelation = set()
    R_composition_S: BinaryRelation = set()
    for ra, rb in R:
        for sa, sb in S:
            if rb == sa:
                S_composition_R.add((ra, sb))

    for sa, sb in S:
        for ra, rb in R:
            if sb == ra:
                R_composition_S.add((sa, rb))

    return (S_composition_R, R_composition_S)


def main() -> None:
    # Configure binary relations here :)
    R: BinaryRelation = {(1, 2), (2, 3), (3, 4)}
    S: BinaryRelation = {(1, 5), (2, 7), (4, 6)}

    # Results of composition
    S_composition_R, R_composition_S = compose_binary_relation((R, S))

    # Also prints out the word 'empty set' instead of set.__repr__
    print(f"S composition R: {S_composition_R or 'empty set'}")
    print(f"R composition S: {R_composition_S or 'empty set'}")


if __name__ == "__main__":
    main()
