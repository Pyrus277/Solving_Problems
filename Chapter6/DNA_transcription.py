# ecoo12r1p2

# DNA - A is always paird with T, C is always paired with G
# For DNA info to be used, it has to be transcribed into a strand of RNA.
# During this process, a portion of one strand of DNA, the transcrption unit, is transcribed.
# The start of the sequence to be transcribed is signaled by a sequence of bases known 
# as a promoter, and the end is signaled by a sequence known as the terminator.
# For our purposes, the promoter is the sequence TATAAT, which begins 10 bases before
# the start of the transcription unit, and the terminator consists of two distinct, 
# complementary reversed sequences of at least length 6 that causess the RNA molecule
# to coil back on itself and pinch off the transcribed strand. If TATAAT appears twice
# on a strand, only the first occurrence counts as the promoter.
#
#
# terminator = two distinct, complementary, reversed sequences of at least len 6

# Approach:
# 1. Find the beginning of the transcription sequence TATAAT
#   a. Find the promoter
#   b. Count 10 from the start of that--this is the beginning of the sequence
#
# 2. Find the end of the transcription sequence
#   a. Grab the sequence one base after the start = A
#   b. Reverse and "translate" that = B
#   c. For each letter + 5 index spaces in A, does that equal a substring in B
#   d. If so, the base before letter in A is the end of the strand to be transcribed
#
# 3. Translate the strand.

def translate(GCTA):
    translated = ""
    for base in GCTA:
        if base == 'G':
            translated += "C"
        if base == 'C':
            translated += "G"
        if base == 'A':
            translated += "T"
        if base == 'T':
            translated += "A"
    return translated

def RNA_translate(GCTA):
    translated = ""
    for base in GCTA:
        if base == 'G':
            translated += "C"
        if base == 'C':
            translated += "G"
        if base == 'A':
            translated += "U"
        if base == 'T':
            translated += "A"
    return translated

for strand in range(1,6):
    # Get the whole strand:
    DNA = input()
    # Use the promoter, TATAAT, to find the start of the transcription sequence
    # and clip off everything prior and put that in a variable. 
    sequence = DNA[(DNA.index('TATAAT') + 10):]
    # Now we need to find the terminator sequence, which will be at least 6 bases long
    # and have a complementary set of bases if we start going thru the sequence in reverse order.
    # How to find this pair?
    # First, take our sequence strand and reverse and translate it,and then put that into its own 
    # variable, tr_sequence.
    tr_sequence = translate(sequence[::-1])
    # Then iterate thru sequence, and for each base, grab the following 5 bases and see if this
    # substring occurs in the reversed and translated sequence. 
    for i in range(len(sequence)):
        # This next line is the key-- the terminator sequence is distinct-- it can't overlap with 
        # itself when the DNA folds! To ensure this, for each step we take thru sequence, we only 
        # search for the corresponding substring in tr_sequence UP to the point where there is i+6 
        # remaining spots left in tr_string. If we don't ensure this buffer, we could get false 
        # positives that are indeed complimentary pairs, but fold in on themselves, thus disqualifying 
        # them from being the terminator sequence. 
        if sequence[i:i+6] in tr_sequence[:-i-6]:
        # So we found the true terminator sequence. The spot before this is where the sequence to be 
        # translated ends.
            end_sequence = i
            break
    # Plug this sequence into our translator function, format the output, and we're done.
    print(f"{strand}:",RNA_translate(sequence[:end_sequence]))

