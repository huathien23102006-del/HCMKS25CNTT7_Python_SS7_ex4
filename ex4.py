# 1 input đầu vào: số lượng phiếu đăng ký: n = int(input())
# chuỗi đăng ký theo định dạng: Họ tên học viên | Tên khóa học | Mã học viên | Email
# output: nếu dữ liệu hợp lệ
# PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA
# Học viên: Nguyen Van A
# Khóa học: Python Basic
# Mã học viên: RK-001
# Email: student01@gmail.com
# Mã xác nhận: RK-001_PYTHON-BASIC
# nếu lỗi: Dữ liệu đăng ký không hợp lệ!
# giải pháp: 
# 1: kiểm tra số lượng phiếu nếu n <= 0 thì in lỗi dừng chương trình
# 2: tách dữ liệu: dùng parts = data.split("|") nếu len(parts) != 4 thì in lỗi và bỏ qua phiếu
# 3: chuẩn hóa: họ tên: name = name.strip().title()
# khóa học: course = course.strip().title()
# mã học viên: student_id = student_id.strip().upper()
# email: email = email.strip().lower()
# 4: kiểm tra email: "@" not in email thì in lỗi và bỏ qua phiếu
# 5: kiểm tra học viên: nếu len(student_id) < 5 thì in lỗi và bỏ qua phiếu
# 6: tạo mã: dùng confirmation_code = student_id + "_" + course.upper().replace(" ", "-") để tạo mã
# Thuật toán:
# Nhập n

# Nếu n <= 0
#     In "Số lượng phiếu đăng ký không hợp lệ!"
#     Kết thúc

# Lặp n lần

#     Nhập chuỗi đăng ký

#     Tách bằng dấu |

#     Nếu không đủ 4 phần
#         In "Dữ liệu đăng ký không hợp lệ!"
#         Bỏ qua phiếu

#     Chuẩn hóa họ tên
#     Chuẩn hóa khóa học
#     Chuẩn hóa mã học viên
#     Chuẩn hóa email

#     Nếu email không chứa @
#         In "Email không hợp lệ!"
#         Bỏ qua phiếu

#     Nếu độ dài mã học viên < 5
#         In "Mã học viên không hợp lệ!"
#         Bỏ qua phiếu

#     Tạo mã xác nhận

#     In phiếu đăng ký đã chuẩn hóa

quantity = int(input("Nhập số lượng phiếu đăng ký: "))

if quantity <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ!")

else:
    for i in range(quantity):
        print(f"\nNhập phiếu đăng ký thứ {i + 1}:")
        registration_data = input()

        parts = registration_data.split("|")

        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ!")
            continue

        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_id = parts[2].strip().upper()
        email = parts[3].strip().lower()

        if "@" not in email:
            print("Email không hợp lệ!")
            continue

        if len(student_id) < 5:
            print("Mã học viên không hợp lệ!")
            continue

        confirmation_code = (
            student_id +
            "_" +
            course_name.upper().replace(" ", "-")
        )

        print("\nPHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA")
        print("Học viên:", student_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_id)
        print("Email:", email)
        print("Mã xác nhận:", confirmation_code)