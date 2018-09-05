#Given a string, return the shortest word/words contained within

def find_short(s):
    store =  []
    for each in s.split():
        cur = len(each)
        store.append(cur)
    low = min(store)
    return low
