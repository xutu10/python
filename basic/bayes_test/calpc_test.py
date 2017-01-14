pc ={ }
doc_class = {'doc1':'arts',
             'doc2':'sports',
             'doc3':'business',
             'doc4':'sports'
}

# get p(c)
counter = 0

for k in doc_class.values():
    if k in pc.keys():
        pc[k] += 1.0
    else:
        pc.update({k:1.0})
    counter += 1.0

for k in pc.keys():
    pc[k] /= counter

print counter
for k,v in pc.items():
    print k,'-',v
    
