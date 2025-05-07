l = [1,2,3,4,5,6,7,8,9,10]

squares = map(lambda x: x**2, l)
squares_list = list(squares)
print(squares_list)

cubes = map(lambda x : x**3 , l)
cubes_list = list(cubes)
print(cubes_list)
