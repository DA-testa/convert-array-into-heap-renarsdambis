def build_heap(data):
    swaps = []
    n = len(data)

    # start from the middle of the array and iterate towards the beginning
    for i in range(n // 2, -1, -1):
        j = i
        # keep swapping until the element is smaller than both its children or it becomes a leaf node
        while j * 2 + 1 < n:
            left = j * 2 + 1
            right = j * 2 + 2 if j * 2 + 2 < n else left
            if data[left] < data[right]:
                smallest = left
            else:
                smallest = right
            if data[j] > data[smallest]:
                data[j], data[smallest] = data[smallest], data[j]
                swaps.append((j, smallest))
                j = smallest
            else:
                break

    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
