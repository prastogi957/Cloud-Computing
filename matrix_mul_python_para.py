import multiprocessing
import random
import time
i_list = []
print("Enter the length x length of matrices")
input_leng= int(input("Enter the length :"))
result_disp=[]
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
      

def process(i):
        # result will be 3x4
        result = [[sum(a * b for a, b in zip(A_row, B_col))
                                for B_col in zip(*B)]
                                        for A_row in A]
        print("Running")
                            


timer_start = time.time()
p = multiprocessing.Pool()  # defaults to os.cpu_count() workers
p.map_async(process, i_list)  # perform process for each i in i_list



p.close()
p.join() # Wait for all child processes to close.
timer_end=time.time()


timer_diff=timer_end-timer_start



print("Time of start - ",timer_start)
print("Time of End - ",timer_end)
print("Time of Difference - ",timer_diff)