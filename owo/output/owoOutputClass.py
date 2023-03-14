from .OutputObject import OutputObject
class owoOutputClass:
  def newObject(self,type: int):
    self.objects.push(OutputObject(type))
  def __init__(self):
    self.objects=[OutputObject(0)]
  # def __iter__(self):
  #   yield [
  #     self.header
  #   ]+self.objects