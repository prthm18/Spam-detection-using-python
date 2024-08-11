#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle
import win32com.client
import tkinter as tk


# In[ ]:


data=pd.read_csv("spam1.csv", encoding="latin-1")


# In[ ]:


data.head()


# In[ ]:


data.columns


# In[ ]:


data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)


# In[ ]:


data.head()


# In[ ]:


data['v1']=data['v1'].map({'ham':0, 'spam':1})


# In[ ]:


data.head()


# In[ ]:





# In[ ]:





# In[ ]:


X=data['v2']
y=data['v1']


# In[ ]:


X.shape


# In[ ]:


y.shape


# In[ ]:


data.isnull().sum()


# In[ ]:


cv=CountVectorizer()


# In[ ]:


X=cv.fit_transform(X)


# In[ ]:


x_train, x_test,y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=42)


# In[ ]:


x_train.shape


# In[ ]:


x_test.shape


# In[ ]:





# In[ ]:


model=MultinomialNB()


# In[ ]:


model.fit(x_train, y_train)


# In[ ]:


model.score(x_test, y_test)


# In[ ]:


msg="You Won 500$"
data = [msg]
vect = cv.transform(data).toarray()
my_prediction = model.predict(vect)


# In[ ]:


vect


# In[ ]:



pickle.dump(model, open('spam.pkl','wb'))
model1 = pickle.load(open('spam.pkl','rb'))


# In[ ]:





# In[ ]:





# In[ ]:


def speak(text):
	speak= win32com.client.Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)


# In[ ]:


def result(msg):
    data = [msg]
    vect = cv.transform(data).toarray()
    my_prediction = model1.predict(vect)
    if my_prediction[0]==1:
        speak("This is a Spam mail")
        print("This is a Spam mail")
    else:
        speak("This is not a Spam mail")
        print("This is not a Spam mail")


# In[ ]:





# In[ ]:



root=tk.Tk()

root.geometry("200x200")
l2=tk.Label(root, text="Email Spam Classification Application")
l2.pack()
l1=tk.Label(root, text="Enter Your Message:")
l1.pack()
text=tk.Entry(root)
text.pack()
def result():
    data = [text.get()]
    vect = cv.transform(data).toarray()
    my_prediction = model1.predict(vect)
    if my_prediction[0]==1:
        speak("This is a Spam mail")
        print("This is a Spam mail")
    else:
        speak("This is not a Spam mail")
        print("This is not a Spam mail")
B=tk.Button(root, text="Click", command=result)
B.pack()
root.mainloop()


# In[ ]:





# In[ ]:




