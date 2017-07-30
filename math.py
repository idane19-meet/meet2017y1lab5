
x = str(input('what do you want to calculate? '))
if x == 'way':
    velocity = int(input("what's the speed?(in km/h) "))
    time = int(input("what's the time?(in hours) "))
    way = int(velocity * time)
    print(str(way) + ' km')
if x == 'velocity':
    way = int(input('how long is the way? (km)'))
    time = int(input("what's the time?(in hours) "))
    velocity = int(way / time)
    print(str(velocity) + ' km/h')
if x == 'time':
    way = int(input('how long is the way?(km) '))
    velocity = int(input("what's the speed?(in km/h) "))
    time = int(way / velocity)
    print(str(time) + ' hours')
