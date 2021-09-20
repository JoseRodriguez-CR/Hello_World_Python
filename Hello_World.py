# 1. TASK: print "Hello World"
print( "Hello World" )

# 2. print "Hello Noelle!" with the name in a variable
name = "Jose Mario"
print( "Hello", name )	# with a comma
print( "Hello " + name )	# with a +

# 3. print "Hello 42!" with the number in a variable
name = 70
print( "Hello", name  )	# with a comma
#print( "Hello " + name  )	# with a +	-- this one should give us an error!
print( "Hello " + str(name)  )	# with a +	str() the error -- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variablescopy
fave_food1 = "hamburger"
fave_food2 = "gallo pinto"
print( "I love to eat {} and {}." .format(fave_food1, fave_food2))  # with .format()
print( "I love to eat %s and %s." % (fave_food1, fave_food2))       # with an f str

#NINJA BONUS: Spend a few minutes playing around with other string methods to see what’s out there!
x = "hey guys, jose here. i'm pretty excited to be here learning python."
print(x.title())
# output: Hey Guys, Jose Here. I'M Pretty Excited To Be Here Learning Python 
y = "THIS IS A ERROR MESSAGE, YOUR COMPUTER IS GOING TO BE RESTARTED RIGHT NOW"
print(y.lower())
# output: this is a error message, your computer is going to be restarted right now
