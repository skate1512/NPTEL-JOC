import matplotlib.pyplot as plt
import random

account=0

x=[]
y=[]

for i in range(365):
    x.append(i+1)
    bet=random.randint(0,10)
    lottery=random.randint(0,10)

    if(bet==lottery):
        account=account+900-100
    else:
        account=account-100
    y.append(account)
print("Account balance after one year:",account)
plt.plot(x,y)
plt.show()