print("Qauntum numbers calculator\nMade by: SalahDin Ahmed\nSpecial thanks to: Ms. Doaa Abdel Menaam\nNOTE: the program can only be used for numbers less than or equal 18")
working = True
while working == True:
    e = input("Enter number of electrons ")
    e = int(e)
    n = 1
    l = 0
    p = e
    o = 2 * n ** 2
    s=['s','p','d','f','g','h']
    ps=[2,6,10,14]
    # claculate the principle quantum number and the number of electrons in the outer energy level
    while not (e <= o):
            n += 1
            o = o + 2 * n ** 2
            p = p - 2 * (n - 1) ** 2
    # calculate the angular quantum number
    while not p <= 2 * (2 * l + 1):
        p = p - 2 * (2 * l + 1)
        l += 1
    # calculate the spin quantum number
    if p <= 2 * l + 1:
        m_s = 0.5
    elif p > 2 * l + 1:
        m_s = -0.5
    # calculate the magnetic quantum number
    if m_s == 0.5:
        m_i = p
    elif m_s == -0.5:
        m_i = p - (2 * l + 1)
    m_l = range(-l, l + 1)[m_i - 1]
    #if 
    # print result
    print("n =", n)
    print("l =", l)
    print("m_l =", m_l)
    print("m_s =", m_s)
    print(p)
    if l <= len(s):
        if n == 1:
            print(n,s[l],"^",p, sep="")
        if n == 2:
            if l == 0:
                print("1s^2 ",n,s[l],"^",p, sep="")
            if l == 1:
                print("1s^2 2s^2 ",n,s[l],"^",p, sep="")
        if n == 3:
            if l == 0:
                print("1s^2 2s^2 2p^6 ",n,s[l],"^",p, sep="")
            if l == 1:
                print("1s^2 2s^2 2p^6 3s^2 ",n,s[l],"^",p, sep="")
