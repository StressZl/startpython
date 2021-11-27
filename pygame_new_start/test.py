import random


def set_room_in_map(Map=None, room_point=None):
    for point in room_point:
        p_x = point[0] + len(Map)//2
        p_y = point[1] + len(Map)//2
        Map[p_x][p_y] = 'O'
    return Map


def set_room_type():
    # 特殊房间的生成几率为10%
    rx = random.randint(0, 10)
    type_value = 1 if rx != 1 else random.randint(2, 4)
    return type_value


def get_room_point(room_point_list, type_value):
    type_dict = {1: '正方形房间', 2: '矩形房间', 3: 'L形房间', 4: '大正方形房间'}
    dir_dict = {'UP': (1, 0), 'DOWN': (-1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}
    dir_list = list(dir_dict.keys())
    last_point = room_point_list[-1]
    all_point_list = []
    for pi in room_point_list:
        all_point_list = all_point_list + pi
    if type_value == 1:
        # 生成单点
        print(type_dict[type_value])
        # 选择方向xx
        random.shuffle(dir_list)
        for dirs in dir_list:
            print(dirs)
            dir_point = dir_dict[dirs]
            d_x = last_point[0]+dir_point[0]
            d_y = last_point[1]+dir_point[1]
            new_point = (d_x, d_y)
            if new_point not in all_point_list:
                break
            return new_point
    if type_value == 2:
        # 生成双点
        for i in range(2):
            print()
        print(type_dict[type_value])
        return [(0, 0), (1, 1)]
    if type_value == 3:
        # 生成三点
        print(type_dict[type_value])
        return [(0, 0), (1, 1), (0, 1)]
    if type_value == 4:
        # 生成四点
        print(type_dict[type_value])
        return [(0, 0), (1, 1), (0, 1), (1, 0)]


# # 创造13*7的格子
# # 初始化房间
# room_data = [['X' for i in range(13)] for j in range(7)]
# # 房间生成算法，一层生成10个房间
# # 创造空地图空间 20*20
# map_data = [['X' for x in range(20)] for y in range(20)]
# type_v = set_room_type()
# room_point = get_room_point(type_v)
# map_data = set_room_in_map(map_data, room_point)
# for i in map_data:
#     print(i)
