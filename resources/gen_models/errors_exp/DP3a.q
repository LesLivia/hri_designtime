simulate[<=400;1]{scs, served[0], served[1], served[2], served[3], served[4], served[5],  humanPositionX[currH-1]/100, humanPositionY[currH-1]/100, robPositionX[currR-1]/100, robPositionY[currR-1]/100, dX[currR-1]/100, dY[currR-1]/100, PATH}
Pr[<=400](<> scs)
E[<=400](max:humanFatigue[0])
E[<=400](max:humanFatigue[1])
E[<=400](max:humanFatigue[2])
E[<=400](max:humanFatigue[3])
E[<=400](max:humanFatigue[4])
E[<=400](max:humanFatigue[5])
