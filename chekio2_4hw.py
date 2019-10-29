def group_equal(els):
   set_ofelements = set(els)
   new_list = []
   for el in set_ofelements:
       new_list.append([el]*els.count(el))
   return new_list

print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4])) #проверка