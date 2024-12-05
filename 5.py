def juft(sonlar):
    result = []
    for son in sonlar:
        birinchi_raqam = int(str(son)[0])
        if birinchi_raqam % 2 == 0:
            result.append((son))
    
    return result
sonlar =[12, 45, 67, 89, 100]
print(juft(sonlar))
