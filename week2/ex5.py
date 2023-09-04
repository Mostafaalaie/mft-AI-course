import numpy as np

a = np.array([[2,3,3],[4,2,1]]) # 2 * 3
print("a = ",a)

b = np.array([[2,3],[4,2]]) # 2 * 3
print("b = ",b)

ar = a * a
print(">>>>>> a(2*3) * a(2*3) >>>>>>",ar)

br = b * b
print(">>>>>> b(2*2) * b(2*2) >>>>>>",br)

# arr = np.matmul(a ,a)
# print(">>>>>> matmul(a ,a) >>>>>>", arr)
# بعلت ستون و سطر ها امکان ضرب ماتریسی .ج.د ندارد

brr = np.matmul(b,b)
print(">>>>>> matmul(b ,b) >>>>>>",brr)