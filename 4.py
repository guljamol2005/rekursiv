n = int(input("Son kiriting: "))
def fibonachchi():
    fib_list = [0, 1]
    while True:
        fib = fib_list[-1] + fib_list[-2]
        if fib > n:  
            break
        fib_list.append(fib)
    return fib_list
result = fibonachchi()
print(f"Fibonacci n gacha: {result}")
