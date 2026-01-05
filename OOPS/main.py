class Factory:
    def __init__(self , material , zips , pockets):
        self.material = material
        self.zips = zips
        self.pockets= pockets
    def show(self):
        print(f'Material:{self.material} ')
        print(f'Pockets:{self.pockets} ')
        print(f'Zips:{self.zips} ')

reebok = Factory("Suede" , 4 , 2)
campus= Factory("Nylon" , 2 ,2)
campus.show()