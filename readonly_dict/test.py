import unittest
from readonly_dict import DictObj


class TestReadonlyDict(unittest.TestCase):
    def test_checkfilename(self):
        self.assertRaises(FileNotFoundError, DictObj.readDict, 'confi.json')

    def test_setattr(self):
        self.assertRaises(AttributeError, checkSetattr, 100)

    def test_delattr(self):
        self.assertRaises(AttributeError, checkDelattr)


def checkSetattr(value):
    mydict = DictObj.readDict('config.json')
    myconfig = DictObj(mydict)
    myconfig.dbname = value


def checkDelattr():
    mydict = DictObj.readDict('config.json')
    myconfig = DictObj(mydict)
    del myconfig.dbname


if __name__ == '__main__':
    unittest.main()
