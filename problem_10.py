from math import floor, ceil
def f(a):
    return ceil(floor(ceil(floor(a)+a**2)+a**3)+a**4)
answer_array = []
for num in range(10000):
    ans =  f(num/1000) 
    if not ans in answer_array:
        answer_array.append(ans)
print(answer_array)