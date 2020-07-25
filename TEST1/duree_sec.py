def duree_second(j, h, m, s):
    if (type(j) == int and j>0) and (type(h) == int and 0<=h<24) and (type(m) == int and 0<=m<60) and (type(s) == int and 0<=s<60):
        j *= 86400
        h *= 3600
        m *= 60
        ds = j + h + m + s
        return ds
    else:
        return -1

print(duree_second(1,5,2,1))