# THƯ MỤC TỔNG QUÁT: CÁC FILE VÀ CHỨC NĂNG CHUNG CỦA HỆ THỐNG

Thư mục này tập hợp **tất cả các tệp, mô-đun và chức năng nền tảng** không nằm trong danh sách phân công riêng của 5 thành viên.

Cấu trúc được tổ chức chuẩn theo cây thư mục dự án (`fe_travel/` và `be_travel/`), cho phép copy/paste đè thẳng vào thư mục gốc dự án bất kỳ lúc nào.

---

## 1. Các Chức Năng Nằm Trong Thư Mục Này

### A. Giao diện & Chức năng Admin bổ sung
- `Admin/DangNhap`: Giao diện trang đăng nhập dành riêng cho Quản trị viên (Admin).
- `Admin/Dashboard`: Bảng điều khiển trung tâm hiển thị biểu đồ và tổng quan số liệu thống kê.
- `Admin/ThongKe`: Toàn bộ các module thống kê (Doanh thu, Khách hàng mới, Vé bán ra, Chi tiêu khách hàng, Tour).
- `Admin/QuanLyBaiViet`: Quản lý tin tức, bài viết cẩm nang du lịch.
- `Admin/QuanLyPhuongTien`: Quản lý danh mục phương tiện vận chuyển (Xe du lịch, máy bay, tàu...).
- `Admin/QuanLySlide`: Quản lý banner quảng cáo và slide hiển thị ở trang chủ.
- `Admin/DatPhongKhachSan`: Quản lý đặt phòng khách sạn.
- `Admin/LienHe`: Quản lý các phản hồi và liên hệ từ khách hàng gửi về.
- `Admin/Profile`: Quản lý thông tin tài khoản và đổi mật khẩu của Admin.

### B. Giao diện & Chức năng Client bổ sung
- `Client/BaiViet` & `ChiTietBaiViet`: Trang danh sách tin tức và xem chi tiết bài viết du lịch.
- `Client/HuongDanVien` & `ChiTietHuongDanVien`: Danh sách và trang hồ sơ chi tiết của các hướng dẫn viên.
- `Client/DatPhongKhachSan` & `KhachSan`: Module tìm kiếm và đặt phòng khách sạn.
- `Client/LienHe`: Trang biểu mẫu gửi thông tin liên hệ cho khách hàng.
- `Client/Profile`: Trang thông tin cá nhân và cập nhật hồ sơ khách hàng.

### C. Giao diện Hướng Dẫn Viên bổ sung
- `HuongDanVien/DangKy`, `DangNhap`, `XacNhanDangKy`, `QuenMatKhau`, `LayLaiMatKhau`: Hệ thống xác thực và cấp tài khoản riêng cho hướng dẫn viên.
- `HuongDanVien/Profile`: Hồ sơ cá nhân của hướng dẫn viên.

### D. Trang lỗi hệ thống
- `NotFound`: Trang lỗi 404 tùy chỉnh khi người dùng truy cập route không tồn tại.

---

## 2. Nền Tảng Khung Hệ Thống (Core & Shared Infrastructure)

### Frontend (`fe_travel/`)
- `src/layout/`: Toàn bộ bố cục giao diện (Header, Footer, Menu, Sidebar cho Client, Admin, Hướng dẫn viên).
- `src/router/index.js`: Cấu hình toàn bộ định tuyến (Routing) của ứng dụng.
- `src/router/checkAdmin.js`: Middleware bảo vệ các route Admin.
- `src/assets/`: Toàn bộ hình ảnh, css, icon, thư viện tĩnh.
- `src/utils/api.js`: File cấu hình axios và interceptor gọi API backend.
- `src/config/tenant.json`: File cấu hình tenant hệ thống.
- `src/App.vue`, `src/main.js`, `src/style.css`: File khởi tạo và stylesheet chính của Vue.
- `package.json`, `vite.config.js`, `index.html`, các file tài liệu Markdown hướng dẫn.

### Backend (`be_travel/`)
- `routes/api.php`, `web.php`, `console.php`: Định nghĩa toàn bộ endpoint API của hệ thống.
- `database/`: Chứa toàn bộ các file `migrations/` (khởi tạo cấu trúc bảng DB), `seeders/` (dữ liệu mẫu ban đầu).
- `config/`: Cấu hình hệ thống Laravel (auth, database, mail, sanctum, app...).
- `app/Http/Controllers/`: `BaiVietController.php`, `ThongKeController.php`, `PhuongTienController.php`, `LienHeController.php`, `Controller.php`.
- `app/Models/`: `BaiViet.php`, `PhuongTien.php`, `LienHe.php`, `User.php`.
- `app/Http/Requests/`: Request validation.
- `app/Services/`: Xử lý nghiệp vụ nâng cao (PayOSService...).
- `app/Jobs/`, `app/Providers/`, `bootstrap/`, `resources/`: Các tầng xử lý dịch vụ nền của Laravel.
- `composer.json`, `artisan`, `.env.example`, `README.md`.