numbers = [ 1,2,5,6,2,4,2,3,6,4,1,5,3,5,6,2,8,9,7,1,11,22,24]
unik = []
for number in numbers:
    if number not in unik:
        unik.append(number)
unik.sort()
print(unik)