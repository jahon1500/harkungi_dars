# ism = []
# n=1
# while True:
#     savol = f"{n}-do'stingizni ismini kiriiting"
#     ismlar = input(savol)
#     ism.append(ism)
#     takrorlash = input("yana ism kiritasizmi")
#     n+=1
#     if takrorlash != "ha":
#         break


# mevalar = ['olam', 'anor', 'nok', 'gilos', 'anjir','sabzi','uzum']
# meva = 'olma'
# while meva in mevalar:
#     mevalar.remove(meva)
# print(mevalar)


talabalar = ['olim','gulom','hasan', 'husan','botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop() # pop bu ro'yhat ichidan matnni oladi.
    baho = input(f"{talaba.title()}ning bahosini kiriting")
    print(f"{talaba.title()} talaba baholandi")
    baholangan_talabalar[talaba] = int(baho)

