def diff_sec(h1,m1,s1, h2,m2,s2):
    if (type(h1) == int and 0<=h1<24) and (type(m1) == int and 0<=m1<60) and (type(s1) == int and 0<=s1<60) and (type(h2) == int and 0<=h2<24) and (type(m2) == int and 0<=m2<60) and (type(s2) == int and 0<=s2<60):
        h1 *= 3600
        m1*= 60
        h2 *= 3600
        m2*= 60

        r1 = h1 + m1 + s1
        r2 = h2 + m2 + s2
        if r2>=r1:
            d = r2-r1
            return d
    
            
            

print(diff_sec(1,0,0,2,0,0))


# def difference_heures(h1, m1, s1, h2, m2, s2):
#     if 0<=h1<24 and 0<=m1<60 and 0<=s1<60 and 0<=h2<24 and 0<=m2<60 and 0<=s2<60:
#         if s2>s1:
#             s1+=60
#             m1-=m1
            
#             if m2>m1:
#                 m1+=60
#                 h1-=1 
#                 d = ((h1-h2)*60*60)+((m1-m2)*60)+s1-s2 
#             elif m1>m2:
#                 d = ((h1-h2)*60*60)+((m1-m2)*60)+s1-s2
#         elif m2>m1:
#             m1+=60
#             h1-=1 
#             d = ((h1-h2)*60*60)+((m1-m2)*60)+s1-s2
#         else:
#             d = ((h1-h2)*60*60)+((m1-m2)*60)+s1-s2
#         return d