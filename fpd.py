import time
import os
import collections
import concurrent.futures
from pprint import pprint
from functools import reduce
scientist = collections.namedtuple('scientist', ['name','nobel','born'])
ada = scientist(name="ada lovelace",nobel=True,born=3443)
richard=scientist(name="feynman",nobel=True,born=1934)
scs = [ada, richard, scientist(name="Tu you",nobel=True,born="1983"), scientist(name="Asd",born="1945",nobel=False),scientist(name="lewin",born=1978,nobel=False),scientist(name="Aqwer",born=1849,nobel=True), scientist(name="Loop",born=8972,nobel=False)]

#fs = (filter(lambda x: x.nobel is True, scs))
#for i in fs:
#    print(i)
n = [3,5,2,8]
print(list(map(lambda x : (x**2)>10,n)))
print(list(filter(lambda x : (x**2)>10,n)))
print((reduce(lambda x,y : (x*y),n)))
#
#def f1(a):
#    return lambda x : a+x
#
#add = f1(2)
#
#print(add(3))
#print(add(5))
#
#def trans(x):
#    print(f'Process {os.getpid()} working record {x.name}')
#    time.sleep(1)
#    result = {'name':x.name, 'age': 2018-x.born}
#    print(f'Process {os.getpid()} done processing record {x.name}')
#    return result
#start = time.time()
#with concurrent.futures.ThreadPoolExecutor() as ex:
#    result = ex.map(trans, scs)
#end = time.time()
#print(f'\n Time to complete {end-start:.2f}s\n')
#pprint(tuple(result))

# decorator functions
#def outf(fun):
#    def inf(*args,**kwargs):
#        print("from the inf function")
#        return fun(*args,**kwargs)
#    return inf
#
#@outf
#def display():
#    print("hey there")
#
#@outf
#def disp_info(name, age):
#    print(f"person is {name} and is {age} year old")
#
#disp_info('jms',45)
#display()

# class decorator functions
class dec_class():
    def __init__(self,origfunc):
        self.origfunc = origfunc

    def __call__(self,*args,**kwargs):
        print('call method executed')
        return self.origfunc(*args,**kwargs)

@dec_class
def display():
    print("hey there")

@dec_class
def disp_info(name, age):
    print(f"person is {name} and is {age} year old")

disp_info('jms',45)
display()


a = (x**2 for x in range(5))
try:
    while a != None:
        print(next(a))
except:
    print("list ends here")
print("yeh bematlab mein")
