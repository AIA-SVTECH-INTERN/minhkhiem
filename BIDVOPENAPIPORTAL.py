import pdfplumber
import os

# Đường dẫn tới file PDF
pdf_path = '/Users/nguyenkhiem/Downloads/1. HUONG DAN TRAI NGHIEM BIDV OPEN API FINAL - Update.pdf'  

# Tạo thư mục để lưu các file .txt 
output_dir = 'output_txt_files'
os.makedirs(output_dir, exist_ok=True)

# Mở file PDF
with pdfplumber.open(pdf_path) as pdf:
   
    for page_number in range(len(pdf.pages)):
        page = pdf.pages[page_number]
        
        # Tìm bảng trên trang
        tables = page.extract_tables()
        
        # Nếu có bảng, xử lý từng bảng
        for table_index, table in enumerate(tables):
            
            for row_index, row in enumerate(table):
                row = [str(cell) if cell is not None else '' for cell in row]
                
                # Tạo tên file cho từng hàng
                file_name = f'output_page_{page_number + 1}_table_{table_index + 1}_row_{row_index + 1}.txt'
                file_path = os.path.join(output_dir, file_name)
                
                # Ghi nội dung hàng vào file
                with open(file_path, 'w', encoding='utf-8') as f:
                    # Ghi từng cột trong hàng, ngăn cách bằng tab
                    f.write('\t'.join(row))  
                
                print(f'Đã ghi vào file: {file_path}')  # In ra thông báo đã ghi file
