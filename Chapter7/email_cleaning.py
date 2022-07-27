# ecoo19r2p1

# Given a list of email addresses, find how many distinct ones 
# there are. Consider that:
# 1. emails are case insensitive
# 2. '.' before the @ are ignored
# 3. a "+" followed by any string before the @ is also ignored.

# Onput - 10 datasets
# Each one starts with int N, the number of email addresses.
# The next N lines each contain an email address.  

# For each dataset, output the number of unique emails.
 
# A function to "clean" a given email address.
def clean_email(email):
    '''Takes a string in the format of an email,
    returns that email in standardized form.'''
    # find the position of the '@' and, if present a '+'
    at_indx = email.index('@')
    if '+' in email:
        pls_indx = email.index('+')

    # if the '+' precedes the '@', mark its place, otherwise
    # store the '@' index
    if '+' in email and  pls_indx < at_indx:
        end_range = pls_indx
    else:
        end_range = at_indx

    # Initialize a string for the part of the email before the '@'
    # and copy the characters that are not a '.' or '+' with a following
    # string. 
    local = ''
    for letter in email[:end_range]:
        if letter != '.':
            local += letter

    # add the domain name to what we put in local, all lowercase
    clean_email = local.lower() + email[at_indx:].lower()

    return clean_email

# Add the cleaned emails to a set and get the length of it. 
for i in range(10):
    N = int(input())
    emails = set()
    for i in range(N):
        emails.add(clean_email(input()))
    print(len(emails))


# A much neater and nicer solution someone else submitted and 
# I want to remember it:

import sys
input = sys.stdin.readline

for data in range(10):
    n = int(input())
    addresses = set()
    for i in range(n):
        user, domain = input().lower().split('@')
        user = user.replace('.','').split('+')[0]
        addresses.add(user + domain)
    print(len(addresses))





