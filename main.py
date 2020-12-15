# from random import randint
#
#
# def get_cost(N, current):
#     return N.cost - current.cost
#
#
# def get_random_N(current):
#     pass
#
#
# def sim_anneal():
#     TI = 0
#     TL = 0
#     current = 0
#     best = current
#
#     T = TI
#     criterion = False
#     while not criterion:
#         for i in range(1, TL):
#             N = get_random_N(current)
#             c = get_cost(N, current)
#             if c <= 0:
#                 pass
#             else:
#                 q = randint(0, 1)
#                 if q < e:
#                     current = N
#         T = f(T)
#         return current


def main():
    file = open('1994_Formula_One.wmg', 'r')

    n = int(file.readline())
    participants = [[int(i), participant] for (i, participant) in [file.readline().strip().split(',') for _ in range(n)]]
    
    print(participants)


if __name__ == "__main__":
    TI = 1.0
    TL = 10
    f = 0.95
    num_non_improve = 5000
    main()
