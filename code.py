# --------------
#Code starts here

# def palindrome(num):
#     while True:
#         num+=1
#         if str(num)==str(num)[::-1]:
#             print(num)
#             break

def palindrome_check(num):
  num=str(num)
  return (num[::-1]==num)

#Function to find the smallest palindrome
def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num
                    
palindrome(8)
palindrome(12)
palindrome(13531)


# --------------
#Code starts here

# def a_scramble(str_1,str_2):
#     rst=True
#     for i in str_2.lower():
#         if i not in str_1.lower():
#             rst=False
#             break
#         else:
#             rst=True
#     return rst

def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)





# --------------
#Code starts here

from math import sqrt

# def check_fib(num):
#     rst=False
#     a,b=0,1
#     while b<=num:
#         if b==num:
#             rst=True
#             break
#         a,b=b,a+b
#     return rst


def is_perfect_square(x):
 
    s = sqrt(x)
    return (int(s)*int(s) == x) 
 
#Function to check for fibonacci number
def check_fib(num):
    if is_perfect_square((5*num*num) + 4) or is_perfect_square((5*num*num) - 4): #Formula for checking fibonacci number
        return True
    
    return False   

check_fib(456)



# --------------
#Code starts here

# def compress(word):
#     word=word.lower()
#     rst=''
#     for i in word:
#         if i not in rst:
#             rst+=i+str(word.count(i))
#     return rst


def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)


# --------------
#Code starts here

# def k_distinct(string,k):
#     rst=False
#     temp=''
#     for i in string:
#         if i not in temp:
#             temp+=i
#     if len(temp)>=k:
#         rst=True
#     return rst

def k_distinct(string,k):
    s_list=(set(string.lower()))
    return len(s_list)>=k



