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

# Current logged in user
currentUser = ""


#---------------------------Function Definitions-----------------------------------

# define our clear function 
def clear(): 
     # for windows 
     if name == 'nt': 
          _ = system('cls') 
  
     # for mac and linux(here, os.name is 'posix') 
     else: 
          _ = system('clear')


# -----------------------------------------------------------------------------------------------
# Create User
#    - verify user doesn't exist
#    - insert user with input parameters
def getRandID():
     return ''.join(random.choice(string.digits) for _ in range(9))


# Returns true if entry exists
def entryExists( cur, input, table, field):
     query = sql.SQL("SELECT {} FROM {} WHERE {} = %s").format(
          sql.Identifier( field ),
          sql.Identifier( table ),
          sql.Identifier( field )
     )
     data = (input,)
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
     global currentUser
     while True:
          username = input("Enter Username [type 'q' to quit]: ")
          if username == 'q':
               clear()
               return False
          elif len(username) <= 255:
               break
     while True:
          password = input("Enter Password (min 6 characters) [type 'q' to quit]: ")
          if password == 'q':
               clear()
               return False
          elif len(password) <= 255 and len(password) >= 6 :
                break
     while True:
          birthday = input("Enter Birthday (MM/DD/YYYY) [type 'q' to quit]: ")
          if birthday == 'q':
               clear()
               return False
          elif validDate(birthday):
                break
     while True:
          email = input("Enter email [type 'q' to quit]: ")
          if email == 'q':
               clear()
               return False
          elif len(email) <= 255 and not entryExists(cur, email, 'users', 'email'):
                break
     if insertUser(cur, username, password, birthday, email):
          clear()
          print("\nUser successfully created!\n")
          currentUser = username
          return True


# -----------------------------------------------------------------------------------------------
# Login
#    - verify user exists
#    - compare password
def validatePassword(cur, username, password):
     query = "SELECT user_password FROM users WHERE user_name = %s AND user_password = %s"
     data = (username, password)
     cur.execute(query, data)
     fetched = cur.fetchone()
     return fetched != None


def login(cur):
     global currentUser
     while True:
          username = input("Enter Username [type 'q' to quit]: ")
          if username == 'q':
               clear()
               return False
          elif len(username) <= 255 and entryExists(cur, username, 'users', 'user_name'):
               break
          else:
               print("Username does not exist.")

     while True:
          password = input("Enter Password [type 'q' to quit]: ")
          if password == 'q':
               clear()
               return False
          elif len(username) <= 255 and validatePassword(cur, username, password):
               currentUser = username
               clear()
               return True
          else:
               print("Invalid password")


# -----------------------------------------------------------------------------------------------
# Create Post 
#    - generate new post id
#    - insert new post with post with input parameters
def getUserID(cur, username):
     cur.execute("SELECT user_id FROM users WHERE user_name = %s", (username,))
     fetched = cur.fetchone()
     return str(fetched)[1:-2]


def insertPost( cur, instructions, recipe_name ):
     newID = getRandID()
     while entryExists( cur, newID, 'recipe_posts', 'post_id'):
          newID = getRandID()
     UserID = getUserID(cur, currentUser)
     now = datetime.datetime.now()
     curDate = str(now.strftime("%m/%d/%Y"))
     SQL = "INSERT INTO cs421g53.recipe_posts (post_id, user_id, instructions, recipe_name, date_made) values (%s, %s, %s, %s, %s)"
     Data = (newID, UserID, instructions, recipe_name, curDate)
     cur.execute(SQL, Data)
     conn.commit()
     return entryExists( cur, newID, 'recipe_posts', 'post_id')


def createPost(cur):
     if(currentUser == ""):
          clear()
          print("You cannot create a post if you are not logged in!")
          return False
     while True:
          recipe_name = input("Enter the name of your recipe [type 'q' to quit]: ")
          if recipe_name == 'q':
               clear()
               return False
          elif len(recipe_name) <= 255:
               break
     while True:
          instructions = input("Enter the steps of your recipe (min 6 characters) [type 'q' to quit]:\n")
          if instructions == 'q':
               clear()
               return False
          if len(instructions) <= 255 and len(instructions) >= 6:
               break   
     if insertPost(cur, instructions, recipe_name):
          clear()
          print("\nPost successfully created!\n")


# -----------------------------------------------------------------------------------------------
# Submit Restaurant Review
#    - display restaurants in db with index
#    - user chooses index
#    - insert review with input parameters
def displayRestaurants():
     print("temp")


def createResReview():
     print("temp")


# -----------------------------------------------------------------------------------------------
# Submit Recipe Review
#    - display recipes in db with index
#    - user recipe index
#    - insert review with input parameters
def getUsername(cur, userID):
     cur.execute("SELECT user_name FROM users WHERE user_id = %s", (userID,))
     fetched = cur.fetchone()
     return str(fetched)[1:-2]


def getRecipeReviews(cur, postID):
     cur.execute("SELECT user_id, content, rating FROM recipe_reviews WHERE post_id = %s", (postID,))
     fetched = cur.fetchall()
     return fetched


def createRecipeReview(cur, postID, content, rating):
     newID = 0
     curReviews = getRecipeReviews(cur, str(postID))
     if(len(curReviews) > 0):
          newID = len(curReviews)
     global currentUser
     UserID = getUserID(cur, currentUser)
     SQL = "INSERT INTO cs421g53.recipe_reviews (recipe_rev_index, rating, content, post_id, user_id) values (%s, %s, %s, %s, %s)"
     Data = (newID, rating, content, str(postID), str(UserID))
     cur.execute(SQL, Data)
     conn.commit()
     return True


def displayRecipes(cur):
     clear()
     cur.execute("SELECT user_id, recipe_name, instructions, date_made, post_id FROM recipe_posts")
     fetched = cur.fetchall()
     for recipe in fetched:
          username = getUsername(cur, str(recipe[0]))
          reviews = getRecipeReviews(cur, str(recipe[4]))
          print("'" + str(recipe[1]) + "'")
          print("     User: " + str(username))
          print("     Instructions: " + str(recipe[2]))
          print("     Created On: " + str(recipe[3]))
          print("")
          if(reviews == []):
               print("This recipe has no reviews.\n")
          else:
               print("Recipe Reviews:\n")
               for review in reviews:
                    revUser = getUsername(cur, str(review[0]))
                    print("     " + revUser + ": " + str(review[1]) + " | Rating: " + str(review[2]) + "\n")
          while True:
               raw_choice = input("What do you want to do?\n 1. Review the recipe\n 2. See the next recipe\n 3. Quit\nYour Selection: ")
               choice = 0
               try:
                    choice = int(raw_choice)
               except:
                    clear()
                    print("'" + str(recipe[1]) + "'")
                    print("     User: " + str(username))
                    print("     Instructions: " + str(recipe[2]))
                    print("     Created On: " + str(recipe[3]))
                    print("")
                    if(reviews == []):
                         print("This recipe has no reviews.\n")
                    else:
                         print("Recipe Reviews:\n")
                         for review in reviews:
                              revUser = getUsername(cur, str(review[0]))
                              print("     " + revUser + ": " + str(review[1]) + " | Rating: " + str(review[2]) + "\n")
                    print("You made a bad choice! Please try again.")
                    continue
               if(choice <= 0 or choice > 3):
                    clear()
                    print("'" + str(recipe[1]) + "'")
                    print("     User: " + str(username))
                    print("     Instructions: " + str(recipe[2]))
                    print("     Created On: " + str(recipe[3]))
                    print("")
                    if(reviews == []):
                         print("This recipe has no reviews.\n")
                    else:
                         print("Recipe Reviews:\n")
                         for review in reviews:
                              revUser = getUsername(cur, str(review[0]))
                              print("     " + revUser + ": " + str(review[1]) + " | Rating: " + str(review[2]) + "\n")
                    print("You made a bad choice! Please try again.")
                    continue
               elif(choice == 3):
                    clear()
                    return True
               elif(choice == 2):
                    clear()
                    break
               elif(choice == 1):
                    global currentUser
                    if(currentUser == ""):
                         clear()
                         print("'" + str(recipe[1]) + "'")
                         print("     User: " + str(username))
                         print("     Instructions: " + str(recipe[2]))
                         print("     Created On: " + str(recipe[3]))
                         print("")
                         if(reviews == []):
                              print("This recipe has no reviews.\n")
                         else:
                              print("Recipe Reviews:\n")
                              for review in reviews:
                                   revUser = getUsername(cur, str(review[0]))
                                   print("     " + revUser + ": " + str(review[1]) + " | Rating: " + str(review[2]) + "\n")
                         print("You are not logged in!")
                         continue
                    while True:
                         newRevContent = input("Write your review:\n")
                         if(len(newRevContent) > 255):
                              continue
                         newRevRating = input("Please give a rating: ")
                         revRating = 0
                         try:
                              revRating = int(newRevRating)
                         except:
                              continue
                         createRecipeReview(cur, str(recipe[4]), newRevContent, str(revRating))
                         break
                    clear()
                    print("'" + str(recipe[1]) + "'")
                    print("     User: " + str(username))
                    print("     Instructions: " + str(recipe[2]))
                    print("     Created On: " + str(recipe[3]))
                    print("")
                    reviews = getRecipeReviews(cur, str(recipe[4]))
                    if(reviews == []):
                         print("This recipe has no reviews.\n")
                    else:
                         print("Recipe Reviews:\n")
                         for review in reviews:
                              revUser = getUsername(cur, str(review[0]))
                              print("     " + revUser + ": " + str(review[1]) + " | Rating: " + str(review[2]) + "\n")
                    continue
     return True


#---------------------------Basic GUI Logic-----------------------------------

def main():
     clear()
     while(True):
          global currentUser
          if(currentUser == ""):
               print("Welcome to Cookbook! You are not logged in.")
          else:
               print("Welcome to Cookbook "+currentUser+"!")
          raw_choice = input("Selection Menu:\n 1. Create User\n 2. Login\n 3. Create Recipe Post\n 4. View Recipes\n 5. View Restaurants\n 6. Logout\n 7. Quit \n\nYour choice: ")
          choice = 0
          try:
               choice = int(raw_choice)
          except:
               clear()
               print("You made a bad choice! Please try again.")
               continue
          if(choice <= 0 or choice > 7):
               clear()
               print("You made a bad choice! Please try again.")
               continue
          clear()
          if(choice == 7):
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
                    login(cur)
                    cur.close()

               # Choice 3
               elif(choice == 3):
                    cur = conn.cursor()
                    createPost(cur)
                    conn.commit()
                    cur.close()

               # Choice 4
               if(choice == 4):
                    cur = conn.cursor()
                    displayRecipes(cur)
                    conn.commit()
                    cur.close()
               
               # Choice 5
               if(choice == 5):
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM cs421g53.Users;")
                    conn.commit()
                    cur.close()

               # Choice 6
               if(choice == 6):
                    clear()
                    currentUser = ""

          except Exception as e:
               print(e)
               cur.close()
               conn.close()
               exit()

main()
