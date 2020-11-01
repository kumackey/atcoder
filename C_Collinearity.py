from fractions import Fraction

N = int(input())
XYs = [list(map(int, input().split())) for i in range(N)]


def judge(xy_a, xy_b, xy_c):
    if(xy_a[0] == xy_b[0]):
        if(xy_c[0] == xy_a[0]):
            return True
        else:
            return False
    else:
        if(xy_c[1] == float((xy_b[1] - xy_a[1]) * (xy_c[0] - xy_a[0])) / (xy_b[0] - xy_a[0]) + xy_a[1]):
            return True
        else:
            return False


for i in range(N):
    for j in range(i):
        for k in range(j):
            if(judge(XYs[i], XYs[j], XYs[k])):
                print('Yes')
                exit()


print('No')
