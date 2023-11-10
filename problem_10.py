from math import floor, ceil; answer_array = []
def f(a): return ceil(floor(ceil(floor(a)+a**2)+a**3)+a**4)
for num in range(10000):
    if not f(num/1000) in answer_array: answer_array.append(f(num/1000)) 
print(answer_array)