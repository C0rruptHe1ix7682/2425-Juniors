import statistics

def Calculate(infile):
    total = 0
    nums = []
    num = infile.readline()
    num = num.rstrip('\n')
    while num != "":
        num = int(num)
        nums.append(num)
        total = total + num
        num = infile.readline()
        num = num.rstrip('\n')

dStDev = (statistics.stdev(nums))

iMin = min(nums)
iMax = max(nums)
dMean = statistics.mean(nums)
print ("Min: " , iMin)
print ("Max: " , iMax)
print ("Mean: " , dMean)
print("Standard Deviation of temps is % s " % (dStDev))

if (abs(iMax-dMean) > (2 * dStDev)) and ((2 * dStDev) < abs(dMean - iMin)):
    print ("Too Hot and Too Cold: Fail!")
elif((abs(iMax-dMean) > (2 * dStDev))):
    print("Too Hot: Fail!")
elif ((2 * dStDev) < abs(dMean - iMin)):
    print("Too Cold: Fail!")
else:
    print("Pass!")

print ("Grill 1:")
infile = open("Grill_1.txt")
Calculate(infile)
infile.close()
print()

print ("Grill 2:")
infile = open("Grill_2.txt")
Calculate(infile)
infile.close()
print()

print ("Grill 3:")
infile = open("Grill_3.txt")
Calculate(infile)
infile.close()
print()

print ("Grill 4:")
infile = open("Grill_4.txt")
Calculate(infile)
infile.close()
print()

print ("Grill 5:")
infile = open("Grill_5.txt")
Calculate(infile)
infile.close()
print()