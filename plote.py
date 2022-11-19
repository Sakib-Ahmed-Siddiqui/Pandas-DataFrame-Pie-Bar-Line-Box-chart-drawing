import pandas as pd
import os.path
import matplotlib.pyplot as plt
import numpy as np
from os import path
import re
import string 
from string import Formatter

menu = ""
dfault_dataset = (r'C:\Users\Administrator\Documents\Python project\file plote\time-use.txt')
dataset = ''



def f_pie():
  
  country_name = input("Enput country: ")
  #print(dataset)
  all_upper = str.upper(country_name)
  first_upper = str.title(country_name)
  df = pd.read_csv(dataset)

  #country = first_upper

  df.set_index('Country', inplace=True)
  my_labels = 'Attending events','Care for household members','Eating and drinking','Education','Housework','Other leisure activities','Other unpaid work & volunteering','Paid work','Personal care','Seeing friends','Shopping','Sleep','Sports','TV and Radio'
  try:
    try:
        df_name = df.loc[first_upper]

        #print(df_name)
    
        plt.pie(df_name, labels = my_labels)
        #plt.pie(df_name, labels = my_labels, autopct='%1.1f%%')
        plt.title('Breakdown of time spent by people in ' + first_upper)
        plt.axis('equal')
        print("Pie chart opens in a new window. Close it to continue...")
        plt.show()
    except KeyError:
        df_name = df.loc[all_upper]
    
        plt.pie(df_name, labels = my_labels)
        #plt.pie(df_name, labels = my_labels, autopct='%1.1f%%')
        plt.title('Breakdown of time spent by people in ' + all_upper)
        plt.axis('equal')
        print("Pie chart opens in a new window. Close it to continue...")
        plt.show()

  except KeyError: 
      print('ERR: That is an invalid or unknown country.')


def f_bar():
	all_df = pd.read_csv('time-use.txt')
	#sort_df = all_df.sort_values(by='Sleep', ascending=False)
	sort_df = all_df.sort_values(by='Sleep', ascending=True)
	df= sort_df.head(10)
	fig, ax = plt.subplots()
	#print(df)

	x = df['Country']
	y = df['Sleep']

	plt.title('When do people sleep for longest time')
	#plt.xlabel('Country', fontsize = 18)
	plt.ylabel('Time(hours)', fontsize = 16)
	plt.bar(x,y)
	plt.xticks(rotation=30)
	ax.set_ylim([450,550])
	print("Bar chart opens in a new window. Close it to continue...")
	plt.show()


def f_line():
	df = pd.read_csv('time-use.txt')
	df2 = df.mean(axis=0)
	#print(df2)

	x= df2[0:]
	plt.title('Worldwide average time spent in different activities')
	#plt.xlabel('', fontsize = 10)
	plt.ylabel('Time(miniutes)', fontsize = 10)
	#print(df2[0:5])
	#plt.plot(x, linestyle = 'dotted')
	plt.plot(x)
	plt.xticks(rotation=90)
	print("Line chart opens in a new window. Close it to continue...")
	plt.show()

def f_box():
	df = pd.read_csv('time-use.txt')
	f = np.random.seed(10)
	box = df['Paid work']
	plt.title('Distribution of time speed in paid work')
	#plt.xlabel('', fontsize = 10)
	plt.ylabel('Time(Hours)', fontsize = 10)
	plt.boxplot(box)
	print("Box chart opens in a new window. Close it to continue...")
	plt.show()

if __name__== "__main__":
  print ("Loading dataset....")
  file_name = input("File Name: ")
  
  if str(path.exists(file_name)) == 'True':
    print ("Dataset Loaded")
    dataset = (r'C:\Users\Administrator\Documents\Python project\file plote\{0}'.format(file_name))
    #print(pd.read_csv(dataset))
  else:
    input ("ERR: File not found...Press Enter to default dataset..")
    dataset = dfault_dataset
    print ("Dataset Loaded")
    #print ("File exists:"+str(path.exists('time-use.txt')))


  while menu != '1' or menu != '2' or menu != '3' or menu != '4' or menu != '5':
    menu = input('\n------Menu------'
                 '\n1. Time components pie chart'
                 '\n2. Top 10 sleep lovers'
                 '\n3. Average activity times'
                 '\n4. Variation in paid-work time'
                 '\n5. Exit'
                 '\nEnter selection: ')

    if menu == '1':
    	f_pie()

    elif menu == '2':
    	f_bar()

    elif menu == '3':
    	f_line()

    elif menu == '4':
    	f_box()

    elif menu == '5':
        exit("Goodbye.")
