def generate_C1(data):
    c1 = set()
    for basket in data:
        for item in basket:
            item = frozenset([item])
            c1.add(item)
    return c1

def generate_Lk(data, Ck, min_support):
    Lk = set()
    item_count = {}
    frequent_item_count = {}

    for basket in data:
        for item in Ck:
            if item.issubset(basket):
                if item in item_count:
                    item_count[item] = item_count[item] + 1
                else:
                    item_count[item] = 1

    for k, v in item_count.items():
        support = v / len(data)
        if support >= min_support:
            Lk.add(k)
            frequent_item_count[k] = support

    return Lk, frequent_item_count

def generate_Ck_next(Lk, k):
    Ck_next = set()
    for s1 in Lk:
        for s2 in  Lk:
            s = s1 | s2
            if len(s) == k:
                Ck_next.add(s)
    
    return Ck_next