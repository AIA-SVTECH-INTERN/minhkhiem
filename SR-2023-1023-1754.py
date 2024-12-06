import imaplib

# Thông tin đăng nhập
email_user = "nguyenminhkhiemlew@gmail.com"  
email_password = "khiemminh" 

# Kết nối đến Gmail IMAP server
try:
    # Tạo kết nối SSL
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    print("Kết nối thành công đến Gmail IMAP server.")

    # Đăng nhập
    imap.login(email_user, email_password)
    print("Đăng nhập thành công.")

    # Kiểm tra hộp thư
    status, mailboxes = imap.list()
    if status == "OK":
        print("Danh sách hộp thư:")
        for mailbox in mailboxes:
            print(mailbox.decode())

    # Chọn hộp thư chính (inbox)
    imap.select("inbox")

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

finally:
    # Đóng kết nối
    if 'imap' in locals():
        imap.logout()
        print("Đã đóng kết nối.")
