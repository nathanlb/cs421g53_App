# 
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

import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=cs421 user=cs421g53 password=group5353 host=comp421.cs.mcgill.ca port=5432")


#---------------------------Basic GUI Logic-----------------------------------

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
while(True):
     raw_choice = input("Welcome to Cookbook!\nSelection Menu:\n 1. Quit\n 2. Sign Up\n 3. Make Recipe Post\n\nYour choice: ")
     choice = 0
     try:
          choice = int(raw_choice)
     except:
          print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou made a bad choice! Please try again.")
          continue
     if(choice <= 0 or choice > 3):
          print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou made a bad choice! Please try again.")
          continue
     print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
     if(choice == 1):
          print("Thank you for using Cookbook!")
          conn.close()
          break
     print("You selected: " + str(choice))


#---------------------------Real Database Logic-----------------------------------

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

