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


def bubble_sort(xs: list[int], size: int) -> None:
    for working_region_offset in range(size - 1):
        for k in range(size - working_region_offset - 1):
            a: int = xs[k]
            b: int = xs[k + 1]
            if a > b:
                xs[k] = b
                xs[k + 1] = a


def insertion_sort(xs: list[int], size: int) -> None:
    for p_idx in range(1, size):
        p_val: int = xs[p_idx]

        i: int = p_idx

        while i > 0 and xs[i - 1] > p_val:
            xs[i] = xs[i - 1]
            i -= 1
        xs[i] = p_val


def __top_down_merge_sort(
    xs: list[int], start_index: int, end_index: int
) -> None:
    if end_index - start_index == 0:
        return

    # if end_index - start_index == 1:
    #     l: int = xs[start_index]
    #     r: int = xs[end_index]
    #     if l > r:
    #         xs[start_index] = r
    #         xs[end_index] = l
    #         return
    #     return

    middle_index: int = (start_index + end_index) // 2

    __top_down_merge_sort(
        xs,
        start_index,
        middle_index,
    )

    __top_down_merge_sort(
        xs,
        middle_index + 1,
        end_index,
    )

    l_ptr: int = start_index
    r_ptr: int = middle_index + 1
    aux: list[int] = []

    while l_ptr <= middle_index and r_ptr <= end_index:
        if xs[l_ptr] > xs[r_ptr]:
            aux.append(xs[r_ptr])
            r_ptr += 1
            continue
        aux.append(xs[l_ptr])
        l_ptr += 1

    while l_ptr <= middle_index:
        aux.append(xs[l_ptr])
        l_ptr += 1

    while r_ptr <= end_index:
        aux.append(xs[r_ptr])
        r_ptr += 1

    for i, a in enumerate(aux, start=start_index):
        xs[i] = a


def top_down_merge_sort(xs: list[int], size: int) -> None:
    __top_down_merge_sort(xs, 0, size - 1)


def selection_sort(xs: list[int], size: int) -> None:
    for offset in range(size - 1):
        sm_val: int = xs[offset]
        sm_idx: int = offset
        for i in range(offset + 1, size):
            if sm_val > xs[i]:
                sm_val = xs[i]
                sm_idx = i
        temp = xs[offset]
        xs[offset] = sm_val
        xs[sm_idx] = temp


def main() -> None:
    k = [7, 5, 3, 2, 1, 17]
    # max_selection_sort(k, 5)
    # print(merge_sort(k, 5))
    # bubble_sort(k, 5)

    # top_down_merge_sort(k, 6)
    insertion_sort(k, 6)

    print(k)


if __name__ == "__main__":
    main()
