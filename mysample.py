
from common import read_input, print_solution
import sys
import math
"""
ABCD
EFGH
"""

def nearcities(city_group1,city_group2, stop_city=None ):
    if city_group1 == [] or  city_group2  == []:
        min_city1  = 0
        min_city2 = 0
        return min_city1, min_city2
    min_length = 0
    min_city1 = 0
    min_city2 = 0
    for x1, y1 in city_group1 :
        for x2, y2 in city_group2 :
            length = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            if min_length == 0 or (min_length > length and (x1,y1) not in [stop_city] and (x2,y2) not in [stop_city]) :
                min_length = length
                min_city1 = (x1, y1)
                min_city2 = (x2, y2)
    if min_city1 == 0:
        min_city1 = ()
    if min_city2 == 0:
        min_city2 = ()
    return min_city1,min_city2

def split_group(data = read_input(sys.argv[1])):
    a_group = []
    a_store = {}
    b_group = []
    b_store = {}
    c_group = []
    c_store = {}
    d_group = []
    d_store = {}
    e_group = []
    e_store = {}
    f_group = []
    f_store = {}
    g_group = []
    g_store = {}
    h_group = []
    h_store = {}
    all_store = {}
    num = 0
    for x, y in data:
        if 0 <= x < 400 :
            if 0 <= y <400 :
                a_group.append((x, y))
                a_store[num] = (x, y)
            elif 400 <= y :
                e_group.append((x,y))
                e_store[num] = (x, y)
        elif 400 <= x < 800 :
            if 0 <= y <400 :
                b_group.append((x, y))
                b_store[num] = (x, y)
            elif 400 <= y :
                f_group.append((x,y))
                f_store[num] = (x, y)
        elif 800 <= x < 1200 :
            if 0 <= y <400 :
                c_group.append((x, y))
                c_store[num] = (x, y)
            elif 400 <= y :
                g_group.append((x,y))
                g_store[num] = (x, y)
        elif 1200 <= x :
            if 0 <= y <400 :
                d_group.append((x, y))
                d_store[num] = (x, y)
            elif 400 <= y :
                h_group.append((x,y))
                h_store[num] = (x, y)
        num+=1

    for idx, city in enumerate(data):
        all_store[idx] = city            
    
    return a_group, b_group, c_group, d_group, e_group, f_group, g_group, h_group, \
        a_store, b_store, c_store, d_store, e_store, f_store, g_store, h_store, all_store

def center_city(xnear1, xnear2):
    x = abs(xnear1[0]- xnear2[0]) / 2
    y = abs(xnear1[1]- xnear2[1]) / 2
    return (x, y)

def line_center_farcity(x_group, xnear1, xnear2):#区画と近い点2つ
    max_length = 0
    uppercity = []
    lowercity = []
    #farcity = (0, 0)
    if x_group == []or len(x_group) == 1  or xnear1 == 0 or xnear2 == 0:
        uppercity == []
        lowercity == []
        farcity = ()
        xnear1_upper = 0
        """
        print('@@@')
        print(x_group, xnear1, xnear2)
        print()
        """
        return uppercity, lowercity, farcity, xnear1_upper
    """
    print()
    print(xnear1)
    print(xnear2)
    """
    farcity = 0
    centerx, centery = center_city(xnear1, xnear2)#隣り合った区画と近い市の中点
    for x, y in x_group:
        length = math.sqrt((centerx-x)**2 + (centery-y)**2)#中点と区画内の他の点の距離
        if (max_length == 0 or max_length < length)and((x,y) not in [xnear1, xnear2, (centerx, centery)]):
            max_length = length
            farcity = (x, y)
    
    m = (centery - farcity[1]) / (centerx - farcity[0])
    high_flag = 0
    X = xnear1[0]
    Y = m * (X - centerx) + centery
    if xnear1[1] > Y :
        high_flag += 1
    elif xnear1[1] <= Y :
        high_flag = 0
    xnear1_upper  = high_flag 
    for x, y in x_group:
        if (x,y) in [farcity, xnear1, xnear2]:
            pass
        else:
            X = x
            Y = m * (X - centerx) + centery
            if y > Y :
                uppercity.append((x,y))
            elif y <= Y :
                lowercity.append((x,y))
    if type(farcity) == int:
        farcity = ()
    
    return uppercity, lowercity , farcity, xnear1_upper


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def dist_sort(startcity, city_lst):
    
    if len(city_lst) ==0:
        return tuple(city_lst)
    elif len(city_lst) == 1:
        return list(city_lst)[0]
    else:
        sorted_city_lst = []
        current_city = startcity
        while True :
            distance_lst = []
            for city in city_lst:
                dist = distance(current_city, city)
                distance_lst.append(dist)
            min_idx = distance_lst.index(min(distance_lst))
            sorted_city_lst.append(city_lst[min_idx])
            current_city = city_lst[min_idx]
            del city_lst[min_idx]
            if len(city_lst) == 0:
                return tuple(sorted_city_lst)


    
if __name__ == '__main__':
    assert len(sys.argv) > 1
    
    a_group, b_group, c_group, d_group, e_group, f_group, g_group, h_group, \
        a_store, b_store, c_store, d_store, e_store, f_store, g_store, h_store, all_store = split_group(data = read_input(sys.argv[1]))
    a_nearb, b_neara = nearcities(a_group, b_group)
    b_nearc, c_nearb = nearcities(b_group, c_group)
    c_neard, d_nearc = nearcities(c_group, d_group)
    d_nearh, h_neard = nearcities(d_group, h_group)
    g_nearh, h_nearg = nearcities(g_group, h_group)
    f_nearg, g_nearf = nearcities(f_group, g_group)
    e_nearf, f_neare = nearcities(e_group, f_group)
    a_neare, e_neara = nearcities(a_group, e_group) 

    
    
    high_a, low_a, farcity_a, a_neareisupper= line_center_farcity(a_group, a_neare, a_nearb)
    high_d, low_d, farcity_d, d_nearcisupper = line_center_farcity(d_group, d_nearc, d_nearh)
    high_h, low_h, farcity_h, h_neardisupper= line_center_farcity(h_group, h_neard, h_nearg)
    high_e, low_e, farcity_e, e_nearfisupper = line_center_farcity(e_group, e_nearf, e_neara)
    high_b, low_b, farcity_b, b_nearaisupper = line_center_farcity(b_group, b_neara, b_nearc)
    high_c, low_c, farcity_c, c_nearbisupper = line_center_farcity(c_group, c_nearb, c_neard)
    high_f, low_f, farcity_f, f_neargisupper = line_center_farcity(f_group, f_nearg, f_neare)
    high_g, low_g, farcity_g, g_nearhisupper = line_center_farcity(g_group, g_nearh, g_nearf)
    
    if b_nearaisupper == 1:
        b_queue = (b_neara, dist_sort(b_neara, high_b), farcity_b, dist_sort(farcity_b, low_b), b_nearc)
    elif b_nearaisupper == 0:
        b_queue = (b_neara, dist_sort(b_neara, low_b), farcity_b, dist_sort(farcity_b, high_b), b_nearc)
    if c_nearbisupper == 1:
        c_queue = (c_nearb, dist_sort(c_nearb, high_c), farcity_c, dist_sort(farcity_c, low_c), c_neard) 
    elif c_nearbisupper == 0:
        c_queue = (c_nearb, dist_sort(c_nearb, low_c), farcity_c, dist_sort(farcity_c, high_c), c_neard)
    if d_nearcisupper == 1:
        d_queue = (d_nearc, dist_sort(d_nearc, high_d), farcity_d, dist_sort(farcity_d, low_d), d_nearh) 
    elif d_nearcisupper == 0:
        d_queue = (d_nearc, dist_sort(d_nearc, low_d), farcity_d, dist_sort(farcity_d, high_d), d_nearh)                
    if h_neardisupper == 1:
        h_queue = (h_neard, dist_sort(h_neard, high_h), farcity_h, dist_sort(farcity_h, low_h), h_nearg) 
    elif h_neardisupper == 0:
        h_queue = (h_neard, dist_sort(h_neard, low_h), farcity_h, dist_sort(farcity_h, high_h), h_nearg)
    if g_nearhisupper == 1:
        g_queue = (g_nearh, dist_sort(g_nearh, high_g), farcity_g, dist_sort(farcity_g, low_g), g_nearf) 
    elif g_nearhisupper == 0:
        g_queue = (g_nearh, dist_sort(g_nearh, low_g), farcity_g, dist_sort(farcity_g, high_g), g_nearf)
    if f_neargisupper == 1:
        f_queue = (f_nearg, dist_sort(f_nearg, high_f), farcity_f, dist_sort(farcity_f, low_f), f_neare) 
    elif f_neargisupper == 0:
        f_queue = (f_nearg, dist_sort(f_nearg, low_f), farcity_f, dist_sort(farcity_f, high_f), f_neare)
    if e_nearfisupper == 1:
        e_queue = (e_nearf, dist_sort(e_nearf, high_e), farcity_e, dist_sort(farcity_e, low_e), e_neara) 
    elif e_nearfisupper == 0:
        e_queue = (e_nearf, dist_sort(e_nearf, low_e), farcity_e, dist_sort(farcity_e, high_e), e_neara)
    if a_neareisupper == 1:
        a_queue = (a_neare, dist_sort(a_neare, high_a), farcity_a, dist_sort(farcity_a, low_a), a_nearb) 
    elif a_neareisupper == 0:
        a_queue = (a_neare, dist_sort(a_neare, low_a), farcity_a, dist_sort(farcity_a, high_a), a_nearb)
    
    
    
    queue_list = {b_queue : b_store, c_queue : c_store, d_queue : d_store, h_queue : h_store, g_queue : g_store, f_queue : f_store, e_queue : e_store, a_queue : a_store }
    que_idx_list  = [b_queue, c_queue,d_queue,h_queue,g_queue,f_queue,e_queue,a_queue]
    que_group_list = [b_group,c_group,d_group,h_group,g_group,f_group,e_group,a_group]
    idx_list = []
    num1 = 0
    num2 =0
    num =0
            
    for queue, group in zip(que_idx_list,que_group_list):
        for idx, element in enumerate(queue):
            if element == () or element == [] or element == 0:
                pass

            elif len(element)>=2 and type(element[0]) == tuple:
                for ele in element:
                    key = [key for key, val in queue_list[queue].items() if ele == val]
                    idx_list += key
                    del group[group.index(ele)]
            else:
                key = [key for key, val in queue_list[queue].items() if element == val ]                
                if key == []:
                    if element == ():
                        pass
                else:
                    if key[0] in idx_list:
                        pass                 
                    else:
                        idx_list += key
                        del group[group.index(element)]
        if len(group) != 0:
            for ele in group:
                key = [key for key, val in queue_list[queue].items() if ele == val]
                
                
                if key == []:
                    key = [key for key, val in all_store.items() if ele == val]
                    if key == []:
                        pass
                    else:
                        if key[0] not in idx_list: 
                            idx_list += key
 
                else:
                    if key[0] not in idx_list: 
                        idx_list += key
    
    for i in range(len(idx_list)):
        for j in range(len(idx_list)):
            if i==j:
                pass
            else:
                N = len(idx_list)
                try:
                    A, B, C, D =  idx_list[i], idx_list[i+1], idx_list[j], idx_list[(j+1) % N]
                    if distance(all_store[A],all_store[B]) + distance(all_store[C],all_store[D])> distance(all_store[A],all_store[C]) + distance(all_store[B],all_store[D]):
                        idx_list[i+1:j+1] = reversed(idx_list[i+1:j+1])

                except IndexError:
                    pass
                    
    
    #print(idx_list)
    #print(len(idx_list))
    #print([x for x in set(idx_list) if idx_list.count(x) > 1])
    #print(sorted(idx_list))
    #
    print_solution(idx_list)
