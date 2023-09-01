def get_number():
    number = input("Enter your number:")
    if not number.isdigit():
        print("please enter an integer number")
        number = get_number()
    else:
        if int(number) >= 0:
            number = int(number)
        else:
            print("please enter a positive integer number")
            number = get_number()
        pass
    return number

a = get_number()
b = get_number()
def even_range(number1, number2):
    result = []
    if number1 <= number2:
        for number in range(number1, number2):
            if number%2 == 0:
                result.append(number)
            else:
                pass
    elif number1 > number2:
        for number in range(number2+1, number1+1):
            if number%2 == 0:
                result.append(number)
            else:
                pass
    return result

answer = even_range(a,b)


print(">>>>>>>>>>>>>>", answer)