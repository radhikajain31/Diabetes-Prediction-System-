# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading
loaded_model=pickle.load(open('C:/Users/Arnav Jain/Desktop/New folder/trained_diabetesmodel.sav','rb'))
new_data=(0,118,84,47,230,45.8,0.551,31)
new_data=np.asarray(new_data)
new_data=new_data.reshape(1,-1)



predict1=loaded_model.predict(new_data)
if(predict1[0]==1):
  print("DIABETES")
else:
  print("You are Healthy")