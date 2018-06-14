import time
import json
#import sys
#sys.setrecursionlimit(1000000)

class DictObj(object):
    __init = False

    def __init__(self, map):
        self.map = map
        self.__init = True

    def __setattr__(self, name, value):
        if(self.__init):
            raise AttributeError('{}.{} is READ ONLY'.format(type(self).__name__, name))
        else:
            object.__setattr__(self, name, value)
    
    def __delattr__(self, name):
        if(self.__init):
            raise AttributeError('{}.{} is READ ONLY.You can delete nothing!'.format(type(self).__name__, name))
        else:
            object.__delattr__(self, name)

    def __getattr__(self, name):
        v = self.map[name]
        if isinstance(v, (dict)):
            return DictObj(v)
        if isinstance(v, (list)):
            r = []
            for i in v:
                r.append(DictObj(i))
            return r
        else:
            return self.map[name]

    def __getitem__(self, name):
        return self.map[name]

    def readDict(filename):
        with open(filename) as f:
            d = json.load(f)
        return d


if __name__ == '__main__':
    #m = {'haha': {'a': 55}, 'bb': [{'c': 32, 'd': 45}, {'c': 22, 'd': 56}]}
    m = DictObj.readDict('config.json')
    print(m)
    book = DictObj(m)
    #print(book.dbname)
    del book.db
    print(book.db)
