class House:

    #Attributes
    #Constructor
    def __init__(self,area: int, color: str, name: str, floor: str, window: str):

        self.area = area
        self.color = color
        self.name = name
        self.floor = floor
        self.window =  window 



    #Methods
        
        def open_gate(self):
            print(f'Opening the gate of{self.name}')
        
        def close_gate(self):
            print(f'Closing the gate of{self.name}')

        def open_door(self):
            print(f'Opening the door of{self.name}')

        def close_door(self):
            print(f'Closing the door of{self.name}')

        def open_lights(self):
            print(f'Opening the lights of{self.name}')

        def open_window(self):
            print(f'Opening the window of{self.name}')

        def __str__(self):
            return 'Bahay mo to'
       
        def get_area(self):
            return self.area
        
        

house1 = House(area=10, color='Red', name='Jaydee House', floor='tiles')
house2 = House(area=20, color='White', name='Marvs House', floor='tiles')
house3 = House(area=69, color='ROYGIBV', name='James Luis House', floor='lava')
house4 = House(area=40, color='Green', name='Jeru House', floor='tiles')

h1 = house1 get.area()

print
