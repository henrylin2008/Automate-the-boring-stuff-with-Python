import re

# Passing a string value representing your regular expression to re.compile() returns a Regex pattern object
# (or simply, a Regex object).
#
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# A Regex object’s search() method searches the string it is passed for any matches to the regex.
# The search() method will return None if the regex pattern is not found in the string. If the pattern is found, the search() method returns a Match object.

mo = phoneNumRegex.search('My number is 415-555-4242.')

# Match objects have a group() method that will return the actual matched text from the searched string.

print('Phone number found: ' + mo.group())

# output: Phone number found: 415-555-4242


# Review of Regular Expression Matching
# While there are several steps to using regular expressions in Python, each step is fairly simple.
# 1. Import the regex module with import re.
# 2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
# 3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
# 4. Call the Match object’s group() method to return a string of the actual matched text.
#
# Shorthand character  Represents
# \d                   Any numeric digit from 0 to 9.
# \D                   Any character that is not a numeric digit from 0 to 9.
# \w                   Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W                   Any character that is not a letter, numeric digit, or the underscore character.
# \s                   Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S                   Any character that is not a space, tab, or newline.


# The ? matches zero or one of the preceding group.
# The * matches zero or more of the preceding group.
# The + matches one or more of the preceding group.
# The {n} matches exactly n of the preceding group.
# The {n,} matches n or more of the preceding group.
# The {,m} matches 0 to m of the preceding group.
# The {n,m} matches at least n and at most m of the preceding group.
# {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# ^spam means the string must begin with spam.
# spam$ means the string must end with spam.
# The . matches any character, except newline characters.
# \d, \w, and \s match a digit, word, or space character, respectively.
# \D, \W, and \S match anything except a digit, word, or space character, respectively.
# [abc] matches any character between the brackets (such as a, b, or c).
# [^abc] matches any character that isn’t between the brackets.
#

# Case-Insensitive Matching:
# To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().
# robocop = re.compile(r'robocop', re.I)
# >>> robocop = re.compile(r'robocop', re.I)
# >>> robocop.search('RoboCop is part man, part machine, all cop.').group()
# 'RoboCop'
#
# sub() method:
# The sub() method for Regex objects is passed two arguments. The first argument is a string to replace any matches. The second is the string for the regular expression.
# The sub() method returns a string with the substitutions applied.
# >>> namesRegex = re.compile(r'Agent \w+')
# >>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'CENSORED gave the secret documents to CENSORED.'

#Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
# >>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
