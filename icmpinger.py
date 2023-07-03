import socket
import ping3
from statistics import mean
from colorama import init, Fore, Style

init()

print(Fore.CYAN + """

d8888b. d888888b d8b   db  d888b  d88888b d8888b.
88  `8D   `88'   888o  88 88' Y8b 88'     88  `8D
88oodD'    88    88V8o 88 88      88ooooo 88oobY'
88~~~      88    88 V8o88 88  ooo 88~~~~~ 88`8b
88        .88.   88  V888 88. ~8~ 88.     88 `88.
88      Y888888P VP   V8P  Y888P  Y88888P 88   YD


                        d888888b  .o88b. .88b  d88. d8888b.
                          `88'   d8P  Y8 88'YbdP`88 88  `8D
                           88    8P      88  88  88 88oodD'
                           88    8b      88  88  88 88~~~
                          .88.   Y8b  d8 88  88  88 88
                        Y888888P  `Y88P' YP  YP  YP 88
                        
                        """ + Style.RESET_ALL)

while True:
    try:
        number = int(input(
            ": تعداد پینگ های مورد نظر را وارد کنید  : \n\n"))
        hostname = input(
            ": آدرس آیپی و یا آدرس وبسایت را وارد نمایید : \n\n")
        port = int(input(
            ": شماره پورت مورد نظر را وارد نمایید  : \n\n"))
        if not (0 <= port <= 65535):
            raise ValueError(" مقدار ورودی نامعتبر است ")
    except ValueError as e:
        print(
            f"{Fore.RED} مقدار ورودی نامعتبر است : {e}{Style.RESET_ALL}")
        continue
    response_times = []
    count = 1

    ip_address = socket.gethostbyname(hostname)
    print(f"{Fore.WHITE} {hostname} : ip is : {ip_address}{Style.RESET_ALL}\n")

    for number in range(number):
        address = f"{hostname}:{port}"
        response_time = ping3.ping(hostname, port)

        if response_time is not None:
            print(
                f"{Fore.CYAN}{count}. {address}  ping delay = {response_time} s{Style.RESET_ALL}")
            response_times.append(response_time)
        else:
            print(
                f"{Fore.RED}{count}. زمان درخواست تمام شد {Style.RESET_ALL}")

        count += 1

    if response_times:
        print()
        print()
        print()
        print(f"""حداکثر زمان پاسخگویی : 
        
{Fore.RED}{max(response_times)} s{Style.RESET_ALL}""")
        print()
        print(f"""حداقل زمان پاسخگویی : 

{Fore.GREEN}{min(response_times)} s{Style.RESET_ALL}""")
        print()
        print(f"""میانگین زمان پاسخگویی : 

{Fore.BLUE}{mean(response_times)} s{Style.RESET_ALL}""")
        print()
        print()
        print()

    addr_info = socket.getaddrinfo(
        hostname, port, socket.AF_INET, socket.SOCK_STREAM)
    for addr in addr_info:
        print("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""f"{Fore.YELLOW} IP : {hostname} (Port {port}): {addr[4][0]}{Style.RESET_ALL}"
              """
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""")

    again = input(f"""{Fore.CYAN}*********************************

"""
                  """* آیا میخواهید دوباره تست بگیرید ? (بله/خیر)*
                  """
                  """
*********************************\n\n""").lower()
    if again != "بله":
        break
