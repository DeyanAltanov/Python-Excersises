class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = args[0]
        for number in range(len(args) - 1):
            result *= args[number + 1]
        return result

    @staticmethod
    def divide(*args):
        result = 0
        for number in range(len(args) - 1):
            result += args[number] / args[number + 1]
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for number in range(len(args) - 1):
            result -= args[number + 1]
        return result