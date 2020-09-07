#!/usr/bin/python3

#date_returned=[9,6,2015]
#date_expected=[6,6,2015]
#print(date_returned[0],date_returned[1],date_returned[2])
#print(date_expected[0],date_expected[1],date_expected[2])
date_returned= [int(x) for x in input().split(' ')]
date_expected= [int(x) for x in input().split(' ')]


fine=0

if date_returned[2] == date_expected[2]:
    if date_returned[1] == date_expected[1]:
        if date_returned[0] == date_expected[0]:
            fine=0
        elif date_expected[0] < date_returned[0]:
            fine = (date_returned[0]-date_expected[0])*15
    elif date_expected[1] < date_returned[1]:
        fine = (date_returned[1]-date_expected[1])*500

elif date_expected[2] < date_returned[2]:
    fine = 10000

print(fine)