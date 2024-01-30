# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces:  ;( :> :} :]

# Example

# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
# Note

# In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.



#MY 3 OPTIONS FOR SOLVING THIS TASK

#Variant 1

def countSmileys1(arr):
    a = 0
    for i in range(len(arr)):
        if len(arr[i])==2:
            if arr[i][0] == ':' or arr[i][0] == ';':
                if arr[i][1] == ')' or arr[i][1] == 'D':
                    a += 1
        if len(arr[i])==3:
            if arr[i][0] == ':' or arr[i][0] == ';':
                if arr[i][1] == '-' or arr[i][1] == '~':
                    if arr[i][2] == ')' or arr[i][2] == 'D':
                        a +=1
    return a
print(countSmileys1([':)',':(',':D',':O',':;']))

#Variant 2

def countSmileys2(arr):
    eyes = [':',';']
    noses = ['','-','~']
    mouses = [')','D']
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouse in mouses:
                face = eye + nose + mouse
                count += arr.count(face)
    return count

#Variant 3 

import re

def countSmileys3(arr):
    pattern = re.compile(r'[:;][-~]?[)D]')
    return sum(1 for face in arr if pattern.match(face))
