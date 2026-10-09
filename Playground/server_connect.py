import time
servers = ["Server_1", "Server_2", "mainframe"]
for s in servers:
    print(f"Connecting to {s}...")
    time.sleep(1)
    print(f"Connected to {s}.")
print("All servers connected successfully.")
