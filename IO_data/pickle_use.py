import pickle
a = [1,2,3]
'''file = open('pickle_example.pickle','wb')
pickle.dump(a,file)
file.close()'''

'''file = open('pickle_example.pickle','rb')
b = pickle.load(file)
file.close()
print(b)'''

with open('pickle_example.pickle','rb') as file:
    b = pickle.load(file)
    print(b)