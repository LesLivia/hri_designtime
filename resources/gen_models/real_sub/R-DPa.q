Pr[<=300](<> scs)
Pr[<=250](<> scs)
Pr[<=200](<> scs)
simulate[<=400;1]{scs, served[0], served[1], served[2],  humanPositionX[currH-1]/100, humanPositionY[currH-1]/100, robPositionX[currR-1]/100, robPositionY[currR-1]/100, dX[currR-1]/100, dY[currR-1]/100, PATH}
E[<=400;1](max:humanFatigue[0])
E[<=400;1](max:humanFatigue[1])
E[<=400;1](max:humanFatigue[2])
E[<=400;1](min:batteryCharge[0])
