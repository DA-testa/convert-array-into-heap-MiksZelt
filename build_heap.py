# python3
# Miks Zeltiņš 13.Grupa 221RDB123


def build_heap(data):
    swaps = []
    amount = len(data)
    for i in range(amount//2, -1, -1):
        sift(amount, data, swaps, i)
    return swaps

def sift(amount, data, swaps, i):
    min_index = i
    left_child = 2*i+1
    right_child = 2*1+2
    
    if left_child < amount and data[min_index] > data[left_child]:
        min_index = left_child
    if right_child < amount and data[min_index] > data[right_child]:
        min_index = right_child
    if min_index != i:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift(amount, data, swaps, min_index)


def main():
    
    text = input()
    if "I" in text:
        n = int(input())
        data = list(map(int, input().strip().split()))

        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)


    elif "F" in text:
        file_name = input()
        while True:
            try:
                file_name = "/tests" + input()
                with open(file_name, 'r', encoding="utf-8") as f:
                    n = int(f.readline().strip())
                    data = list(map(int, f.readline().strip().split()))
            swaps = build_heap(data)
            assert len(data) == n
            print(len(swaps))
            for i, j in swaps:
                print(i, j)


if __name__ == "__main__":
    main()
