f = open("data.txt", "r")

with open("data.txt") as f:
    lines = f.readlines()

print("Number of lines:", len(lines))