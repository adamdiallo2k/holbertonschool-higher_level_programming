#!/usr/bin/python3

def element_at(my_list, idx):
   if my_list == None:
      return None
   if not (0 <= idx <= len(my_list)):
     return None
   return my_list[idx]
