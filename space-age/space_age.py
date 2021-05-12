class SpaceAge:
    def __init__(self, seconds):
        self.years_on_earth = seconds/31557600


    def convert(self, n):
        return round(self.years_on_earth/n, 2)


    def on_earth(self):
        return round(self.years_on_earth, 2)


    def on_neptune(self):
        return self.convert(164.79132)


    def on_uranus(self):
        return self.convert(84.016846)
        

    def on_saturn(self):
        return self.convert(29.447498)


    def on_jupiter(self):
        return self.convert(11.862615)


    def on_mars(self):
        return self.convert(1.8808158)


    def on_venus(self):
        return self.convert(0.61519726)
    
    
    def on_mercury(self):
        return self.convert(0.2408467)
    
