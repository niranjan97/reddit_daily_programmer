#variable_notation.py

#Daily Programmer Challenge #140
#Variable notation to convert between CamcelCase, snake_case & capitalized_snake_case
#Problemset found here: https://www.reddit.com/r/dailyprogrammer/comments/1q6pq5/11413_challenge_140_easy_variable_notation/



def main(num, inp):
    if num == '0': #CAMCEL
        inp = inp.split()
        newstring = inp[0]
        for i in range(1, len(inp)):
            newstring = newstring + inp[i].capitalize()
        print(newstring)

    if num == '1': #snake_case
        newstring = inp.lower()
        print(newstring.replace(" ", "_"))

    if num == '2': #SNAKE_CASE
        newstring = inp.upper()
        print(newstring.replace(" ", "_"))

main( input("0 - CamCel, 1 - snake_case, 2 - SNAKE_CASE: "), input("Enter string to convert:"))
