print("Name: Anshu\n Rollno.: 2210997037")
string_List=["apple","banana","orange","apple","grapes","banana","kiwi","orange","mango","apple"]
duplicated=[]
duplicated_indices=[]
for i in range(len(string_List)):
    item=string_List[i]
    if item in string_List[:i]+string_List[i+1:]:
        if item not in duplicated:
            duplicated.append(item)
            duplicated_indices.append([i])
        else:
            duplicated_indices[duplicated.index(item)].append(i)
for i in range(len(duplicated)):
    print(f"Duplicate'{duplicated[i]}'found at indices:",duplicated_indices[i])
    
