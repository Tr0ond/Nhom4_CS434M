import subprocess

def run_git_commands():
    REMOTE = "origin"
    BRANCH = "master"

    try:
        print("1. Đang gom file thay đổi...")
        subprocess.run(["git", "add", "."], check=True)

        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        
        if status.stdout.strip():
            message = input("Nhập ghi chú commit (bấm Enter để dùng mặc định): ")
            if not message.strip():
                message = "Update project code"
            print("2. Đang tạo commit...")
            subprocess.run(["git", "commit", "-m", message], check=True)
        else:
            print("Không có thay đổi mới, tiến hành đồng bộ...")

        print(f"3. Đang tải code mới nhất từ {REMOTE}/{BRANCH}...")
        subprocess.run(["git", "pull", REMOTE, BRANCH, "--allow-unrelated-histories"], check=True)

        print(f"4. Đang đẩy code lên {REMOTE}/{BRANCH}...")
        subprocess.run(["git", "push", REMOTE, BRANCH], check=True)

        print(f"\n---> THÀNH CÔNG: ĐÃ ĐẨY CODE LÊN NHÓM (nhánh {BRANCH})!")

    except subprocess.CalledProcessError as e:
        print(f"\n[LỖI] Không thể thực hiện: {e}")

if __name__ == "__main__":
    run_git_commands()