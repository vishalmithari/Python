str1 = "This is a double quoted string"
str2 = 'This is a single quoted string'
str3 = """ This is a triple quoted string """

print(str1,str2,str3)

print("Single element form the string using indexing : ",str1[0])
print(" print element using positive indexing: ",str2[0:6])
print(" print element using negative indexing: ",str3[-1])
print("Length of the string: ",len(str1))
print("String in lower case: ",str1.lower())
print("String in upper case: ",str2.upper())
print("String in title case: ",str3.title())