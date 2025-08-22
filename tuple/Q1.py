# Configuration system for a web server

# Server settings
server_ip = ("192", "168", "1", "10")  # Tuple - cannot be changed
allowed_ips = ["192.168.1.2", "192.168.1.3"]  # List - can be updated

# Function to update allowed_ips
def update_allowed_ips(new_ip):
    if new_ip not in allowed_ips:
        allowed_ips.append(new_ip)
        print(f"IP {new_ip} added to allowed list.")
    else:
        print(f"IP {new_ip} is already allowed.")

# Function to display current configuration
def display_config():
    print("=== Server Configuration ===")
    print("Server IP (unchangeable):", ".".join(server_ip))
    print("Allowed IPs (modifiable):", allowed_ips)

# Trying to update allowed_ips
display_config()
update_allowed_ips("192.168.1.4")
update_allowed_ips("192.168.1.2")  # Duplicate

# Attempt to change server_ip (should be avoided)
try:
    server_ip[0] = "10"  # This will raise an error since tuple is immutable
except TypeError:
    print("Error: Cannot change server_ip. It is fixed.")

# Display updated config
display_config()