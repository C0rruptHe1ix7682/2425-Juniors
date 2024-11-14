BASE_YEAR = 1903

def main():
    year_dict = year_dict
    count_dict = count_dict
    input_file = open('WorldSeriesWinners.txt', 'r')
    winner = winner
    winners = input_file.readlines()

for i in range(len(winner)):
    team = winner[i].rstrip('\n')

year = BASE_YEAR + i
if year >= 1904:
    year += 1

if year >= 1994:
    year += 1

year_dict[str(year)] = team

if team in count_dict:
    count_dict[team] += 1
else:
    count_dict[team] = 1

year = input('Enter a year in the range 1903-2009: ')

if year == '1904' or year == '1994':
    print("The world series wasn't played in the year", year)
elif year<'1903' or year > '2009':
    print('The data for the year', year, \
'is not included in our database.')

else:
    winner = year_dict[year]
    wins = count_dict[winner]

    print('The team that won the world series in ', \
          year, ' is the ', winner, '.', sep='')

print('They won the world series', wins, 'times.')

main()


#code doesn't run correctly, needs to define properly and relook through code.