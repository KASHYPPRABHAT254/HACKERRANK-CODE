import operator
from operator import itemgetter

def person_lister(f):
    def inner(people):
        # complete the function
        #people.sort(key=operator.itemgetter(2))
        people = sorted(people, key = lambda x: (int(x[2])))
        ret = []
        for i in people:
            ret.append(f(i))
        return ret
    return inner  
@person_lister
