if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a = max(arr)
    b = []
    for i in range(len(arr)):
        if(arr[i]<a):
            b.append(arr[i])
print(max(b))
