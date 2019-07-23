# (n/2)(2a+(n-1)d)
def gcd(num1, num2):
    res = 0
    while True:
        remainder = num1 % num2
        if remainder != 0:
            num1 = num2
            num2 = remainder
        else:
            res = num2
            break
    return res


def lcm(num1, num2):
    mul = num1*num2
    return mul/gcd(num1, num2)


def findSum(num):
    return num * (num+1)/2


# def findSum1(num1, num2):
#     return num2 * (num1+1)/2


if __name__ == "__main__":
    print(gcd(21, 25))
    print(lcm(15, 12))
    print(findSum(5))
    # print(findSum(1, 5))
