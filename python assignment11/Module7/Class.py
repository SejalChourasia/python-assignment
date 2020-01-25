import random
class coin:
    def __init__(self):
        self.sideup='Heads'
    def toss(self):
        if(random.randint(0,1))==0:
            sideup='Heads'
        else:
            sideup='Tails'
    def get_sideup(self):
        return self.sideup

def main():
    my_coin=coin()
    print("This side is up:",my_coin.get_sideup())
    print('Tossing the coin')
    my_coin.toss()
    print("This side is up",my_coin.get_sideup())

main()
