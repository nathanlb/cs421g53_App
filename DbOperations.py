#!/usr/bin/env python

import random, string

# Create User
#    - verify user doesn't exist
#    - insert user with input parameters
def getRandID():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))

def verifyUser( cur, email ):
    cur.execute("SELECT email FROM cs421g53.users WHERE email = %s", email)
    fetchedUser = cur.fetchone()
    return fetchedUser != None

def insertUser( cur, id, username, password, birthday, email ):

    newID = getRandID()
    cur.execute("SELECT  FROM cs421g53.users WHERE email = %s", email)
    fetchedUser = cur.fetchone()

    cur.execute("INSERT INTO cs421g53.users (id, user_name, user_password, birthday, email, score) values ('%s', '%s', '%s', '%s', '%s', 0)", (id, username, password, birthday, email))

def createUser():


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