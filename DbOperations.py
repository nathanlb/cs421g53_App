#!/usr/bin/env python

import random, string
import datetime

# Create User
#    - verify user doesn't exist
#    - insert user with input parameters
def getRandID():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))

# Returns true if entry exists
def entryExists( cur, input, table, field):
    cur.execute("SELECT %s FROM cs421g53.%s WHERE %s = %s", (field, table, input, input))
    fetched = cur.fetchone()
    return fetched != None

# Insert new user into table
def insertUser( conn, cur, username, password, birthday, email ):
    newID = getRandID()
    while entryExists( cur, newID, 'users', 'user_id'):
        newID = getRandID()

    cur.execute("INSERT INTO cs421g53.users (id, user_name, user_password, birthday, email, score) values ('%s', '%s', '%s', '%s', '%s', 0)", (newID, username, password, birthday, email))
    conn.commit()
    return entryExists( cur, newID, 'users', 'user_id')

def validDate( date ):
    try:
        datetime.datetime.strptime(date, '%m/%d/%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be MM/DD/YYYY")

def createUser(conn, cur):
    while true:
        username = input("Enter Username: ")
        if len(username) <= 255:
                break
    while true:
        password = input("Enter Password: ")
        if len(password) <= 255:
                break
    while true:
        birthday = input("Enter Birthday (MM/DD/YYYY): ")
        if validDate(birthday):
                break

    while true:
        email = input("Enter email: ")
        if len(email) <= 255 and not entryExists(cur, email, 'users', 'email'):
                break
   
   if insertUser(conn, cur, username, password, birthday, email):
           print("\nUser successfully created!\n")


        


# Login
#    - verify user exists
#    - compare password
def login():

# Create Post 
#    - generate new post id
#    - insert new post with post with input parameters
def genPostId():

def createPost():

# Submit Restaurant Review
#    - display restaurants in db with index
#    - user chooses index
#    - insert review with input parameters
def displayRestaurants():

def createResReview():

# Submit Recipe Review
#    - display recipes in db with index
#    - user recipe index
#    - insert review with input parameters

def displayRecipes():

def createRecipeReview():