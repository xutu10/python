tuna = "fish"
if tuna == "cat":
    print 'this is cat'
    print "yes"
elif tuna == "dog":
    print "dog"
elif tuna == "fish":
    print "fish"
else:
    print "not fish"

print "------------"
one = [1,2,3]
two = [1,2,3]
print one == two
print one is two

a = b = "haha"
print a is b

if "h" in a:
    print "python is good"
if "hah" in a:
    print "python is super"

print "-------"
num1 = 4
num2 = 9
if num1 >3 and num2 < 7:
    print "%i, %i" % (num1,num2)
elif num1 > 7 or num2 >4:
    print "%i" % num1
