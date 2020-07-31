import sys
print(sys,argv)
hours, salary_per_our, bonus = map(float, sys.argv[1:])
print('Salary - {}'.format(hours * salary_per_our + bonus))

#Task 2
my_list = [1, 2, 4, 59, 3, 1, 5, 8]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i-1] and i != 0]
print(new_list)

#Task 3

print([x for x in range(28, 241) if x % 20 == 0 or x % 21 == 0])

#Task 4

my_list = [2, 3, 5, 1, 2, 1, 5, 4, 8, 7, 9]
new_list = [x for x in my_list if my_list.count(x) == 1]

#Task 5

from functools import reduce
def nul_list(n1, n2)
    return  n1 * n2
my_list = [x for x in range(100, 1001) if x % 2 == 0]
reduce(nul_list, my_list)

#Task 6

from itertools import  count, cycle
for i in count(int(input('Введите стартовое число: ')))
    print(i)

#Task 7

from math import factorial
from itertools import count
def fibo_gen()
    for el in count(1):
        yield factorial(el)
x = 0
for i in fibo_gen():
    count
    print('Factorial {} - {}'.format(x + 1, i))
    if x == 14;
    break
    x+=1