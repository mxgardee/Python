

#3-4
Guest_list = ['Tom','Garfield','Top Cat']
print(Guest_list)
messagE =f"\n{Guest_list[0].title()} is invited to my party."
print(messagE)
messagE =f"{Guest_list[1].title()} is invited to my party."
print(messagE)
messagE =f"{Guest_list[2].title()} is invited to my party."
print(messagE)

#3-5
print(Guest_list[2])
Guest_list.remove('Top Cat')
Guest_list.insert(3, "Edward")
print(Guest_list)

#3-6
Guest_list.insert(0, 'James')
Guest_list.insert(3, 'Jack')
Guest_list.insert(4, 'Med')

print(Guest_list)