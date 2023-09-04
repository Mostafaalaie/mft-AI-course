import datetime


def get_string():
  user_input = input("Enter the string: ")
  return user_input

def check_type(input_string):
  str_list = input_string.split(',')
  type_corrected_list = []
  for item in str_list:
    try: 
      temp = datetime.datetime.strptime(item, '%Y-%m-%d')
      type_corrected_list.append(temp)
      #return 'Date'
    except ValueError:
      try:
      # Convert to int
        temp = int(item)
        type_corrected_list.append(temp)
        #return 'Integer'
      except ValueError:
        try:
        # Convert to float
          temp = float(item)
          type_corrected_list.append(temp)
          #return 'Float'
        except ValueError:
        # Check for string
          if isinstance(item, str):
            temp = item
            type_corrected_list.append(temp)
            #return 'String'
          else:
            temp = item + " (Unknown Type)"
            type_corrected_list.append(temp)
            #return 'Unknown'

  return type_corrected_list



#a = 'ali,22,1.54,2022-05-23,test,65'
a = get_string()

b = check_type(a)

print(b)

    