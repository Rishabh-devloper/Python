class Factory:
    def __init__(self , material , zips):
        self.material=material
        self.zips= zips
        
class BhopalFactory(Factory):
    def __init__(self, material, zips , color):
        super().__init__(material, zips)
        self.color=color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color , pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets
    def show(self):
        print(f"Material:{self.material} \n zips:{self.zips} \n Color:{self.color} \n Pockets:{self.pockets}")

obj = PuneFactory("Leather" , 4, "blue" , "5")
obj.show()