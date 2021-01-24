def make_tree(part_list):
    sub_parts = [part_list[a] for a in range(len(part_list)) if type(part_list[a][1]) != tuple]
    sub_parts_catalogue = [sub_parts[a][0] for a in range(len(sub_parts))]
    part_list = [part_list[a] for a in range(len(part_list)) if type(part_list[a][1]) == tuple]
    while part_list:
        new = []
        for i in range(len(part_list)):
            for e in range(1, len(part_list[i])):
                if part_list[i][e][1] in sub_parts_catalogue:
                    ind = sub_parts_catalogue.index(part_list[i][e][1])
                    part = sub_parts[ind]
                    part_list[i][e] = (part_list[i][e][0], part)
            if all(type(part) == list for (_, part) in part_list[i][1:]):
                sub_parts.append(part_list[i])
                sub_parts_catalogue.append(part_list[i][0])
                new.append(i)
        if len(part_list) == 1:
            tree = part_list[0]
            part_list = []
        else:
            for a in reversed(new):
                del part_list[a]

    return tree


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



def calculate_price(part_list):
    def helper(x):
        if type(x[1]) == float:
            return x[1]
        res = 0
        for i in range(1, len(x)):
            res += x[i][0] * helper(x[i][1:][0])
        return res
    return helper(make_tree(part_list))


def required_parts(part_list):
    def helper(x):
        if type(x[1]) == float:
            return [(1, x[0])]
        res = []
        for i in range(1, len(x)):
            branch = helper(x[i][1:][0])
            for a in range(len(branch)):
                res.append((x[i][0]*branch[a][0], branch[a][1]))
        return res

    return helper(make_tree(part_list))


tre = ["bike", (2, ["wheel", (1, ["rim", 60.]), (1, ["spoke", 120.]),(1, ["hub", (2, ["gear", 25.]), (1, ["axle", (5, ["bolt", 0.1]), (7, ["nut", 0.15])])])]), (1, ["frame", (1, ["rearframe", 175.]), (1, ["frontframe", (1, ["fork", 22.5]), (2, ["handle", 10.])])])]
stock_list = [(2, "rim"), (2, "spoke"), (4, "gear"), (8, "bolt"), (12, "nut"), (1, "rearframe"), (1, "fork"), (1, "handle")]

def stock_check(part_list, stock_list):
    need = required_parts(part_list)
    need_catalogue = [need[a][1] for a in range(len(need))]
    necessary_stock = [stock_list[a] for a in range(len(stock_list)) if stock_list[a][1] in need_catalogue ]
    stock_catalogue = [necessary_stock[a][1] for a in range(len(necessary_stock))]
    short = []
    for part in need:
        if part[1] in stock_catalogue:
            ind = stock_catalogue.index(part[1])
            l = part[0] - stock_list[ind][0]
            if l > 0:
                short.append((part[1], l))
        else:
            short.append((part[1], part[0]))
    return short



# print(make_tree(lst))
# print(calculate_price(lst))
# print(required_parts(lst))
# print(stock_check(lst,stock_list))