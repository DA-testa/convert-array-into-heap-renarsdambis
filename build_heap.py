def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(i, data, swaps)
    return swaps

def sift_down(i, data, swaps):
    n = len(data)
    min_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(min_index, data, swaps)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    # Determine input type
    input_type = input()
    if "i" in input_type:
        pass
    elif "f" in input_type:
        while True:
            try:
                file_name = "/tests" + input()
                with open(file_name, 'r', encoding="utf-8") as f:
                    n = int(f.readline().strip())
                    data = list(map(int, f.readline().strip().split()))
                    assert len(data) == n
                    swaps = build_heap(data)
                    print(len(swaps))
                    for i, j in swaps:
                        print(i, j)
                    break
            except FileNotFoundError:
                print("File not found. Try again.")
    else:
        print("Invalid input type. Try again.")


if __name__ == "__main__":
    main()