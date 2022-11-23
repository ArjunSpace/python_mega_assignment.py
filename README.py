# python_mega_assignment.py
Q1. Why do we call Python as a general purpose and high-level programming language?

   Python has vast application in various domains like Data science,Data Analytics
 web development and Machine learning and many more, hence it is called as general purpose.
 and it is a programming language which is human readable hence it is a high level programming language.

Q2. Why is Python called a dynamically typed language?

   In python the values will be stored in memory randomly irrespective of its data type and 
variable name will bind with the memory location. There is no need to declare the data type 
to the variable

Q3. List some pros and cons of Python programming language?

  	pros                               cons

	1.Easy to understand              1.Indentation 
	2.Vast applications  		    2.High memory consumption
 	 Ex. Data science,
      	web development
	3.Open source			    3.Complex multi threding
	4.Huge set of libraries           4.Dynamically typed
	5.Large Community                 5.Security

Q4. In what all domains can we use Python?
Data science, web development, gaming

Q5. What are variable and how can we declare them?

	Variable is name given to the memory location. Variables can be declared by following some set of rules.
    the rules are:
		1.Should start with the alphabet
		2.Should not use any special character except underscore (_)

Q6. How can we take an input from the user in Python?

	input from user can be taken by using input() function.


Q7. What is the default datatype of the value that has been taken as an input using input() function?

	Always a string

Q8. What is type casting?
	
	Convertion of one data type into another data type 

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

	yes, taking multiple inputs is possible with the input() function by using split method or list comprehension method
    Ex: # taking three inputs at a time
	x, y, z = input("Enter three values: ").split()
	print("Total number of students: ", x)
	print("Number of boys is : ", y)
	print("Number of girls is : ", z)
	

	
Q10. What are keywords?

	key words in python are reserved words that can not be used as a variable name, function name,
     or any other identifier.	
     Ex: True,False,if,else etc..	

Q11. Can we use keywords as a variable? Support your answer with reason.

	Keywords are predefined, reserved words used in Python programming that have special meanings to the compiler.

We cannot use a keyword as a variable name, function name, or any other identifier. They are used to define the syntax and structure of the Python language.

Q12. What is indentation? What's the use of indentaion in Python?

	Indentation refers to the spaces at the beginning of a code line.
     Where in other programming languages the indentation in code is for readability only,  
     the indentation in Python is very important.

     Python uses indentation to indicate a block of code.

Q13. How can we throw some output in Python?

	output can be throwned in python using print() function

Q14. What are operators in Python?

	Python Operators in general are used to perform operations on values and variables.
     These are standard symbols used for the purpose of logical and arithmetic operations
 Arthematic operators:
 Arithmetic operators are used to performing mathematical operations like addition, subtraction, multiplication, and division.

	
Operator	Description							Syntax

+	        Addition: adds two operands					x + y
–	        Subtraction: subtracts two operands				x – y
*		Multiplication: multiplies two operands				x * y
/		Division (float): divides the first operand by the second	x / y
//		Division (floor): divides the first operand by the second	x // y
%		Modulus: returns the remainder when the first operand is 
	                 divided by the second					x % y
**		Power: Returns first raised to power second			x ** y

Comparison Operators:
                    Comparison of Relational operators compares the values. 
		    It either returns True or False according to the condition.
		
Operator	Description								Syntax
>		Greater than: True if the left operand is greater than the right	x > y
<		Less than: True if the left operand is less than the right		x < y
==		Equal to: True if both operands are equal				x == y
!=		Not equal to – True if operands are not equal				x != y
>=		Greater than or equal to True if the left operand is
		greater than or equal to the right					x >= y
<=		Less than or equal to True if the left operand is less than 
		or equal to the right							x <= y
is 		x is the same as y							x is y
is not		x is not the same as y							x is not y

Logical Operators:
Logical operators perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.

Operator	Description						Syntax
and		Logical AND: True if both the operands are true		x and y
or		Logical OR: True if either of the operands is true 	x or y
not		Logical NOT: True if the operand is false 		not x

	
	
Q15. What is difference between / and // operators?

	/ is an opearator used for float division
	// is an operator used for integer division
	
Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```

x = "iNeuron"
print(x*4)


Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

int_num = int(input("Enter the number"))
if int_num % 2 == 0:
    print(int_num," is Even")
else:
    print(int_num, " is odd" ) 
Q18. What are boolean operator?

 	 The opearators representing or gives an idea wheather it is true or false to an condition, the boolean key words are:
		"True","False"
	
Q19. What will the output of the following?
```
1 or 0  >>>> True

0 and 0  >>>> False

True and False and True >>> False

1 or 0 or 0  >>>> True

Q20. What are conditional statements in Python?

          There comes situations in real life when we need to do some specific task and based on some specific conditions and,
      we decide what should we do next. Similarly there comes a situation in programming where a specific task is to be 
      performed if a specific condition is True. In such cases, conditional statements can be used. 
The following are the conditional statements provided by Python. 

if
if..else
Nested if
if-elif statements.

Q21. What is use of 'if', 'elif' and 'else' keywords?

 These key words are used to apply various conditions to the expression. filtering can be done by these key words.


Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

		age = int(input("Enter your age"))

		if age >= 18:
   		    print("I can vote")
		else:
    		    print("I can't vote")

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]

code:
numbers = [12, 75, 150, 180, 145, 525, 50]
sum = 0
for i in numbers:
    if i % 2 == 0:
        sum += i
print("sum of even numbers in the list is",sum) 


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

num1,num2,num3 = input("Enter 3 values").split()
if num1 > num2 and num1 > num3:
  print(num1,"is the largest number ")
elif num2 > num1 and num2 > num3:
   print(num2,"is the largest number ")
else:
  print(num3,"is the largest number")


       OR

def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

print(maximum(1,2,3))

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
numbers = [12, 75, 150, 180, 145, 525, 50]
list = []
for i in numbers:
  if i > 150:
    
    if i > 500:
      break
    continue
  if i % 5 == 0:
    list.append(i)
print(list)   
   

		

Q26. What is a string? How can we declare string in Python?

Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".
string in python can be declared by using str() function

Q27. How can we access the string using its index?

	Individual characters in a string can be accessed by 
specifying the string name followed by a number in square brackets ( [] ).
String indexing in Python is zero-based: the first character in the string
has  index 0 , the next has index 1 , and so on.

Q28. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "iNeuron"
```

string = "Big Data iNeuron"
print(string[9:16])

Q29. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "norueNi"
```

string = "Big Data iNeuron"
print(string[16:8:-1])

o/p : norueNi

Q30. Resverse the string given in the above question.
string = "Big Data iNeuron"

print(string[::-1])

o/p: norueNi ataD giB

Q31. How can you delete entire string at once?

string = "Big Data iNeuron"
string = string.replace("Big Data iNeuron", '')

Q32. What is escape sequence?

An escape character is a backslash \ followed by the character you want to insert.

Code    	Result	
\'	      Single Quote	
\\	      Backslash	
\n	      New Line	
\r	      Carriage Return	
\t	      Tab	
\b	      Backspace	
\f	      Form Feed	
\ooo	    Octal value	
\xhh	    Hex value
Q33. How can you print the below string?
```
'iNeuron's Big Data Course'
```
print("iNeuron's Big Data Course")

   or
  
print(' iNeuron\'s Big Data Course')


Q34. What is a list in Python?
	The list is a sequence data type which is used to store the collection of data.
     Lists in Python can be created by just placing the sequence inside the square brackets[].
     A single list may contain DataTypes like Integers, Strings, as well as Objects. 
     Lists are mutable, and hence, they can be altered even after their creation.


Q35. How can you create a list in Python?

Lists in Python can be created by just placing the sequence inside the square brackets[].


Q36. How can we access the elements in a list?

 	In order to access the list items refer to the index number. 
     Use the index operator [ ] to access an item in a list. 
     The index must be an integer. Nested lists are accessed using nested indexing. 


Q37. Write a code to access the word "iNeuron" from the given list.
```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
``` 
print(lst[4][2])

o/p: iNeuron

Q38. Take a list as an input from the user and find the length of the list.

def len_list():
  lst = list(input("enter the list: "))
  print(len(lst))

len_list()

Q39. Add the word "Big" in the 3rd index of the given list.
```
lst = ["Welcome", "to", "Data", "course"]
```

lst = ["Welcome", "to", "Data", "course"]
lst.insert(3,'Big')
print(lst)
print(lst.index('Big')) #to verify the index

o/p: ['Welcome', 'to', 'Data', 'Big', 'course']
      3

Q40. What is a tuple? How is it different from list?
  Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store 
collections of data, the other 3 are List, Set, and Dictionary,
all with different qualities and usage.
  A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.

   LIST	                                          TUPLE
1	Lists are mutable	                           Tuples are immutable
2	The implication of iterations is             The implication of iterations is comparatively Faster
Time-consuming	                      
3	The list is better for performing
operations, such as insertion and deletion.	   Tuple data type is appropriate for accessing the elements
4	Lists consume more memory	                  Tuple consumes less memory as compared to the list
5	Lists have several built-in methods	         Tuple does not have many built-in methods.
6	The unexpected changes and errors            In tuple, it is hard to take place
are more likely to occur	.

Q41. How can you create a tuple in Python?
	
	A tuple in Python can be created by enclosing all the comma-separated elements inside the parenthesis ()

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

tuple = ()
tuple.append("arjun")
print(tuple)

	it is not possible to add any element into the tuple, as tuple is a immutable object

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?

	No, appending two tuple is not possible, As tuple was immutable object

Q44. Take a tuple as an input and print the count of elements in it.

input = (1,2)
#print(type(input))
print(len(input))


Q45. What are sets in Python?

	Sets are used to store multiple items in a single variable.
A set is a collection which is unordered, unchangeable*, and unindexed.

Q46. How can you create a set?
	
	Set can be created by using function set().
Ex: set1 = set() or set2 = {1,2,3}

Q47. Create a set and add "iNeuron" in your set.

string1 = "iNeuron"
set1 = set()
set1.add(string1)
print("set1 = ",set1)
o/p:
set1 =  {'iNeuron'}


Q48. Try to add multiple values using add() function.

list1 = list(range(10))
set1 = set()
for i in list1:
  set1.add(i)
print(set1)
o/p:
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

Q49. How is update() different from add()?

	Element can be updated to another value by update() function.
Element can be added after the last element by add() function

Q50. What is clear() in sets?

	clear() method removes all elements in a set.
	
Q51. What is frozen set?

	Python frozenset() Method creates an immutable Set object from an iterable. 
It is a built-in Python function. 

As it is a set object therefore we cannot have duplicate values in the frozenset.

Q52. How is frozen set different from set?
 
	Frozen set is just an immutable version of a Python set object. 
While elements of a set can be modified at any time, 
elements of the frozen set remain the same after creation. 
Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.

Q53. What is union() in sets? Explain via code.

set_a = {1,2,3,4,5,6}
set_b = {3,6,8,9,10}
print(set_a | set_b)

o/p: {1, 2, 3, 4, 5, 6, 8, 9, 10}
union() function is an opearation between the sets. 
union opearation adds the unique values into a set

Q54. What is intersection() in sets? Explain via code.

set_a = {1,2,3,4,5,6}
set_b = {3,6,8,9,10}
print(set_a & set_b)
o/p: {3, 6}
intersection() function returns the values which are common in both sets

Q55. What is dictionary in Python?
 
	Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered, changeable and do not allow duplicates.

Q56. How is dictionary different from all other data structures.

 The dictionary Data Structure in Python is an unordered collection of items.
While other Data Structures use only one value as the element, 
the dictionary is a slightly more compound data structure.
It makes use of two elements i.e. a pair of elements, namely, a key and a value.

Q57. How can we delare a dictionary in Python?
 
	In Python, a dictionary can be created by placing a sequence of elements
within curly {} braces, separated by ‘comma’. Dictionary holds pairs of values, 
one being the Key and the other corresponding pair element being its Key:value. 
Values in a dictionary can be of any data type and can be duplicated, 
whereas keys can’t be repeated and must be immutable. 

Q58. What will the output of the following?
```

var = {}
print(type(var))
```
o/p: <class 'dict'>, it is a dictionary

Q59. How can we add an element in a dictionary?

dict2 = {}
dict2['name'] = 'arjun'
dict2['age'] = 22
dict2['skills'] = ['Python', 'SQL']
print(dict2)

#dict2['name'] = 'arjun', it will add key value pair 
name: arjun into existing dictionary

Q60. Create a dictionary and access all the values in that dictionary.

dict2 = {}
dict2['name'] = 'arjun'
dict2['age'] = 22
dict2['skills'] = ['Python', 'SQL']
dict2['states_visited'] = ('UP', 'Goa')
dict2[45] = 'Random Key'
print(dict2)
for k,v in dict2.items():
  print("values are : ",v)
  
 o/p:
 {'name': 'arjun', 'age': 22, 'skills': ['Python', 'SQL'], 'states_visited': ('UP', 'Goa'), 45: 'Random Key'}
values are :  arjun
values are :  22
values are :  ['Python', 'SQL']
values are :  ('UP', 'Goa')
values are :  Random Key

Q61. Create a nested dictionary and access all the element in the inner dictionary.

dict2 = {}
dict2['name'] = 'arjun'
dict2['age'] = 22
dict2['skills'] = ['Python', 'SQL']
dict2['states_visited'] = ('UP', 'Goa')
dict2[45] = 'Random Key'
dict2['other_details'] = {'color' : 'Black', 'nationality' : 'Indian'}

print(dict2['other_details']['color'])

o/p: Black

Q62. What is the use of get() function?

	The get() method returns the value of the item with the specified key.

dict2.get("skills")
o/p: ['Python', 'SQL']
Q63. What is the use of items() function?

	The items() method returns a view object. The view object contains 
the key-value pairs of the dictionary, as tuples in a list.
The view object will reflect any changes done to the dictionary

Q64. What is the use of pop() function?

	The pop() method removes the item at the given index from the list and returns the removed item.

list1 = list(range(10))
print("original list = ", list1)
list1.pop(9)
print("final list = ", list1)
o/p:
original list =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
final list =  [0, 1, 2, 3, 4, 5, 6, 7, 8]

Q65. What is the use of popitems() function?

	The popitem() method removes the item that was last inserted into the dictionary. 
In versions before 3.7, the popitem() method removes a random item.
Ex:
	dict2.popitem()
        print(dict2)
o/p:
	{'name': 'arjun',
 'age': 22,
 'skills': ['Python', 'SQL'],
 'states_visited': ('UP', 'Goa'),
 45: 'Random Key'}
	
Q66. What is the use of keys() function?

	The keys() method in Python Dictionary, returns a view object that displays
a list of all the keys in the dictionary in order of insertion using Python.

print(dict2.keys())
o/p:
dict_keys(['name', 'age', 'skills', 'states_visited', 45])
Q67. What is the use of values() function? 

	values() is an inbuilt method in Python programming language that returns a view object.
The view object contains the values of the dictionary, as a list.

print(dict2.values())
o/p:
	dict_values(['arjun', 22, ['Python', 'SQL'], ('UP', 'Goa'), 'Random Key'])
	
Q68. What are loops in Python?

	Looping means repeating something over and over until a particular condition is satisfied.
loops used in python are for loop and while loop

Q69. How many type of loop are there in Python?

	3 types of loops are there in python namely for loop, while loop and nested loop

Q70. What is the difference between for and while loops?

for loop:
	
	A for loop is a control flow statement that executes code for a predefined number of iterations. 
The keyword used in this control flow statement is “for”. 
When the number of iterations is already known, the for loop is used.

while loop:
	
	A loop that runs a single statement or a set of statements for a given true condition.
This loop is represented by the keyword "while."When the number of iterations is unknown, 
a "while" loop is used. The statement is repeated until the boolean value is false.

Q71. What is the use of continue statement?
  
	The continue keyword is used to end the current iteration in a for loop or in a while loop,
and continues to the next iteration.

Q72. What is the use of break statement?
  
	break statement in Python is used to bring the control out of the loop when some external 
condition is triggered. break statement is put inside the loop body 

Q73. What is the use of pass statement?

	pass statement can be used in for loop when user doesn’t know what to code inside the loop

Q74. What is the use of range() function?

	The Python range() function returns a sequence of numbers, in a given range. 
Syntax: range(start, stop, step)

Q75. How can you loop over a dictionary?

	looping over a dictionary can be done by using for loop
ex:
    dict = {'a' : 1, 'b' : 2}
for k,v in dict.items():
	print('keys :',k)
o/p:
keys : a
keys : b
### Coding problems
Q76. Write a Python program to find the factorial of a given number.

def factorial(n):

    if n == 0 or n == 1:
        return 1

    result = 1
    for num in range(1, n+1):
        result = result * num
    
    return result
    

Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100

def simple_intrest():
  p = int(input('Enter the principle amount '))
  t = int(input('Enter the time duration in years '))
  r = int(input('Enter Annual rate of intrst '))
  SI = (p*t*r)/100
  return SI

simple_intrest()

 or
  
  def simple_intrest(**kwargs):
   p = kwargs['principle']
   t = kwargs['time']
   r = kwargs['rate']
   SI = (p*t*r)/100
   return SI

simple_intrest(principle = 1000, time = 2, rate = 2)

Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

def compound_intrest(**kwargs):
   p = kwargs['principle']
   t = kwargs['time']
   r = kwargs['rate']
   CI = p*(1+(r/100))**t
   return CI

compound_intrest(principle = 1000, time = 2, rate = 10)

Q79. Write a Python program to check if a number is prime or not.

def is_prime():
  n = int(input('Enter the number '))
  if n > 1:
    for i in range(2,n):  
      if n % i == 0:       # for checking factors of n
        print(n, 'is not a prime number')
        break     #if condition satisfies come out of loop
                  # as 1 multiple is enough
    else:
        print(n, 'is a prime number')

is_prime()
Q80. Write a Python program to check Armstrong Number.

def is_armstring():
  n = input('Enter the number ')
  sum = 0
  for i in n:
    r = int(i)
    sum += r**3
  if sum == int(n):
    print(n, 'is a arm string number')
  else:
    print(n, 'is not a arm string number')
is_armstring()  


Q81. Write a Python program to find the n-th Fibonacci Number.

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(8))

Q82. Write a Python program to interchange the first and last element in a list.

def interchange():
  lst1 = list(input("enter the list : "))
  print("original list : ",lst1)
  last_element = lst1[0]
  lst1[0] = lst1[-1]
  lst1.pop()
  lst1.append(last_element)
  
  print("list after exchanging elements : ",lst1)

interchange()

o/p:
enter the list : 12345
original list :  ['1', '2', '3', '4', '5']
list after exchanging elements :  ['5', '2', '3', '4', '1']

           or 
           
 list = list(input("enter the list : "))
list[0], list[-1] = list[-1], list[0]
print(list)

o/p:
enter the list : 12345
['5', '2', '3', '4', '1']

Q83. Write a Python program to swap two elements in a list.

def swap_pos(lst1,pos1,pos2):
  
  lst1[pos1], lst1[pos2] = lst1[pos2], lst1[pos1]
  return lst1

lst1 = [1,2,3,4,5,6,7]
swap_pos(lst1,1,4)

Q84. Write a Python program to find N largest element from a list.

def Nth_max(n):
  list1 = list(input('enter the list : '))
  print('original list is :',list1)
  list1.sort()
  print('sorted list : ', list1)
  print(list1[-n])


Nth_max(4)

o/p:
enter the list : 123456
original list is : ['1', '2', '3', '4', '5', '6']
sorted list :  ['1', '2', '3', '4', '5', '6']
3

Q85. Write a Python program to find cumulative sum of a list.


def cum_list(list):
  #list must contain only numerics
  sum = 0
  for i in list:
    sum += int(i)
    
  return sum

list = ['1','2','3']
cum_list(list)
  
Q86. Write a Python program to check if a string is palindrome or not.

def is_polyndrome():
  string = str(input("enter the string :"))
  n = len(string)
  print(n)
  for i in range(0,int((n-1)/2)):
    if string[i] != string[(n-1)-i]:
      return ("No!! it is not a polyndrome")
  else:
    return ("yes!!, it is a polyndrome")

is_polyndrome()

o/p:
enter the string :RACECAR
7
yes!!, it is a polyndrome

Q87. Write a Python program to remove i'th element from a string.

def remove_item(str1,i):
  before_index = str1[:i]
  after_index = str1[i+1:]
  final_string = before_index + after_index
  return final_string
str1 = 'arjun'
remove_item(str1,3)

o/p:
   arjn

Q88. Write a Python program to check if a substring is present in a given string.

def sub_string():
  str = input("enter the input :")
  sub_str = input("enter the input :")
  if sub_str in str:
    print('yes!!, it is a substring') 
  else:
    print('No!!, it is not a substring try another')

sub_string()

o/p:
   enter the input :python is fun and joy
enter the input : joy
yes!!, it is a substring

enter the input :python is fun and cool
enter the input :joy
No!!, it is not a substring try another

Q89. Write a Python program to find words which are greater than given length k.

def words_of_length(str,k):
  lst = str.split()
  for i in lst:
    if len(i) > k:
      print(i)
      
    
str = "python is very fun as well as cool"
words_of_length(str,3)

o/p:
   python
   very
   well
   cool
Q90. Write a Python program to extract unquire dictionary values.

def extract_values(dict):
  lst = []
  for k,v in dict.items():
    #print(v)
    lst.append(v)
  #print(lst)
  unique = set(lst)
  print("unique dictionary values are", unique)


dict = { 'a' : 1, 'b' : 2, 'c' : 1}
extract_values(dict)

o/p: 
   unique dictionary values are {1, 2}
Q91. Write a Python program to merge two dictionary.

def merge_dict(dict_1,dict_2):
  dict_1.update(dict_2)
  return dict_1

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

merge_dict(dict_1,dict_2)

o/p:
   {1: 'a', 2: 'c', 4: 'd'}
Q92. Write a Python program to convert a list of tuples into dictionary.
```
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
```

def dict1(list):
  print(dict(list))


list = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
dict1(list)
o/p:
{'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
```
def convertion_list(list):
  list1 = []
  for i in list:
    k = (i,i**3)
    list1.append(k)
  return list1

list = [9, 5, 6]
convertion_list(list)


Q94. Write a Python program to get all combinations of 2 tuples.
```
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
```
def combination(tup1,tup2):
  list1 = [(i,j) for i in tup1 for j in tup2]
  list1 += [(j,i) for j in tup2 for i in tup1]
  return list1

tup1 = (7,2)
tup2 = (7,8)
combination(tup1,tup2)

o/p:
[(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

Q95. Write a Python program to sort a list of tuples by second item.
```
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
```
def sort_tuple(list):
  list.sort(key = lambda list: list[1])
  return list


list = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
sort_tuple(list)
Q96. Write a python program to print below pattern.
```
* 
* * 
* * * 
* * * * 
* * * * * 
```
def shape(len):
  for i in range (len):
    for j in range(i+1):
      print("*", end = " ") #space included
    print()

len = 5
shape(len)

o/p:
* 
* * 
* * * 
* * * * 
* * * * *
Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****
```

def shape(n):
  for i in range(n):
    for j in range(i,n):
      print(' ', end = ' ')
  
    for j in range(i+1):
      print('*', end = ' ') #space between stars included
    print()   

shape(5)

o/p:
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

def triangle(n):
     
    # number of spaces
    k = n - 1
    # outer loop to handle number of rows
    for i in range(0, n):
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")     
        # decrementing k after each loop
        k = k - 1    
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):       
            # printing stars
            print("* ", end="")     
        # ending line after each row
        print()

triangle(5)

o/p: 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

#code for combining increasing and decreasing 
#triangle of stars
def shape(n):
  for i in range(n):
    for j in range(i,n):
      print(' ', end = ' ')
    for j in range(i):
      print("*", end = " ")
    for j in range(i+1):
      print('*', end = " ")
    print()
shape(5)

o/p:
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
```
def shape_num(n):
  for i in range(n):
    for j in range(i+1):
      print(j+1, end = ' ')
    print()

shape_num(5)
o/p:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E 

def shape_alphabet(n):
  p = 65 #ASSCI value for A
  for i in range(n):
    for j in range(i+1):
      print(chr(p), end = ' ')    #chr converts asscci value to character
    p +=1
    print()

shape_alphabet(5)
o/p:
A 
B B 
C C C 
D D D D 
E E E E E
