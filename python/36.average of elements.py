def find_average(arr): 
    total = sum(arr) 
    return total / len(arr) 
 
 
my_array = [1, 2, 3, 4, 5] 
average = find_average(my_array) 
print("The average of the array is:", average)