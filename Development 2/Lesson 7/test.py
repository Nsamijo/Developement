class Stoel:
  def __init__(self, bezet, nummer, zaal):
    self.bezet = bezet
    self.nummer = nummer
    self.zaal = zaal
  
  def getLocation(self):
    '''get the location'''
    return str(self.zaal) + str(self.nummer)

  def getStatus(self):
    '''the status'''
    return self.bezet

  def setStatus(self, status):
    '''set the status'''
    self.bezet = status


class Zaal:
  
  def __init__(self, ID, seatsCount):
    self.ID = ID
    self.SEATS_AMOUNT = seatsCount
    self.seats = {}
    self.addChairs()

  def addChairs(self):
    '''add chairs to the thing'''
    for x in range(1, self.SEATS_AMOUNT + 1):
      self.seats.update({str(self.ID) + str(x): Stoel(False, x, self.ID)})

  def reserve(self, seatID):
    '''reserve a seat'''
    try:
      self.seats[seatID].setStatus(True)
      return self.seats[seatID].getLocation() + ' reservation = ' + str(self.seats[seatID].getStatus())
    except:
      print('ID not valid')
      return -1

  def getValidSeats(self):
    '''get free seats'''
    temp = 0
    for x in self.seats.keys():
      if not self.seats[x].getStatus():
        temp += 1
    if temp == 0:
      return 'No valid seats.'
    return 'Valid seats: ' + str(temp)

A1 = Zaal('A', 100)
for x in range(1, 100):
  A1.reserve('A' + str(x))
print(A1.getValidSeats())