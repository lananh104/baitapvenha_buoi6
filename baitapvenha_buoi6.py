""" BÀI TẬP VỀ NHÀ BUỔI 07 - DICTIONARY:
Bài 00: Viết chương trình tính tích các phần tử trong một dict
Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict
Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key
Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict
Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict
Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
        Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
Ví dụ:
    dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
    keys = ["name", "salary"]
    Output: {'name': 'Kelly', 'salary': 8000}
Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String
Ví dụ:
    Input: ‘Stringings’
    Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2,  ‘n’: 2, ‘g’: 2, ‘s’: 1}
Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
Ví dụ:
    Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    Output: {'item1': 1150, 'item2': 300}
"""
# Bài 00: Viết chương trình tính tích các phần tử trong một dict
a={"cam":4,"táo":3,"xoài":7}
p=1
for i in a.values():
    p*=i
print("Tích các phần tử trong dict trên là: ", p)


# Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict
a={"cam":4,"táo":3,"xoài":7}
print("Giá trị lớn nhất của trường value trong dict trên là: ",max(a.values()))
print("Giá trị nhỏ nhất của trường value trong dict trên là: ",min(a.values()))


# Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key
a={"m":"mango","c":"cherry","a":"apple","o":"orange","b":"blueberry"}
b=dict(sorted(a.items(),key=lambda x:x[0]))
print("Dict sau khi sắp xếp các phần tử là: \n",b)


# Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict
a={"a":"abc","b":"abc","c":"cde","h":"hz"}
b=list(a.values())
c=[]
for i in b:
    if b.count(i)==1:
        c.append(i)
print("Các giá trị không trùng lặp từ dict là",c)


# Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict
a={2:4,4:16,1:1,7:49,6:36,3:9,5:25}
b=sorted(a.items(), key=lambda x:x[0])
c=dict(b[0:3])
print("Ba phần tử có key lớn nhất là: ",c)


# Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
        # Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
a={
    "a":["a","an","apple","amazing","amzon","account"],
    "b":["banana","bluberry","ball","boy","book","bedroom","baby"],
    "c":["char","cake","call","cancel","car","care","candy"],
    "d":["daddy","done","daily","display","dismiss"]
}
b=list(a.values())
for i in range(len(b)):
    print("Phần tử thứ 5 trong trường value của phần tử %s trong Dict là: %s "%(i,b[i][4]))


# Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
a={2:4,4:16,1:1,7:49,6:36,3:9,5:25}
b={2:4,4:16,8:64,6:36,10:100}
c={}
for key_a,value_a in a.items():
    for key_b,value_b in b.items():
        if key_a == key_b and value_a==value_b:
            c.update({key_a:value_a})
print("Các phần tử chung của 2 dict là: \n",c)


#Bài 7:Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
new_dict={key:values for key,values in sampleDict.items() if key=="name" or key=="salary" }
print("Dict mới là: ", new_dict)


# Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
a = {2: 4, 4: 16, 1: 1, 7: 49, 6: 36, 3: 9, 5: 25}
b=list(sorted(a.items(),key=lambda a:a[1],reverse=True))
c=dict(b[0:3])
print("Ba phần tử có giá trị lớn nhất là: \n",c)


# Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một String
# Ví dụ:
#     Input: ‘Stringings’
#     Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2,  ‘n’: 2, ‘g’: 2, ‘s’: 1}
a="Stringings"
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("Số lần xuất hiện các ký tự trong chuỗi là: \n",count)


# Bài 10: Viết hàm đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
a="Ò ó o Ò ó o Tiếng gà Tiếng gà Giục quả na Mở mắt Tròn xoe Giục hàng tre Đâm măng Nhọn hoắt"
b=a.split(" ")
count={}
for i in b:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("Số lần xuất hiện các từ đơn trong một đoạn văn bản là: \n",count)


# Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
# Ví dụ:
#     Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#     Output: {'item1': 1150, 'item2': 300}
a={
    "a":["a","an","apple","amazing","amzon","account"],
    "b":["banana","bluberry","ball","boy","book","bedroom","baby"],
    "c":["char","cake","call","cancel","car","care","candy"],
    "d":["daddy","done","daily","display","dismiss"]
}
b={key:value for key,value in a.items() if key == "a" or key == "c" }
print("Dict mới là: \n",b)
