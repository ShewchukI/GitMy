def size_vector(x):
    return len (x)


def norma_vector(x):
   # norma = 0     #перший спосіб
   # for element in x:
   #     norma += element**2
   # return (norma**1/2)
   norma = sum ([element**2 for element in x])**0,5 #другий спосіб
   return norma

def scalar_dob_vect(x,y):  #скалярний добуток векторів
    try:
        assert size_vector(x) == size_vector(y), f"розмірності векторів {x} та {y} різні"
        scalar_dob = 0
        for i in range(size_vector(x)):
            scalar_dob += x[i]*y[i]
        return scalar_dob
    except AssertionError as e:
        print(e)

def perpend_vector(x,y):
    if scalar_dob_vect == 0:
        return True
    else:
        False

def kolinear_vector(x,y):#колінеарність векторів
    try:
        assert size_vector(x) == size_vector(y), f"розмірності векторів {x} та {y} різні"
        scalar_dob = 0
        for i in range(size_vector(x)):
            scalar_dob += x[i]*y[i]
        return scalar_dob
    except AssertionError as e:
        print(e)
def differ_vectors (v1, v2):
    n = len (v1)
    v = [ ]
    for i in range (n):
        v[i] = v1[i]-v2[i]
    return v

# a = [2, 2, 5]
# print(norma_vector(a))
# b = [1, 2]
# c = [1,0,-1]
# print (scalar_dob_vect(a,b))
# print(scalar_dob_vect(a, c))

if __name__ == "__main__":
    a = [2, 2, 5]
    print(norma_vector(a))
    b = [1, 2]
    c = [1,0,-1]
    print (scalar_dob_vect(a,b))
    print(scalar_dob_vect(a, c))