def main():
    def findMin(x):
        minNum = x[0]
        for i in x:
            if minNum > i:
                minNum = i
        return minNum

    print(findMin([0, 1, 2, 3, 4, 5, -3, 2, 4, -56]))# = -56


main()
