
class Reservation:
    ser = 0
    reservationsData = []

    ## Trocar IDs por objetos
    def __init__(self, court, userName, user, date, startTime, endTime):
        self.resID = self.__class__.ser
        self.__class__.ser+=1
        self.court = court
        self.userName = userName
        self.user = user
        self.reservationData = (date, startTime, endTime)
        __class__.reservationsData.append(self.__dict__)

    def getResData(self):

        return self.reservationsData
    

    def getResUser(self):

        return self.user
    
    def getResID(self):

        return self.resID