so_gio_lam = float(input("Nhập số giờ làm: "))
luong_gio = float(input("Nhập nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gtc = 44
gvc = max(0, so_gio_lam - gtc)
thuc_linh = gtc * luong_gio + gvc * luong_gio * 1.5
print(f"Số tiền thực lĩnh của NV: {thuc_linh}")