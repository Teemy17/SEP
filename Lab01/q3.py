def binary_search(num, arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if end >= start:
        mid = (start + end) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            return binary_search(num, arr, mid + 1, end)
        else:
            return binary_search(num, arr, start, mid - 1)
    else:
        return False
    
if __name__ == '__main__':
    arr = [2, 3, 4, 7, 8]
    num = 7
    print(binary_search(num, arr))