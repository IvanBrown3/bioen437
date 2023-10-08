import numpy as np
import matplotlib.pyplot as plt
import tellurium as te



r = te.loada(''' 
              
        v: A -> B; Vm*A/(Km + A)
        
        Vm = 1; Km = 0.5; A = 3;
        
        
        
        ''')

#x = np.arange (0,5,0.1)

#y = []

#for A in x:
    r.A = A
    rate = r.v
    y.append(r.v)
    print(rate)

#plt.plot(x,y,'-r')
#plt.show()

#print([x**2 for x in np.arrange(1, 10, 0.1)])

def getRate(S):
    r.A = S
    return r.v

x = np.arrange(0,5,0.1)
Km = np.arrange(0.1,2,0.4)


for p in Km:
    r.Km = p
    #assign tellrium model to Km defined above
    y = [getRate (S) for S in x]
    plt.plot(x, y)

plt.show()
#list of rate for all x using the defined rate above

