from Dragon import *
dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")
print(dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")
print()

dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr + dr1
print(dr, dr1, dr2, sep="\n")

print(dr("Welcome"))
