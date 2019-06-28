# coding = utf-8 

def consumer():
    print('enter consumer.')
    r = ''
    while True:
        print('enter consumer while.')
        n = yield r 
        if not n:
            print('consumer return.')
            return 
        print('consuming %s' % n)
        r = '200 OK'


def produce(c):
    print('entry produce.')
    c.send(None)
    n = 0
    while n < 5:
        print('enter produce while.')
        n += 1
        print('Producing %s' % n)
        r = c.send(n)
        print('comsumer return %s' % r)
    c.close()

c = consumer()
produce(c)



