ip_address = input("Введите IP: ")
segments = ip_address.split('.')

if len(segments) != 4:
    print("Адрес — это четыре числа, разделённые точками.")
else:
    valid_ip = True
    for segment in segments:
        if not segment.isdigit():
            print(f"{segment} — это не целое число.")
            valid_ip = False
            break
        elif not (0 <= int(segment) <= 255):
            print(f"{segment} превышает 255.")
            valid_ip = False
            break

    if valid_ip:
        print("IP-адрес корректен.")
