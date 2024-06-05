import json
from process import read_data
from apriori import generate_C1, generate_Lk, generate_Ck_next, Ck_support, association_rules

if __name__ == "__main__":
    data = read_data('../data/keyword_link.txt')
    with open('../tmp/data.json', 'w') as file:
        json.dump(data, file)

    c1 = generate_C1(data)
    c1_list = [list(item) for item in c1]
    with open('../tmp/C1.json', 'w') as file:
        json.dump(c1_list, file)

    l1, l1_count = generate_Lk(data, c1, 0.15)
    l1_list = [list(item) for item in l1]
    with open('../tmp/L1.json', 'w') as file:
        json.dump(l1_list, file)
    
    c2 = generate_Ck_next(l1, 2)
    c2_list = [list(item) for item in c2]
    with open('../tmp/C2.json', 'w') as file:
        json.dump(c2_list, file)

    l2, l2_count = generate_Lk(data, c2, 0.15)
    l2_list = [list(item) for item in l2]
    with open('../tmp/L2.json', 'w') as file:
        json.dump(l2_list, file)
    
    c3 = generate_Ck_next(l2, 3)
    c3_list = [list(item) for item in c3]
    with open('../tmp/C3.json', 'w') as file:
        json.dump(c3_list, file)

    l3, l3_count = generate_Lk(data, c3, 0.15)
    l3_list = [list(item) for item in l3]
    with open('../tmp/L3.json', 'w') as file:
        json.dump(l3_list, file)

    c4 = generate_Ck_next(l3, 4)
    c4_list = [list(item) for item in c4]
    with open('../tmp/C4.json', 'w') as file:
        json.dump(c4_list, file)
    
    l4, l4_count = generate_Lk(data, c4, 0.15)
    l4_list = [list(item) for item in l4]
    with open('../tmp/L4.json', 'w') as file:
        json.dump(l4_list, file)

    