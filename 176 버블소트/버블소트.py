import sys

def merge_sort(arr,N,result):
    def sort(low, high,result):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid,result)
        sort(mid, high,result)
        merge(low, mid, high,result)

    def merge(low, mid, high,result):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] <= arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
                result[0] += mid-l

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, N,result)

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
result = [0]

merge_sort(arr,N,result)
#print(arr)
print(result[0])