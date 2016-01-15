#playing_stock_249.py


#Daily Programmer Challenge #249.
#Playing the Stock Market.

#Problemset found here: https://www.reddit.com/r/dailyprogrammer/comments/40h9pd/20160111_challenge_249_easy_playing_the_stock/

ticks = int(input("Enter ticks for the day:"))
ticks = ticks.split()
flt = []
for i in ticks:
    flt.append(float(i)) #Convert input ticks to floats

def playing_stock(flt):
    final_ticks = []
    while len(flt) >= 3:
        if flt.index(min(flt)) > flt.index(max(flt)):
            flt.remove(max(flt))
            
        if  flt.index(max(flt)) == flt.index(min(flt)) + 1:
            flt.remove(max(flt))

        else:
            final_ticks.append(min(flt))
            final_ticks.append(max(flt))
            break
    print(final_ticks)


                
