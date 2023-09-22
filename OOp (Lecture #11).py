#!/usr/bin/env python
# coding: utf-8

# In[5]:


dir("")


# In[10]:


class Apple:
    pass
class Apple:
    colour=""
    flavour=""
    
jonagold= Apple()
jonagold.colour= "red"
jonagold.flavour= "sweet"
print(jonagold.colour)
print(jonagold.flavour)


# In[12]:


class Apple:
    pass
class Apple:
    colour=""
    flavour=""
    
jonagold= Apple()
jonagold.colour= "red"
jonagold.flavour= "sweet"
print(jonagold.colour.upper())
print(jonagold.flavour.lower())


# In[14]:


gold = Apple()
gold.colour = "green"
gold.flavour =" tart"
print(gold.colour.upper())
print(gold.flavour.lower())
goldi = Apple()
goldi.colour = "yellow"
goldi.flavour =" sour"
print(goldi.colour.upper())
print(goldi.flavour.lower())


# In[23]:


class Flower:
    color= "unknown"
rose = Flower()
rose.color= "red"

voilet = Flower()
voilet.color = "blue"

forYOu= "this for you"

print("roses are {},".format(rose.color))
print("voilet are {},".format(voilet.color))
print(forYOu)


# In[24]:


class Cat:
    name= ""
    def speak (self):
        print("meow {},".format(self.name))
        
myluna = Cat()
myluna.name="luna"
myluna.speak()


# In[30]:


class Animal:
    name=""
    def speak(self):
        print("cow {},".format(self.name))
    
bella = Animal()
bella.name ="Bella"
bella.speak()


# In[34]:


class Cat:
    year=0
    def age (self):
        return self.year*12
mycat =Cat()
mycat.years =2
mycat.age()


# In[43]:


class Apple:
    def __init__(self,color,flover):
        self.color = color
        self.flover = flover
jonagold = Apple("red","sweet")
print(jonagold.color)
print(jonagold.flover)


# In[45]:


class Apple:
    def __init__(self,color,flover):
        self.color = color
        self.flover = flover
    def __str__(self):
        return("this apple is{},this flover is{}," .format(self.color,self.flover))
jonagold = Apple("red","sweet")
print(jonagold.color)
print(jonagold.flover)


# In[46]:


help(Apple)


# In[49]:


def t0second(hours,minutes,seconds):
    """this is hours"""
    returns (hours*3600+minutes*60+seconds)


# In[50]:


help(t0second)


# In[54]:


class Person:
    def __init__ (self,name):
        self.name=name
    def greeting(self):
        """namae of the person"""
        print("my name {name}.".format(name=self.name))   


# In[55]:


help(Person)


# In[60]:


class Fruit:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
class Apple(Fruit):
     pass
class Grapes(Fruit):
    pass
jonagold = Apple("red","sweet")
gold = Grapes("Green","sour")
print(jonagold.color)
print(jonagold.flavor)
print(gold.color)
print(gold.flavor)


# In[66]:


class Clothing:
    material=""
    def __init__(self,name):
        self.name= name
    def checkmatereial(self):
        print("this is {}made of {},".format(self.name,self.material))
        
class shirt(Clothing):
    material ="cotton"  
    
polo = shirt("polo")
polo.checkmaterial()


# In[ ]:




