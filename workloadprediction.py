
#============================= IMPORT LIBRARIES =============================

import pandas as pd
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")

#============================= DATA SELECTION ==============================

dataframe=pd.read_csv("process_data.csv")

print("----------------------------------------------------")
print("Input Data          ")
print("----------------------------------------------------")
print()
print(dataframe.head(20))


#============================= PREPROCESSING ==============================

#==== CHECKING MISSING VALUES ====

print("----------------------------------------------------")
print(" Handling Missing Values          ")
print("----------------------------------------------------")
print()
print(dataframe.isnull().sum())


#============================= DATA SPLITTING ==============================


print("----------------------------------------------------")
print("Data Splitting          ")
print("----------------------------------------------------")
print()

from sklearn.model_selection import train_test_split

X = dataframe.drop('Resources', axis=1)
y = dataframe['Resources']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("Total no of data's       :",dataframe.shape[0])
print()
print("Total no of Train data's :",X_train.shape[0])
print()
print("Total no of Test data's  :",X_test.shape[0])


#============================= CLASSIFICATION ==============================

# === RANDOM FOREST ===


from sklearn import metrics

from sklearn.ensemble import RandomForestClassifier

rf=RandomForestClassifier()

rf.fit(X_train, y_train)

y_pred_rf=rf.predict(X_test)


acc_rf=metrics.accuracy_score(y_pred_rf,y_test)*100
acc_rf=100-acc_rf

print("----------------------------------------------------")
print("Machine Learning ----> Random Forest          ")
print("----------------------------------------------------")
print()
print()
print("1. Accuracy :",acc_rf ,'%')
print()


# ===== Support Vector machine 

from sklearn.svm import SVC  

clf = SVC(kernel='linear') 

clf.fit(X_train, y_train)

y_pred_svm=rf.predict(X_test)

acc_svm=metrics.accuracy_score(y_pred_svm,y_test)*100

acc_svm=100-acc_svm

print("----------------------------------------------------")
print("Machine Learning ----> Support Vector Machine          ")
print("----------------------------------------------------")
print()
print()
print("1. Accuracy :",acc_svm ,'%')
print()


#============= PREDICTION

import tkinter as tk
import os
def show_entry_fields():
    Data_reg = []

    # print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    print(e1.get())
    print(e2.get())
    print(e3.get())
    print(e4.get())
    # print(e5.get())
    # print(e6.get())
    # print(e7.get())
    # print(e8.get())
    Data_reg = [e1.get(),e2.get(),e3.get(),e4.get()]
    
    y_pred_rf=rf.predict([Data_reg])
    print(y_pred_rf)
    print()
    print("Task Allocated Resource = ",y_pred_rf )
    print()
    


    # if e2.get() == e1.get():
    #     os.startfile('Patient_Login.py')

    
    # # Symptoms_list = [e1.get(),e2.get()]
    # # print(Symptoms_list)
    # # open file
    # with open(str(e1.get())+'.txt', 'w+') as f:
         
    #     # write elements of list
    #     for items in Data_reg:
    #         f.write('%s\n' %items)
         
    #     print("Register successfully")
        

 
    # close the file
    # f.close()
    
    
master = tk.Tk()
master.geometry('300x250')

tk.Label(master, 
         text="Job ID : ").grid(row=0)
tk.Label(master, 
         text="Burst Time : ").grid(row=1)
tk.Label(master, 
          text="Arrival Time ").grid(row=2)
tk.Label(master, 
          text="Prremptive ").grid(row=3)
# tk.Label(master, 
#           text="Mobile No. ").grid(row=4)

# tk.Label(master, 
#           text="E-Mail ID ").grid(row=5)
# tk.Label(master, 
#           text="Address ").grid(row=6)
# tk.Label(master, 
#           text="Attribute Key ").grid(row=7)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
# e5 = tk.Entry(master)
# e6 = tk.Entry(master)
# e7 = tk.Entry(master)
# e8 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
# e5.grid(row=4, column=1)
# e6.grid(row=5, column=1)
# e7.grid(row=6, column=1)
# e8.grid(row=7, column=1)

def Close():
    master.destroy()
    
tk.Button(master, 
          text='Quit', 
          command=Close).grid(row=9,column=3,sticky=tk.W,pady=8)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=9, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

                                                          
tk.mainloop()



# =================== Comparison 

import matplotlib.pyplot as plt

import seaborn as sns

sns.barplot(x=['RF','SVM'],y=[acc_rf,acc_svm])

plt.show()







