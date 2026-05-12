import threading
import requests
import random
import time


user_agents = [# 1. **General Browsers**
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.64',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Opera/76.0.4017.94',

    # 2. **Mobile Browsers**
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; ARM; rv:87.0) Gecko/87.0 Firefox/87.0',
    'Mozilla/5.0 (Linux; Android 9; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36',
]

def checker_url(url):
    try:
            headers = {
    "User-Agent": random.choice(user_agents)
}
            r = requests.get(url, headers=headers, timeout=10)
            
            if r.status_code == 200:
                print(f"Status: {r.status_code} | URL: {url}")
                time.sleep(2)

            else:
                print(f"Status: {r.status_code} | URL: {url}")
                time.sleep(2)

    except requests.exceptions.RequestException as e:
        print(f"[ERROR]: {url} -> {e}")
        time.sleep(2)

def scan_admin(target, admin_paths):

    print(f"\nScanning: {target}\n")

    threads = [ ]

    for path in admin_paths:

        url = target + path
        time.sleep(0.5)

        t = threading.Thread(target=checker_url, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    
target = input("Target URL: ").strip()


if not target.startswith(("http://","https://")):
    target = "http://" + target


admin_paths = [
    "/admin",
    "/admin/",
    "/admin/login",
    "/admin/logout",
    "/admin/dashboard",
    "/admin/index",
    "/admin/home",

    "/admin-panel",
    "/admin_panel",
    "/adminarea",
    "/admin-area",
    "/adminpage",

    "/admin-console",
    "/adminconsole",
    "/admincp",
    "/admincp/login",

    "/administrator",
    "/administrator/index.php",
    "/administrator/login",

    "/adm",
    "/admin1",
    "/admin2",

    "/adminportal",
    "/adminsite",
    "/adminaccess",
    "/adminzone",

    "/backend",
    "/backend/login",
    "/backoffice",

    "/cms",
    "/cms-admin",
    "/cms/login",

    "/controlpanel",
    "/cpanel",

    "/dashboard",
    "/dashboard/login",

    "/manage",
    "/manager/login",

    "/moderator",
    "/moderator/login",

    "/panel",
    "/panel/login",

    "/portal",
    "/portal/login",

    "/secure",

    "/superadmin",
    "/superuser",
    "/superuser/login",

    "/system",
    "/system/dashboard",

    "/siteadmin",
    "/site-admin",

    "/staff",
    "/staffpanel",

    "/webadmin",
    "/webmaster",
    "/webpanel",

    "/login",
    "/signin",
    "/auth",
    "/access",

    "/config",
    "/setup",
    "/root",

    "/phpmyadmin",
    "/pma",

    "/wp-admin",
    "/wp-login.php"
]

scan_admin(target, admin_paths)