# 欧几里得求最大公约数
def gcd(num1, num2):
    if (num1 < num2):
        num1, num2 = num2, num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


if __name__ == '__main__':
    print(gcd(8, 24))
