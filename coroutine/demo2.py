# coding = utf-8

def test():
    for i in range(5):
        print('start.')
        yield
        print('end.')


t = test()
print('1')
next(t)
t.send(1)
print('2')
t.send(1)
print('3')
t.send(1)
print('4')
t.send(1)
print('5')



