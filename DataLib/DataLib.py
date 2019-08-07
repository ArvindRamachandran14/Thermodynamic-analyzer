""" DataLib.py
    Data used by the controller. """
#   Change history:
#       03/12/2019 - KDT:   Original issue.
# Modified 5/28/2019 6:02 pm

class Register():
    def __init__(self, _i, _n, _TS, _v):
        self.index = _i
        self.name = _n
        self.timestamp = _TS
        self.value = _v


class DataLib():
    # Controller data manager
    def __init__(self):
        
        # THermocouples
        self.TC1 = Register(10, 'TC1', '00:00:00', 0.0) 
        self.TC2 = Register(11, 'TC2', '00:00:00', 0.0)
        self.TC3 = Register(12, 'TC3', '00:00:00', 0.0)
        self.TC4 = Register(13, 'TC4', 0.0)

        # Measured values
        self.RH = Register(20, 'RH', 0.0)   # Chamber relative humidity (%)
        self.pH2O = Register(21, 'pH2O', 0.0)    # Partial pressure H20 (Pa)
        self.pCO2 = Register(22, 'pCO2', 0.0)   # Partial pressure CO2 (Pa)
        self.pAtm = Register(23, 'pAtm', 0.0)   # Atmospheric pressure (kPa)

        # Weights
        self.Tare = Register(30, "Tare", 0.0)
        self.SmpWt = Register(31, 'SmpWt', 0.0)

        # Setpoints
        self.CTemp = Register(40, 'CTemp', 23.0) # Chamber temperature (degC)
        self.CRH = Register(41, "CRH", 0.20)# Chamber relative humidity (%)

        # PID values
        self.TC_P = Register(50, 'TC_P', 0.0)
        self.TC_I = Register(51, 'TC_I', 0.0)
        self.TC_D = Register(52, 'TC_D', 0.0)
        self.RH_P = Register(53, 'RH_P', 0.0)
        self.RH_I = Register(54, 'RH_I', 0.0)
        self.RH_D = Register(55, 'RH_D', 0.0)

        # Control
        self.Run = Register(1, "Run", False)

        # The parameter dictionary
        self.parmDict = {
            self.TC1.index: self.TC1,
            self.TC2.index: self.TC2,
            self.TC3.index: self.TC3,
            self.TC4.index: self.TC4,
            self.RH.index: self.RH,
            self.pH2O.index: self.pH2O,
            self.pCO2.index: self.pCO2,
            self.pAtm.index: self.pAtm,
            self.Tare.index: self.Tare,
            self.SmpWt.index: self.SmpWt,
            self.CTemp.index: self.CTemp,
            self.RH.index: self.CRH,
            self.TC_P.index: self.TC_P,
            self.TC_I.index: self.TC_I,
            self.TC_D.index: self.TC_D,
            self.RH_P.index: self.RH_P,
            self.RH_I.index: self.RH_I,
            self.RH_D.index: self.RH_D,
            self.Run.index: self.Run
        }

    def getParmDict(self):
        return self.parmDict

    def setParm(self, key, value):
        if key in self.parmDict:
            self.parmDict[key].value = value
            return True
        else:
            return False

    def getParm(self, key):
        if key in self.parmDict:
            value = self.parmDict[key].value
        else:
            value = float('NaN')
        return value

    def parmName(self, key):
        if key in self.parmDict:
            name = self.parmDict[key].name
        else:
            name = ''
        return name
