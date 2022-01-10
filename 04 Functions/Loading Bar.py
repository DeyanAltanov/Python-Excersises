num = int(input())


def loading_bar(number):
    loading = '['
    for i in range(0, number, 10):
        loading += '%'
    if number < 100:
        for i in range(number, 100, 10):
            loading += '.'
        loading += ']'
        print(f'{number}% {loading}')
        print('Still loading...')
    else:
        loading += ']'
        print(f'{number}% Complete!')
        print(loading)


loading_bar(num)