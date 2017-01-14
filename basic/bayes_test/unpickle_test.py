import pickle
import dic_class

dic_class.dic = pickle.load(file("dict.pickle","rb"))
print dic_class.dic.data
