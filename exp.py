#! /data/data/com.termux/files/usr/bin/python3
import speechrecogniser as sr

print ("HELLOW WORLD!")
list1 = ["Santosh" , "Prabha" , "Rahul" , "Sunita" , "Adhya" , "Arya" , "Bhavya" ]
print (len(list1))
tab = int(input("Please input the number for table :"))
for a in range (1,11):
	print(a,"X",tab,"=",(tab*a))
