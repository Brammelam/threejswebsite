#!C:\Users\bramm\AppData\Local\Programs\Python\Python310\python.exe

import sys
import os
import catt
import random


print("Content-Type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Casting bussruta</title>")
print("</head>")
print("<body>")
print("<h1> Now casting 'Rekk du bussen?'<h1>")
print("</body>")
print("<html>")


try:
    os.system("catt -d 10.0.0.6 cast_site " + "http://bit.ly/3pjDNPC")
    response = {
    "success": True,
    "message": "Cast successfully!"
    }
except Exception as e:
    response = {
    "success": False,
    "message": str(e)
    }

# Set the response headers and print the JSON response
print("Content-Type: application/json")
print()
print(json.dumps(response))
