# -*- coding: utf-8 -*-
"""CustomerChurn Picklefile exec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iGgoSaBgk_Gx_cB79tkF3Aqu1_C_27S8
"""

import pickle

with open('customer_churn.pkl','rb') as file:
  clf = pickle.load(file)

prediction = clf.predict([[0,29.85,29.85,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,1,1,0,1]])

if(prediction == 0):
  print('The customer will not churn')
else:
  print('The customer will churn')

