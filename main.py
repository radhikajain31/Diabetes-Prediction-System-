# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:37:34 2024

@author: Arnav Jain
"""

import numpy as np 
import pickle 
import streamlit as st

loaded_model=pickle.load(open('./trained_diabetesmodel.sav','rb'))


def diab_pred(input_data):
    new_data=np.asarray(input_data)
    new_data=new_data.reshape(1,-1)



    predict1=loaded_model.predict(new_data)
    if(predict1[0]==1):
      return "Diabetes"
    else:
      return "You are Healthy"

    
def main():
    
    #giving title
    
    st.title('Diabetes Prediction WebApp')


# takeing ip

#Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
  

    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose Lvl')
    BloodPressure=st.text_input('BloodPressure value')
    SkinThickness=st.text_input('SkinThickness value')
    Insulin=st.text_input('Insulin Lvl')
    BMI=st.text_input('BMI value ')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
    Age=st.text_input('Age of the Person')

       
  
    diagnosis=''
    
    
    
    if st.button('Diabetes Test Result'):
        diagnosis=diab_pred([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])




    st.success(diagnosis)
    


if __name__=='__main__':
    main()





















    
