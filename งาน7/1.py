income = float(input("กรุณาใส่รายได้ของคุณ (บาท): "))
if income >= 15000:
    if income < 70000:
        card_type = "บัตรเงิน"
    elif income < 100000:
        card_type = "บัตรทอง"
    else:
        card_type = "บัตร Platinum"
    print(f"คุณสามารถทำ{card_type}ได้")
else:
    print("คุณไม่สามารถทำบัตรเครดิตได้ เนื่องจากรายได้น้อยกว่า 15,000 บาท")