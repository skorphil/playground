# The set of plates is given. The task is to calculate all weight variations for single dumbbelllllll

## Plate with some default attributes. Let's assume they also can have different width.


class Plate:
    def __init__(self, weight, color="black", material="steel", width=1):
        self.weight = weight
        self.color = color
        self.material = material
        self.width = width


## Bar with it's own weight and limited capacity for plates


class Bar:
    def __init__(self, max_plates_width, bar_weight):
        self.max_plates = max_plates_width
        self.bar_weight = bar_weight


## Dumbbell as a combination of bar and plates


class Dumbbell:
    def __init__(self, bar, plates):
        self.bar = bar
        self.plates = plates


## Available plates

# plate_1 = Plate(2.5, width=3)
# plate_5 = Plate(2.5, width=2)
# plate_2 = Plate(1, "white", material="cast_iron")
# plate_3 = Plate(0.5, "white")

# print(plate_1.width)

# how to put object in list https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/#:~:text=We%20can%20create%20list%20of,class%20and%20can%20access%20them.
plate_list = []
plate_list.append(Plate(2.5, width=3))
plate_list.append(Plate(2.5, width=2))
plate_list.append(Plate(1, "white", material="cast_iron"))
plate_list.append(Plate(1, "white", material="cast_iron"))
plate_list.append(Plate(1, "black", material="cast_iron"))
plate_list.append(Plate(0.5, "red"))

for obj in plate_list:
    print(obj.weight, obj.color, obj.material, obj.width, sep=", ")


## Available bars
# bar_1 = Bar(7, 2)
# bar_2 = Bar(4, 2)
bar_list = []
bar_list.append(Bar(7, 2))
bar_list.append(Bar(4, 1))

# def make_all_dumbbells(bar, plates):
# Both sides are equal weight
# Each side have enough width for plates

# right side weight = sum plate.weight
# left side weight = sum plate.weight
# left = right

# left side width = bar.max_width_plates - (sum plate.width)
# left side width >= 0


# #     print(barbell.bar_weight)


# weight_variations(bar, plates)
