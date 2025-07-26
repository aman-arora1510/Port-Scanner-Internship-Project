import socket
import threading
import queue
import time # We'll use this to see the performance difference 

print_lock = threading.Lock() # A lock to ensure clean output when multiple threads print

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for connection
        result = sock.connect_ex((target, port))

        with print_lock: # Acquire lock before printing
            if result == 0:
                print(f"Port {port} is open", end="")
                try:
                    # Attempt to receive data (banner) - this might not always work or be useful
                    banner = sock.recv(1024).decode().strip()
                    if banner:
                        print(f" - Service: {banner}")
                    else:
                        print() # Newline if no banner
                except:
                    print() # Newline if error during banner grabbing
        sock.close()
    except socket.gaierror:
        with print_lock:
            print("Hostname could not be resolved. Exiting scan.")
        # Put a mechanism to stop all threads if hostname fails for one thread (advanced)
        # For now, just exit this thread's execution
        return
    except socket.error as e:
        # You can uncomment this for more detailed debugging
        # with print_lock:
        #     print(f"Socket error for port {port}: {e}")
        return

def worker(target, q):
    while True:
        port = q.get() # Get a port from the queue
        if port is None: # Sentinel value to signal thread to exit
            break
        scan_port(target, port)
        q.task_done() # Indicate that the task is done

def main():
    target = input("Enter the target IP address or hostname: ")

    try:
        start_port = int(input("Enter the starting port number: "))
        end_port = int(input("Enter the ending port number: "))
    except ValueError:
        print("Invalid port number. Please enter integers.")
        return

    if start_port > end_port:
        print("Starting port cannot be greater than ending port.")
        return

    num_threads = int(input("Enter the number of threads (e.g., 50, 100): "))
    if num_threads <= 0:
        print("Number of threads must be positive.")
        return

    ports_to_scan = queue.Queue()
    for port in range(start_port, end_port + 1):
        ports_to_scan.put(port) # Add all ports to the queue

    threads = []
    start_time = time.time()

    print(f"Scanning ports {start_port}-{end_port} on {target} with {num_threads} threads...")

    # Create and start worker threads
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(target, ports_to_scan))
        t.daemon = True # Allow main program to exit even if threads are running
        t.start()
        threads.append(t)

    # Wait for all tasks in the queue to be processed
    ports_to_scan.join()

    # Stop worker threads by putting sentinel values (None) in the queue
    for _ in range(num_threads):
        ports_to_scan.put(None)
    for t in threads:
        t.join() # Wait for each thread to finish

    end_time = time.time()
    print(f"\nScan completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()