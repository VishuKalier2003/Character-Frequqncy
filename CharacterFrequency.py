'''Consider an input as a sentence of integers and then evaluate the frequency of each character and find out which character has the maximum occurrence per word... neglect the whitespaces
                Eg:- input = 1233 1223 3345 33346 11122
                1st. abcc => 1 = 1, 2 = 1, 3 = 2     max => 3
                2nd. abbc => 1 = 1, 2 = 2, 3 = 1     max => 2
                3rd. ccfg => 3 = 2, 4 = 1, 5 = 1     max => 3
                4th. ccchi => 3 = 3, 4 = 1, 6 = 1    max => 3
                5th. aaabb => 1 = 3, 2 = 2           max => 1
                Since 3 occurs most in maximum frequency array per word, c is the maximum frequency character'''

import numpy as np
s = input("Enter a sentence :")
x = int(input("Enter number of words :"))
list_s = s.split(" ")    # The delimiter entered is whitespace
array = np.array([])
for i in range(0, x):
    array = np.append(array, [""])

l2 = []
for i in range(0, x):
    # Creating array of the ith word
    sub = np.array(list_s[i])
    # Then converting the array to list which makes the character splitting easy
    l1 = sub.tolist()
    for j in range(0, len(l1)):     # Adding characters to new list for splitting purpose
        l2.append(l1[j])
    r = list(map(int, l2))      # List type casting
    # Converting to Array for the bincount operation
    arr = np.array(r)     
    print("The array after splitting", i+1, "word :", arr)
    print()
    a = np.bincount(arr).argmax()          # The argmax function works only for integer
    l2 = []
    array[i] = a

array1 = list(map(int, array))        # List type casting to integer
print("The maximum frequency array :", array1)
print()
a = np.bincount(array1).argmax()     # Again using bincount operation for the maximum character frequency
print("The maximum frequency character per word is :",a)