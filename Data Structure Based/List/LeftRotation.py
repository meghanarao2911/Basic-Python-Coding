#Program to rotate the list by 'n'elements

list1=[12,20,30,40,50]
print("Enter the number of rotations to rotate")
n=int(input("Enter n"))
rotate_arr=list1[n:]+list1[:n]
print("Rotated list",rotate_arr)