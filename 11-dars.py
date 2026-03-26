# mevalar = {
#     'olma': 10000,
#     'anor': 15000,
#     'anjir': 5000,
#     'shaftoli': 20000
# }
# print("do'kondagi mevalar")
# for mahsulot in mevalar:
#     print(mevalar.keys())


telefonlar = {
    'ali':'samsung',
    'vali':'iphone',
    'hasan':'infinix',
    'husan': 'samsung'
}
# print("quyidagi telefondan foydalanadi")
# for tel in telefonlar.values():
#     print(tel)
print("quyidagi telefondan foydalanadi")
for tel in set(telefonlar.values()):
    print(tel)
