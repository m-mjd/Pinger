import socket
import time
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


                        d888888b  .o88b. d8888b.
                        `~~88~~' d8P  Y8 88  `8D
                           88    8P      88oodD'
                           88    8b      88~~~
                           88    Y8b  d8 88
                           YP     `Y88P' 88 
                           
                           """ + Style.RESET_ALL)

while True:
    try:
        hostname = input(Fore.WHITE + ": آدرس آی‌پی یا وبسایت را وارد کنید : \n" + Style.RESET_ALL)
        ip_address = socket.gethostbyname(hostname)
        port = int(input(Fore.WHITE + ": شماره پورت را وارد کنید : \n" + Style.RESET_ALL))
        if not (0 <= port <= 65535):
            raise ValueError("شماره پورت نامعتبر است")
            
        number = int(input(Fore.WHITE + ": تعداد درخواست‌ها را وارد کنید : \n" + Style.RESET_ALL))
    except ValueError as e:
        print(Fore.RED + f"مقدار ورودی نامعتبر است : {e}" + Style.RESET_ALL)
        continue

    times = []
    for i in range(number):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        start_time = time.time()
        try:
            s.connect((ip_address, port))
            s.shutdown(socket.SHUT_RDWR)
            end_time = time.time()
            times.append((end_time - start_time) * 1000)
            print(Fore.CYAN + f"{i+1}. {hostname}:{port} ping delay = {times[-1]:.5f} s" + Style.RESET_ALL)
        except ConnectionRefusedError:
            print(Fore.RED + "اتصال با میزبان رد شد" + Style.RESET_ALL)
        except socket.gaierror:
            print(Fore.RED + "نام میزبان نامعتبر است" + Style.RESET_ALL)
        finally:
            s.close()

    if times:
        min_time = min(times)
        max_time = max(times)
        avg_time = mean(times)
        print()
        print()
        print()
        print(f"""حداکثر زمان پاسخگویی: 
        
{Fore.RED}{max_time:.5f} s{Style.RESET_ALL}""")
        print()
        print(f"""حداقل زمان پاسخگویی:

{Fore.GREEN}{min_time:.5f} s{Style.RESET_ALL}""")
        print()
        print(f"""میانگین زمان پاسخگویی:

{Fore.BLUE}{avg_time:.5f} s{Style.RESET_ALL}""")
        print()
        print()
        print()
    addr_info = socket.getaddrinfo(hostname, port, socket.AF_INET, socket.SOCK_STREAM)
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
