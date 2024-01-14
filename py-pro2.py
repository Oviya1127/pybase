#list operations
#creating list
print("creating list\n")
list1=[1,2,3,4,5]
print(list1)
print("------------------------------------------------------------------------------------------------------")


print("creting list using list() function\n")
print(list([1,2,3,4,5]))
print("------------------------------------------------------------------------------------------------------")


#access list element
print("indexing on list:\n")
print(list1[0])
print(list1[2])
print("------------------------------------------------------------------------------------------------------")


#negative indexing
print("negative indexing on list:\n")
print(list1[-1])
print(list1[-2])
print("------------------------------------------------------------------------------------------------------")


#slicing a list
print("slicing operation on list:\n")
print(list1[0:3])
print(list1[2:-1])
print(list1[0:-1])
print(list1[-1::])
print("------------------------------------------------------------------------------------------------------")


#add element to list
list1.append(6)
print("add an item to the end of the list\n",list1)
print("------------------------------------------------------------------------------------------------------")



#extend list
list2=[7,8,9,10]
list1.extend(list2)
print("extending list item\n",list1)
print("------------------------------------------------------------------------------------------------------")

#insert
list1.insert(10,11)
print("insertig list item\n",list1)
print("------------------------------------------------------------------------------------------------------")

#change list item
list1[10]=12
print("changing list item\n",list1)
print("------------------------------------------------------------------------------------------------------")

#pop()
list1.pop()
print("poping list item\n",list1)
print("------------------------------------------------------------------------------------------------------")


#del an element from list
del list1[9]
print("deleting list item\n",list1)
print("------------------------------------------------------------------------------------------------------")



#remove item
list1.remove(4)
print("removing list item\n",list1)
print("------------------------------------------------------------------------------------------------------")


#reverse the list
list1.reverse()
print("reversing list item\n",list1)
print("------------------------------------------------------------------------------------------------------")


#sorting list in ascending order
list1.sort()
print("sorting list in ascending order\n",list1)
print("------------------------------------------------------------------------------------------------------")


#sorting list in decending order
list1.sort()
list1.reverse()
print("sorting list in decending order\n",list1)
print("------------------------------------------------------------------------------------------------------")


#copy list
list2=list1.copy()
print("copy list1 to list2\n",list2)
print("------------------------------------------------------------------------------------------------------")

#count
print("The count of the given item in the list\n",list1.count(2))
print("------------------------------------------------------------------------------------------------------")


#index
print( "The index of the first matched given item\n",list1.index(3))
print("------------------------------------------------------------------------------------------------------")


#clear
list1.clear()
print("clearing all the list item\n",list1)

print("------------------------------------------------------------------------------------------------------")
#tuple operations
list1=(1,"python",4.5,2,3,4,5)
print(list1)
print("first index value is:",list1[0])
print("last index value is:",list1[-1])
print("slicing operations:")
print(list1[0:3])
print(list1[0::2])
print(list1[::-1])
print()
print("--------------------------------------------------------------")
print()
#create dictionary
price={'pencil':5,'eraser':2,'scale':5,'sharpner':4}


#printing dictionary
print(price)
print("---------------------------------------------------------------------")
#copy dictionary
price2=price.copy()
print("copy of price dictionary\n",price2)
print("---------------------------------------------------------------------")



#valid dictionary
price={'pencle':5,'scale':5,'eraser':2,'sharpner':[4,5]}#list as value is possible
print(price)
print("sharpner value is in list",price['sharpner'])
print("---------------------------------------------------------------------")


#invalid dictionary
'''price={[1,2]:5,'scale':5,'eraser':2,'sharpner':5}
error:using a list as a key is not allowed'''


#length of dictionary
print("length of dictionary",len(price))
print("---------------------------------------------------------------------")

#aacess dictionary item
print("value of scale",price['scale'])
print("---------------------------------------------------------------------")


#aacess dictionary item by get()
print("value of scale by get() function:",price.get('scale'))
print("---------------------------------------------------------------------")

#change dictionary item
price['sharpner']=5
print(price)
print("---------------------------------------------------------------------")

#add item
price['ink_pen']=25
print("after adding item to dictionary:",price)
print("---------------------------------------------------------------------")


#pop item
print(price.popitem())

#pop
print("pop operation")
price.pop('sharpner')
print(price)
print("---------------------------------------------------------------------")

#keys
print("the key of dictionary are:",price.keys())
print("---------------------------------------------------------------------")


#values
print("the values of dictionary are:",price.values())
print("---------------------------------------------------------------------")




#del item
del price['pencle']
print("after deleting item from dictionary:",price)
print("---------------------------------------------------------------------")



#clear item
price.clear()
print("after clearing dictionary:",price)
print("---------------------------------------------------------------------")


'''
Function	Description
pop()	        Remove the item with the specified key.
update()	Add or change dictionary items.
clear()	        Remove all the items from the dictionary.
keys()	        Returns all the dictionary's keys.
values()	Returns all the dictionary's values.
get()	        Returns the value of the specified key.
popitem()	Returns the last inserted key and value as a tuple.
copy()	        Returns a copy of the dictionary.
'''

#set operations
set1={1,2,3,4,5}
set2={2,3,4,5,5}
print("set1 and set2 are:")
print(set1) #printing set
print(set2)
print()
print("--------------------------------------------------------------")
print()
print("union")
print(set1|set2) #union
print()
print("--------------------------------------------------------------")
print()
print("intersection")
print(set1&set2) #intersection
print()
print("--------------------------------------------------------------")
print()
print("difference")
print(set1-set2) #difference
