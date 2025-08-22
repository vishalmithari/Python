list1=[]
list1=input("Enter the elements of the list : ").split()
print("The list is: ", list1)


print("*******List Operations*******")

print("****Opration 1 : Accessing Element form the List.****")
print("First element of the list: ",list1[0])
print("Last element of the list: ",list1[-1])

print("****Operation 2 : Slicing the List.****")
print("First three element of the list: ",list1[1:4])
print("reverse element of the list: ",list1[::-1])

print("****operation 3:Adding new element****")
list1.append(input("Enter the new element to  added: "))
print("List after adding new element: ", list1)
list1.insert(0, input("Enter the new element to be inserted at the beginning: "))
print("List after inserting new elements: ", list1)

print("****Operation 4: Removing element from the list.****")
list1.remove(input("Enter the element to be removed: "))
print("List after removing the element: ", list1)
