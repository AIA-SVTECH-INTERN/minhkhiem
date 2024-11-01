# Dữ liệu cho từng nhóm
erp_solution_providers = """
1. Thông tin ngân hàng (mạng lưới, lãi suất, tỉ giá)
2. Vấn tin thông tin tài khoản doanh nghiệp - Kết nối BIDV iBank
3. Chuyển tiền trong nước doanh nghiệp - Kết nối BIDV iBank
4. Thanh toán lương doanh nghiệp - Kết nối BIDV iBank
5. Đăng ký thanh toán hóa đơn định kỳ - Kết nối BIDV iBank
"""
payment_intermediaries = """
1. Thông tin ngân hàng (mạng lưới, lãi suất, tỉ giá)
2. Vấn tin thông tin tài khoản doanh nghiệp - Kết nối BIDV iBank
3. Chuyển tiền trong nước doanh nghiệp - Kết nối BIDV iBank
4. Thanh toán lương doanh nghiệp - Kết nối BIDV iBank
5. Đăng ký thanh toán hóa đơn định kỳ - Kết nối BIDV iBank
"""

sales_solution_providers = """
1. Thông tin ngân hàng (mạng lưới, lãi suất, tỉ giá)
2. Vấn tin thông tin tài khoản doanh nghiệp - Kết nối BIDV iBank
3. Chuyển tiền trong nước doanh nghiệp - Kết nối BIDV iBank
4. Thanh toán lương doanh nghiệp - Kết nối BIDV iBank
5. Đăng ký thanh toán hóa đơn định kỳ - Kết nối BIDV iBank
"""

hotel_management_platform_providers = """
1. Thông tin ngân hàng (mạng lưới, lãi suất, tỉ giá)
2. Vấn tin thông tin tài khoản doanh nghiệp - Kết nối BIDV iBank
3. Chuyển tiền trong nước doanh nghiệp - Kết nối BIDV iBank
4. Thanh toán lương doanh nghiệp - Kết nối BIDV iBank
5. Đăng ký thanh toán hóa đơn định kỳ - Kết nối BIDV iBank
"""

direct_enterprise_clients = """
1. Thông tin ngân hàng (mạng lưới, lãi suất, tỉ giá)
2. Vấn tin thông tin tài khoản doanh nghiệp - Kết nối BIDV iBank
3. Chuyển tiền trong nước doanh nghiệp - Kết nối BIDV iBank
4. Thanh toán lương doanh nghiệp - Kết nối BIDV iBank
5. Đăng ký thanh toán hóa đơn định kỳ - Kết nối BIDV iBank
"""


# Tạo đường dẫn cho file
file_paths = {
    "Nhóm ERP": "/mnt/data/nhom_erp.txt",
    "Nhóm Trung Gian Thanh Toán": "/mnt/data/nhom_trung_gian_thanh_toan.txt",
    "Nhóm Giải Pháp Bán Hàng": "/mnt/data/nhom_giai_phap_ban_hang.txt",
    "Nhóm Quản Lý Khách Sạn": "/mnt/data/nhom_quan_ly_khach_san.txt",
    "Nhóm Khách Hàng Doanh Nghiệp Trực Tiếp": "/mnt/data/nhom_khach_hang_doanh_nghiep_truc_tiep.txt"
}

# Lưu dữ liệu vào file 
with open(file_paths["Nhóm ERP"], 'w') as f:
    f.write(erp_solution_providers)

with open(file_paths["Nhóm Trung Gian Thanh Toán"], 'w') as f:
    f.write(payment_intermediaries)

with open(file_paths["Nhóm Giải Pháp Bán Hàng"], 'w') as f:
    f.write(sales_solution_providers)

with open(file_paths["Nhóm Quản Lý Khách Sạn"], 'w') as f:
    f.write(hotel_management_platform_providers)

with open(file_paths["Nhóm Khách Hàng Doanh Nghiệp Trực Tiếp"], 'w') as f:
    f.write(direct_enterprise_clients)
