import string

b = 1
while b<5:
    print b
    b += 1
print "------------"

gl = ["milk","meat","beef"]
for food in gl:
    print "i want " + food
print "---------------"
    
ages = {"dad":46,"mom":45,"daughter":23}
for item in ages:
    print item, ages[item]

print "---------"
while 1:
#    name = raw_input("input name:")
    name = input("your name:")
    if name == "xutu": break
