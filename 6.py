text = input("Matn kiriting: ")
def matn(text):
    uzun_soz = ""
    uzunlik = 0
    for soz in text.split():
        if len(soz) > uzunlik:
            uzun_soz = soz
            uzunlik = len(soz)
    return uzun_soz
uzun_soz= matn(text)
print(f"natija: {uzun_soz}")
