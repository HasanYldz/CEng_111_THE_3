def make_tree(part_list):
    sub_parts = [part_list[a] for a in range(len(part_list)) if type(part_list[a][1]) != tuple]
    sub_parts_catalogue = [sub_parts[a][0] for a in range(len(sub_parts))]
    part_list = [part_list[a] for a in range(len(part_list)) if type(part_list[a][1]) == tuple]
    new_sub = []
    for a in range(10):
        for i in range(len(part_list)):
            for e in range(1, len(part_list[i])):
                if part_list[i][e][1] in sub_parts_catalogue:
                    ind = sub_parts_catalogue.index(part_list[i][e][1])
                    part = sub_parts[ind]
                    part_list[i][e] = (part_list[i][e][0], part)
            if all(type(part) == list for part in part_list[i][1:]):
                sub_parts.append(part_list[i])
                sub_parts_catalogue.append(part_list[i][0])
    return sub_parts


lst =        [["bike", (2, "wheel"), (1, "frame")],
             ["wheel", (1, "rim"), (1, "spoke"),(1, "hub")],
             ["rim", 60.],
             ["spoke", 120.],
             ["hub", (2, "gear"), (1, "axle")],
             ["gear", 25.],
             ["axle", (5, "bolt"), (7, "nut")],
             ["bolt", 0.1],
             ["nut", 0.15],
             ["frame", (1, "rearframe"), (1, "frontframe")],
             ["rearframe", 175.],
             ["frontframe", (1, "fork"), (2, "handle")],
             ["fork", 22.5],
             ["handle", 10.]]

tree = ["bike", (2, ["wheel", (1, ["rim", 60.]), (1, ["spoke", 120.]),(1, ["hub", (2, ["gear", 25.]), (1, ["axle", (5, ["bolt", 0.1]), (7, ["nut", 0.15])])])]), (1, ["frame", (1, ["rearframe", 175.]), (1, ["frontframe", (1, ["fork", 22.5]), (2, ["handle", 10.])])])]
deneme = [['bike', (2, 'wheel'), (1, 'frame')], ['wheel', (1, ['rim', 60.0]), (1, ['spoke', 120.0]), (1, 'hub')], ['hub', (2, ['gear', 25.0]), (1, 'axle')], ['axle', (5, ['bolt', 0.1]), (7, ['nut', 0.15])], ['frame', (1, ['rearframe', 175.0]), (1, 'frontframe')], ['frontframe', (1, ['fork', 22.5]), (2, ['handle', 10.0])]]
def calculate_price(part_list):
    tree = part_list
    if type(tree[1]) == float:
        return tree[1]
    res = 0
    for i in range(1,len(tree)):
        res += tree[i][0] * calculate_price(tree[i][1:][0])
    return res


print(make_tree(lst))

