#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().set_next_input('Q1. What is the relationship between classes and modules');get_ipython().run_line_magic('pinfo', 'modules')



get_ipython().set_next_input('Q2. How do you make instances and classes');get_ipython().run_line_magic('pinfo', 'classes')



get_ipython().set_next_input('Q3. Where and how should be class attributes created');get_ipython().run_line_magic('pinfo', 'created')



get_ipython().set_next_input('Q4. Where and how are instance attributes created');get_ipython().run_line_magic('pinfo', 'created')



get_ipython().set_next_input('Q5. What does the term "self" in a Python class mean');get_ipython().run_line_magic('pinfo', 'mean')



get_ipython().set_next_input('Q6. How does a Python class handle operator overloading');get_ipython().run_line_magic('pinfo', 'overloading')



get_ipython().set_next_input('Q7. When do you consider allowing operator overloading of your classes');get_ipython().run_line_magic('pinfo', 'classes')

Q1. What is the relationship between classes and modules?
Solution: Basically, a class can be instantiated but a module cannot. A module will never be anything other than a library of methods. A class can be so much more -- it can hold its state (by keeping track of instance variables) and be duplicated as many times as you want.Q2. How do you make instances and classes?
Sol: To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.


# In[4]:


'''Q3. Where and how should be class attributes created?
Sol: Class attributes are attributes which are owned by the class itself. They will be shared by all the instances of the class. Therefore they have the same value for every instance. We define class attributes outside all the methods, usually they are placed at the top, right below the class header.
EX:''' 
class A:
    a = "I am a class attribute!"

x = A()
y = A()
print(x.a)
print(y.a)
## But be careful, if you want to change a class attribute, you have to do it with the notation ClassName.AttributeName. 
## Otherwise, you will create a new instance variable. 


# In[5]:


'''Q4. Where and how are instance attributes created?
Sol: Instance Attributes are unique to each object, (an instance is another name for an object).
Here, any Dog object we create will be able to store its name and age. 
We can change either attribute of either dog, without affecting any other dog objects we’ve created.
This __init__ is called the initializer. 
It is automatically called when we instantiate the class. 
It’s job is to make sure the class has any attributes it needs. 
It’s sometimes also used to make sure that the object is in a valid state when it’s instantiated, like making sure the user didn’t enter a negative age for the dog.
We have to include the self parameter so that our initializer has a reference to the new object being instantiated.'''
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

Q5. What does the term "self" in a Python class mean?
Sol: self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in pythonQ6. How does a Python class handle operator overloading?
sol:Python operators work for built-in classes. ... For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings. This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading.Q7. When do you consider allowing operator overloading of your classes?
Sol: We will consider allowing operator overloading in our classes when we want to perform perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.