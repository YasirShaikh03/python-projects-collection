a= int(input("ENter any no :")) 

if(a % 2 == 0 ):
    print(f"EVEN NO {a}")
    
else:
    print(f"ODD NO  {a} ")


s=str(input("ENTER ANY WORD"))
print(s[::-1])


n = int(input("ENter any no :")) 

b,c=0,1
for _ in range(n):
    print(b, end=" ")
    b,c=c,b+c
    
    
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


def is_palindrome(p):
    # convert to uppercase to ignore case and compare with reversed string
    return p.upper() == p[::-1].upper()

# take input
p = input("ENTER YOUR WORD: ")

# check palindrome
print("Is palindrome:", is_palindrome(p))

# print reversed word
print("Reversed word:", p[::-1])


#biggner

num=int( input("Enter any no  :"))
print(num*num )

squares = [i**2 for i in range(1, 11)]
print(squares)  


amg = int(input("ENTER YOUR NO"))

m= len(str(amg))
sum_digital = (int(digital)**m for digital in str(amg))

if amg==sum_digital:
    print("amstrong")
else :
    print("not amstrong")
    
    
sq = lambda x : x**2
print(sq(5))    


for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)
        
F = int(input("ENTER ANY NO"))   
if F % 3 == 0 and F % 5 == 0:
    print(f"fizzbuzz {F}")
elif F % 3 == 0:
    print(f"FIZZ {F}")
elif F % 5 == 0:
    print(f"BUZZ {F}")
else:
    print(F)  
   
    
ST = [1,2,3,4,5,6,7,8,9,10]
double   = list(map(lambda x: x*2 , ST))  
print(double)

FIL = list(filter( lambda x : x % 2 == 0, ST))
print(FIL)


LI =[1,2,3,3,4,5,6,3,7,5,6,1,2]

uniqlist= list(set(LI))
print(uniqlist)

def c_vowel(s):
    return sum(1 for char in s.lower() if char in "aeiou")
print(c_vowel("HELLOW WORLD"))

def anagram(s1,s2):
    return sorted(s1.lower()) == sorted(s2.lower())
print(anagram("yasir", "isayr"))
        

def missingnum(N, n):
    return n * (n + 1) // 2 - sum(N)

print(missingnum([1,3,5,6], 6))
