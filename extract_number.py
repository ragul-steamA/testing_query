def extract_phone_number(s):
    parts = s.split('+')
    for part in parts:
        if part.isdigit() and len(part) == 12:
            return part
f=open("numbers.txt", "w", encoding="utf8")
with open('extract.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        print(num)
        phone_number = extract_phone_number(num)
        print(phone_number)
        
        f.write(str(phone_number))
        f.write('\n')
