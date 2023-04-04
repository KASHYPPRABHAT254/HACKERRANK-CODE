cube = lambda x: x**3  # complete the lambda function 

def fibonacci(n):
    x = 0
    y = 1
    z = 0
    a = []
    for i in range(n):
        a.append(z)
        x = y
        y = z
        z = x+y
    return a
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
