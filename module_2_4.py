# list_ = ['one', 'two', 'three']
# list_2 = [2, 3, 4, 5, 1]
# sum_ = 0
# for i in range(len(list_2)): # 1, 2, 3, 4
#     sum_ += list_2[i]
#
# print(sum_)

# for i in range(1, 11): # i - 1
#     for j in range(1, 11): # j - 1, 2, 3...
#         print(f'{i} x {j} = {i * j}')
#
# dict_ = {'a' : 1, 'b' : 2, 'c' : 3}
# for i in dict_:
#     print(i, dict_[i])

# for i, k in dict_.items():
#     print(i, dict_[i])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    is_prime = True
    if i == 1:
        continue
    else:
        for j in range(2, i-1):
            if i % j == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print("numbers:", numbers)
print("Primes:", primes)
print("Not Primes:", not_primes)



