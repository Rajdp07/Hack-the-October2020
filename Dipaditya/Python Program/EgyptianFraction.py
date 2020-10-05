from math import ceil


def egyptian_fraction(Num, Den):
    x = ceil(Den / Num)


if __name__ == '__main__':
    num, den, N = [int(input()), int(input()), int(input())]

    if N >= 2:
        if num > den and N < num:
            print("Impossible Situation!!!!")
        else:
            egyptian_fraction(num, den)
    else:
        print("Wrong Input!!!")
