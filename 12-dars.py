car0 = {
    'model': 'lacetti',
    'rang': 'qora',
    'yil': 2012,
    'narh': 15000,
    'km': 50000,
    'karobka':'avtomat'

}
car1 = {
    'model' : "cobalt",
    'rang' : "oq",
    'yil' :2023,
    'narh' :16000,
    'karobka':'avtomat'

}
car2 = {
    'model': "nexia",
    'rang': "oq",
    'yil': 2025,
    'narh': 1500,
    'karobka':'mexanika'

}
# car = car2
# print(f"{car['model']},"
#       f"{car['rang']} rang,"
#       f"{car['yil']},"
#       f"{car['narh']},"
#       f"{car['karobka']}")

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model']},"
          f"{car['rang']} rang,"
          f"{car['yil']},"
          f"{car['narh']},"
          f"{car['karobka']}")