#Create a function that can receive two 'fangs' and determine if the product of the two is a valid vampire number.

#6 * 21 = 126
# 6 and 21 would be valid 'fangs' for a vampire number as the
# digits 6, 1, and 2 are present in both the product and multiplicands

#10 * 11 = 110
# 110 is not a vampire number since there are three 1's in the
# multiplicands, but only two 1's in the product

def vampire_test(x, y):
	value = x * y
	value_as_list = [ int(a) for a in str(value) if str(a).isdigit() ]
	multiplicant_as_list = [ int(i) for i in str(x) if str(i).isdigit() ] + [ int(i) for i in str(y) if str(i).isdigit() ]
	sign_for_product = "-" if value < 0 else "+"
	sign_for_multiplicant_x = "-" if x < 0 else "+"
	sign_for_multiplicant_y = "-" if y < 0 else "+"
	return True if sorted(value_as_list) == sorted(multiplicant_as_list) and (sign_for_product == sign_for_multiplicant_x or sign_for_product == sign_for_multiplicant_y) else False
