class Calculator:
    def __init__(self):
        self.__historic = []


    def add(self, number1, number2):
        result = number1 + number2
        self.__historic.append(
            {
                'operation':'+',
                'numbers': [number1, number2],
                'result': result
            }
        )
        return result

    def subtraction(self, number1, number2):
        result  =  number1 - number2
        self.__historic.append(
            {
                'operation':'-',
                'numbers': [number1, number2],
                'result': result
            }
        )
        return result

    def multiply(self, number1, number2):
        result = number1 * number2
        self.__historic.append(
            {
                'operation':'*',
                'numbers': [number1, number2],
                'result': result
            }
        )
        return result

    def division(self, number1, number2):
        if number2 == 0:
            raise "Divisao por zero e invalido"
        result = number1/number2
        self.__historic.append(
            {
                'operation':'/',
                'numbers': [number1, number2],
                'result': result
            }
        )
        return result

    def show_historic(self):
        print(self.__historic)



calc = Calculator()

result = calc.division(4, 0)

calc.show_historic()