# ism = input("ismingiz nima?")
# savol = f"salom {ism.title()} yoshingiz nechida?"
# yosh = input("yoshingiz nechida?")
# yosh = int(yosh)
# boyi = input("bo'yingiz nechi metr")
# boy = float(boyi)


# son = 1
# while son <=100:
#     print(son)
#     son += 2

# savol = "istalgan son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' kiriting)"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# savol = "istalgan son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' kiriting)"
# while True:
#     qiymat = input(savol)
#     if qiymat == "exit":
#         break
#     else:
#         print(float(qiymat)-34)

# sonlar = list(range(1,10))
# for son in sonlar:
#     if son ==7:
#         continue #bu kodni davom etiradi
#         #  break bu kodni to'tatadi
#     print(f"{son} ning kvadrati {son**2} ga teng")

son = 10
while son <100:
    son += 1
    if son %2!=0:
        continue
    else:
        print(son)