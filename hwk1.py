#------------------------
#--------hwk1.py---------
#-----by PJ Sheldon------
#------------------------

#first name input
firstname = input('what is your First name?')

#last name input
lastname = input('What is your last name?')

#full name variable
fullname = firstname + " " + lastname

#concatination 
print('SEC 290 welcomes ' + fullname + ' to the World of Python!')

#String format
print("{} {} {}".format('SEC 290 welcomes', fullname, 'to the World of Python!'))
