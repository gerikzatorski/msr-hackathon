lights = [False] * 100

def switch_light(x):
    if lights[x]:
        lights[x] = False
    else:
        lights[x] =True

def flip_by_increment(x):
    i = 0
    while i < 100:
        switch_light(i)
        i += x

def print_on_lights():
    i =0
    while i < 100:
        if lights[i]:
            print i
        i += 1

def print_states():
    for i in range(100):
        print lights[i]

if __name__ == '__main__':
    person = 1
    while person < 100:
        flip_by_increment(person)
        person += 1
    print_on_lights()
