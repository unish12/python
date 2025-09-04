Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a ={'a','b','c'}
print(a)
{'a', 'b', 'c'}
type(a)
<class 'set'>
b={'a','a','b','b'}
type(b)
<class 'set'>
print(b)
{'a', 'b'}
dictionary ={
    "name":"unish",
    "age":19,
    "address":"kathmandu"
    }
type(dictionary)
<class 'dict'>
dict=("hello world")
type(dict)
<class 'str'>
print(dictonary["name"])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(dictonary["name"])
NameError: name 'dictonary' is not defined. Did you mean: 'dictionary'?
print(dictionary["name"])
unish
print(dictionary["age"])
19
print(dictionary["address "])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(dictionary["address "])
KeyError: 'address '
>>> print(dictionary["address"])
kathmandu
>>> dictionary.values
<built-in method values of dict object at 0x000001BBC5703F80>9o
>>> dictionary.values()
dict_values(['unish', 19, 'kathmandu'])
>>> dictionary["nam"]="sita"
>>> print(dictionary)
{'name': 'unish', 'age': 19, 'address': 'kathmandu', 'nam': 'sita'}
>>> dictionary["name"]="ram"
>>> print(dictionary)
{'name': 'ram', 'age': 19, 'address': 'kathmandu', 'nam': 'sita'}
>>> list =["hello",23,34,5,(1,2,1),('a','b')]
>>> print(list)
['hello', 23, 34, 5, (1, 2, 1), ('a', 'b')]
>>> type(list)
<class 'list'>
>>> list[4][0]
1
>>> 
>>> 
>>> 

... 
>>> list[5]
('a', 'b')
>>> gender="sigma"'
SyntaxError: unterminated string literal (detected at line 1)
>>> gender="sigma"
>>> if gender == "male";
SyntaxError: invalid syntax
>>> gender ="gay"
>>> if gender == "mal
SyntaxError: unterminated string literal (detected at line 1)
if gender == "mal
>>> cls
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
