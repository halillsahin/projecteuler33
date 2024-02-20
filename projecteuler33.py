pay=set()
payda=set()

for i in range(10,100):
    for a in range(10,100):
        bi=set()
        ba=set()
        for c in str(i):
            bi.add(c)
            for d in str(a):
                ba.add(d)
                if bi.intersection(ba):
                    x=(bi.difference(ba))
                    f=(ba.difference(bi))
                    for s in x:
                        for w in f:
                            if int(w)!=0:
                                if float(s)/float(w)==float(i)/float(a) and (i*a)%100!=0:
                                    payda.add(a)
                                    if i not in payda :
                                        pay.add(i)

                                         
                                    
                                    
                                        

                
                    
        bi.clear()
        ba.clear()

h=payda.difference(pay)
payda_çarpımı=1
pay_çarpımı=1
for paylar in pay:
    pay_çarpımı*=paylar
for paydalar in h:
    payda_çarpımı*=paydalar


print(payda_çarpımı/pay_çarpımı)

