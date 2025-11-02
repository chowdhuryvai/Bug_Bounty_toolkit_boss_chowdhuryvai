#!/usr/bin/env python3
"""
ChowdhuryVai Bug Bounty Toolkit
Professional Security Assessment Tool
Created by ChowdhuryVai
"""

import os
import sys
import time
import socket
import threading
import subprocess
import requests
import urllib.parse
import random
import zipfile
import hashlib
import base64
import json
import re
import ssl
from datetime import datetime
from urllib.request import urlopen

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class ChowdhuryVaiToolkit:
    def __init__(self):
        self.author = "ChowdhuryVai"
        self.version = "3.0"
        self.telegram_id = "https://t.me/darkvaiadmin"
        self.telegram_channel = "https://t.me/windowspremiumkey"
        self.website = "https://crackyworld.com/"
        self.target = ""
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def banner(self):
        banner = f"""
{Colors.RED}{Colors.BOLD}
    ██████╗██╗  ██╗ ██████╗ ██╗    ██╗██████╗ ██╗   ██╗██████╗ ██╗   ██╗██╗   ██╗ █████╗ ██╗
   ██╔════╝██║  ██║██╔═══██╗██║    ██║██╔══██╗██║   ██║██╔══██╗╚██╗ ██╔╝██║   ██║██╔══██╗██║
   ██║     ███████║██║   ██║██║ █╗ ██║██║  ██║██║   ██║██████╔╝ ╚████╔╝ ██║   ██║███████║██║
   ██║     ██╔══██║██║   ██║██║███╗██║██║  ██║██║   ██║██╔══██╗  ╚██╔╝  ██║   ██║██╔══██║██║
   ╚██████╗██║  ██║╚██████╔╝╚███╔███╔╝██████╔╝╚██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║███████╗
    ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
    
    {Colors.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗
    {Colors.CYAN}║               BUG BOUNTY & SECURITY TOOLKIT v3.0 PROFESSIONAL               ║
    {Colors.CYAN}║                                                                              ║
    {Colors.YELLOW}║           Telegram: https://t.me/darkvaiadmin                             ║
    {Colors.YELLOW}║           Channel:  https://t.me/windowspremiumkey                        ║
    {Colors.YELLOW}║           Website:   https://crackyworld.com                              ║
    {Colors.CYAN}║                                                                              ║
    {Colors.CYAN}╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.END}
        """
        print(banner)
    
    def loading_animation(self, message):
        animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        for i in range(15):
            time.sleep(0.1)
            sys.stdout.write(f"\r{Colors.CYAN}[{animation[i % len(animation)]}] {message}{Colors.END}")
            sys.stdout.flush()
        print()
    
    def menu(self):
        menu_options = [
            f"{Colors.GREEN}1.{Colors.END} Subdomain Scanner",
            f"{Colors.GREEN}2.{Colors.END} Port Scanner",
            f"{Colors.GREEN}3.{Colors.END} Directory Brute Forcer",
            f"{Colors.GREEN}4.{Colors.END} SQL Injection Tester",
            f"{Colors.GREEN}5.{Colors.END} XSS Vulnerability Scanner",
            f"{Colors.GREEN}6.{Colors.END} CMS Detection",
            f"{Colors.GREEN}7.{Colors.END} WHOIS Lookup",
            f"{Colors.GREEN}8.{Colors.END} SSL Certificate Info",
            f"{Colors.GREEN}9.{Colors.END} DNS Enumeration",
            f"{Colors.GREEN}10.{Colors.END} HTTP Header Analyzer",
            f"{Colors.GREEN}11.{Colors.END} Crawler",
            f"{Colors.GREEN}12.{Colors.END} Admin Panel Finder",
            f"{Colors.GREEN}13.{Colors.END} Backup File Finder",
            f"{Colors.GREEN}14.{Colors.END} Email Harvester",
            f"{Colors.BLUE}15.{Colors.END} 🔧 Utilities",
            f"{Colors.GREEN}16.{Colors.END} About & Contact",
            f"{Colors.RED}0.{Colors.END} Exit"
        ]
        
        while True:
            self.clear_screen()
            self.banner()
            print(f"{Colors.CYAN}{Colors.BOLD}Available Tools:{Colors.END}\n")
            for option in menu_options:
                print(f"    {option}")
            
            print(f"\n{Colors.YELLOW}{Colors.BOLD}Contact Info:{Colors.END}")
            print(f"    {Colors.WHITE}Telegram ID: {self.telegram_id}{Colors.END}")
            print(f"    {Colors.WHITE}Telegram Channel: {self.telegram_channel}{Colors.END}")
            print(f"    {Colors.WHITE}Website: {self.website}{Colors.END}")
            
            try:
                choice = input(f"\n{Colors.GREEN}{Colors.BOLD}[+] Select an option: {Colors.END}")
                
                if choice == "1":
                    self.subdomain_scanner()
                elif choice == "2":
                    self.port_scanner()
                elif choice == "3":
                    self.directory_bruteforcer()
                elif choice == "4":
                    self.sql_injection_tester()
                elif choice == "5":
                    self.xss_scanner()
                elif choice == "6":
                    self.cms_detector()
                elif choice == "7":
                    self.whois_lookup()
                elif choice == "8":
                    self.ssl_checker()
                elif choice == "9":
                    self.dns_enumeration()
                elif choice == "10":
                    self.header_analyzer()
                elif choice == "11":
                    self.web_crawler()
                elif choice == "12":
                    self.admin_finder()
                elif choice == "13":
                    self.backup_finder()
                elif choice == "14":
                    self.email_harvester()
                elif choice == "15":
                    self.utilities_menu()
                elif choice == "16":
                    self.about()
                elif choice == "0":
                    print(f"\n{Colors.RED}Thanks for using ChowdhuryVai Toolkit!{Colors.END}")
                    sys.exit()
                else:
                    input(f"{Colors.RED}Invalid option! Press Enter to continue...{Colors.END}")
            
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}Tool interrupted by user.{Colors.END}")
                sys.exit()
    
    def utilities_menu(self):
        while True:
            self.clear_screen()
            self.banner()
            print(f"{Colors.BLUE}{Colors.BOLD}[=== 🔧 Utilities Menu ===]{Colors.END}\n")
            
            utilities = [
                f"{Colors.GREEN}1.{Colors.END} Phishing Attack",
                f"{Colors.GREEN}2.{Colors.END} Password Zip Cracked Attack",
                f"{Colors.GREEN}3.{Colors.END} Password Decrypted Attack",
                f"{Colors.GREEN}4.{Colors.END} Password Encrypted",
                f"{Colors.GREEN}5.{Colors.END} Search In DataBase",
                f"{Colors.GREEN}6.{Colors.END} Dark Web Links",
                f"{Colors.GREEN}7.{Colors.END} IP Generator",
                f"{Colors.RED}0.{Colors.END} Back to Main Menu"
            ]
            
            for util in utilities:
                print(f"    {util}")
            
            try:
                choice = input(f"\n{Colors.GREEN}{Colors.BOLD}[+] Select utility: {Colors.END}")
                
                if choice == "1":
                    self.phishing_attack()
                elif choice == "2":
                    self.password_zip_crack()
                elif choice == "3":
                    self.password_decrypt()
                elif choice == "4":
                    self.password_encrypt()
                elif choice == "5":
                    self.search_database()
                elif choice == "6":
                    self.dark_web_links()
                elif choice == "7":
                    self.ip_generator()
                elif choice == "0":
                    return
                else:
                    input(f"{Colors.RED}Invalid option! Press Enter to continue...{Colors.END}")
                    
            except KeyboardInterrupt:
                return

    def phishing_attack(self):
        print(f"\n{Colors.RED}{Colors.BOLD}[=== Phishing Attack Simulator ===]{Colors.END}")
        print(f"{Colors.YELLOW}[!] This is for educational purposes only!{Colors.END}")
        
        print(f"\n{Colors.CYAN}Available Templates:{Colors.END}")
        templates = [
            "1. Facebook Login",
            "2. Gmail Login", 
            "3. Instagram Login",
            "4. Twitter Login",
            "5. Custom Template"
        ]
        
        for template in templates:
            print(f"    {template}")
        
        try:
            choice = input(f"\n{Colors.GREEN}[+] Select template: {Colors.END}")
            target_url = input(f"{Colors.GREEN}[+] Enter target domain (without http): {Colors.END}")
            
            if not target_url:
                print(f"{Colors.RED}[-] Target URL required!{Colors.END}")
                return
            
            self.loading_animation("Generating phishing page...")
            
            templates_data = {
                "1": {"name": "Facebook", "file": "facebook_phish.html"},
                "2": {"name": "Gmail", "file": "gmail_phish.html"},
                "3": {"name": "Instagram", "file": "instagram_phish.html"},
                "4": {"name": "Twitter", "file": "twitter_phish.html"},
                "5": {"name": "Custom", "file": "custom_phish.html"}
            }
            
            if choice in templates_data:
                template_info = templates_data[choice]
                print(f"\n{Colors.GREEN}[+] {template_info['name']} phishing template generated!{Colors.END}")
                print(f"{Colors.CYAN}[+] Template saved as: {template_info['file']}{Colors.END}")
                print(f"{Colors.YELLOW}[!] This is a simulation for educational purposes{Colors.END}")
                
                # Create simple HTML template
                html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{template_info['name']} Login</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #f0f0f0; }}
        .login-box {{ width: 300px; margin: 100px auto; padding: 20px; background: white; border-radius: 5px; }}
        input {{ width: 100%; padding: 10px; margin: 5px 0; }}
        button {{ width: 100%; padding: 10px; background: #1877f2; color: white; border: none; }}
    </style>
</head>
<body>
    <div class="login-box">
        <h2>{template_info['name']} Login</h2>
        <input type="text" placeholder="Email or Phone" id="username">
        <input type="password" placeholder="Password" id="password">
        <button onclick="login()">Log In</button>
        <p style="color:red; font-size:12px;">This is a security test page</p>
    </div>
    <script>
        function login() {{
            var username = document.getElementById('username').value;
            var password = document.getElementById('password').value;
            alert('Educational Purpose Only!\\nUsername: ' + username + '\\nPassword: ' + password);
        }}
    </script>
</body>
</html>
                """
                
                with open(template_info['file'], 'w') as f:
                    f.write(html_content)
                
                print(f"{Colors.GREEN}[+] Phishing page created successfully!{Colors.END}")
                print(f"{Colors.YELLOW}[!] Remember: Only use for authorized testing{Colors.END}")
                
            else:
                print(f"{Colors.RED}[-] Invalid template selection!{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def password_zip_crack(self):
        print(f"\n{Colors.RED}{Colors.BOLD}[=== Password Zip Crack Attack ===]{Colors.END}")
        
        try:
            zip_file = input(f"{Colors.GREEN}[+] Enter ZIP file path: {Colors.END}")
            
            if not os.path.exists(zip_file):
                print(f"{Colors.RED}[-] ZIP file not found!{Colors.END}")
                return
            
            print(f"\n{Colors.CYAN}Attack Methods:{Colors.END}")
            methods = ["1. Dictionary Attack", "2. Brute Force (Basic)", "3. Common Passwords"]
            
            for method in methods:
                print(f"    {method}")
            
            method_choice = input(f"\n{Colors.GREEN}[+] Select method: {Colors.END}")
            
            self.loading_animation("Cracking ZIP password...")
            
            common_passwords = [
                "password", "123456", "12345678", "1234", "qwerty", "12345", 
                "dragon", "baseball", "football", "letmein", "monkey", "696969",
                "abc123", "mustang", "michael", "shadow", "master", "jennifer",
                "111111", "2000", "jordan", "superman", "harley", "1234567",
                "freedom", "charlie", "trustno1", "robert", "buster", "thomas"
            ]
            
            cracked = False
            password_found = ""
            
            if method_choice == "1":
                wordlist = input(f"{Colors.GREEN}[+] Enter wordlist file path: {Colors.END}")
                if os.path.exists(wordlist):
                    with open(wordlist, 'r', errors='ignore') as f:
                        passwords = f.readlines()
                else:
                    print(f"{Colors.YELLOW}[-] Wordlist not found, using common passwords{Colors.END}")
                    passwords = common_passwords
            elif method_choice == "2":
                # Simple brute force with common patterns
                passwords = common_passwords + [str(i) for i in range(10000)]
            else:
                passwords = common_passwords
            
            for pwd in passwords:
                try:
                    pwd = pwd.strip()
                    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                        zip_ref.extractall(pwd=pwd.encode())
                    cracked = True
                    password_found = pwd
                    break
                except:
                    continue
            
            if cracked:
                print(f"\n{Colors.GREEN}[+] Password cracked successfully!{Colors.END}")
                print(f"{Colors.GREEN}[+] Password: {password_found}{Colors.END}")
            else:
                print(f"\n{Colors.RED}[-] Failed to crack password{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def password_decrypt(self):
        print(f"\n{Colors.RED}{Colors.BOLD}[=== Password Decryption Attack ===]{Colors.END}")
        
        try:
            encrypted_hash = input(f"{Colors.GREEN}[+] Enter hash to decrypt: {Colors.END}")
            hash_type = input(f"{Colors.GREEN}[+] Enter hash type (md5/sha1/sha256): {Colors.END}").lower()
            
            if hash_type not in ['md5', 'sha1', 'sha256']:
                print(f"{Colors.RED}[-] Unsupported hash type!{Colors.END}")
                return
            
            self.loading_animation("Decrypting hash...")
            
            # Common passwords to test against
            common_passwords = [
                "password", "123456", "123456789", "admin", "qwerty", "letmein",
                "welcome", "monkey", "password1", "1234567", "12345678", "abc123"
            ]
            
            decrypted = False
            found_password = ""
            
            for pwd in common_passwords:
                test_hash = ""
                if hash_type == 'md5':
                    test_hash = hashlib.md5(pwd.encode()).hexdigest()
                elif hash_type == 'sha1':
                    test_hash = hashlib.sha1(pwd.encode()).hexdigest()
                elif hash_type == 'sha256':
                    test_hash = hashlib.sha256(pwd.encode()).hexdigest()
                
                if test_hash == encrypted_hash:
                    decrypted = True
                    found_password = pwd
                    break
            
            if decrypted:
                print(f"\n{Colors.GREEN}[+] Hash decrypted successfully!{Colors.END}")
                print(f"{Colors.GREEN}[+] Password: {found_password}{Colors.END}")
                print(f"{Colors.GREEN}[+] Hash Type: {hash_type}{Colors.END}")
            else:
                print(f"\n{Colors.RED}[-] Failed to decrypt hash{Colors.END}")
                print(f"{Colors.YELLOW}[!] Try with a larger wordlist{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def password_encrypt(self):
        print(f"\n{Colors.RED}{Colors.BOLD}[=== Password Encryption ===]{Colors.END}")
        
        try:
            password = input(f"{Colors.GREEN}[+] Enter password to encrypt: {Colors.END}")
            
            print(f"\n{Colors.CYAN}Available Encryption Methods:{Colors.END}")
            methods = ["1. MD5", "2. SHA1", "3. SHA256", "4. Base64", "5. All Methods"]
            
            for method in methods:
                print(f"    {method}")
            
            choice = input(f"\n{Colors.GREEN}[+] Select method: {Colors.END}")
            
            self.loading_animation("Encrypting password...")
            
            print(f"\n{Colors.GREEN}[+] Encryption Results:{Colors.END}")
            
            if choice in ['1', '5']:
                md5_hash = hashlib.md5(password.encode()).hexdigest()
                print(f"{Colors.CYAN}MD5: {md5_hash}{Colors.END}")
            
            if choice in ['2', '5']:
                sha1_hash = hashlib.sha1(password.encode()).hexdigest()
                print(f"{Colors.CYAN}SHA1: {sha1_hash}{Colors.END}")
            
            if choice in ['3', '5']:
                sha256_hash = hashlib.sha256(password.encode()).hexdigest()
                print(f"{Colors.CYAN}SHA256: {sha256_hash}{Colors.END}")
            
            if choice in ['4', '5']:
                base64_enc = base64.b64encode(password.encode()).decode()
                print(f"{Colors.CYAN}Base64: {base64_enc}{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def search_database(self):
        print(f"\n{Colors.RED}{Colors.BOLD}[=== Search In Database ===]{Colors.END}")
        
        try:
            # Simulated database of leaked credentials
            simulated_db = {
                "users": [
                    {"username": "admin", "password": "admin123", "email": "admin@test.com", "source": "Test DB"},
                    {"username": "user1", "password": "password123", "email": "user1@email.com", "source": "Leak 2023"},
                    {"username": "john_doe", "password": "john123", "email": "john@example.com", "source": "Breach 2022"},
                    {"username": "jane_smith", "password": "jane2023", "email": "jane@test.org", "source": "Leak 2023"}
                ],
                "emails": [
                    {"email": "admin@company.com", "password": "Company@123", "breach": "Company DB 2023"},
                    {"email": "support@service.com", "password": "Support2023!", "breach": "Service Leak"}
                ]
            }
            
            search_type = input(f"{Colors.GREEN}[+] Search by (1) Username (2) Email (3) Password: {Colors.END}")
            search_term = input(f"{Colors.GREEN}[+] Enter search term: {Colors.END}")
            
            self.loading_animation("Searching in database...")
            
            results = []
            
            if search_type == "1":
                for user in simulated_db["users"]:
                    if search_term.lower() in user["username"].lower():
                        results.append(user)
            elif search_type == "2":
                # Search in users
                for user in simulated_db["users"]:
                    if search_term.lower() in user["email"].lower():
                        results.append(user)
                # Search in emails
                for email in simulated_db["emails"]:
                    if search_term.lower() in email["email"].lower():
                        results.append(email)
            elif search_type == "3":
                for user in simulated_db["users"]:
                    if search_term.lower() in user["password"].lower():
                        results.append(user)
            
            if results:
                print(f"\n{Colors.GREEN}[+] Found {len(results)} results:{Colors.END}")
                for i, result in enumerate(results, 1):
                    print(f"\n{Colors.CYAN}Result {i}:{Colors.END}")
                    for key, value in result.items():
                        print(f"  {Colors.YELLOW}{key}: {Colors.WHITE}{value}{Colors.END}")
            else:
                print(f"\n{Colors.RED}[-] No results found{Colors.END}")
                print(f"{Colors.YELLOW}[!] This is a simulated database for demonstration{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def dark_web_links(self):
        print(f"\n{Colors.RED}{Colors.BOLD}[=== Dark Web Links (Educational) ===]{Colors.END}")
        print(f"{Colors.YELLOW}[!] WARNING: For educational purposes only!{Colors.END}")
        print(f"{Colors.YELLOW}[!] Accessing dark web can be illegal in your country{Colors.END}")
        
        dark_web_info = {
            "Tor Network": [
                "Requires Tor Browser to access",
                "Download from: https://www.torproject.org/",
                ".onion sites are only accessible via Tor"
            ],
            "Security Notes": [
                "Use VPN with Tor for extra security",
                "Never use personal information",
                "Be aware of scams and illegal content",
                "Use virtual machines for safety"
            ],
            "Legal Alternatives": [
                "Use security forums for information",
                "Practice on legal platforms like HackTheBox",
                "Use TryHackMe for learning",
                "Participate in bug bounty programs"
            ]
        }
        
        for category, items in dark_web_info.items():
            print(f"\n{Colors.CYAN}{category}:{Colors.END}")
            for item in items:
                print(f"  {Colors.WHITE}• {item}{Colors.END}")
        
        print(f"\n{Colors.RED}[!] IMPORTANT LEGAL NOTICE:{Colors.END}")
        print(f"{Colors.YELLOW}• Only use for authorized security research{Colors.END}")
        print(f"{Colors.YELLOW}• Respect laws and regulations{Colors.END}")
        print(f"{Colors.YELLOW}• Use ethical hacking principles{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def ip_generator(self):
        print(f"\n{Colors.RED}{Colors.BOLD}[=== IP Generator ===]{Colors.END}")
        
        try:
            print(f"\n{Colors.CYAN}Generation Options:{Colors.END}")
            options = [
                "1. Random IP Addresses",
                "2. Specific Country IPs",
                "3. Private Network IPs", 
                "4. Custom Range IPs"
            ]
            
            for option in options:
                print(f"    {option}")
            
            choice = input(f"\n{Colors.GREEN}[+] Select option: {Colors.END}")
            count = int(input(f"{Colors.GREEN}[+] How many IPs to generate: {Colors.END}"))
            
            self.loading_animation("Generating IP addresses...")
            
            generated_ips = []
            
            if choice == "1":
                # Random IPs
                for _ in range(count):
                    ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
                    generated_ips.append(ip)
                    
            elif choice == "2":
                # Country-specific IP ranges (simulated)
                countries = {
                    "1": {"name": "USA", "range": "192.168"},
                    "2": {"name": "UK", "range": "193.168"}, 
                    "3": {"name": "Germany", "range": "194.168"},
                    "4": {"name": "Japan", "range": "195.168"}
                }
                
                print(f"\n{Colors.CYAN}Available Countries:{Colors.END}")
                for key, country in countries.items():
                    print(f"    {key}. {country['name']}")
                
                country_choice = input(f"{Colors.GREEN}[+] Select country: {Colors.END}")
                
                if country_choice in countries:
                    base = countries[country_choice]["range"]
                    for i in range(count):
                        ip = f"{base}.{random.randint(1, 254)}.{random.randint(1, 254)}"
                        generated_ips.append(ip)
            
            elif choice == "3":
                # Private IPs
                private_ranges = [
                    "10", "172.16", "192.168"
                ]
                base = random.choice(private_ranges)
                for i in range(count):
                    if base == "10":
                        ip = f"10.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
                    elif base == "172.16":
                        ip = f"172.16.{random.randint(0, 31)}.{random.randint(1, 254)}"
                    else:
                        ip = f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"
                    generated_ips.append(ip)
            
            elif choice == "4":
                # Custom range
                base = input(f"{Colors.GREEN}[+] Enter IP base (e.g., 192.168.1): {Colors.END}")
                for i in range(count):
                    ip = f"{base}.{random.randint(1, 254)}"
                    generated_ips.append(ip)
            
            # Display generated IPs
            print(f"\n{Colors.GREEN}[+] Generated {len(generated_ips)} IP addresses:{Colors.END}")
            for i, ip in enumerate(generated_ips, 1):
                print(f"  {Colors.CYAN}{i}. {ip}{Colors.END}")
            
            # Save to file option
            save = input(f"\n{Colors.GREEN}[+] Save to file? (y/n): {Colors.END}").lower()
            if save == 'y':
                filename = f"generated_ips_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, 'w') as f:
                    for ip in generated_ips:
                        f.write(ip + '\n')
                print(f"{Colors.GREEN}[+] IPs saved to: {filename}{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def get_target(self):
        self.target = input(f"{Colors.GREEN}[+] Enter target domain/IP: {Colors.END}").strip()
        if not self.target:
            print(f"{Colors.RED}[-] Target cannot be empty!{Colors.END}")
            return False
        return True

    def subdomain_scanner(self):
        print(f"\n{Colors.CYAN}[=== Subdomain Scanner ===]{Colors.END}")
        if not self.get_target():
            return
        
        common_subdomains = [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
            'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test',
            'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn', 'ns3',
            'mail2', 'new', 'mysql', 'old', 'lists', 'support', 'mobile', 'mx', 'static'
        ]
        
        found_subdomains = []
        self.loading_animation("Scanning for subdomains...")
        
        for sub in common_subdomains:
            domain = f"{sub}.{self.target}"
            try:
                socket.gethostbyname(domain)
                found_subdomains.append(domain)
                print(f"{Colors.GREEN}[+] Found: {domain}{Colors.END}")
            except socket.gaierror:
                continue
        
        print(f"\n{Colors.CYAN}[+] Scan completed! Found {len(found_subdomains)} subdomains.{Colors.END}")
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def port_scanner(self):
        print(f"\n{Colors.CYAN}[=== Port Scanner ===]{Colors.END}")
        if not self.get_target():
            return
        
        common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995, 
                       1723, 3306, 3389, 5900, 8080, 8443]
        
        open_ports = []
        self.loading_animation(f"Scanning ports on {self.target}...")
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))
                sock.close()
                if result == 0:
                    open_ports.append(port)
                    try:
                        service = socket.getservbyport(port, 'tcp')
                    except:
                        service = "unknown"
                    print(f"{Colors.GREEN}[+] Port {port} ({service}) is open{Colors.END}")
            except:
                pass
        
        threads = []
        for port in common_ports:
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        print(f"\n{Colors.CYAN}[+] Scan completed! Found {len(open_ports)} open ports.{Colors.END}")
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def directory_bruteforcer(self):
        print(f"\n{Colors.CYAN}[=== Directory Brute Forcer ===]{Colors.END}")
        if not self.get_target():
            return
        
        common_dirs = [
            'admin', 'administrator', 'login', 'wp-admin', 'cpanel', 'phpmyadmin',
            'backup', 'backups', 'tmp', 'temp', 'uploads', 'images', 'css', 'js',
            'config', 'database', 'db', 'sql', 'backup.sql', 'old', 'test',
            'admin/login', 'wp-login.php', 'administrator/login', 'user/login'
        ]
        
        protocol = input(f"{Colors.GREEN}[+] Use HTTPS? (y/n): {Colors.END}").strip().lower()
        base_url = f"https://{self.target}" if protocol == 'y' else f"http://{self.target}"
        
        found_dirs = []
        self.loading_animation("Brute forcing directories...")
        
        for directory in common_dirs:
            url = f"{base_url}/{directory}"
            try:
                response = requests.get(url, timeout=5, verify=False)
                if response.status_code == 200:
                    found_dirs.append(url)
                    print(f"{Colors.GREEN}[+] Found: {url} (Status: {response.status_code}){Colors.END}")
                elif response.status_code in [301, 302, 307, 308]:
                    print(f"{Colors.YELLOW}[+] Found: {url} (Redirect: {response.status_code}){Colors.END}")
            except:
                continue
        
        print(f"\n{Colors.CYAN}[+] Scan completed! Found {len(found_dirs)} accessible directories.{Colors.END}")
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def sql_injection_tester(self):
        print(f"\n{Colors.CYAN}[=== SQL Injection Tester ===]{Colors.END}")
        if not self.get_target():
            return
        
        protocol = input(f"{Colors.GREEN}[+] Use HTTPS? (y/n): {Colors.END}").strip().lower()
        base_url = f"https://{self.target}" if protocol == 'y' else f"http://{self.target}"
        
        payloads = [
            "'",
            "';",
            "' OR '1'='1",
            "' OR 1=1--",
            "' UNION SELECT 1,2,3--"
        ]
        
        test_params = ['id', 'page', 'category', 'user', 'product', 'search']
        
        self.loading_animation("Testing for SQL Injection vulnerabilities...")
        
        vulnerable = False
        for param in test_params:
            for payload in payloads:
                test_url = f"{base_url}?{param}={urllib.parse.quote(payload)}"
                try:
                    response = requests.get(test_url, timeout=5, verify=False)
                    content_lower = response.text.lower()
                    if any(error in content_lower for error in ['sql', 'mysql', 'ora-', 'syntax', 'error']):
                        print(f"{Colors.RED}[!] Possible SQL Injection: {test_url}{Colors.END}")
                        vulnerable = True
                        break
                except:
                    continue
        
        if not vulnerable:
            print(f"{Colors.YELLOW}[-] No obvious SQL Injection vulnerabilities found.{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def xss_scanner(self):
        print(f"\n{Colors.CYAN}[=== XSS Vulnerability Scanner ===]{Colors.END}")
        if not self.get_target():
            return
        
        protocol = input(f"{Colors.GREEN}[+] Use HTTPS? (y/n): {Colors.END}").strip().lower()
        base_url = f"https://{self.target}" if protocol == 'y' else f"http://{self.target}"
        
        payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>"
        ]
        
        test_params = ['q', 'search', 'query', 'keyword', 'name', 'message', 'comment']
        
        self.loading_animation("Testing for XSS vulnerabilities...")
        
        vulnerable = False
        for param in test_params:
            for payload in payloads:
                test_url = f"{base_url}?{param}={urllib.parse.quote(payload)}"
                try:
                    response = requests.get(test_url, timeout=5, verify=False)
                    # Simple check for unescaped payload
                    if payload in response.text:
                        print(f"{Colors.RED}[!] Possible XSS: {test_url}{Colors.END}")
                        vulnerable = True
                        break
                except:
                    continue
        
        if not vulnerable:
            print(f"{Colors.YELLOW}[-] No obvious XSS vulnerabilities found.{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def cms_detector(self):
        print(f"\n{Colors.CYAN}[=== CMS Detection ===]{Colors.END}")
        if not self.get_target():
            return
        
        protocol = input(f"{Colors.GREEN}[+] Use HTTPS? (y/n): {Colors.END}").strip().lower()
        base_url = f"https://{self.target}" if protocol == 'y' else f"http://{self.target}"
        
        cms_indicators = {
            'WordPress': ['/wp-content/', '/wp-admin/', 'wp-json'],
            'Joomla': ['/media/jui/', '/administrator/', 'com_content'],
            'Drupal': ['/sites/default/', '/misc/drupal.js', 'Drupal.settings'],
            'Magento': ['/skin/frontend/', '/media/logo/', 'Mage.Cookies.path']
        }
        
        self.loading_animation("Detecting CMS...")
        
        try:
            response = requests.get(base_url, timeout=5, verify=False)
            detected_cms = []
            
            for cms, indicators in cms_indicators.items():
                for indicator in indicators:
                    if indicator in response.text:
                        if cms not in detected_cms:
                            detected_cms.append(cms)
                            print(f"{Colors.GREEN}[+] Detected: {cms}{Colors.END}")
                            break
            
            if not detected_cms:
                print(f"{Colors.YELLOW}[-] Could not detect CMS or custom CMS{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def whois_lookup(self):
        print(f"\n{Colors.CYAN}[=== WHOIS Lookup ===]{Colors.END}")
        if not self.get_target():
            return
        
        self.loading_animation("Performing WHOIS lookup...")
        
        try:
            # Simple WHOIS using socket connection
            whois_server = "whois.iana.org"
            whois_port = 43
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((whois_server, whois_port))
            sock.send(f"{self.target}\r\n".encode())
            
            response = b""
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                response += data
            
            sock.close()
            
            whois_info = response.decode('utf-8', errors='ignore')
            
            print(f"\n{Colors.GREEN}[+] WHOIS Information for {self.target}:{Colors.END}")
            print(f"{Colors.CYAN}{whois_info[:1000]}...{Colors.END}")  # Show first 1000 chars
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
            print(f"{Colors.YELLOW}[!] Try installing python-whois: pip install python-whois{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def ssl_checker(self):
        print(f"\n{Colors.CYAN}[=== SSL Certificate Checker ===]{Colors.END}")
        if not self.get_target():
            return
        
        self.loading_animation("Checking SSL certificate...")
        
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.target, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=self.target) as ssock:
                    cert = ssock.getpeercert()
                    
                    print(f"\n{Colors.GREEN}[+] SSL Certificate Information:{Colors.END}")
                    if 'subject' in cert:
                        subject = cert['subject']
                        for item in subject:
                            for key, value in item:
                                if key == 'commonName':
                                    print(f"{Colors.CYAN}Common Name: {value}{Colors.END}")
                    
                    if 'issuer' in cert:
                        issuer = cert['issuer']
                        for item in issuer:
                            for key, value in item:
                                if key == 'organizationName':
                                    print(f"{Colors.CYAN}Issuer: {value}{Colors.END}")
                    
                    if 'notAfter' in cert:
                        from datetime import datetime
                        exp_date = cert['notAfter']
                        print(f"{Colors.CYAN}Expiration: {exp_date}{Colors.END}")
                        
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def dns_enumeration(self):
        print(f"\n{Colors.CYAN}[=== DNS Enumeration ===]{Colors.END}")
        if not self.get_target():
            return
        
        self.loading_animation("Enumerating DNS records...")
        
        try:
            # A record
            try:
                a_record = socket.gethostbyname(self.target)
                print(f"{Colors.GREEN}[+] A Record: {a_record}{Colors.END}")
            except:
                print(f"{Colors.RED}[-] Could not resolve A record{Colors.END}")
            
            # Additional DNS info using system commands
            print(f"\n{Colors.CYAN}[+] Additional DNS Information:{Colors.END}")
            
            # Try nslookup if available
            try:
                result = subprocess.run(['nslookup', self.target], capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    print(f"{Colors.WHITE}{result.stdout}{Colors.END}")
            except:
                print(f"{Colors.YELLOW}[-] nslookup not available{Colors.END}")
                    
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def header_analyzer(self):
        print(f"\n{Colors.CYAN}[=== HTTP Header Analyzer ===]{Colors.END}")
        if not self.get_target():
            return
        
        protocol = input(f"{Colors.GREEN}[+] Use HTTPS? (y/n): {Colors.END}").strip().lower()
        base_url = f"https://{self.target}" if protocol == 'y' else f"http://{self.target}"
        
        self.loading_animation("Analyzing HTTP headers...")
        
        try:
            response = requests.get(base_url, timeout=5, verify=False)
            
            print(f"\n{Colors.GREEN}[+] HTTP Headers for {base_url}:{Colors.END}")
            for header, value in response.headers.items():
                print(f"{Colors.CYAN}{header}: {value}{Colors.END}")
            
            # Security header checks
            security_headers = {
                'X-Frame-Options': 'Prevents clickjacking',
                'X-Content-Type-Options': 'Prevents MIME sniffing',
                'X-XSS-Protection': 'XSS protection',
                'Strict-Transport-Security': 'Enforces HTTPS',
                'Content-Security-Policy': 'Content security policy'
            }
            
            print(f"\n{Colors.GREEN}[+] Security Headers Analysis:{Colors.END}")
            for header, description in security_headers.items():
                if header in response.headers:
                    print(f"{Colors.GREEN}[✓] {header}: {response.headers[header]} - {description}{Colors.END}")
                else:
                    print(f"{Colors.RED}[✗] {header}: Missing - {description}{Colors.END}")
                    
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def web_crawler(self):
        print(f"\n{Colors.CYAN}[=== Web Crawler ===]{Colors.END}")
        if not self.get_target():
            return
        
        protocol = input(f"{Colors.GREEN}[+] Use HTTPS? (y/n): {Colors.END}").strip().lower()
        base_url = f"https://{self.target}" if protocol == 'y' else f"http://{self.target}"
        
        self.loading_animation("Crawling website...")
        
        try:
            response = requests.get(base_url, timeout=5, verify=False)
            links = []
            
            # Simple link extraction using regex
            link_pattern = r'href=[\'"]?([^\'" >]+)'
            found_links = re.findall(link_pattern, response.text)
            
            for link in found_links[:20]:  # Limit to first 20 links
                if link.startswith('http'):
                    links.append(link)
                elif link.startswith('/'):
                    links.append(base_url + link)
                else:
                    links.append(base_url + '/' + link)
            
            print(f"\n{Colors.GREEN}[+] Found {len(set(links))} unique links:{Colors.END}")
            for link in set(links):  # Remove duplicates
                print(f"{Colors.CYAN}  {link}{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def admin_finder(self):
        print(f"\n{Colors.CYAN}[=== Admin Panel Finder ===]{Colors.END}")
        if not self.get_target():
            return
        
        protocol = input(f"{Colors.GREEN}[+] Use HTTPS? (y/n): {Colors.END}").strip().lower()
        base_url = f"https://{self.target}" if protocol == 'y' else f"http://{self.target}"
        
        admin_paths = [
            'admin', 'administrator', 'wp-admin', 'admin/login', 'administrator/login',
            'adminarea', 'adminpanel', 'user/login', 'login/admin', 'panel',
            'manage', 'management', 'admincp', 'admin_cp', 'cp', 'controlpanel'
        ]
        
        found_panels = []
        self.loading_animation("Searching for admin panels...")
        
        for path in admin_paths:
            url = f"{base_url}/{path}"
            try:
                response = requests.get(url, timeout=3, verify=False)
                if response.status_code in [200, 301, 302, 403]:
                    found_panels.append((url, response.status_code))
                    status_color = Colors.GREEN if response.status_code == 200 else Colors.YELLOW
                    print(f"{status_color}[+] Admin Panel: {url} (Status: {response.status_code}){Colors.END}")
            except:
                continue
        
        if not found_panels:
            print(f"{Colors.YELLOW}[-] No admin panels found{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def backup_finder(self):
        print(f"\n{Colors.CYAN}[=== Backup File Finder ===]{Colors.END}")
        if not self.get_target():
            return
        
        protocol = input(f"{Colors.GREEN}[+] Use HTTPS? (y/n): {Colors.END}").strip().lower()
        base_url = f"https://{self.target}" if protocol == 'y' else f"http://{self.target}"
        
        backup_files = [
            'backup.zip', 'backup.tar', 'backup.tar.gz', 'backup.sql',
            'backup.rar', 'backup.7z', 'backup.bak', 'database.zip',
            'database.sql', 'db.zip', 'db.sql', 'dump.zip', 'dump.sql'
        ]
        
        found_backups = []
        self.loading_animation("Searching for backup files...")
        
        for file in backup_files:
            url = f"{base_url}/{file}"
            try:
                response = requests.get(url, timeout=3, verify=False)
                if response.status_code == 200 and len(response.content) > 0:
                    found_backups.append(url)
                    print(f"{Colors.RED}[!] Backup file found: {url} (Size: {len(response.content)} bytes){Colors.END}")
            except:
                continue
        
        if not found_backups:
            print(f"{Colors.YELLOW}[-] No backup files found{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def email_harvester(self):
        print(f"\n{Colors.CYAN}[=== Email Harvester ===]{Colors.END}")
        if not self.get_target():
            return
        
        protocol = input(f"{Colors.GREEN}[+] Use HTTPS? (y/n): {Colors.END}").strip().lower()
        base_url = f"https://{self.target}" if protocol == 'y' else f"http://{self.target}"
        
        self.loading_animation("Harvesting emails...")
        
        try:
            response = requests.get(base_url, timeout=5, verify=False)
            
            # Simple email regex pattern
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, response.text)
            
            if emails:
                print(f"\n{Colors.GREEN}[+] Found {len(set(emails))} unique emails:{Colors.END}")
                for email in set(emails):
                    print(f"{Colors.CYAN}  {email}{Colors.END}")
            else:
                print(f"{Colors.YELLOW}[-] No emails found on the main page{Colors.END}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

    def about(self):
        self.clear_screen()
        self.banner()
        
        about_text = f"""
{Colors.CYAN}{Colors.BOLD}[=== About ChowdhuryVai Security Toolkit ===]{Colors.END}

{Colors.GREEN}Version:{Colors.END} {self.version}
{Colors.GREEN}Author:{Colors.END} {self.author}
{Colors.GREEN}Description:{Colors.END} Professional Bug Bounty & Security Assessment Toolkit

{Colors.YELLOW}Main Features:{Colors.END}
• 15+ Security Assessment Tools
• 7+ Utility Tools  
• Phishing Simulation
• Password Cracking Tools
• Encryption/Decryption
• Database Search
• IP Generation

{Colors.BLUE}Utility Tools:{Colors.END}
• Phishing Attack Simulator
• ZIP Password Cracker
• Hash Decryption
• Password Encryption  
• Database Search
• Dark Web Information
• IP Address Generator

{Colors.RED}Important Notice:{Colors.END}
This tool is for educational and authorized security testing only.
Always get proper permission before testing any website or network.

{Colors.CYAN}Contact Information:{Colors.END}
{Colors.WHITE}Telegram ID: {self.telegram_id}{Colors.END}
{Colors.WHITE}Telegram Channel: {self.telegram_channel}{Colors.END}
{Colors.WHITE}Website: {self.website}{Colors.END}

{Colors.YELLOW}Use responsibly and ethically!{Colors.END}
        """
        
        print(about_text)
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

def main():
    try:
        toolkit = ChowdhuryVaiToolkit()
        toolkit.menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Tool interrupted by user.{Colors.END}")
        sys.exit()
    except Exception as e:
        print(f"{Colors.RED}An error occurred: {e}{Colors.END}")
        sys.exit()

if __name__ == "__main__":
    main()
