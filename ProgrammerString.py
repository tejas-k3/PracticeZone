""" Programmer String
A programmer string contains letters that can be rearranged to form
the word 'programmer' and is a substring of a longer string. Note that
the strings 'programmer', 'grammeproer', and 'prozmerqgram' are all
classifed as programmer strings by this definition. Given a string,
determine the number of indices taht lie between the rightmost and
leftmost programmer strings that it contains.
######## EXAMPLE ################
s = `programmerxxxprozmerqgram` #
#################################
In this example, indices 0-9 form one programmer string & indices 13-24
contains another. There are 3 indices between the programmer, so the
function returns 3. Write a function `programmerString` which takes 
string input & returns int value which is difference between both the strings
"""
