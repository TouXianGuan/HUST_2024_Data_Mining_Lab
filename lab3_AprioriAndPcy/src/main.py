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

    c1_count = Ck_support(data, c1)
    c1_count_dict = {str(k).replace('frozenset(', '').replace(')', ''): v for k, v in c1_count.items()}
    with open('../tmp/C1_count.json', 'w') as file:
        json.dump(c1_count_dict, file)

    l1, l1_count = generate_Lk(data, c1, 0.15)
    l1_list = [list(item) for item in l1]
    l1_count_dict = {str(k).replace('frozenset(', '').replace(')', ''): v for k, v in l1_count.items()}
    with open('../tmp/L1.json', 'w') as file:
        json.dump(l1_list, file)
    with open('../result/L1_count.json', 'w') as file:
        json.dump(l1_count_dict, file)
    print('len_L1:', len(l1))
    
    c2 = generate_Ck_next(l1, 2)
    c2_list = [list(item) for item in c2]
    with open('../tmp/C2.json', 'w') as file:
        json.dump(c2_list, file)

    c2_count = Ck_support(data, c2)
    c2_count_dict = {str(k).replace('frozenset(', '').replace(')', ''): v for k, v in c2_count.items()}
    with open('../tmp/C2_count.json', 'w') as file:
        json.dump(c2_count_dict, file)

    l2, l2_count = generate_Lk(data, c2, 0.15)
    l2_list = [list(item) for item in l2]
    l2_count_dict = {str(k).replace('frozenset(', '').replace(')', ''): v for k, v in l2_count.items()}
    with open('../tmp/L2.json', 'w') as file:
        json.dump(l2_list, file)
    with open('../result/L2_count.json', 'w') as file:
        json.dump(l2_count_dict, file)
    print('len_L2:', len(l2))
    
    c3 = generate_Ck_next(l2, 3)
    c3_list = [list(item) for item in c3]
    with open('../tmp/C3.json', 'w') as file:
        json.dump(c3_list, file)

    c3_count = Ck_support(data, c3)
    c3_count_dict = {str(k).replace('frozenset(', '').replace(')', ''): v for k, v in c3_count.items()}
    with open('../tmp/C3_count.json', 'w') as file:
        json.dump(c3_count_dict, file)

    l3, l3_count = generate_Lk(data, c3, 0.15)
    l3_list = [list(item) for item in l3]
    l3_count_dict = {str(k).replace('frozenset(', '').replace(')', ''): v for k, v in l3_count.items()}
    with open('../tmp/L3.json', 'w') as file:
        json.dump(l3_list, file)
    with open('../result/L3_count.json', 'w') as file:
        json.dump(l3_count_dict, file)
    print('len_L3:', len(l3))

    c4 = generate_Ck_next(l3, 4)
    c4_list = [list(item) for item in c4]
    with open('../tmp/C4.json', 'w') as file:
        json.dump(c4_list, file)
    
    l4, l4_count = generate_Lk(data, c4, 0.15)
    l4_list = [list(item) for item in l4]
    l4_count_dict = {str(k).replace('frozenset(', '').replace(')', ''): v for k, v in l4_count.items()}
    with open('../tmp/L4.json', 'w') as file:
        json.dump(l4_list, file)
    with open('../result/L4_count.json', 'w') as file:
        json.dump(l4_count_dict, file)
    print('len_L4:', len(l4))

    rules_2 = association_rules(c1, l1_count, c2_count, 0.3)
    rules_2_dict = {str(k).replace('frozenset(', '').replace(')', ''): v for k, v in rules_2.items()}
    with open('../result/rules_2.json', 'w') as file:
        json.dump(rules_2_dict, file)
    print('rules_2:', len(rules_2))

    rules_3 = association_rules(c1, l2_count, c3_count, 0.3)
    rules_3_dict = {str(k).replace('frozenset(', '').replace(')', ''): v for k, v in rules_3.items()}
    with open('../result/rules_3.json', 'w') as file:
        json.dump(rules_3_dict, file)
    print('rules_3:', len(rules_3))

    print('rules:', len(rules_2) + len(rules_3))