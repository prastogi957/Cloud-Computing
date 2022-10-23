# Program to multiply two matrices using list comprehension
import random
import time
print("Enter the length x length of matrices")
input_leng= int(input("Enter the length :"))

A=[]
B=[]

for _ in range(input_leng):  # This for loop is to arrange rows  
    r = []  
    for __ in range(input_leng):  # This for loop is to arrange columns  
        r.append(random.randint(1,10))  
    A.append(r)  
  
for _ in range(input_leng):  # This for loop is to arrange rows  
    s = []  
    for __ in range(input_leng):  # This for loop is to arrange columns  
        s.append(random.randint(1,10))  
    B.append(s)  


timer_start = time.time()
# result will be 3x4
result = [[sum(a * b for a, b in zip(A_row, B_col))
						for B_col in zip(*B)]
								for A_row in A]
timer_end=time.time()

timer_diff=timer_end-timer_start

print("Time of start - ",timer_start)
print("Time of End - ",timer_end)
print("Time of Difference - ",timer_diff)

#for t in result:
#	print(t)
