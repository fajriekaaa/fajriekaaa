def get_ltp(img, radius, neighbor, thresh, jumlah_binning):
  result_ltp = []
  upper_pattern = []
  lower_pattern = []
  res_upper = []
  res_lower = []
  for i in range(radius, len(img)-radius):
    for j in range(radius, len(img[i])-radius):
      center = img[i][j]upper_pattern.clear()
      lower_pattern.clear()
      top_left = [i -radius, j -radius]
      for theta in range(0, neighbor):
        rad = math.pi*(theta)/neighbor*2
        x = round(radius * math.sin(rad))+radius+top_left[0]
        y = round(radius * math.cos(rad))+radius+top_left[1]
        if theta != 0:
          if xtemp == x and ytemp == y:
            continue
        neig = img[x][y] 
        if neig >= center + thresh:
          upper_pattern.append(1)
          lower_pattern.append(0)
        elif abs(center -neig) < thresh or abs(neig -center) < thresh:
          upper_pattern.append(0)
          lower_pattern.append(0)
        elif neig <= center -thresh:
          upper_pattern.append(0)
          lower_pattern.append(1)
        xtemp, ytemp = x, y
      #konversi dansimpan nilai int
      u_string = [str(u) for u in upper_pattern]
      bin_string = ''.join(u_string)
      res_upper.append(int(bin_string, 2) + 256)
      l_string = [str(u) for u in lower_pattern]
      bin_string = ''.join(l_string)
      res_lower.append(int(bin_string, 2))
  res_all = res_lower + res_upper
