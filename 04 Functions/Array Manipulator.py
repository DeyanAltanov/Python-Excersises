args = input().split(' ')

array = list(map(int, args))

cmd = input()


def array_manipulator(command):
    cmd = command.split(' ')
    if cmd[0] == 'max':
        if cmd[1] == 'even':
            even = False
            for i in range(0, len(array)):
                if int(array[i]) % 2 == 0:
                    even = True
                    break
            max_even = 0
            mad_max = 0
            for i in range(0, len(array)):
                if int(array[i]) % 2 == 0 and int(array[i]) >= max_even:
                    max_even = int(array[i])
                    mad_max = i
            if not even:
                return 'No matches'
            else:
                return mad_max
        elif cmd[1] == 'odd':
            odd = False
            for i in range(0, len(array)):
                if int(array[i]) % 2 == 1:
                    odd = True
                    break
            max_odd = 0
            mad_max = 0
            for i in range(0, len(array)):
                if int(array[i]) % 2 == 1 and int(array[i]) >= max_odd:
                    max_odd = int(array[i])
                    mad_max = i
            if not odd:
                return 'No matches'
            else:
                return mad_max
    elif cmd[0] == 'min':
        if cmd[1] == 'even':
            even = False
            for i in range(0, len(array)):
                if int(array[i]) % 2 == 0:
                    even = True
                    break
            min_even = 2147483650
            mad_max = 0
            for i in range(0, len(array)):
                if int(array[i]) % 2 == 0 and int(array[i]) <= min_even:
                    min_even = int(array[i])
                    mad_max = i
            if min_even == 2147483650:
                return 'No matches'
            else:
                return mad_max
        elif cmd[1] == 'odd':
            odd = False
            for i in range(0, len(array)):
                if int(array[i]) % 2 == 1:
                    odd = True
                    break
            min_odd = 2147483649
            mad_max = 0
            for i in range(0, len(array)):
                if int(array[i]) % 2 == 1 and int(array[i]) <= min_odd:
                    min_odd = int(array[i])
                    mad_max = i
            if odd == 2147483649:
                return 'No matches'
            else:
                return mad_max
    elif cmd[0] == 'first':
        if cmd[2] == 'even':
            if int(cmd[1]) > len(array):
                return 'Invalid count'
            else:
                evens = []
                count = []
                for i in range(0, len(array)):
                    if int(array[i]) % 2 == 0:
                        evens.append(array[i])
                if len(evens) == 0 or len(evens) <= int(cmd[1]):
                    return evens
                else:
                    for i in range(0, int(cmd[1])):
                        count.append(evens[i])
                return count
        elif cmd[2] == 'odd':
            if int(cmd[1]) > len(array):
                return 'Invalid count'
            else:
                odds = []
                count = []
                for i in range(0, len(array)):
                    if int(array[i]) % 2 == 1:
                        odds.append(array[i])
                if len(odds) == 0 or len(odds) <= int(cmd[1]):
                    return odds
                else:
                    for i in range(0, int(cmd[1])):
                        count.append(odds[i])
                return count
    elif cmd[0] == 'last':
        if cmd[2] == 'even':
            if int(cmd[1]) > len(array):
                return 'Invalid count'
            else:
                evens = []
                count = []
                for i in range(0, len(array)):
                    if int(array[i]) % 2 == 0:
                        evens.append(array[i])
                evens.reverse()
                if len(evens) == 0 or len(evens)  <= int(cmd[1]):
                    return evens
                else:
                    for i in range(0, int(cmd[1])):
                        count.append(evens[i])
                count.reverse()
                return count
        elif cmd[2] == 'odd':
            if int(cmd[1]) > len(array):
                return 'Invalid count'
            else:
                odds = []
                count = []
                for i in range(0, len(array)):
                    if int(array[i]) % 2 == 1:
                        odds.append(array[i])
                odds.reverse()
                if len(odds) == 0 or len(odds) <= int(cmd[1]):
                    return odds
                else:
                    for i in range(0, int(cmd[1])):
                        count.append(odds[i])
                count.reverse()
                return count


while not cmd == 'end':
    c = cmd.split(' ')
    if c[0] == 'exchange':
        if 0 <= int(c[1]) < len(array):
            ar1 = array[0:int(c[1]) + 1]
            ar2 = array[int(c[1]) + 1:]
            array.clear()
            array = ar2 + ar1
        else:
            print('Invalid index')
    else:
        print(array_manipulator(cmd))

    cmd = input()

print(array)