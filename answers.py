# Given a list of distinct numbers,
#  return another list which contains the sum of all pairs of numbers in the given list
#  (the same pair should not be taken twice).
def sum_list(given_list):
    summ=[]
    operated_list=given_list
    for items in operated_list:
        for ele in operated_list:
            ele=ele+items
            summ.append(ele)
        operated_list.remove(items)
    return summ
sum_list([1,1,2,3])
            

#Given a list of distinct numbers (may contain zero),
# return another list which contains the ratio of all pairs of numbers in the given list 
# (the same pair should not be taken twice).
def ratio_list(given_list):
    ratio=[]
    operated_list=given_list
    for items in operated_list:
        if items!=0:
            for ele in operated_list:
                if ele!=0:
                    num = (items/ele)
                    ratio.append(num)
            operated_list.remove(items)
    return ratio

ratio_list([1,5,4,6,2,3])
        

#Given a list of positive integers, return a list of the factorial of all these numbers.
fibonacci_series=[0,1]      
def fibo_num(num):
    if num==0:
        return []
    elif num==1:
        return [0]
    else:
        while (num>fibonacci_series[-1]):      
            fibonacci_series.append(fibonacci_series[-1]+fibonacci_series[-2])
        return fibonacci_series
print(fibo_num(0))

#Given a positive integer, return a list of all prime numbers from 1 up to this number.
def is_prime(num):
    if num<=1:
        False
    elif num==2:
        return num
    else:
        for elements in range(2, num):
            if num%elements==0:
                return False
        return num
list_prime=[]
def nums_prime(ranges):
    for items in range(2,ranges+1):
        if is_prime(items)!= False:
            list_prime.append(is_prime(items))
    return list_prime 
print(nums_prime(22))   


#Given a positive integer, return the sum of all prime numbers from 1 up to this number.
def is_prime(num):
    if num<=1:
        False
    elif num==2:
        return num
    else:
        for elements in range(2, num):
            if num%elements==0:
                return False
        return num
    
def sum_prime(ranges):
    prime=0
    for items in range(2,ranges+1):
        if is_prime(items)!= False:
                prime+=items
    return prime
            
    
print(sum_prime(22))   


# #Given a list of numbers,
#  return another list of co-primes and count how many co-primes are there in this given list.
def gcd(num1, num2):
    if num1 > num2:
        for i in range(1, num2 + 1):
            if num1 % i == 0 and num2 % i == 0:
                result = i
        return result
    else:
        for i in range(1, num1 + 1):
            if num1 % i == 0 and num2 % i == 0:
                result = i
        return result
    
def co_prime(num1, num2):
    if gcd(num1, num2)==1:
        return True
        
def co_prm_list(given_list):
    co_prime_=[]
    count=0
    for i in range(len(given_list)):
        for j in range(i + 1, len(given_list)):
            if co_prime(given_list[i], given_list[j])==True:
                co_prime_.append((given_list[i], given_list[j]))
                count += 1
        
    return f"pairs of co-prime number is {co_prime_}, and number of pairs are {count}"
co_prm_list([54,19,2,35,17])
              
        
#Given a list of integers, sort it on your own and return the median.

def sorting(given_list):
    smallest_num=given_list[0]
    new_list=given_list
    sorted_list=[]
    while new_list:  
        smallest_num = new_list[0]  
        for items in new_list:
            if items<smallest_num:
                smallest_num=items
        sorted_list.append(smallest_num)
        new_list.remove(smallest_num)
    return sorted_list
def median(given_list):
    n=len(given_list)
    new_list=sorting(given_list)
    if len(given_list)%2==0:
        result = ((new_list[n//2 - 1] + new_list[n//2])) / 2
        return result
    else:
        return new_list[(n//2)]
        

print(f"the sorted list is {sorting([5,2,65,154,12,0,1,33])} and the median is {median([5,2,65,154,12,0,33])}")

            
#Given a list of integers, return its mode
# (list of numbers with highest frequency of occurrence).
# Do not use a dictionary.
def mode(given_list):
    mode_list=[]
    another_list=[]
    highest_frequency=0
    for i in range(len(given_list)):
        if given_list[i] not in another_list:
            count=0
            for j in range(len(given_list)):
                if given_list[i]==given_list[j]:
                    count+=1
            another_list.append(given_list[i])
            
            if count>highest_frequency:
                highest_frequency=count
                mode_list.append(given_list[i])
            elif count==highest_frequency:
                mode_list.append(given_list[i])
        return mode_list, count
mode([1,1,1,2,5,1,2,5,1,2,4,5,2,1,8])


#Given a list of lists of integers, return a list that is sorted based on the sum of each inner list. 
#Do not use any inbuilt function for sorting.
def sum_list(arr):
  sum_array=[]
  for items in arr:
    addition=0
    for ele in items:
      addition+=ele
    sum_array.append(addition)
  return sum_array
sum_list([[1,2,3,4,5,6,7],[8,9,10,11,12,13],[14,15,16],[17,18,19,20,21],[22,23,24,25]])