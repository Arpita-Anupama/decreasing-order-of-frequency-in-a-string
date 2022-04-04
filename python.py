str = "mississippi"
frequency = {}
for i in str :
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print ("count of all the characters in mississippi is:" + str(frequency) );
    
