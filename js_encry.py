#coding:utf-8

# source : http://www.aspxhome.com/javascript/program/20103/1284528.htm

#this is the key
ts="8ABC7DLO5MN6Z9EFGdeJfghijkHIVrstuvwWSTUXYabclmnopqKPQRxyz01234"

# encode the content, jia mi
def s52e(n):
    N  = len(ts)
    N2 = N * N
    N5 = N * 5
    nl = len(n)
    t  = []

    def m (y):
        t.append(ts[y])

    for x in range(nl):
        a = ord(n[x])
        if (a<N5):
            m(int(a/N)),
            m(a%N)
        else:
            m(int(a/N2) + 5)
            m(int(a/N)%N)
            m(a%N)
    s = ''.join(t)
    return str(len(str(len(s)))) + str(len(s)) + s


# decode the content, jie mi
def s52d (n):
    c = n[0]
    if not c.isdigit():
        return ''
    c = n[1:1+int(c)]
    if not c.isdigit():
        return ''
    c = int(c)
    
    nl = len(n)
    t  = []
    x  = len(str(c)) + 1
    
    def m (y) :
        return ts.index(n[y])

    N = len(ts)

    if (nl != x+c):
        return ''

    while (x<nl):
        a = m(x)
        x += 1
        if (a<5):
            f = a*N+m(x)
        else:
            f = (a-5)*N*N+m(x)*N+m(x+1)
            x+= 1

        t.append(chr(f))
        x+= 1

    return ''.join(t)

