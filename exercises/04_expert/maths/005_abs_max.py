def absMax(x):

    j = x[0]
    for i in x:
        if abs(i) > abs(j):
            j = i
    return j


def main():
    a = [1, 2, -11]
    print(absMax(a)) # = -11


main()
