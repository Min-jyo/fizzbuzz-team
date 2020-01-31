for i in (list(map(lambda i: (i%3==0)*"fizz\n" + (i%5==0)*"buzz\n" + (i%15==0)*"fizzbuzz\n", range(1, 101)))):
    print(i, end='')