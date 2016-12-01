#!/usr/bin/python
__author__ = "Sriram Jayaraman"

import MySQLdb

def dbConnect():
  cursor.execute('CREATE DATABASE IF NOT EXISTS python;')
  cursor.execute("USE python")
  cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT(6)  UNSIGNED AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(30) NOT NULL);")	

def dbLink(name):
  cursor.execute("INSERT INTO users (firstname) VALUES (%s)",(name))
  db.commit()

def checkName(name):
  flag = 0
  cursor.execute("SELECT firstname FROM users")
  data = cursor.fetchall()
  for row in data :
    if name == row["firstname"]:
     flag = 1
     break

  if flag == 1 :
    checkName = raw_input("Is your name " + name + "? ") 
    if checkName.lower() == "yes":    
     print "Hello, " + name  
    else:    
     name = raw_input("We're sorry about that. What is your name again?")
     checkName(name)    
  else :
    dbLink(name)
    print "Welcome aboard, "+ name

db = MySQLdb.connect(host="localhost", user="root", passwd="root")
cursor = db.cursor(MySQLdb.cursors.DictCursor)
dbConnect()
uname = raw_input("Enter your name: ")
checkName(uname)
