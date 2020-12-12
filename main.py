def main():
    f = open('1994_Formula_One.wmg', 'r')
    n = int(f.readline())
    for _ in range(n):
        print(f.readline())


if __name__ == "__main__":
    main()