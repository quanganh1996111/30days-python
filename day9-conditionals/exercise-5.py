# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

season=input('Your month is: ')
print(season)
if season=='September' or season=='October' or season=='November':
    print('The Season is Autumn.')
elif season=='Demcember' or season=='January' or season=='Febuary':
    print('The Season is Winter.')
elif season=='March' or season=='April' or season=='May':
    print('The Season is Spring')
elif season=='July' or season=='June' or season=='August':
    print('The season is Summer')
else:
    print('You do not type the right Month')