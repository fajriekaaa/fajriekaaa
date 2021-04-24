def lvq_train(X, y, a, b, max_ep):
    #initiating classes
    c, train_idx = np.unique(y, True)
    
    #initiating bobot awal
    W = np.array(X)[train_idx].astype(np.float64)
    #initiating train data
    train = np.array([e for i, e in enumerate(zip(X, y)) if i not in train_idx])
    X = train[:, 0]
    y = train[:, 1]
            
    ep = 0
    while ep < max_ep:
        for i, x in enumerate(X):
            #langkah 4 ||x - Wj||
            print('x',x)
            print('w',w)
            
            d = [sum((w-x) ** 2) for w in W]
            min = np.argmin(d)
            
            s = 1 if y[i] == c[min] else -1
            W[min] += s * a * (x - W[min])
    
        a *= b
        ep += 1
    
    return W, c
