import re

#https://automatetheboringstuff.com/2e/chapter7/ - READ this for complete regex information.

'''
.* (Greedy match)

.: This matches any character except a newline (so it can match letters, digits, spaces, punctuation, etc.).
*: This is a quantifier that means "zero or more occurrences" of the preceding element (in this case, any character).
Greedy means that .* will match as many characters as possible. It tries to match as much as it can, even if it means it will consume more characters than needed.


.*? (Non-greedy match)
    .: Matches any character except a newline.
    *: Means "zero or more occurrences" of the preceding element.
    ?: This is what makes the match non-greedy. It means "match as few characters as possible" while still satisfying the rest of the pattern.
        Difference between Greedy .* and Non-Greedy .*?
    Greedy .* tries to match everything that satisfies the pattern. It will keep matching characters until it finds the last possible valid match that fits the entire regular expression.
    Non-Greedy .*? tries to match the smallest number of characters needed to satisfy the pattern. It stops at the first valid match it can find.
'''

# Non-greedy version to match shortest possible sequence
batRegex = re.compile(r"Iron.*?man")  # .* will match ironman ironman ironman - as ONE string.
# .*? will create a list and return 3 matches.

# Test string
result = re.findall(batRegex, "Ironman Ironmanwowowowman Ironmanwow Ironmanhello Ironmanagain")

# Print the matches
for i in result:
    print("Match found:", i)



names = re.compile(r'First Name: (.*?) Last Name: (\S+)')  #anything that is not space tab or newline and one or more times.
name = "First Name: Ajay kumar Last Name: Prahladbhai here"

result = names.search(name)

print("name is -> ", result)


text = "<to serve humans> for dinner>"
non_greedy = re.compile(r'<(.*?)>')
result = non_greedy.findall(text)
print(result)

greedy = re.compile(r'<(.*)>')
result = greedy.findall(text)
print(result)

"""
?  -> says the group matches zero or [[one]] times. 
*  -> group matches zero or [[more]] times. 
+  -> says the group matches [[one]] or more times. 
{3} -> can match a specific number of times. 
{3,4} -> matches maximum and minimum number of times. 
{3,} -> says there is no minimum or maximum.  (min 3 and more )

re.compile(r'\d+\s\w+') -- starts with digit that can be one or more digits. then space then words one or more times.

greedy matching match the longest string possible, non greedy match the shortest string possible.
putting a question mark after the curly braces makes it do a non greedy match. 

--- Shorthand codes for common character class

\d - any numeric digit from 0 to 9
\D - any character that is not a numeric from 0 to 9

\w - any letter, numeric digit, or the underscore character 
\W - any character that is not a letter, numeric digit or the underscore. 

\s - any space tab or newline
\S - opposite of \s , any that is not space tab or newline.


^Word - starts with particular word. 
word$ -> ends with particular 'word'

re.compile(r'^\d+$') - stars with digits that is one or more end with with digit.
will match "23234324234" but not this "12312312x234"

re.compile(r'.at') - anything that ends with at 
will find cat mat sat dat every possible combinations with at in the end.

re.compile(r'First Name: (.*) Last Name: (.*)')

. is a wild card, it matches anything except new lines 
to add new lines, you can do following
re.compile(r'.*', re.DOTALL) - To match new lines as well.
re.I second param to re.compile(,) to make matching case-insensitive 


"""

# any string that has @ in that

email_regex = re.compile(r'''(
                         [a-zA-Z0-9._%+-]+
                         @
                         [a-zA-Z0-9._%+-]+
                         (\.[a-zA-Z]{2,4}))''', re.VERBOSE)

validEmail = " email is -  ajay@gmail.com  a@a.com 1222@gmail.com 2@2.com"

result = email_regex.findall(validEmail)

for i in result:
    for j in range(1):
        print(i[j])


date_regex = re.compile(r'(0[0-9]|[12][0-9]|3[01])/(0[0-9]|1[12])/(1[0-9]|[1-9][0-9][0-9][0-9])')

text = ("22/11/9999 The regular expression doesn’t have to detect correct days for each "
        "month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. "
        "Then store these strings into variables named month, day, and year, "
        "and write additional code that can detect if it is a valid date. "
        "April, June, September, and November have 30 days, February has 28 days, "
        "and the rest of the months have 31 days. February has 29 days in leap years. "
        "Leap years are every year evenly divisible by 4, except for years evenly divisible"
        " by 100, unless the year is also evenly divisible by 400. "
        "Note how this calculation makes it impossible to make a reasonably sized "
        "regular expression that can detect a valid date.")
result = date_regex.findall(text)

print(result)

for i in result:
    for index, j in enumerate(i):
        if index == len(i)-1:
            print(j)
        else:
            print(j, end="/")

