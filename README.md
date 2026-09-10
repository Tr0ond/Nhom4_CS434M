# PHÂN CÔNG NHIỆM VỤ: PHẠM THU HUYỀN

Thư mục này được tổ chức **chuẩn theo cây thư mục dự án**. Bạn chỉ cần copy 2 thư mục `fe_travel` và `be_travel` dán thẳng vào thư mục gốc của project để sử dụng ngay!

---

## 1. Cây Thư Mục Chi Tiết (Folder Tree)

```
1. Pham Thu Huyen/
├── README.md
├── fe_travel/
│   └── src/
│       ├── components/
│       │   ├── Admin/
│       │   │   ├── NhanVien/           # [3.2.23] Quản lý nhân viên (Admin)
│       │   │   │   └── index.vue
│       │   │   └── PhanQuyen/          # [3.2.36] Phân quyền chức vụ (Admin)
│       │   │       └── index.vue
│       │   └── Client/
│       │       ├── DangKy/             # [3.2.2] Form đăng ký tài khoản khách hàng
│       │       │   └── index.vue
│       │       ├── DangNhap/           # [3.2.1] Form đăng nhập khách hàng
│       │       │   └── index.vue
│       │       ├── LayLaiMatKhau/      # [3.2.1] Giao diện đặt lại mật khẩu
│       │       │   └── index.vue
│       │       ├── QuenMatKhau/        # [3.2.1] Giao diện gửi mail quên mật khẩu
│       │       │   └── index.vue
│       │       └── XacNhanDangKy/      # [3.2.2] Giao diện kích hoạt tài khoản
│       │           └── index.vue
│       └── router/
│           └── checkClient.js          # Guard kiểm tra đăng nhập khách hàng
└── be_travel/
    └── app/
        ├── Http/
        │   └── Controllers/
        │       ├── ChucNangController.php   # [3.2.36] Quản lý danh mục chức năng
        │       ├── ChucVuController.php     # [3.2.36] Quản lý chức vụ
        │       ├── KhachHangController.php  # [3.2.1 & 3.2.2] Auth khách hàng
        │       ├── NhanVienController.php   # [3.2.23] Quản lý nhân viên
        │       └── PhanQuyenController.php  # [3.2.36] Xử lý ma trận phân quyền
        ├── Mail/
        │   └── mailMaster.php               # [3.2.2] Gửi mail kích hoạt tài khoản
        └── Models/
            ├── ChucNang.php                 # Model Chức năng
            ├── ChucVu.php                   # Model Chức vụ
            ├── KhachHang.php                # Model Khách hàng
            ├── NhanVien.php                 # Model Nhân viên
            └── PhanQuyen.php                # Model Phân quyền
```

---

## 2. Bảng Ánh Xạ Chức Năng Báo Cáo
- **3.2.1. Đăng nhập (Khách hàng)**: `fe_travel/src/components/Client/DangNhap`, `QuenMatKhau`, `LayLaiMatKhau`, `checkClient.js` và `KhachHangController.php`, `KhachHang.php`.
- **3.2.2. Đăng ký tài khoản (Khách vãng lai)**: `fe_travel/src/components/Client/DangKy`, `XacNhanDangKy` và `KhachHangController.php`, `KhachHang.php`, `mailMaster.php`.
- **3.2.23. Quản lý tài khoản nhân viên (Admin)**: `fe_travel/src/components/Admin/NhanVien` và `NhanVienController.php`, `NhanVien.php`.
- **3.2.36. Phân Quyền (Admin)**: `fe_travel/src/components/Admin/PhanQuyen` và `PhanQuyenController.php`, `ChucVuController.php`, `ChucNangController.php`, Models (`PhanQuyen.php`, `ChucVu.php`, `ChucNang.php`).