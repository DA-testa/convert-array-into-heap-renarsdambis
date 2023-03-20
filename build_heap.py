def build_heap(data):
    swaps = []
    n = len(data)
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
    input_type = input("Enter the input type (i or f): ")
    if input_type == "i":
        n = int(input("Enter the number of elements: "))
        data = list(map(int, input("Enter the elements: ").split()))
        assert len(data) == n
        swaps = build_heap(data)
        print("Number of swaps:", len(swaps))
        for i, j in swaps:
            print(i, j)
    elif input_type == "f":
        while True:
            try:
                file_name = input("Enter the file name: ")
                with open(file_name, "r") as f:
                    n = int(f.readline().strip())
                    data = list(map(int, f.readline().strip().split()))
                    assert len(data) == n
                    swaps = build_heap(data)
                    print("Number of swaps:", len(swaps))
                    for i, j in swaps:
                        print(i, j)
                    break
            except FileNotFoundError:
                print("File not found. Try again.")
    else:
        print("Invalid input type. Try again.")


if __name__ == "__main__":
    main()
