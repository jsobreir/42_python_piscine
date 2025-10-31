ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple_temp = list(ft_tuple)
ft_tuple_temp[1] = "Portugal!"
ft_tuple = tuple(ft_tuple_temp)
list1 = ["Porto!"]
ft_set.update(list1)
ft_set.remove("tutu!")
ft_set = {"Hello", "Porto!"}
ft_dict["Hello"] = "42Porto!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
