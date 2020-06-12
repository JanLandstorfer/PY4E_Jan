maxv = 0
minv = None
minvold = 0

while True :
    sval = input ('Enter an INT Number: ')
    if sval == 'done':
        #print('All Done!')
        print('Maximum is', maxv)
        print('Minimum is', minv)
        break
    else:
        try:
            ival = int(sval)
        except:
            print('Invalid Input')
        if ival > maxv:
            maxv = ival
        if minv is None or ival < minv:         #bei Initalisierung mit "None"
            minv = ival
