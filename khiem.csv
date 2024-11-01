import csv

# Dữ liệu mẫu để ghi vào file CSV
email_data = [
    ['From', 'Sent', 'To', 'Subject'],
    ['NGUYỄN HUYỀN LINH <erp@svtech.com.vn>', 
     'Monday, October 23, 2023 6:02 PM', 
     'nguyenhuuthanh1@vnpt.vn\nsupport.nw@svtech.com.vn\nktm.ip@vnpt.vn\nhn.techsupports@svtech.com.vn\nhien.nguyen@svtech.com.vn', 
     'Ticket được cập nhật: SR-2023-1023-1754 - VNPT NET - SLA - Hỗ trợ kiểm tra lỗi khi commit trên thiết bị HNI-PE5 và HNI-PE6 - SN: JN1262538AFA
     Kính gửi Quý khách hàng,

 

Ticket SR-2023-1023-1754

Nội dung hỗ trợ: VNPT NET - SLA - Hỗ trợ kiểm tra lỗi khi commit trên thiết bị HNI-PE5 và HNI-PE6 - SN: JN1262538AFA

Thông tin Ticket được cập nhật các thông tin sau vào lúc 23/10/2023 17:54:31:

Độ ưu tiên: Minor
Mức độ hỗ trợ: VNPT-Premium
Kỹ sư phụ trách:
Họ và Tên: NGUYỄN HOÀNG HIẾU
SĐT : 0979110251
Anh chị sử dụng số ticket/email này để theo dõi và cập nhật tình hình thực hiện.

Trân trọng,

']
]

# Tạo file CSV và ghi dữ liệu
with open('email_separate_to_output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(email_data)

print("File CSV đã được tạo.")
