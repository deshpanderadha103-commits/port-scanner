import socket

print("=== Python Port Scanner ===")

target = input("Enter target IP: ")

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    8000: "HTTP-ALT"
}

print(f"\nScanning target: {target}")
print("-" * 40)

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        service = services.get(port, "Unknown")
        print(f"[+] Port {port} OPEN ({service})")

    s.close()

print("\nScan completed.")
