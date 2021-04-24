def get_rgb(img):
    red = []
    gre = []
    blu = []
    
    for i in range(len(img)):
        for j in range(len(img[i])):
            red.append(img[i][j][2])
            gre.append(img[i][j][1])
            blu.append(img[i][j][0])
    
    #mean
    mean_red = np.mean(red)
    mean_gre = np.mean(gre)
    mean_blu = np.mean(blu)
    
    return mean_red, mean_gre, mean_blu
