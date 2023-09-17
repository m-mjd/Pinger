import ping3
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from colorama import init, Fore, Style

init()
print(Fore.RED + "\nIt is better not to choose a number higher than 500 because some ports may remain due to high traffic\n"+Fore.RED +"Fast and inaccurate scanning = high numbers\n"+Fore.GREEN +"Slow and accurate scanning = low count\n" + Style.RESET_ALL)
workers =input("\nEnter the number of simultaneous scans:")
workers=int(workers)
print(Fore.RED + "\nIf you have selected a large number of simultaneous scans, you must also select a large number here so that no problem occurs\n"+ Style.RESET_ALL)
time_out = int(input("Enter the timeout for each port:"))
def get_port():
    while True:
        try:
            port = int(input("Enter a port number: "))
            if not (0 <= port <= 65535):
                print(Fore.RED + "Invalid port number. Please enter a number between 0 and 65535." + Style.RESET_ALL)
            else:
                return port
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid port number." + Style.RESET_ALL)

host = input("Enter the host address: ")

# Ping the host to see if it's reachable
ping_time = ping3.ping(host, timeout=10, unit="ms")
if ping_time is not None:
    if ping_time > 1000:
        print(Fore.RED + "Server is filtered." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "\nServer Ping. TIME : {} \n".format(ping_time) + Style.RESET_ALL)
        min_port = get_port()
        max_port = get_port()
        open_ports = []

        def check_port(port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(time_out)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                ping_time = ping3.ping(host, timeout=4, unit="ms")
                if ping_time is not None:
                    a = 1
                else:
                    print(Fore.MAGENTA + "\n\nPing to {}:{} is unsuccessful\n\n".format(host, port) + Style.RESET_ALL)
            sock.close()

            return port

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(check_port, port) for port in range(min_port, max_port+1)]
            for future in tqdm(as_completed(futures), total=len(futures)):
                _ = future.result()

        if len(open_ports) == 0:
            print(Fore.RED + "\n\nNo open ports found.\n\n" + Style.RESET_ALL)
        else:
            open_ports.sort()
            print(Fore.BLUE + "\n\nOpen ports: [\n" + Style.RESET_ALL)
            for port in open_ports:
                 print(Fore.GREEN , port , Style.RESET_ALL)
            print(Fore.BLUE + "\n]\n" + Style.RESET_ALL)
else:
        print(Fore.GREEN + "\nServer Ping. TIME : {} \n".format(ping_time) + Style.RESET_ALL)
        min_port = get_port()
        max_port = get_port()
        open_ports = []

        def check_port(port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(time_out)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                ping_time = ping3.ping(host, timeout=4, unit="ms")
                if ping_time is not None:
                    a = 1
                else:
                    print(Fore.MAGENTA + "\n\nPing to {}:{} is unsuccessful\n\n".format(host, port) + Style.RESET_ALL)
            sock.close()

            return port

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(check_port, port) for port in range(min_port, max_port+1)]
            for future in tqdm(as_completed(futures), total=len(futures)):
                _ = future.result()

        if len(open_ports) == 0:
            print(Fore.RED + "\n\nNo open ports found.\n\n" + Style.RESET_ALL)
        else:
            open_ports.sort()
            print(Fore.BLUE + "\n\nOpen ports: [\n" + Style.RESET_ALL)
            for port in open_ports:
                 print(Fore.GREEN , port , Style.RESET_ALL)
            print(Fore.BLUE + "\n]\n" + Style.RESET_ALL)
