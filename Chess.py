from Queue import Queue

MOVEMENTS = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
map_axis = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

def is_already_verified(verifieds, position):
    for verified in verifieds:
        if verified.x_axis == position.x_axis and verified.y_axis == position.y_axis:
            return True
    return False

def get_possible_movements(position):
    ref = []
    for sum_x, sum_y in MOVEMENTS:
        new_position = Position(0, int(position.x_axis) + sum_x, int(position.y_axis) + sum_y)
        if new_position.is_valid_position:
            ref.append(new_position)
    return ref

class Position:
    def __init__(self, movements, x_axis, y_axis):
        self.movements = movements
        self.x_axis = x_axis
        self.y_axis = y_axis

    @property
    def is_valid_position(self):
        return (0 <= self.x_axis < 8) and (0 <= self.y_axis < 8)

def solving(source, aim):
    ref_queue = Queue(64)
    ref_queue.insert(source)
    verifieds = []

    while not ref_queue.is_empty:
        node = ref_queue.remove()
        if node.y_axis == aim.y_axis and node.x_axis == aim.x_axis:
            return node.movements
        else:
            for new_movement in get_possible_movements(node):
                if not is_already_verified(verifieds, new_movement):
                    new_movement.movements = node.movements + 1
                    ref_queue.insert(new_movement)
                    verifieds.append(node)

    raise Exception("Not found")


source = input()
source = Position(0, int(source[1])-1, map_axis[source[0]])

aim = input()
aim = Position(0, int(aim[1])-1, map_axis[aim[0]])

result = solving(source, aim)
print("Movimentos: %d" % (result))