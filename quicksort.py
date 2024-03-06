import random

def quicksort(n):
    if len(n) <= 1:
        return n
    else:
        l_list = []
        m_list = []
        r_list = []
        q = random.choice([x for x in n])
        for a in n:
            if a['date'] < q['date']:
                l_list.append(a)
            elif a['date'] > q['date']:
                r_list.append(a)
            else:
                m_list.append(a)
        return quicksort(l_list) + m_list + quicksort(r_list)