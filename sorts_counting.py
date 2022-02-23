def counting(arr: list) -> list:
    out = [0 for x in range(len(arr))]
    counts = [0 for x in range(max(arr) + 1)]

    yield out

    for i in arr:
        counts[i] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    for item in arr:
        out[counts[item] - 1] = item
        counts[item] -= 1

        yield out


def count_radix(arr: list, idx: int) -> list:
    out = [0 for x in range(len(arr))]
    counts = [0 for x in range(10)]  # 0 to 10

    for i in arr:
        amount_of = i // 10 ** idx
        counts[amount_of % 10] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        amount_of = arr[i] // 10 ** idx
        dig = amount_of % 10
        out[counts[dig] - 1] = arr[i]
        counts[dig] -= 1

    return out


def radix(arr: list) -> list:
    m = max(arr)
    max_len = len(str(m))

    for idx in range(max_len):
        arr = count_radix(arr, idx)
        yield arr
