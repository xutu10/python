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

print 'before', output.items()

#output.update({'item0':1})

for k, v in doc_class.items():
   output.update({k:v})

print 'after', output.items()

    
