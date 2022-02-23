def selection(arr: list) -> list:
    for i in range(len(arr) - 1):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr


def insertion(arr: list) -> list:
    for i in range(1, len(arr)):
        comp = arr[i]
        pointer = i - 1

        while pointer >= 0 and comp < arr[pointer]:
            arr[pointer + 1] = arr[pointer]
            pointer -= 1

            yield arr

        arr[pointer + 1] = comp
        yield arr


def bubble(arr: list) -> list:
    n = len(arr)
    for i in range(n - 1):
        swap = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True

                yield arr

        if not swap:
            break
