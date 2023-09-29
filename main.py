def max_selection_sort(seq: list[int], n: int) -> None:
    for i in range(n):
        max_val_index: int = 0
        # optimized by starting j from 1 instead of 0
        for j in range(1, n - i):
            if seq[j] > seq[max_val_index]:
                max_val_index = j
        temp = seq[n - i - 1]
        seq[n - i - 1] = seq[max_val_index]
        seq[max_val_index] = temp


def merge_sort(seq: list[int], n: int) -> list[int]:
    if n == 1:
        return seq
    middle: int = n // 2
    left: list[int] = merge_sort(seq[:middle], middle)
    right: list[int] = merge_sort(seq[middle:], n - middle)
    sorted_seq: list[int] = [0 for _ in range(n)]
    i: int = 0
    j: int = 0
    for k in range(n):
        if i < middle and j + middle >= n:
            sorted_seq[k] = left[i]
            i = i + 1
        elif i >= middle and j + middle < n:
            sorted_seq[k] = right[j]
            j = j + 1
        elif left[i] < right[j]:
            sorted_seq[k] = left[i]
            i = i + 1
        elif left[i] > right[j]:
            sorted_seq[k] = right[j]
            j = j + 1
    return sorted_seq


def main() -> None:
    k = [7, 5, 3, 2, 1]
    # max_selection_sort(k, 5)
    print(merge_sort(k, 5))


if __name__ == "__main__":
    main()
