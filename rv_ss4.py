# đầu vào
#bước 1 nhập dữ liệu đầu vào
# bước 2 dựa vào dữ liệu đầu và để xử lí
#in ra đáp án
bill = int(input("Nhập tổng hóa đơn ban đầu: "))
if bill >= 500:
    discount = bill* (10/100)
    total = bill - discount
    print("Được giảm giá: ",total)
else :
    print("Không được giảm giá")
