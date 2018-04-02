'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
def accum(s):
    newstring = ''
    for x in range (0, (len(s)-1)):
        newstring = newstring + s[x].capitalize() + s[x].lower()*(x) + '-'
    newstring = newstring + s[(len(s)-1)].capitalize() + s[len(s)-1].lower()*(len(s)-1)
    return newstring