#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import csv
filename = '0526_to_0703_UvaldeTexasShooting.csv.gzip.gzip' #input the name of the file
n_lines = 50000 # number of lines to read 
count_files = 0 # number of files that'll get generated , no need to modify
len_of_data = 0 # length of the data, no need to modify
counter = 0 # each iteration, no need to ,modify
index = False # if index is required in the saved csv
compression = 'gzip' #'infer' default, change to default if your file extension is different
path = os.getcwd()+"\\files" #folder in which you want to keep the files


# In[2]:


def create_dir():
    if(os.path.isdir(path)==False):
        os.mkdir(path)


# In[10]:


def split_files_and_save():
    while True:
        global filename
        global counter
        global path
        global n_lines
        global len_of_data
        global compression
        global index
        global count_files
        begin,end = counter*n_lines,counter*n_lines+n_lines
        print("reading file for - start index: "+str(begin)+"   - end index: "+str(end))   
        df = pd.read_csv(filename, engine='python', compression=compression,encoding='utf-8', quoting=csv.QUOTE_ALL,  skiprows = [i for i in range(1, begin) ], index_col=0, nrows=n_lines)
        print("Head:",df.index[1],"\tTail:",df.index[-1])
        if(len(df)<n_lines):
            print("List of Columns = ",df.columns)
            break
        else:
            count_files+=1
            len_of_data += len(df)
            print("saving dataframe of length: "+str(len(df)))
            df.to_csv(path+"\\start-"+str(begin)+"_end-"+str(end)+"_len-"+str(len(df))+".csv",index=index)
            print("file saved: ",path+"\\start-"+str(begin)+"_end-"+str(end)+"_len-"+str(len(df))+".csv")
        counter+=1
    print("Number of files generated is : ",count_files)
    print("Length of data in CSV is : ",len_of_data)
    print("The files can be found in : ",path)


# In[ ]:


create_dir()
split_files_and_save()


# In[ ]:




