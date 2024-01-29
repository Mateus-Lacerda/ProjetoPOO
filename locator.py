import court
from  user import User

class Locator(User):
    locatorSer = 0

    def __init__(self, name, email, phoneNumber, username, password):
        super(Locator,self).__init__(name, email, phoneNumber, username, password)
        self.userType = "Locator"
        self.locatorID = self.__class__.locatorSer
        self.__class__.locatorSer+=1
        self.ownedCourts = []
        self.object = self
        super().userData["Locator"].append(self.__dict__)
        super().updateUserData("Locator")
    
    def getID(self):

        return self.locatorID
    

    def addCourts(self, courtType, location, pricePerHour, maxPlayers, courtagenda):
        thisCourt = court.Court(self.object, self.locatorID, courtType, location, pricePerHour, maxPlayers, courtagenda)
        print("______________________________________")
        print(f"Locator {self.locatorID} added court {thisCourt.getCourtID()}")
        super().updateUserData("Locator")
    
    def getCourts(self, courtID):
        return self.ownedCourts[courtID]
