# fucntions

def average(a,b,c):
    return (a+b+c)/3

print(average(2,3,4))


# default arguments must be placed at end
def cal_product(a, b=1):
    return a*b

def print_len(list):
    print(len(list))

nums = [1,2,3,4,5,6]

print_len(nums)

def sumOfNatural(n):
    if(n==0):
        return 0
    return n + sumOfNatural(n-1)

print(sumOfNatural(10))

def printList(index, list):
    if(index == len(list)):
        return
    else:
        print(list[index], end= " ")
        printList(index+1, list)

printList(0,nums)

print()