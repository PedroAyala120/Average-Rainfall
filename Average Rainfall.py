#This Program will collect data and calculate the average rainfall over a period of years
#Pedro Ayala

#initialize variables
rainfall = 0

#user inputs number of years
year = int(input('Input the number of years: '))

#loop for each year
for i in range (1, year + 1):
    print ('Year #', i)  #print year number
    for month in range (0, 12): #nested loop for each month
        print ('Month #', month + 1)  #print Month number
        rain = int(input('How much did it rain this month? '))  #asks for rain input
        rainfall += rain    #adds up total rainfall
        month += 1          #increments month value

#calculate average
avg = rainfall / (month * i)

#print results
print ('total rainfall for ', month * i, 'months: ', rainfall)
print ('average rainfall for ', month * i, 'months: ', avg)
