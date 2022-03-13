'''
We can use a class to create emulate a context manager.
This uses the __enter__ method upon instantiation of the with statement and __exit__
upon finishing the with statement
'''
from dataclasses import dataclass


@dataclass
class House:
    rooms: int
    kitchen: bool
    dirty_dishes: int = 30
    vacuumed: bool = False
    inside: bool = False

    def __enter__(self):
        self.inside = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.inside = False

    def do_dishes(self, num_dishes):
        if not self.inside:
            raise ValueError('You need to be inside to do the dishes!')

        if not self.kitchen:
            raise ValueError('You need a kitchen to do dishes!')

        else:
            self.dirty_dishes -= num_dishes
            print(f'You cleaned {num_dishes} dishes, {self.dirty_dishes} dishes remain!')

    def vacuum(self):
        if not self.inside:
            raise ValueError('You need to be inside to do the dishes!')

        else:
            self.vacuumed = True
            print(f'Vacuumed {self.rooms} rooms!')


if __name__ == '__main__':
    house = House(rooms=4, kitchen=True, dirty_dishes=50, vacuumed=False, inside=False)

    # Must be inside to do various jobs. Always exit the house when finished cleaning!
    house.inside = True
    house.vacuum()
    house.do_dishes(5)
    house.inside = False

    # Use a with statement to control the entering and exiting
    with House(rooms=4, kitchen=True) as h:
        h.vacuum()
        h.do_dishes(5)
