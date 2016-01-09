#disemvoweler.py

#Challenge #149, https://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/

#Removes vowels from input string

inp = input("Enter string to strip: ")

inp = inp.replace(" ", "")
def vowel_strip(inp):
    stripped = ""
    remainder = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in inp:
        if i in vowels:
            remainder = remainder + i
        else:
            stripped = stripped + i
    print(stripped)
    print(remainder)


vowel_strip(inp)

            
