import dic_class
import pickle

if __name__ == "__main__":
    first_pick = dic_class.dic()
    pickle.dump(first_pick,file("dict.pickle","wb") )
    
