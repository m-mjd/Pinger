import ping3
import socket
from statistics import mean

while True:
    try:
        print("**************************************************")
        print("**************************************************")
        print()
        number = int(input(" تعداد پینگ های مورد نظر را وارد کنید  : "))
        print()
        print("**************************************************")
        print()
        hostname = input(" آدرس آیپی و یا آدرس وبسایت را وارد نمایید : ")
        print()
        print("**************************************************")
        port = int(input(" شماره پورت مورد نظر را وارد نمایید  : "))
        if not (0 <= port <= 65535):
            raise ValueError(" شماره پورت نامعتبر است ")
    except ValueError as e:
        print(f" شماره پورت نامعتبر است : {e}")
        continue
    response_times = []
    count = 1

    ip_address = socket.gethostbyname(hostname)
    print(f" آدرس آیپی از {hostname}: {ip_address}\n")

    for number in range(number):
        address = f"{hostname}:{port}"
        response_time = ping3.ping(hostname, port)

        if response_time is not None:
            print(
                f"{count}. {address}  آنلاین است : زمان پاسخگویی  = {response_time} s")
            response_times.append(response_time)
        else:
            print(f"{count}. زمان درخواست تمام شد ")

        count += 1

    if response_times:
        print()
        print()
        print("******************************************************")
        print(f" حداکثر زمان پاسخگویی : {max(response_times)} s")
        print("******************************************************")
        print(f" حداقل زمان پاسخگویی : {min(response_times)} s")
        print("******************************************************")
        print(f" میانگین زمان پاسخگویی : {mean(response_times)} s")
        print("******************************************************")
        print()
        print()

    addr_info = socket.getaddrinfo(
        hostname, port, socket.AF_INET, socket.SOCK_STREAM)
    for addr in addr_info:
        print("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""f" IP : {hostname} (Port {port}): {addr[4][0]}""""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""")

    again = input("""*********************************

"""
                  """* آیا میخواهید دوباره تست بگیرید ? (بله/خیر)*
                  """
                  """
*********************************\n\n""").lower()
    if again != "بله":
        print(" برنامه پایان یافت خدانگهدار ")
        break
