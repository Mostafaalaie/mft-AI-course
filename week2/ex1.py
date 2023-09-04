import re


def get_string():
  user_input = input("Enter the operatin: ")
  return user_input

def devide_str(operation_str):
  #objects_list = operation_str.split
  res = re.findall(r'[0-9\.]+|[^0-9\.]+', operation_str)
  return res

def solve(str_list):
  answer = None
  a = int(str_list[0])
  b = int(str_list[2])
  for item in str_list:
    if item == '+':
      answer = a + b
    elif item == '-':
      answer = a - b
    elif item == '*':
      answer = a * b
    elif item == '/':
      answer  = a / b
    else:
      pass
  return answer

a = get_string()
b = devide_str(a)
print(b)
answer = solve(devide_str(a))

print( answer )