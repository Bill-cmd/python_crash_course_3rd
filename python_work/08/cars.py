def make_car(manufacturer, model, **args):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in args.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
