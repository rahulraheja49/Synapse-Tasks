# importing required modules
import json
from matplotlib import pyplot as plt
import numpy as np

with open('./data.json') as f:
    data = json.load(f)
    
info = data['data']

# counting the parameters
count_Sports = 0
count_Technology = 0
count_Fashion = 0
count_Games = 0
count_Environment = 0
count_male = 0
count_female = 0
count_1824 = 0
count_2534 = 0
count_3544 = 0
count_4554 = 0
count_55 = 0
count_ios = 0
count_android = 0
count_married = 0
count_single = 0
for part in info:
    if(part['event_name'] == 'Fund Project'):
        # category
        if(part['category'] == 'Sports'):
            count_Sports += 1
        elif(part['category'] == 'Games'):
            count_Games += 1
        elif(part['category'] == 'Technology'):
            count_Technology += 1
        elif(part['category'] == 'Fashion'):
            count_Fashion += 1
        elif(part['category'] == 'Environment'):
            count_Environment += 1
        
        # gender
        if(part['gender'] == 'M'):
            count_male +=1
        elif(part['gender'] == 'F'):
            count_female += 1
        
        # age
        if(part['age'] == '18-24'):
            count_1824 += 1
        elif(part['age'] == '25-34'):
            count_2534 += 1
        elif(part['age'] == '35-44'):
            count_3544 += 1
        elif(part['age'] == '45-54'):
            count_4554 += 1
        elif(part['age'] == '55+'):
            count_55 += 1
            
        # device
        if(part['device'] == 'iOS'):
            count_ios += 1
        elif(part['device'] == 'android'):
            count_android += 1
        
        # maritial status
        if(part['marital_status'] == 'married'):
            count_married += 1
        elif(part['marital_status'] == 'single'):
            count_single += 1
            
            
# plotting the pie charts
fig1 = plt.figure()
ax1 = fig1.add_axes([0,0,1,1])
ax1.axis('equal')
categories = ['Sports', 'Technology', 'Fashion', 'Games', 'Environment']
funding1 = [count_Sports, count_Technology, count_Fashion, count_Games, count_Environment]
ax1.pie(funding1, labels = categories,autopct='%1.2f%%')
plt.show()

fig2 = plt.figure()
ax2 = fig2.add_axes([0,0,1,1])
ax2.axis('equal')
genders = ['Male', 'Female']
funding2 = [count_male, count_female]
ax2.pie(funding2, labels= genders, autopct='%1.2f%%')
plt.show()

fig3 = plt.figure()
ax3 = fig3.add_axes([0,0,1,1])
ax3.axis('equal')
devices = ['iOS', 'android']
funding3 = [count_ios, count_android]
ax3.pie(funding3, labels= devices, autopct='%1.2f%%')
plt.show()

fig4 = plt.figure()
ax4 = fig4.add_axes([0,0,1,1])
ax4.axis('equal')
marital_status = ['single', 'married']
funding4 = [count_single, count_married]
ax4.pie(funding4, labels= marital_status, autopct='%1.2f%%')
plt.show()

fig5 = plt.figure()
ax5 = fig5.add_axes([0,0,1,1])
ax5.axis('equal')
ages = ['18-24', '25-34', '35-44', '45-54', '55+']
funding5 = [count_1824, count_2534, count_3544, count_4554, count_55]
ax5.pie(funding5, labels = ages,autopct='%1.2f%%')
plt.show()

# plotting the bar graphs
fig1a = plt.figure()
ax1a = fig1a.add_axes([0,0,1,1])
categories = ['Sports', 'Technology', 'Fashion', 'Games', 'Environment']
funding1 = [count_Sports, count_Technology, count_Fashion, count_Games, count_Environment]
ax1a.bar(categories,funding1)
plt.show()

fig2a = plt.figure()
ax2a = fig2a.add_axes([0,0,1,1])
genders = ['Male', 'Female']
funding2 = [count_male, count_female]
ax2a.bar(genders, funding2)
plt.show()

fig3a = plt.figure()
ax3a = fig3a.add_axes([0,0,1,1])
devices = ['iOS', 'android']
funding3 = [count_ios, count_android]
ax3a.bar(devices, funding3)
plt.show()

fig4a = plt.figure()
ax4a = fig4a.add_axes([0,0,1,1])
marital_status = ['single', 'married']
funding4 = [count_single, count_married]
ax4a.bar(marital_status, funding4)
plt.show()

fig5a = plt.figure()
ax5a = fig5a.add_axes([0,0,1,1])
ages = ['18-24', '25-34', '35-44', '45-54', '55+']
funding5 = [count_1824, count_2534, count_3544, count_4554, count_55]
ax5a.bar(ages, funding5)
plt.show()
