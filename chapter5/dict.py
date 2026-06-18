# dict is unordered , mutable , indexed  data type
marks={
    "sheela":100,
    "neela":99,
    "peela":45

}

#dict methods 
# print(marks.items()) #dict_items([('sheela', 100), ('neela', 99), ('peela', 45)])
# print(marks.keys())  #dict_keys(['sheela', 'neela', 'peela'])
# print(marks.values())
# marks.update(
#     {
#         "sheela":50
#     }
# )
# print(marks.items())

print(marks.get("akshita")) #prints None
# print(marks["harry"]) # if key does not exists return error 
print(marks["sheela"])
