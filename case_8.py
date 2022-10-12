class CoffeeGrinder:
    manufacturer = 'Bosch'
    color = 'black'
    capacity = 300  # grams
    grinding_speed = 2.5  # grams in second
    millstone_material = 'steel'
    size = '120×160×350'  # millimeters
    servings = range(1, 5)
    grind_size = range(1, 10)

    def __init__(self, servings, grind_size):
        self.servings = servings
        self.grind_size = grind_size
        self.active = False
        print('Количество порций = ', servings, '\nРазмер помола = ', grind_size)

    def switchon(self):
        self.active = True
        print('On')

    def switchoff(self):
        self.active = False
        print('Off')


my_grinder = CoffeeGrinder(2, 6)
my_grinder.switchon()

