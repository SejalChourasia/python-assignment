class car:
    def __init__(self,colour,mileage):
        self.colour=colour
        self.mileage=mileage
    def __str__(self):
        return f'a {self.colour} car having {self.mileage} mileage'
def main():
    c=car('red',75)
    print(c)
main()
