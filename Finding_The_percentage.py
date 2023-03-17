if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a = student_marks[query_name]
    s = 0.00
    for i in range(0,len(a)):
        s = s + a[i]
    print('%.2f' % (s/len(a)))
