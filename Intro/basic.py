print(7/8)
print(5*6)

#Exponentiation
print(4 ** 2)

#Modulo
print(18 % 7)


print(100 * 1.1 **7)

type(a)

savings = 100

print(savings)

savings = 100
factor = 1.1
result = savings * factor**7
print(result)

desc = 'compound interest'

profitable = True

savings = 100
factor = 1.1
desc = "compound interest"

year1 = savings * factor

print(type(year1))

doubledesc = desc + desc 

print(doubledesc)

#create list
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = [hall, kit, liv, bed, bath]

print(areas)

areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

print(areas)

house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

print(house)
print(type(house))

#subsect from a list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print(areas[1])
print(areas[-1])
print(areas[5])

eat_sleep_area = areas[3] + areas[7]
print(eat_sleep_area)

# substract one to six element 
downstairs = areas[:6]

upstairs = areas[-4:]

print(downstairs)
print(upstairs)

#change list value
areas[-1] = 10.50
areas[-1] = 10.50

areas_1 = areas + ["poolhouse", 24.5]

areas_2 = areas_1 + ["garage", 15.45]

#creat a copy list that do not affect original list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas)
areas_copy[0] = 5.0
print(areas)


