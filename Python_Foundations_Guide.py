# ==============================================================================
# PART 1: SYSTEM NOTES & ARCHITECTURE ARCHIVES (Stored as multi-line strings)
# ==============================================================================

NGINX_AWS_DEPLOYMENT = """
--- AWS EC2 & NGINX Reverse Proxy Cheat Sheet ---
1. Provision EC2: Open Port 22 (SSH), Port 80 (HTTP), Port 443 (HTTPS).
2. Connect & Install: 
   $ sudo apt update && sudo apt install nginx -y
3. Configure Reverse Proxy (/etc/nginx/sites-available/default):
   location / {
       proxy_pass http://127.0.0.1:3000; # Points to internal app port
       proxy_set_header Host $host;
       proxy_set_header X-Real-IP $remote_addr;
   }
4. SSL Termination: Run 'sudo certbot --nginx -d yourdomain.com'
5. Load Balancing: Define an 'upstream cluster_name { server IP1; server IP2; }' 
   and pass it via proxy_pass. Methods include Round-Robin, least_conn, or ip_hash.
"""

WEB_SERVER_ROLES = """
--- Static vs Dynamic Web Servers ---
- Web Server: Hosts files, reads incoming HTTP requests via Port 80/443, returns status codes (200 OK, 404 Missing).
- Static Servers: Sends pristine HTML/CSS/JS files straight from storage to client.
- Dynamic Servers: Updates templates on-the-fly by parsing data from an application server and database.
"""


# ==============================================================================
# PART 2: THE FIZZBUZZ ALGORITHM COMPARISON
# ==============================================================================
print("--- 1. FizzBuzz Comparison: Multi-Conditional vs String Concatenation ---")

entry_size = 15  # Simulated user element input

# Approach A: Your Optimized Logic (Clean, readable, explicitly handles combinations)
your_final = []
for i in range(1, entry_size + 1):
    if i % 3 == 0 and i % 5 == 0:
        your_final.append("fizzbuzz")
    elif i % 3 == 0:
        your_final.append("fizz")
    elif i % 5 == 0:
        your_final.append("buzz")
    else:
        your_final.append(i)
print(f"Your Clear Block Output: {your_final}")

# Approach B: The Instructor's String Concatenation (Highly scalable for extra rules)
instructor_list = []
for num in range(1, entry_size + 1):
    result_str = ""  # Reinitialized fresh at the start of each iteration
    if num % 3 == 0:
        result_str += "fizz"
    if num % 5 == 0:
        result_str += "buzz"
        
    # Checking if string state remains empty (meaning not a multiple of 3 or 5)
    if result_str == "":
        instructor_list.append(num)
    else:
        instructor_list.append(result_str)
print(f"Instructor Built String Output: {instructor_list}\n" + "="*50 + "\n")


# ==============================================================================
# PART 3: REVERSE LOOPS & LOGICAL TRUTH TABLES
# ==============================================================================
print("--- 2. Python Sequencers, Reverse Counting, and Truth Tables ---")

# Exclusive stop demonstration (Forward hits 95, backward counts down to 5)
print("Forward Upward Step (0 to 100 step 5):")
for i in range(0, 100, 5):
    print(i, end=" ")
print("\nReverse Countdown Step (100 to 0 step -5):")
for i in range(100, 0, -5):
    print(i, end=" ")
print("\n")

# Evaluating Boolean Logic Operations
print(f"True or True   -> {True or True}")
print(f"False or True  -> {False or True}")
print(f"True or False  -> {True or False}")
print(f"False or False -> {False or False}\n" + "="*50 + "\n")


# ==============================================================================
# PART 4: DATA STRUCTURES & THE COMPREHENSIVE SET BOUNCER
# ==============================================================================
print("--- 3. Collection Traversals & Set Conversions ---")

# List Processing
list1 = ["hello", "welcome", "user"]
print(f"Original Ordered List: {list1}")

# Dictionary Parsing using .items(), .keys(), and .values()
dictionary = {"first": "ravi", "second": "seema", "third": "meena"}
for k, l in dictionary.items():
    print(f"Position Token: {k} | Evaluated Name: {l}")

# Tuple Initialization
tu = (6, 7, 8, 9, 10)

# Set Conversions (Purges duplicates, completely scrambles order via Hash Tables & Salts)
raw_tuple_with_duplicates = (3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 21)
converted_set = set(raw_tuple_with_duplicates)
dict_keys_set = set(dictionary)
dict_values_set = set(dictionary.values())

print(f"Tuple transformed to unique Set: {converted_set}")
print(f"Dictionary keys isolated as Set: {dict_keys_set}")
print(f"Dictionary values isolated as Set: {dict_values_set}\n" + "="*50 + "\n")


# ==============================================================================
# PART 5: EXTENSIVE STRING METHODS & GOLD-STANDARD TYPE VALIDATION
# ==============================================================================
print("--- 4. Built-in String Cleansing & Type Verification ---")

raw_input_simulation = "   rAvI kUmAr   "
cleaned_input = raw_input_simulation.strip()     # Erases edge padding spaces
lowercase_input = cleaned_input.lower()          # Forces lowercase for safe validation
titlecase_output = cleaned_input.title()         # Capitalizes individual word leads

print(f"Cleaned Title Case Output: {titlecase_output}")
print(f"Is Alphabetic Verification? -> {titlecase_output.replace(' ', '').isalpha()}") # Space stripped out to verify letters

# Using gold-standard isinstance() checking across native types
print(f"Is 25 an instance of Integer? -> {isinstance(25, int)}")
print(f"Is converted_set a Set?      -> {isinstance(converted_set, set)}\n" + "="*50 + "\n")


# ==============================================================================
# PART 6: MASTER LOOP CONTEXT (INPUT CONTROLLER WITH JUMP ACTIONS)
# ==============================================================================
print("--- 5. Main Production Runtime Environment Loop ---")

# Infinite execution cycle using break to step out and continue to bypass logic
while True:
    num_input = input("Enter a valid whole number (or 'q' to safely quit): ")
    
    # Check for text string entries
    if num_input.isalpha():
        # Case Insensitive evaluation rule utilizing an inclusion list array
        if num_input in ['q', 'Q', 'quit', 'QUIT']:
            print("Execution successfully halted. Breaking out of loop structure!")
            break  # Completely terminates the loop
        else:
            print("❌ Input contains non-numeric text characters. Please try again.")
            continue  # Skips remaining check steps, forces immediate turn re-evaluation
            
    # Check for pure numeric digit string lines
    elif num_input.isdigit():
        processed_int = int(num_input)  # Safe conversion now that validation passed
        
        # Mathematical module evaluation
        if processed_int % 2 == 0:
            print(f"🎉 Even Number Verified: {processed_int}")
        else:
            print(f"🎉 Odd Number Verified: {processed_int}")
            
    # Traps negative values, symbols (@, #), floating decimals, or blank empty spaces
    else:
        print("❌ Special symbols, spaces, or decimals detected. Input must be an integer.")

print("\nAll operational phases successfully verified.")
