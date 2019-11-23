# 质因数分解


def divide(num):
    list = []
    i = 2
    while num > 1:
        if num % i == 0:
            list.append(i)
            num = num / i
        else:
            i += 1
    return list


if __name__ == '__main__':
    print(divide(20))
