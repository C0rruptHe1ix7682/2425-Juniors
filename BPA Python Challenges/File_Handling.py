f = open("data.txt", "r")

with open("data.txt") as f:
    lines = f.readlines()

print("Number of lines:", len(lines))

#I originally created the file and the first line is meant to read said file an count the number of lines. The 3rd line and it's function is meant to caluculate the amount and prepare it. The print is meant to show us the final number!