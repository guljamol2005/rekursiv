text = input("Matn kiriting: ")
def matn (text):
    harf = {}
    for char in text:
        if char != " ":  
            if char in harf:
                harf[char] += 1
            else:
                harf[char] = 1
    result = list((count, char) for char, count in harf.items())
    print(result)
matn(text)
