import subprocess

def run_git_commands():
    # Cấu hình cố định Repo & Nhánh của nhóm
    REMOTE = "origin"
    BRANCH = "master"

    try:
        # 1. Gom tất cả các file vừa thêm/sửa vào Git
        print("1. Đang gom file thay đổi...")
        subprocess.run(["git", "add", "."], check=True)

        # 2. Kiểm tra xem có file nào mới không
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        
        if status.stdout.strip():
            message = input("Nhập ghi chú commit (bấm Enter để dùng mặc định): ")
            if not message.strip():
                message = "Update project code"
            print("2. Đang tạo commit...")
            subprocess.run(["git", "commit", "-m", message], check=True)
        else:
            print("Không có thay đổi mới để commit, tiến hành đồng bộ...")

        # 3. Kéo code mới nhất từ nhánh master của nhóm về trước
        print(f"3. Đang tải code mới nhất từ {REMOTE}/{BRANCH}...")
        subprocess.run(["git", "pull", REMOTE, BRANCH, "--rebase"], check=True)

        # 4. Đẩy code lên đúng nhánh master của nhóm
        print(f"4. Đang đẩy code lên {REMOTE}/{BRANCH}...")
        subprocess.run(["git", "push", REMOTE, BRANCH], check=True)

        print(f"\n---> HOÀN THÀNH: ĐÃ ĐẨY CODE LÊN TRANG GITHUB NHÓM (nhánh {BRANCH})!")

    except subprocess.CalledProcessError as e:
        print(f"\n[LỖI] Không thể đẩy code: {e}")

if __name__ == "__main__":
    run_git_commands()