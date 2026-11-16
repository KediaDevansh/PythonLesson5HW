def fibonacci():
    print("=== Fibonacci Series ===")
    n = int(input("Enter the no of times you want to display the fibonacci series"))
    i = 1
    a = 0
    b = 1
    print(a,",")
    print(b,",")
    while i<=(n-2):
        s = a+b
        print(s,",")
        a=b
        b=s
        i = i+1
fibonacci()
    