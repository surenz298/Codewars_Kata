#A digital root is the recursive sum of all the digits in a number.
#Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

#digital_root(16)
#=> 1 + 6
#=> 7

#digital_root(942)
#=> 9 + 4 + 2
#=> 15 ...
#=> 1 + 5
#=> 6

def digital_root(n):
    parse_number_as_list = [ int(x) for x in str(n) ]
    sum_of_list = 0
    while len(parse_number_as_list) > 1:
        for items in parse_number_as_list:
            sum_of_list += items
        parse_number_as_list = [ int(x) for x in str(sum_of_list) ]
        sum_of_list = 0
    return int(parse_number_as_list[0])
