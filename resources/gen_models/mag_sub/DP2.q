Pr[<=520](<> scs)
simulate[<=400]{scs, served[0], served[1], served[2], served[3], served[4],  humanPositionX[currH-1]/100, humanPositionY[currH-1]/100, robPositionX[currR-1]/100, robPositionY[currR-1]/100, dX[currR-1]/100, dY[currR-1]/100, PATH}
E[<=520](max:humanFatigue[0])
E[<=520](max:humanFatigue[1])
E[<=520](max:humanFatigue[2])
E[<=520](max:humanFatigue[3])
E[<=520](max:humanFatigue[4])
E[<=520](min:batteryCharge[0])
