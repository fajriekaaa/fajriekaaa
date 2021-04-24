def get_hsv(img_hsv):
    
    hue = []
    sat = []
    val = []
    
    for i in range(len(img_hsv)):
        for j in range(len(img_hsv[i])):
            hue.append(img_hsv[i][j][0])
            sat.append(img_hsv[i][j][1])
            val.append(img_hsv[i][j][2])
    
    #mean
    mean_hue = np.mean(hue)
    mean_sat = np.mean(sat)
    mean_val = np.mean(val)
    
    return mean_hue, mean_sat, mean_val
