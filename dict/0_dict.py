from multidict import CIMultiDict

dic = CIMultiDict()
dic["key"] = "1234"
print(dic["KEy"])


a = {'a':'aaaa'}
print(type(a))
print(CIMultiDict(a)['A'])