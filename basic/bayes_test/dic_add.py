output ={ }
doc_class = {'doc1':'arts',
             'doc2':'sports',
             'doc3':'business'    
}
doc_feature = {'doc1':
               {
                   'the' :17,
                   'world' :12
               },
               'doc2':
               {
                   'hello' : 2,
                   'hi' : 15
               },
               'doc3':
               {
                   'english' : 4,
                   "german" : 3
               }
}


# test syntax
# print doc_feature['doc1']['the']

# test del
del doc_feature['doc1']['the']
for k, v in doc_feature.items():
   output.update({k:v})


print 'before', output.items()

#output.update({'item0':1})

for k, v in doc_class.items():
   output.update({k:v})

print 'after', output.items()
print '--------------'
output.clear()

print 'before feature', output.items()
for k, v in doc_feature.items():
   output.update({k:v})

print 'after feature', output.items()
print '+++++++++++'
print output['doc1']
print "add+++++++"
output['doc1'].update({'foot':2})
print 'after adding', output.items()
a = 'doc2'
output[a].update({'foot':100})
print 'after adding', output.items()
