import os
import pickle
curentdir = os.path.dirname(__file__)
file = open(os.path.join(curentdir,'r.p'),'r')
instagram_response = pickle.load(file)
