class Fraction:
    # 表示分子和分母
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    # 希望打印时以 num/den的格式打印
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # 类的实例直接用做运算是不行的,需要定义如何相等,如何相加
    def __add__(self, other):
        # 分数相加,直接统一分母
        newden = self.den * other.den
        newnum = self.num * other.den + other.num * self.den
        # 化简,求最大公约数
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        return (self.num * other.den) == (self.den * other.num)


def gcd(m, n):
    # 对于整数 m 和 n，如果 m 能被 n 整除，那么它们的最大公因数就是 n
    while m % n != 0:
        # 否则,结果是 n 与 m 除以 n 的余数的最大公因数
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


# 1/2
n1 = Fraction(1, 2)
n2 = Fraction(2, 5)
n3 = Fraction(2, 5)
print(n1, n2)
print(n1 + n2)
print(n1 == n2, n2 == n3)
