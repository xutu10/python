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
               },
               'doc4':
               {
                   'football':7,
                   'trainer' :3
               }
}

doc_class = {'doc1':'arts',
             'doc2':'sports',
             'doc3':'business',
             'doc4':'sports'
}

# class : times
pc = {}
# class :{word:times}
pxc = {}

counter = 0

# beginning of for loop
for k in doc_feature.keys():
    counter += 1
    class_name = doc_class[k]

    # handle pc
    if class_name in pc.keys():
        pc[class_name] += 1.0
    else:
        # class occurs first time
        # add class_name as key in pc
        pc.update({class_name:1.0})
                
    # handle pxc
    # store subdict in doc_feature
    dict_temp = doc_feature[k]
    # whether class already as key in pxc
    if class_name in pxc.keys():
        # increment counter of class
        pxc[class_name]['class_counter'] += 1
        # walk through subdict in doc_feature
        for key in dict_temp.keys():
            # whether word as key already in subdict of pxc 
            if key in pxc[class_name].keys():
                # increment value of word
                pxc[class_name][key] += 1
            else:
                # add new word in subdict
                pxc[class_name].update({key:1.0})
    else:
        # class name occurs first time
        # add class name as key in pxc
        # and add classcounter as key in subdict of pxc
        pxc.update({class_name:{}})
        pxc[class_name].update({'class_counter':1})
        # walk through subdict from feature
        # add word in subdict of pxc
        for key in dict_temp.keys():
            pxc[class_name].update({key:1.0})

# ending of for loop

# calculate probability for each class in pc
for k in pc.keys():
   print pc[k]

print counter
for k in pc.keys():
    pc[k] /= counter

#calculate pro for each word in each class
for k in pxc.keys():
    # store counter of class
    counter_tmp = pxc[k]['class_counter']
    # remove the counter item from subdict
    del pxc[k]['class_counter']
    
    for key in pxc[k].keys():
        # frequency devided by freqeuency of class
        pxc[k][key] /= counter_tmp

print 'pc------------'        
for k,v in pc.items():
    print k,'-',v

print 'pxc-----------'
for k,v in pxc.items():
    print k,'-',v
