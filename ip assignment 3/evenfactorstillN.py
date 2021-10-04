def even_factors(x, n):
    print("Even factors of", x, "till", n, "are:")
    for i in range(1, x + 1):
        if i <= n and i % 2 == 0 and x % i == 0:
            print(i)


num = int(input("Even factors of: "))
N = int(input("Till: "))
even_factors(num, N)
