# N = pupils, K = apples, x = apples_per_person, y = leftovers
N = int(input('pupils:'))
K = int(input('apples:'))
x = K // N
y = K % N
print(x)
print(y)
