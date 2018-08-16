# -*- coding:utf-8 -*- 
# @Time		:2018/8/16 4:21 PM
# @Author	:Coast Cao

class T():
  def __init__(self):
    a = 1;
    self.b = a + 1;
    self.a = 2;
    print("id of a: %d" % id(a));
    print("id of self.a: %d" % id(self.a));

  def p(self):
    print("self.a= %d " % self.a);
    #print(a);
    print("self.b= %d " % self.b);

t = T();
t.p();