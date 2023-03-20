# python3
# Miks Zeltiņš 13.Grupa 221RDB123


def build_heap(data):
    swaps = []
    amount = len(data)
    for i in range(amount//2, -1, -1):
        sift(amount, data, swaps, i)
    return swaps

def sift(amount, data, swaps, i):
    left_child = 2*i+1
    right_child = 2*i+2
    min_index = i

    if left_child < amount and data[min_index] > data[left_child]:
        min_index = left_child
    if right_child < amount and data[min_index] > data[right_child]:
        min_index = right_child
    if min_index != i:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append(i, min_index)
        sift(amount, data, swaps, min_index)


def main():
    data = 0
    text = input()
    if text == "I":
        n = int(input())
        data = list(map(int, input().strip().split()))

    elif text == "F":
        filename = input()
        with open("tests/"+filename, 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))

    assert len(data) == n 

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
            print(i, j)


if __name__ == "__main__":
    main()
