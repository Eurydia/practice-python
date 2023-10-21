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
        i: int = p_idx

        while i > 0 and xs[i - 1] > xs[i]:
            temp = xs[i]
            xs[i] = xs[i - 1]
            xs[i - 1] = temp
            i -= 1


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
        sm_idx: int = offset
        for i in range(offset + 1, size):
            if xs[sm_idx] > xs[i]:
                sm_idx = i
        temp = xs[offset]
        xs[offset] = xs[sm_idx]
        xs[sm_idx] = temp


def heapsort_construct(
    xs: list[int], size: int, parent_index: int
) -> None:
    while (2 * parent_index) + 1 < size:
        left_child_index: int = (2 * parent_index) + 1
        target_child: int = left_child_index

        if (left_child_index + 1 < size) and (
            xs[left_child_index] < xs[left_child_index + 1]
        ):
            target_child += 1

        if xs[parent_index] >= xs[target_child]:
            return

        temp: int = xs[parent_index]
        xs[parent_index] = xs[target_child]
        xs[target_child] = temp

        parent_index = target_child


def heapsort_init_heap(xs: list[int], size: int) -> None:
    for i in reversed(range(size)):
        heapsort_construct(xs, size, i)


def heapsort(xs: list[int], size: int) -> None:
    heapsort_init_heap(xs, size)

    for i in reversed(range(1, size)):
        temp = xs[0]
        xs[0] = xs[i]
        xs[i] = temp

        heapsort_construct(xs, i, 0)


def main() -> None:
    k = [
        12,
        3,
        7,
        17,
        5,
        2,
        1,
        6,
        11,
        14,
        15,
        9,
        18,
        4,
        16,
        13,
        20,
        19,
        10,
        8,
    ]
    # max_selection_sort(k, 5)
    # print(merge_sort(k, 5))
    # bubble_sort(k, 5)

    # top_down_merge_sort(k, 6)
    # insertion_sort(k, 6)
    # heapsort(k, 20)
    selection_sort(k, 20)

    print(k)


if __name__ == "__main__":
    main()
