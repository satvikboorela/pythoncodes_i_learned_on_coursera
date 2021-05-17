from party import PartyAnimal

class CricketFan(PartyAnimal):
   points = 0
   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name,"points",self.points)

s = PartyAnimal("jimmy")
s.party()
j = CricketFan("Jammy")
j.party()
j.six()
print(dir(j))
