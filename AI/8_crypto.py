for a in range(10):
    for b in range (10):
        if a != b:
            ab = 10 * a + b
            if a+b == ab:
                print('true')
            else:
                print('false')