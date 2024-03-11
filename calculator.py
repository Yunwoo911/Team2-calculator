# 사용자로부터 입력 받기
num1 = int(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요(+, -, *, /): ")
num2 = int(input("두 번째 숫자를 입력하세요: "))

# 연산자에 따른 계산 수행 및 결과 출력
if operator == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("0으로 나눌 수 없습니다.")
else:
    print("잘못된 연산자입니다. 프로그램을 다시 실행해주세요.")
