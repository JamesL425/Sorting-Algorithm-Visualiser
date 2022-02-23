def bogo(arr: list) -> list:
    import random
    s = False

    while not s:
        random.shuffle(arr)
        s = True

        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                s = False
                break

        yield arr


def gnome(arr: list) -> list:
    gnome_pos = 0

    while gnome_pos < len(arr) - 1:
        if arr[gnome_pos] > arr[gnome_pos + 1]:
            arr[gnome_pos], arr[gnome_pos + 1] = arr[gnome_pos + 1], arr[gnome_pos]
            gnome_pos -= 1

        else:
            gnome_pos += 1

        if gnome_pos < 0:
            gnome_pos = 0

        yield arr


def cocktail(arr: list) -> list:
    start = 0
    end = len(arr)
    swap = True

    while swap:
        swap = False
        for i in range(start, end - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
                yield arr

        if not swap:
            break

        end -= 1
        swap = False

        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swap = True
                yield arr

        if not swap:
            break

        start += 1
