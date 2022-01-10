integers = input()

n = int(input())

integer_list = integers.split(' ')

integer_list = [int(x) for x in integer_list]

for i in range(0, n):
    integer_list.remove(min(integer_list))

print(integer_list)