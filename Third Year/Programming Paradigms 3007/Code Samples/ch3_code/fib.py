def fib(n):
    if(n<=1):
        return n

    fn1 = 1
    fn2 = 0
    count = 1

    while(count!=n):
        fn = fn1+fn2

        fn2 = fn1
        fn1 = fn
        count+=1

    return fn


for i in range(0,11):
    print("fib("+str(i)+")= "+str(fib(i)))
