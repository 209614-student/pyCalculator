class CalculatorEngine:
    """
    Count result of main operation of calculator.

    :param a: first number in mathematical operation
    :type a: float
    :param b: second number in mathematical operation
    :type b: float
    """
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def add(self):
        """
        Adding operation of class parameters.
        """
        return int(self.a + self.b)

    def mul(self):
        """
        Subtraction operation of class parameters.
        """
        return self.a * self.b

    def div(self):
        """
        Multiplication operation of class parameters
        """
        return self.a / self.b

    def sub(self):
        """
        Division operation of class parameters
        """
        return self.a - self.b


def adding_to_history(func) -> object:
    """
    Return function given in parameter.

    :param func:  function given in parameter
    :return: func: function given in parameter
    """
    def add_to_history() -> None:
        """
        Add operation to history.txt file.

        """
        f = open("history.txt", "a+")
        a, b, operation, result1 = func()
        f.write(" {} {} {} = {} \r\n".format(a, operation, b, result1))
        f.close()
    return add_to_history


@adding_to_history
def result_of_calc() -> (float, float, str, float):
    """
    Calculate and return the result of the operation for given numbers

    :return: a, b, operation, result
    :rtype: (int, int, str, int)
    """
    operation = ['+',
                 '-',
                 '*',
                 '/']
    result = None
    choice = 0
    while True:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            obj = CalculatorEngine(a, b)
            while result is None:
                print("0. Exit")
                print("1. Add")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    result = obj.add()
                    print("Result: ", result)
                elif choice == 2:
                    result = obj.sub()
                    print("Result: ", result)
                elif choice == 3:
                    result = obj.mul()
                    print("result: ", result)
               elif choice == 4:
                    result = round(obj.div(), 2)
                    print("Result: ", result)
                elif choice == 0:
                    break
                else:
                    print("Invalid choice!!")
                operation = operation[choice-1]
            return a, b, operation, result
        except ValueError:
            print("It is not a number! :(  ")
        except ZeroDivisionError:
            print("Cannot divide by zero!  ")


def delete_from_history() -> None:
    """
    Delete the content of the file by replacing it with an empty file.
    """
    with open("history.txt", "w") as f:
        f.write(" \r")


def read_history() -> None:
    """
    Read the content of the file.
    """
    with open("history.txt", "r") as f:
        file_contents = f.read()
        print(file_contents)
        f.close()


def history_handling() -> None:
    """
    Handle reading and deleting history.
    """
    while True:
        read_history()
        e = input("Exit type 'Y' or delete history type 'D' ---->")
        if e == 'Y':
            break
        if e == 'D':
            delete_from_history()
            break


def main_interface() -> None:
    """
    Handle the main interface of the calculator.
    """
    print("Hello!\nFollow the guide! \n")

    while True:
        try:
            y = input("Go to: calculator \ntype 'C'\nhistory - type 'H' \nquit - 'q'\n ---> ")
            if y == 'C':
                result_of_calc()
            if y == 'H':
                history_handling()
            if y == 'q':
                break
            else:
                print("invalid sign")
        except ValueError:
            print ("Invalid sign, try again!:(  ")

if __name__ == '__main__':
    main_interface()