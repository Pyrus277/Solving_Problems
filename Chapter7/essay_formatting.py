# This problem can be found here: http://usaco.org/index.php?page=viewproblem2&cpid=987

# Bessie is writing an essay. Each word contains only upper and lowercase letters.
# Teacher has specified the max number of characters not including spaces that can 
# Occur per line.
# If the next word fits on the current line, add it to the current line,
# otherwise, put the word on a new line, and this line becomes the current line.
# Output the essay with the correct number of lines.
#
# Input: 
# First line contains two ints separated by a space: Number of words n in the 
# essay b/w 1 and 100. Second int is max characters per line k b/w 1 and 80.
# Second line contains n words, with a space b/w each pair of words. Each word
# has at most k characters.
#
# Output: 
# Write the properly formatted output to word.out

# Open the file and store the number of words, characters per line, and text in variables
with open('word.in','r') as fhand:
    constraints = fhand.readline().split(' ')
    words = int(constraints[0]) 
    line_maxchar = int(constraints[1])
    text = fhand.readline()

text = text.split(' ') # Turn the text into a list of words
line_content = "" # Initialize a line content string variable...   
count = 0 # and a counter variable to be compated with the line_maxchar number

# Iterate thru the list of words
for i in range(words):
    # Increment the count variable according to each word
    count += len(text[i])
    # As long as the count variable doesn't exceed the maximum amount, keep adding 
    # words to line_content
    if count <= line_maxchar:
        line_content += text[i]+' '
    # When we do exceed the character count max per line, write(append) the contents of
    # line content to the word.out file. Then empty out line_content, reset count, and 
    # add the current word to the newly reset line_content.
    if count > line_maxchar:
        with open("word.out", "a") as word_out:
            word_out.write(line_content.rstrip() + '\n' )
        line_content = ""
        count = 0
        count +=len(text[i])
        line_content += text[i]+' '
    # So far we're only appending when count exceeds line_maxchar, so this next bit "catches"
    # and appends the last word which will not cause count to exceed line_maxchar. 
    if i == words - 1:
        with open("word.out", "a") as word_out:
            word_out.write(line_content.rstrip() + '\n' )