# 一元二次方程求解
# y = ax^2 + bx + c
import math


def equation(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return {'status': -1, 'count': 0, 'data': 'this equation has no solution.'}
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return {'status': 0, 'count': 2, 'data': {'x1': x1, 'x2': x2}}
    else:
        return {'status': 0, 'data': {'x': -b / (2 * a)}}
