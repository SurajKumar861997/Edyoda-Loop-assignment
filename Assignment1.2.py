#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      hp1
#
# Created:     16-07-2022
# Copyright:   (c) hp1 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Write a Python program that accepts a word from the user and reverse it.
str1 = input("Enter a word for reverse : ") #User input the word
for x in range(len(str1)-1,-1,-1): # Defining the range to reverse the given word
    print(str1[x], end = "")  # 'end' parameter is used to print the output in asingle line