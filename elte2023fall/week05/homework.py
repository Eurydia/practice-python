# Task 5.1
def read_int(prompt: str, lower: int, upper: int) -> None:
    valid_input: bool = False

    while not valid_input:
        try:
            v: int = int(input(prompt))

            if v < lower or v > upper:
                print(
                    f"Error: the value is not within permitted range ({lower}..{upper})"
                )
                continue

            print(f"The value is {v}")

        except ValueError:
            print("Error: wrong input")
            continue


# task 5.2
class Stack:
    def __init__(self):
        self._stk = []

    def push(self, val):
        self._stk.append(val)

    def pop(self):
        val = self._stk[-1]
        del self._stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self) -> None:
        super().__init__()
        self._size: int = 0
        self._max_remembered_size: int = 0

    def get_counter(self) -> int:
        return self._size

    def push(self, val) -> None:
        if self._max_remembered_size > self._size:
            self._stk[self._size] = val
            self._size += 1
            return

        self._stk.append(val)
        self._max_remembered_size += 1

    def pop(self) -> object | None:
        if self._size < 1:
            return None

        v: object = self._stk[self._size - 1]
        self._size -= 1
        return v


# Task 5.3
class QueueFullException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Queue:
    def __init__(self, size: int):
        self._size: int = size
        self._items: list[object] = [None for _ in range(size)]
        self._curr_size: int = 0

    def put(self, item) -> None:
        if self._size > self._curr_size:
            self._items[self._curr_size] = item
            self._curr_size += 1
            return

        raise QueueFullException("Queue is full")

    def get(self) -> object:
        if self._curr_size < 1:
            print("Queue empty")
            return None

        v: object = self._items[0]

        for i in range(self._curr_size - 1):
            self._items[i] = self._items[i + 1]

        self._curr_size -= 1
        self._items[self._curr_size] = None
        return v


def main() -> None:
    # read_int("enter number", -10, 10)

    # stk: CountingStack = CountingStack()
    # for _ in range(100):
    #     stk.push(1)
    # for _ in range(100):
    #     stk.pop()
    # print(stk.get_counter())

    q: Queue = Queue(10)
    for i in range(10):
        q.put(i)


if __name__ == "__main__":
    main()
