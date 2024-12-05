n = int(input("Son kiriting: "))
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
print(f"Sonning faktoriali: {faktorial(n)}")
