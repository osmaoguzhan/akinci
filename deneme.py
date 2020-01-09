def convert(text):
    keyValue={
        'Ç':'C',
        'ç':'c',
        'Ğ':'G',
        'ğ':'g',
        'İ':'I',
        'ı':'i',
        'Ö':'O',
        'ö':'o',
        'Ş':'S',
        'ş':'s',
        'Ü':'U',
        'ü':'u'
    }
    for key in keyValue.keys():
        if key in text:
          text= text.replace(key,keyValue[key])
        else:
            print("Yok")
    return text
print(convert("ÇçĞğİıÖöŞşÜü"))