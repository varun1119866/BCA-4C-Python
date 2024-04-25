print("Name: Anshu\n Rollno.: 2210997037")
array=[[1,2,3],[4,5,6],[7,8,9]]
row_products=[]
for row in array:
    product=1
    for num in row:
        product*=num
    row_products.append(product)
column_products=[]
for i in range(len(array[0])):
    product=1
    for j in range(len(array)):
        product*=array[j][i]
    column_products.append(product)
print("Array:")
for row in array:
    print(row)
print("Product of every row:",row_products)
print("Product of every column:",column_products)
