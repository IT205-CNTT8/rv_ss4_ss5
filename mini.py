vehicles = []
next_id = 1
RATE_MOTORBIKE = 2000
RATE_CAR = 5000
while True:
    print("===============================")
    print("1. Check-in")
    print("2. Báo cáo")
    print("3. Tìm kiếm")
    print("4. Check-out")
    print("5. Thoát")
    print("===============================")
    choice_s = input("Chọn (1-5): ").strip()
    if choice_s == "":
        print("ERR-01: Dữ liệu bắt buộc không được để trống.")
        continue
    try:
        choice = int(choice_s)
    except ValueError:
        print("Lựa chọn phải là số. Nhập lại.")
        continue
    if choice == 1:
        plate = input("Nhập biển số: ").strip().upper()
        if plate == "":
            print("ERR-01: Dữ liệu bắt buộc không được để trống.")
            continue
        exists = False
        for v in vehicles:
            if v['plate'] == plate:
                exists = True
                break
        if exists:
            print("ERR-05: Biển số đã tồn tại trong bãi.")
            continue
        while True:
            t_s = input("Nhập loại (1: Xe máy, 2: Ô tô): ").strip()
            if t_s == "":
                print("ERR-01: Dữ liệu bắt buộc không được để trống.")
                continue
            try:
                t = int(t_s)
            except ValueError:
                print("Loại phải là số. Nhập lại.")
                continue
            if t not in (1, 2):
                print("Loại phải là 1 hoặc 2. Nhập lại.")
                continue
            break
        while True:
            entry_s = input("Nhập giờ vào (0-23): ").strip()
            if entry_s == "":
                print("ERR-01: Dữ liệu bắt buộc không được để trống.")
                continue
            try:
                entry = int(entry_s)
            except ValueError:
                print("Giá trị phải là số nguyên. Nhập lại.")
                continue
            if entry < 0 or entry > 23:
                print("Giờ phải trong 0-23. Nhập lại.")
                continue
            break
        vehicles.append({'id': next_id, 'plate': plate, 'type': t, 'entry_time': entry})
        print(f"Đã thêm xe ID={next_id}, Biển số={plate}")
        next_id += 1

    elif choice == 2:
        if not vehicles:
            print("ERR-02: Bãi xe trống.")
            continue
        print(f"{'ID':<5}{'Biển số':<12}{'Loại':<8}{'Giờ vào':<8}")
        for v in vehicles:
            loai = 'Xe máy' if v['type'] == 1 else 'Ô tô'
            print(f"{v['id']:<5}{v['plate']:<12}{loai:<8}{v['entry_time']:<8}")

    elif choice == 3:
        plate = input("Nhập biển số cần tìm: ").strip().upper()
        if plate == "":
            print("ERR-01: Dữ liệu bắt buộc không được để trống.")
            continue
        found = None
        for v in vehicles:
            if v['plate'] == plate:
                found = v
                break
        if found is None:
            print("ERR-04: Không tìm thấy xe.")
        else:
            print(found)
    elif choice == 4:
        plate = input("Nhập biển số check-out: ").strip().upper()
        if plate == "":
            print("ERR-01: Dữ liệu bắt buộc không được để trống.")
            continue
        found = None
        for v in vehicles:
            if v['plate'] == plate:
                found = v
                break
        if found is None:
            print("ERR-04: Không tìm thấy xe.")
            continue
        entry = found['entry_time']
        while True:
            exit_s = input("Nhập giờ ra (0-23): ").strip()
            if exit_s == "":
                print("ERR-01: Dữ liệu bắt buộc không được để trống.")
                continue
            try:
                exit_time = int(exit_s)
            except ValueError:
                print("Giá trị phải là số nguyên. Nhập lại.")
                continue
            if exit_time < 0 or exit_time > 23:
                print("Giờ phải trong 0-23. Nhập lại.")
                continue
            if exit_time < entry:
                print("ERR-03: Giờ ra phải >= giờ vào. Nhập lại.")
                continue
            break
        hours = exit_time - entry
        if hours == 0:
            hours = 1
        rate = RATE_MOTORBIKE if found['type'] == 1 else RATE_CAR
        fee = hours * rate
        print("----- HÓA ĐƠN -----")
        print(f"Biển số: {found['plate']}")
        print(f"Loại: {'Xe máy' if found['type']==1 else 'Ô tô'}")
        print(f"Giờ vào: {entry}, Giờ ra: {exit_time}")
        print(f"Thời gian: {hours} giờ, Phí: {fee} VND")
        vehicles.remove(found)

    elif choice == 5:
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Nhập 1-5.")