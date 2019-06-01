
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_heigh = 74 # inches
my_weight = 180.00 * 0.453592 # lbs to kg
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(my_weight)

print "Let's talk about %s." % my_name
print "He's %d %d inches tall." % (my_heigh, 2)
print("He's {0} kilos heavy.".format(my_weight))
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is trick, try to get it exactly right
print "If I add %d,  %d, and %d I get %d." % (my_age, my_heigh, my_weight, my_age + my_heigh + my_weight)



print('bla 1 = {0}, bla 2 = {1}, bla 3 = {2}'.format(1, 20, 999))
