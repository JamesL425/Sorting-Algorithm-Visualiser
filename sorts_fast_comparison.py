def join(left_half, right_half):
    if len(left_half) == 1 and len(right_half) == 1:
        if left_half[0] > right_half[0]:
            return [right_half[0], left_half[0]]

        else:
            return [left_half[0], right_half[0]]

    out_arr = []
    i, j = 0, 0

    while i <= len(left_half) - 1 or j <= len(right_half) - 1:
        if i >= len(left_half):
            out_arr.append(right_half[j])
            j += 1
            continue

        if j >= len(right_half):
            out_arr.append(left_half[i])
            i += 1
            continue

        if left_half[i] < right_half[j]:
            out_arr.append(left_half[i])
            i += 1
        else:
            out_arr.append(right_half[j])
            j += 1

    return out_arr


def listify(arr):
    out_arr = []
    l = False
    for i in arr:
        if isinstance(i, list):
            l = True

    if not l:
        return arr

    for i in arr:
        out_arr.extend(i)

    return out_arr


def merge(arr: list) -> list:
    all_list = [[item] for item in arr]

    yield listify(all_list)

    while len(all_list) > 1:
        l1 = all_list.pop(0)
        l2 = all_list.pop(0)

        all_list.append(join(l1, l2))
        yield listify(all_list)
