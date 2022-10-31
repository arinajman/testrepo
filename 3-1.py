hours=input('Enter hours: ')
rate=input('Enter rate: ')
fhours=float(hours)
frate=float(rate)
pay=fhours*frate
if fhours>40:
    mhours=fhours-40
    pay=pay+mhours*frate/2
print('Pay:',pay)
