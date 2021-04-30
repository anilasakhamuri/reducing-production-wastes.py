# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:30:46 2021

@author: anila chowdary
"""
print("********* PRESERVE THE PRECIOUS ************ ")
name_place=input("Enter the name of the place where production to be caculated : ")
number_farmers=int(input("Enter the number of farmers present in that place: "))
number_people=int(input("Enter the number of people living in that place : "))
tpdn=0
tcns=0
list_farmers=[]
list_people=[]
for i in range(number_farmers):
    list_farmers.append(int(input("enter the present farmer production for one year in measure of quintals : ")))
print("total production is : ",sum(list_farmers))
tpdn=sum(list_farmers)
avgpro = tpdn//number_farmers
for k in range(number_people):
    list_people.append(int(input("enter the present family consumption for one year in measure of quintals : ")))
tcns=sum(list_people)
print("total consumption of the people in that city : ",sum(list_people))
avgcns = tcns//number_people
print("the average production for one year in this city: ",avgpro)
print("the average consumption for one year in this city: ",avgcns)
netrate = avgpro-avgcns
print("The amount of crop that remained waste: ",netrate)



























