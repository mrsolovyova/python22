class CoffeeGrinder:
    manufacturer = 'Bosch'
    color = 'black'
    capacity = 300  # grams
    grinding_speed = 2.5  # grams in second
    millstone_material = 'steel'
    size = '120×160×350'  # millimeters

    def __init__(self, servings=None, grind_size=None, **kwargs):
        self.active = False
        print('Количество порций = ', servings, '\nРазмер помола = ', grind_size)

    def switch(self):
        if self.active is False:
            self.active = True
            print('On')
        else:
            self.active = False
            print('Off')


my_grinder = CoffeeGrinder(servings=2, grind_size=5)
my_grinder.switch()
my_grinder.switch()

