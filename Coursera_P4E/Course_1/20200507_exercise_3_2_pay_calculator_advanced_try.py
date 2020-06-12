sh = input("Enter Hours:")
sr = input("Enter Rate")
fh = float(sh)
fr = float(sr)

if fh > 40 :
    print ("Overtime")
    reg = fr * 40
    otp = (fh - 40) * (fr * 1.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay", xp)        
