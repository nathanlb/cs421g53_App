#!/usr/bin/env python

# COMP 421: Project Deliverable 3
# Group 53 (Dylan Sandfelder, Mostafa Saadat, Nathan Lafrance Berger, Thinesh Balakumar)
# 
# PRE-RUN SETUP:
# sudo pip3 install psycopg2
# sudo pip3 install psycopg2-binary
# 
# This file is meant to run using Python 3
# 
# Make sure you are connected to the McGill VPN
# 
from os import system, name
import datetime
import random
import string

import psycopg2
from psycopg2 import sql

# Connect to an existing database
conn = psycopg2.connect("dbname=cs421 user=cs421g53 password=group5353 host=comp421.cs.mcgill.ca port=5432")


# Create User
#    - verify user doesn't exist
#    - insert user with input parameters
def getRandID():
    return ''.join(random.choice(string.digits) for _ in range(9))

# Returns true if entry exists
def entryExists( cur, input, table, field):
    #table = "cs421g53."+table
    query = sql.SQL("SELECT {} FROM {} WHERE {} = %s").format(
          sql.Identifier( field ),
          sql.Identifier( table ),
          sql.Identifier( field )
    )
    data = (input,)
    print(query.as_string(conn))
    cur.execute(query, data)
    fetched = cur.fetchone()
    return fetched != None

# Insert new user into table
def insertUser( cur, username, password, birthday, email ):
    newID = getRandID()
    while entryExists( cur, newID, 'users', 'user_id'):
        newID = getRandID()

    SQL = "INSERT INTO cs421g53.users (user_id, user_name, user_password, birthday, email, score) values (%s, %s, %s, %s, %s, 0)"
    Data = (newID, username, password, birthday, email,)
    print(Data)
    input("Press Enter")
    cur.execute(SQL, Data)
    conn.commit()
    return entryExists( cur, newID, 'users', 'user_id')

def validDate( date ):
    try:
        datetime.datetime.strptime(date, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def createUser(cur):
    while True:
        username = input("Enter Username: ")
        if len(username) <= 255:
                break
    while True:
        password = input("Enter Password (min 6 characters): ")
        if len(password) <= 255 and len(password) >= 6 :
                break
    while True:
        birthday = input("Enter Birthday (MM/DD/YYYY): ")
        if validDate(birthday):
                break

    while True:
        email = input("Enter email: ")
        if len(email) <= 255 and not entryExists(cur, email, 'users', 'email'):
                break
   
    if insertUser(cur, username, password, birthday, email):
           print("\nUser successfully created!\n")


# Login
#    - verify user exists
#    - compare password
def login():
     print("temp")

# Create Post 
#    - generate new post id
#    - insert new post with post with input parameters
def genPostId():
     print("temp")

def createPost():
     print("temp")

# Submit Restaurant Review
#    - display restaurants in db with index
#    - user chooses index
#    - insert review with input parameters
def displayRestaurants():
     print("temp")

def createResReview():
     print("temp")

# Submit Recipe Review
#    - display recipes in db with index
#    - user recipe index
#    - insert review with input parameters
def displayRecipes():
     print("temp")

def createRecipeReview():
     print("temp")

# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#---------------------------Basic GUI Logic-----------------------------------
def main():
     print("\n\n\n\n")
     while(True):
          raw_choice = input("Welcome to Cookbook!\nSelection Menu:\n 1. Create User\n 2. Login\n 3. Make Recipe Post\n 4. Make Restaurant Review\n 5. Make Reciper Review \n 6. Quit \n\nYour choice: ")
          choice = 0
          try:
               choice = int(raw_choice)
          except:
               clear()
               print("You made a bad choice! Please try again.")
               continue
          if(choice <= 0 or choice > 6):
               clear()
               print("You made a bad choice! Please try again.")
               continue
          clear()
          if(choice == 6):
               print("Thank you for using Cookbook!")
               conn.close()
               break
          print("You selected: " + str(choice))

     #---------------------------Real Database Logic-----------------------------------
          try:
               # Choice 1
               if(choice == 1):
                    cur = conn.cursor()
                    createUser(cur)
                    cur.close()

               # Choice 2
               if(choice == 2):
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM cs421g53.Users;")
                    conn.commit()
                    cur.close()

               # Choice 3
               elif(choice == 3):
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM cs421g53.Users;")
                    conn.commit()
                    cur.close()

               # Choice 4
               if(choice == 4):
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM cs421g53.Users;")
                    conn.commit()
                    cur.close()
               
               # Choice 5
               if(choice == 5):
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM cs421g53.Users;")
                    conn.commit()
                    cur.close()
          except Exception as e:
               print(e)
               cur.close()
               conn.close()
               exit()

main()
