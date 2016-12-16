#Count the number of Duplicates
#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphanumeric characters, including digits, uppercase and lowercase alphabets.

#Example

#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"aabbcdeB" -> 2 # 'a' and 'b'
#"indivisibility" -> 1 # 'i'
#"Indivisibilities" -> 2 # 'i' and 's'
#"aa11" -> 2 # 'a' and '1'

def duplicate_count(text):
    textList = list(text.lower()) # get a list of letters from the string
    dict = {}
    for i in range(len(textList)):
        if textList.count(textList[i])> 1:# check is a word is repeated more than once
            dict[textList[i]] = textList.count(textList[i]) # if so add them to a dictonary
    return len([ k for k, v in dict.items() if v > 1 ]) # retreive the count of such keys where the value is > 1
