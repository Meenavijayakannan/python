class Circle:
    def __init__(self,radi):
        self.radius = radi


    def __str__(self):
        return f'Radius : {self.radius}'

moon = Circle(1737)
print(moon)
