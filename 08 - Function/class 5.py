#Formula to calculate EMI is: PXRX(1+R)^N /[(1+R)^N-1]

def emiCalculate (principal, rate, time):
    r= rate/12/100
    emi= (principal*r*(1+r)**time)/((1+r)**time-1)

    return emi

print(emiCalculate(5000000,8.75,240))
