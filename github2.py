x={"name":'sneha', "password":999109}
a=int(input("press 1 for old name \n press 2 for new name \n press 3 for old pass \n press 4 for new pass"))
if a ==1:
    print("old name is = ",x['name'])
elif a == 2:
    x["name"] = input("Enter New Name = ")
    print("New Name is = ",x['name'])
elif a==3:
    print("old pass is =", x["password"])
elif a==4:
    x["password"]=input("enter new password")
    print("New password is = ",x['password'])
else:
    print("invalid")

