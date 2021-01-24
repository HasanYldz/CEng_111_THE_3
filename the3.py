def make_tree(part_list):
    sub_parts_tuples = [part_list[a] for a in range(len(part_list)) if type(part_list[a][1]) != tuple]
    sub_parts = [sub_parts_tuples[a][0] for a in range(len(sub_parts_tuples))]
    part_list = [part_list[a] for a in range(len(part_list)) if type(part_list[a][1]) == tuple]
    new_sub = []
    # while part_list != []:
    for i in range(len(part_list)):
        for e in range(1, len(part_list[i])):
            if part_list[i][e][1] in sub_parts:
                ind = sub_parts.index(part_list[i][e][1])
                part = sub_parts_tuples[ind]
                part_list[i][e] = [part_list[i][e][0], part]
    return part_list


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

print(make_tree(lst))

