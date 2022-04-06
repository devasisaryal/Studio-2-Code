#################################
# Program Filename: Studio 2
# 6 April 2022
# Description: calculates how many gallons of gas a specific type of car will use in 1 year
# assuming the average amount of driving per year an Oregonian will do according to the FHWA
# and the cost to that person depending on their car type and fuel cost
# Inputs: MPG, Cost of gas
#Constants:
OREGONMILES= 14032 #miles/year/person
KWH= 33.7 #per 1 gallon

#Gallons used per year calculations
mpg= 108 #highway
gallon_used_per_year= OREGONMILES/mpg #gallons
print(gallon_used_per_year)

#Cost mof gas yearly calculations
costofgas= 4.72 #dollars
costofgasyearly= gallon_used_per_year*costofgas
print(costofgasyearly)

#Cost of power yearly calculations
priceperkwh= 0.1116 #dollars
yearlypowerprice = gallon_used_per_year*KWH*priceperkwh #dollars
print(yearlypowerprice)
