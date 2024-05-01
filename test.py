a = ['banh mi ba huan', 'bugerking']
b = ['quan 1', 'quan 3']
c = [['banh mi thit', 'banh mi cha', 'banh mi trung'], []]


ten_quan = []
dia_chi = []
ten_mon= []

for i in range(0,len(a)):
    mon = c[i]
    quan = a[i]
    dc = b[i]
    if mon: 
        for n in mon: 
                ten_quan.append(quan)
                dia_chi.append(dc)
                ten_mon.append(n)
    else: 
         ten_quan.append(quan)
         dia_chi.append(dc)
         ten_mon.append('None')

print(ten_mon)
