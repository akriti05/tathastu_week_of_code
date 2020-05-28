from itertools import permutations
x=input("Enter a string : ")
per = [''.join(p) for p in permutations(x)]
print(per)
