import numpy as np

# a = np.array([1,2,3])
# #print(a.dtype)
#
# a.dtype = np.float32
# print(a.dtype)
#
#
# py_polje = [[1,2,3,4],
#             [5,34,3,2]]
#
# enpe = np.array(py_polje)
# print(enpe.shape)


# a = np.ones((4,2), dtype=np.uint32)
# print(a)
#
# b = np.full((3,4),6)
# print(b)

# a = np.arange(2,11,3)
# print(a)

# a = np.linspace(5,10, num=5)
# print(a)

# a = np.array([2,3,4])
# b = np.array([5,7,2])
#print(a+b)
#print(a*b)

# c = np.matmul(a,b)
#print(c)


# a = np.array([1,2,34,4,5,6])
# print(a[3])
# a[3] = 21
# print(a)
#
# a = np.array([[1,2,3,4],
#              [4,5,6,7],
#              [11,3,4,5],
#              [44,5,7,22]])

#print(a[0:2, 1]) # 0:2 uzima samo retke od 0 do 2 i prvi index svakog uzetog retka
#print(a[:,1]) # uzima sve retke i prvi index svakog retka
#print(a[1:3, :])

#print(a[1, 1])
#print(a[3,1])
#print(a[1::2,1])
#print(a[1:3, 1::2]) #uzimamo svaki drugi stupac s dvojkom na kraju

#print(a[1::2,1::2])


# a = np.array([1,2,3,4])
#
# b = a.reshape(2,2)
# print(b)


# a = np.array([[1,2,3],
#              [4,5,6]])
#
# b = a.reshape((6))
# print(b.shape)


# a = np.array([[1,2,3],
#              [4,5,6]])
#
# b = a.swapaxes(0,1)
# print(b)


# a = np.array([[1,2,3,4],
#              [4,5,6,7],
#              [11,3,4,5],
#              [4,5,7,22]])

# print(a.mean())
# print(a.prod())
#
# a.sort()
# print(a)

#print(a.argmax()) #vraca na kojem je indexu najveca vrijednost, to je 15
