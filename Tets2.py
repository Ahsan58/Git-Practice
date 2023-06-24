def check_vowels_chracter(input,vowles):
    if input in vowles_list:
        print(input,"is vowel character")
    else:
        print(input,"is not vowels")
   
print("Please Enter a character")
input_char = input()
vowles_list = ['a','e','i','o','u']
check_vowels_chracter(input_char,vowles_list)

def find_factorial(n):  
    if n == 1:  
       return n   
    else:
        factorial_no = n*(find_factorial(n-1) )
        return factorial_no

num = int(input("Enter a number: ")) 
if num < 0 :
    print("Factorial not exist") 

if num == 0 :
    print("Factorial is 1") 
fact_value = find_factorial(num)  
print('Factorial of ',num,' is ',fact_value)