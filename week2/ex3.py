def get_string(msg):
  user_input = input("Enter the {} list: ".format(msg))
  return user_input


a = get_string("title")
b = get_string("value")

def match(titles, values):
  mached_list = []
  titles_list = titles.split(',')
  values_list = values.split(',')
  if not len(values_list) == len(titles_list):
    if len(values_list) > len(titles_list):
      print("You don't have enough title for your values")
    else:
      print("You don't have enough values for your titles")

  else:
    for index in range(0,len(titles_list)):
      item = titles_list[index] + ":" + values_list[index]
      mached_list.append(item)

  return mached_list

result = match(a,b)
print(">>>>>>>>",result)
