class Calculator:
    def add(self, x, y):
        pass
    def subtract(self, x, y):
        return x-y
    def multiply(self, x, y):
        pass
    def divide(self, x, y):
        pass



def main():
    calculator = Calculator()

    while True:
        expression = input("더하기, 빼기, 나누기, 곱하기 연산만 가능합니다. 입력예시(1+1)\n q를 누르면 종료됩니다.")

        try:
            num1, symbol, num2 = expression[0], expression[1], expression[2]
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter the expression in correct format.")
            continue


if __name__ == "__main__":
    main()