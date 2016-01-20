#!/usr/bin/python3

#rovarspraket_212.py

#Reddit Daily Challenge #212 [Easy], Encode the Rovarspraket secret language

#problemset found here: https://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/

import string
 
consonants = []
vowels_exclude = ['a', 'e', 'i', 'o', 'u', 'y', 'ö', 'å', 'ä' ' ' ] #y included because Rovarspraket is Swedish and Swedish is weird

for i in string.ascii_lowercase:
    if i in vowels_exclude:
        continue
    else:
        consonants.append(i)

def rovarspraket_encode(inp_string):
    inp_string = list(inp_string)
    for i in inp_string:
        if i in consonants:
            inp_string[inp_string.index(i)] = i +'o'+i
        else:
            continue
    print("".join(inp_string))


rovarspraket_decode('sosmometothohinongog')
