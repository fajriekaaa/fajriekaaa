def lvq_test(x, W):
    W, c = W
    d = [sum((w - x) ** 2) for w in W]
    return c[np.argmin(d)]
