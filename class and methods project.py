#!/usr/bin/env python
# coding: utf-8

# In[2]:


class character():

    def __init__(self,name):
        self.name=name
        self.__score=0
        self.__life=3
        
    def welcome(self):
        return "Wellcome to fight game"
    
    def user(self):
        self.user=input("Player name:-")
    
    def gameon(self):
        print("Get ready to fight",self.user)    

    def displaylife(self):
        return self.__life
    
    def displayscore(self):
        return self.__score
    
    def matchstatus(self):
        win=20
        health=0
        if self.__score>=win:
            print("Victory")
        elif self.__life==health:
            print("Game Over")
        else:
            print("Still you are in game play smart You can do it")
    
    def punch(self):
        self.__score=self.__score+5
    def kick(self):
        self.__score=self.__score+10
    def knockout(self):
        self.__score=self.__score+15
        
    def stabbed(self):
        self.__life=self.__life -1
        
    def Rules(self):
        print("Game rules of Aman fight club as follows: \n\n"+"Punch->5 points \n"+"kick->10 points \n"+ "knockout->15 points \n"+ "Stabbed-> Total life 3 if stabbed 1 life lost \n" "Victory-> 20 points needed \n\n")
        
    def scores(self):
        print("Game name:-",self.name)
        print("Initial Score:-",self.displayscore())
        print("Initial Life:-",self.displaylife())
        
cool=character("Aman fight club")
cool.Rules()  

cool.scores()


# In[3]:


cool.welcome()


# In[4]:


cool.user()


# In[5]:


cool.displayscore()


# In[6]:


cool.matchstatus()


# In[7]:


cool.stabbed()


# In[8]:


cool.stabbed()


# In[9]:


cool.knockout()


# In[10]:


cool.matchstatus()


# In[11]:


cool.scores()


# In[12]:


cool.knockout()


# In[13]:


cool.scores()


# In[14]:


cool.matchstatus()


# In[ ]:




