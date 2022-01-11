tickets = input().split(',')

for ticket in tickets:
    ticket = ticket.strip()
    first_part, second_part = ticket[:int(len(ticket)/2)], ticket[int(len(ticket)/2):]
    match = False

    if len(ticket) == 20:
        if '@@@@@@@@@@' in first_part and second_part:
            print(f"ticket " f'"{ticket}" ' f"- 10@ Jackpot!")
            match = True
        elif 6 * '@' in first_part and second_part:
            count_left = first_part.count('@')
            count_right = second_part.count('@')
            if count_left > count_right:
                print(f"ticket " f'"{ticket}" ' f"- {count_right}@")
            else:
                print(f"ticket " f'"{ticket}" ' f"- {count_left}@")
            match = True
        if '##########' in first_part and second_part:
            print(f"ticket " f'"{ticket}" ' f"- 10# Jackpot!")
            match = True
        elif 6 * '#' in first_part and second_part:
            count_left = first_part.count('#')
            count_right = second_part.count('#')
            if count_left > count_right:
                print(f"ticket " f'"{ticket}" ' f"- {second_part}#")
            else:
                print(f"ticket " f'"{ticket}" ' f"- {count_right}#")
            match = True
        if '$$$$$$$$$$' in first_part and second_part:
            print(f"ticket " f'"{ticket}" ' f"- 10$ Jackpot!")
            match = True
        elif 6 * '$' in first_part and second_part:
            count_left = first_part.count('$')
            count_right = second_part.count('$')
            if count_left > count_right:
                print(f"ticket " f'"{ticket}" ' f"- {second_part}$")
            else:
                print(f"ticket " f'"{ticket}" ' f"- {count_right}$")
            match = True
        if '^^^^^^^^^^' in first_part and second_part:
            print(f"ticket " f'"{ticket}" ' f"- 10^ Jackpot!")
            match = True
        elif 6 * '^' in first_part and second_part:
            count_left = first_part.count('^')
            count_right = second_part.count('^')
            if count_left > count_right:
                print(f"ticket " f'"{ticket}" ' f"- {second_part}^")
            else:
                print(f"ticket " f'"{ticket}" ' f"- {count_right}^")
            match = True
        if match is False:
            print(f"ticket " f'"{ticket}" ' f"- no match")
    else:
        print("invalid ticket")