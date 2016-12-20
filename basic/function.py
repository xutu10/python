def hey(x):
    return "hey " + x

#x = "xutu"
print hey("hony")

print "---------"
def name(one="hey", two="xu"):
    print "%s,%s" % (one, two)

name("xutu","wang")
name()

print "---------"
def profile(name, *ages): #indicate a tuple
    print name
    print ages

profile("xu",12,13,14)
