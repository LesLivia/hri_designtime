from enum import Enum
from typing import List

from src.domain.human import Human
from src.domain.robot import Robot

ND = -1


class Query_Type(Enum):
    P_SCS = 'pscs'
    P_FAIL = 'pfail'
    E_FTG = 'eftg'
    E_CHG = 'echg'
    SIM = 'sim'

    @staticmethod
    def parse_query(s: str):
        if s == 'pscs':
            return Query_Type.P_SCS
        elif s == 'pfail':
            return Query_Type.P_FAIL
        elif s == 'eftg':
            return Query_Type.E_FTG
        elif s == 'echg':
            return Query_Type.E_CHG
        else:
            return Query_Type.SIM


class Query:
    def __init__(self, t: Query_Type, tau: int, n: int, hums: List[Human], robs: List[Robot]):
        self.t = t
        self.tau = tau
        self.n = n
        self.hums = hums
        self.robs = robs

    def get_query(self):
        if self.t == Query_Type.P_SCS:
            if self.n != ND:
                return "Pr[<={};{}](<> scs)\n".format(self.tau, self.n)
            else:
                return "Pr[<={}](<> scs)\n".format(self.tau)
        elif self.t == Query_Type.P_FAIL:
            if self.n != ND:
                return "Pr[<={};{}](<> fail)\n".format(self.tau, self.n)
            else:
                return "Pr[<={}](<> fail)\n".format(self.tau)
        elif self.t == Query_Type.E_FTG:
            if self.n != ND:
                q = ''
                for (i, h) in enumerate(self.hums):
                    if h.path != 2:
                        q += "E[<={};{}](max:humanFatigue[{}])\n".format(self.tau, self.n, i)
                return q
            else:
                q = ''
                for (i, h) in enumerate(self.hums):
                    if h.path != 2:
                        q += "E[<={}](max:humanFatigue[{}])\n".format(self.tau, i)
                return q
        elif self.t == Query_Type.E_CHG:
            if self.n != ND:
                q = ''
                for (i, r) in enumerate(self.robs):
                    q += "E[<={};{}](min:batteryCharge[{}])\n".format(self.tau, self.n, i)
                return q
            else:
                q = ''
                for (i, r) in enumerate(self.robs):
                    q += "E[<={}](min:batteryCharge[{}])\n".format(self.tau, i)
                return q
        else:
            served = ''.join(['served[{}], '.format(h.h_id-1) for (i, h) in enumerate(self.hums) if h.path != 2])
            if self.n != ND:
                return "simulate[<={};{}]{{scs, {} humanPositionX[currH-1]/100, humanPositionY[currH-1]/100, " \
                       "robPositionX[currR-1]/100, robPositionY[currR-1]/100}}\n".format(self.tau, self.n, served)
            else:
                return "simulate[<={}]{{scs, {} humanPositionX[currH-1]/100, humanPositionY[currH-1]/100, " \
                       "robPositionX[currR-1]/100, robPositionY[currR-1]/100}}\n".format(self.tau, served)
