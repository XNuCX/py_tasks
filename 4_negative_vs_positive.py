def ispos(n):
    if n >= 0:
        return n
    return 0
def isneg(n):
    if n < 0:
        return n
    return 0
def sums(p, n):
    print(sum(n))
    print(sum(p))

def compare(p, n):
    if sum(p) > abs(sum(n)):
        sums(p, n)
        print("The positives are stronger than the negatives")
    else:
        sums(p, n)
        print("The negatives are stronger than the positives")
num_list = [int(el) for el in input().split(" ")]
positive = [ispos(el) for el in num_list]
negative = [isneg(el) for el in num_list]
compare(positive, negative)