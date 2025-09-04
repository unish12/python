Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name="unish"
print(name)
unish
age ="20"
print(type(age))
<class 'str'>
<class 'str'>
SyntaxError: invalid syntax
age = 20
print(type(age))
<class 'int'>
print(type(name))
<class 'str'>
roll no = 43
SyntaxError: invalid syntax
rollno =32
print(type(rollno))
<class 'int'>
name = 30
print(type(name))
<class 'int'>
cgpa =4.3
name ="unish"
type(cgpa)
<class 'float'>
GPAS=[3.4,3.2,3.6,3.8]
tyoe(GPAS)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tyoe(GPAS)
NameError: name 'tyoe' is not defined. Did you mean: 'type'?
type(GPAS)
<class 'list'>
city,province,country ="kathmandu","Bagmati","Nepal"
print (city,province,country)
kathmandu Bagmati Nepal
graduated = False
type(graduated)
<class 'bool'>
adult =True
a = 20
print (a+audult)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print (a+audult)
NameError: name 'audult' is not defined. Did you mean: 'adult'?
>>> print (a+adult)
21
>>> print(type(adult))
<class 'bool'>
>>> achievements = none
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    achievements = none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> achievements = None
>>> parents = ("sita Aale","Hari balami")
>>> type(parents)
<class 'tuple'>
>>> print(type(parents))
<class 'tuple'>
>>> print(GPAS[0])
3.4
>>> print(type(GPAS[0]))
<class 'float'>
>>> print(GPAS[3])
3.8
>>> print(GPAS[-1])
3.8
>>> print(GPAS[-2])
3.6
>>> print(GPAS[-4])
3.4
>>> print(GPAS[9])
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(GPAS[9])
IndexError: list index out of range
>>> GPAS[-1]=4
>>> print(GPAS)
[3.4, 3.2, 3.6, 4]
>>> parents[0]
'sita Aale'
>>> GPAS[0:4:2]
[3.4, 3.6]
