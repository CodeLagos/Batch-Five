#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzAB1234567890@!#'
length = input('password length?')
length = int(length)
password = ''
for c in range(length):
   password += random.choice(chars)
print(password)

