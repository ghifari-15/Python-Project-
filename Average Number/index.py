# first value to start
start = int(input("Enter the start of array : "))
#end of value 
end = int(input("Enter the end of array: "))

#empty array
arr = []
total = 0

#loops for insert every element of numbers into array
for i in range(start, end + 1):
    arr.append(i)   

#summarize of every elements
for elements in arr:
    total += elements 

#count of length in array
len_arr = len(arr)

if len_arr != 0:
    result = total / len_arr
    print(arr)
    print(result)
    
else:
    print("Cannot get the average cause the number represence as 0")


 


