import matplotlib.pyplot as pyplot
import matplotlib.patches as mpatches

ns1 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 27, 42]

ws1 = [0.05, 0.0225, 0.0175, 0.0475, 0.06, 0.06, 0.08, 0.09, 0.12, 0.12, 0.1025, 0.0925, 0.0525, 0.0525, 0.02, 0.01, 0.025, 0.05, 0.0075, 0.0025, 0.005, 0.0025]

ns2 = [34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59 ,60, 61, 62, 63, 64, 68, 105]

ws2 = [0.01, 0.01, 0.02, 0.03, 0.02, 0.01, 0.03, 0.03, 0.02, 0.06, 0.02, 0.04, 0.11, 0.04, 0.05, 0.05, 0.06, 0.06, 0.03, 0.04, 0.04, 0.02, 0.02, 0.04, 0.03, 0.03, 0.03, 0.01, 0.01, 0.01, 0.01, 0.01]

ns = []
for i in range(2):
    ns.append(4)
for i in range(9):
    ns.append(5)
for i in range(7):
    ns.append(6)
for i in range(19):
    ns.append(7)
for i in range(24):
    ns.append(8)
for i in range(24):
    ns.append(9)
for i in range(32):
    ns.append(10)
for i in range(36):
    ns.append(11)
for i in range(48):
    ns.append(12)
for i in range(48):
    ns.append(13)
for i in range(41):
    ns.append(14)
for i in range(37):
    ns.append(15)
for i in range(21):
    ns.append(16)
for i in range(21):
    ns.append(17)
for i in range(8):
    ns.append(18)
for i in range(4):
    ns.append(19)
for i in range(10):
    ns.append(20)
for i in range(2):
    ns.append(21)
for i in range(3):
    ns.append(23)
for i in range(1):
    ns.append(24)
for i in range(2):
    ns.append(27)
for i in range(1):
    ns.append(42)

ns_2 = []
for i in range(1):
    ns_2.append(34)
for i in range(1):
    ns_2.append(35)
for i in range(2):
    ns_2.append(37)
for i in range(3):
    ns_2.append(38)
for i in range(2):
    ns_2.append(39)
for i in range(1):
    ns_2.append(40)
for i in range(3):
    ns_2.append(41)
for i in range(3):
    ns_2.append(42)
for i in range(2):
    ns_2.append(43)
for i in range(6):
    ns_2.append(44)
for i in range(2):
    ns_2.append(45)
for i in range(4):
    ns_2.append(46)
for i in range(11):
    ns_2.append(47)
for i in range(4):
    ns_2.append(48)
for i in range(5):
    ns_2.append(49)
for i in range(5):
    ns_2.append(50)
for i in range(6):
    ns_2.append(51)
for i in range(6):
    ns_2.append(52)
for i in range(3):
    ns_2.append(53)
for i in range(4):
    ns_2.append(54)
for i in range(4):
    ns_2.append(55)
for i in range(2):
    ns_2.append(56)
for i in range(2):
    ns_2.append(57)
for i in range(4):
    ns_2.append(58)
for i in range(3):
    ns_2.append(59)
for i in range(3):
    ns_2.append(60)
for i in range(3):
    ns_2.append(61)
for i in range(1):
    ns_2.append(62)
for i in range(1):
    ns_2.append(63)
for i in range(1):
    ns_2.append(64)
for i in range(1):
    ns_2.append(68)
for i in range(1):
    ns_2.append(105)

print(sum(ns), 'sum ns')
print(sum(ns_2), 'sum ns_2')

summary = 0
counter = 0
for i in range(100):
    summary = summary + (ns_2[i] - 50.25)*(ns[i] - 50.25)
    #if (abs(12.5625 - ns[i]) <= 2*4.03):
        #counter+=1
    
print (summary, 'summary 100')
print (counter, 'counter')



pyplot.xlabel('Число импульсов $n$')
pyplot.ylabel('Доля случаев $w$')

pyplot.hist(ns, bins = 80, density=True, color = 'orange')

plpt = pyplot.twiny()

plpt.hist(ns_2, bins = 80, density=True, color = 'blue', alpha = 0.65)
#pyplot.hist(ns1, len(ns1), weights = ws1, density = True, color = 'black')




#ns2_ = []
#for i in ns2:
    #ns2_.append(i*1)

#ws1_ = []
#for i in ws1:
    #ws1_.append(i*0.5)

#ws2_ = []
#for i in ws2:
    #ws2_.append(i*0.5)



print (len(ns2), len(ws2))
#pyplot.hist2d(ns1, ws1, 22)
#pyplot.hist(ns1, 22, weights = ws1, density = True, cumulative = -1, color = 'orange')
#pyplot.hist(ns2_, 32, weights = ws2)
#pyplot.margins(x = 0.25)

#pyplot.margins(y = 2)
#plpt = pyplot.twiny()


#plpt.hist(ns2, 32, weights = ws2, density = True, cumulative = -1, color = 'blue', alpha=0.65)
#plpt.hist(ns1, 22, weights = ws1, color = 'red')
#plpt.margins(y = 2)

red_patch = mpatches.Patch(color='orange', label='Гистограмма для t 10 с')
blue_patch = mpatches.Patch(color = 'blue', alpha=0.65, label='Гистограмма для t 40 с')
pyplot.legend(handles=[red_patch, blue_patch])

pyplot.show()
