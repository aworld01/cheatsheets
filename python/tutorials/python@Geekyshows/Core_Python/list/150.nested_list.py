# # A list within another list is called as nested list or nesting of a list.

#a = [1,2,3,4,[5,6,7,8]]
#print(a)

#a = [1,2,3,4]
#b = [5,6,7,8,a]
#print(b)

#a = [[10,20,30,40,50],
#       [60,70,80,90,100]]
#print(a)


# # accessing list
#a = [10,20,30,40,50,[60,70,80,90,100]]
#print(a)
#print(a[0])
#print(a[3])
#print(a[5])
#print(a[5][3])

#a = [[10,20,30,40,50],
#        [60,70,80,90,100]]
#print(a)
#print(a[0][3])
#print(a[1])
#print(a[1][2])



# # modifing list
a = [10,20,30,40,50,[60,70,80,90,100]]
print('Before modification',a)
a[1] = 200
print('After modification',a)
a[5][1] = 180
print('After modification',a)