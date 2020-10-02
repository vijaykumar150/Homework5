#example 1
def gen_print(n):
    num = 0
    while num < n:
        print(num)
        num += 1


(gen_print(5))


#example 2
def gen_print(n):
    num = 0
    while num < n:
        if num%2==0:
            print(num)
            num+=1
        else:
            num += 1
(gen_print(5))
