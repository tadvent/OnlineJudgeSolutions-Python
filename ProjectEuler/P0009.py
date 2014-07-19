def findans():
    for a in range(1, 333):
        for b in range(a+1, 500):
            c = 1000 - (a + b)
            if b >= c:
                break
            if a*a + b*b == c*c:
                return a, b, c

if __name__ == "__main__":
    a, b, c = findans()
    print(a, b, c)
    print(a*b*c)

