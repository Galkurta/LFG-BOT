import requests
import json
import os
import time
import signal
from tqdm import tqdm
from colorama import init, Fore, Style
from dotenv import load_dotenv
from requests.exceptions import RequestException

# Initialize colorama
init(autoreset=True)

# Load environment variables
load_dotenv()

ACCOUNT_API_URL = os.getenv('ACCOUNT_API_URL')
MINING_API_URL = os.getenv('MINING_API_URL')
TASK_API_URL = os.getenv('TASK_API_URL')
UPGRADE_API_URL = os.getenv('UPGRADE_API_URL')

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def read_file_lines(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def print_header(text):
    print(f"{Fore.CYAN}{Style.BRIGHT}{text}")

def print_success(text):
    print(f"{Fore.GREEN}{Style.BRIGHT}{text}")

def print_error(text):
    print(f"{Fore.RED}{Style.BRIGHT}{text}")

def print_info(text):
    print(f"{Fore.YELLOW}{Style.BRIGHT}{text}")

def make_request(method, url, headers, data=None):
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=data)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        response.raise_for_status()
        return response
    except RequestException as e:
        print_error(f"Request error: {e}")
    return None

def fetch_account_data(query_id):
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "miniapp-initdata": query_id,
        "origin": "https://miniapp.lfgweb3.app",
        "referer": "https://miniapp.lfgweb3.app/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    response = make_request('GET', ACCOUNT_API_URL, headers)
    if response and response.status_code == 200:
        try:
            data = response.json()
            account = data.get('data', {}).get('account', {})
            print_header("Account Information")
            print_info(f"Username: {account.get('username', 'N/A')} | Points: {account.get('points', 'N/A')} | Level: {account.get('level', 'N/A')}")
            return data
        except json.JSONDecodeError:
            print_error("Unable to parse account data.")
    else:
        print_error("Error occurred while logging into the account!")
    return None

def fetch_mining_data(query_id):
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "miniapp-initdata": query_id,
        "origin": "https://miniapp.lfgweb3.app",
        "referer": "https://miniapp.lfgweb3.app/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    response = make_request('GET', MINING_API_URL, headers)
    if response and response.status_code == 200:
        try:
            data = response.json()
            state = data.get('data', {}).get('state', {})
            print_header("Mining Information")
            print_info(f"Profit per second: {state.get('mine_per_sec', 'N/A')} | Profit per hour: {state.get('mine_rate', 'N/A')}")
            print_success("Successfully harvested machine profits to account.")
            return data
        except json.JSONDecodeError:
            print_error("Unable to parse account mining data.")
    else:
        print_error("Error occurred while parsing account mining data!")
    return None

def watch_tasks(query_id):
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "miniapp-initdata": query_id,
        "origin": "https://miniapp.lfgweb3.app",
        "referer": "https://miniapp.lfgweb3.app/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    print_header("Ad Watching Task")
    response = make_request('POST', TASK_API_URL, headers)
    if response and response.status_code == 200:
        try:
            data = response.json()
            watch_code = data.get('data', {}).get('watch_code', '')
            if watch_code:
                payload = {"data": {"watch_code": watch_code}}
                watch_response = make_request('POST', TASK_API_URL, headers, data=payload)
                if watch_response and watch_response.status_code == 200:
                    print_success(f"Successfully completed ad watching task: {watch_code}.")
                else:
                    print_error("Error occurred while performing ad watching task!")
            else:
                print_error("Unable to find ad watching code.")
        except json.JSONDecodeError:
            print_error("Unable to parse ad watching data.")
    else:
        print_error("Error occurred while fetching ad watching data!")

def upgrade_mining_machine(query_id):
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/json",
        "miniapp-initdata": query_id,
        "origin": "https://miniapp.lfgweb3.app",
        "referer": "https://miniapp.lfgweb3.app/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    print_header("Machine Upgrade")
    response = make_request('GET', MINING_API_URL, headers)
    if response and response.status_code == 200:
        try:
            mining_data = response.json()
            state = mining_data.get('data', {}).get('state', {})
            points = state.get('points', 0)
            machines = mining_data.get('data', {}).get('machine', [])
            upgrade_messages = []
            failed_machines = []
            for machine in machines:
                if machine.get('level', 0) < 100:
                    upgrade_cost = machine.get('upgrade_cost', 0)
                    if points >= upgrade_cost:
                        payload = {"data": {"machine_key": machine['machine_key']}}
                        upgrade_response = make_request('POST', UPGRADE_API_URL, headers, data=payload)
                        if upgrade_response and upgrade_response.status_code == 200:
                            upgrade_messages.append(machine['name'])
                        else:
                            failed_machines.append(machine['name'])
                    else:
                        failed_machines.append(machine['name'])
                else:
                    failed_machines.append(machine['name'])
            if upgrade_messages:
                print_success(f"Successfully upgraded: [{', '.join(upgrade_messages)}].")
            if failed_machines:
                print_error(f"Unable to upgrade: [{', '.join(failed_machines)}].")
        except json.JSONDecodeError:
            print_error("Unable to parse machine upgrade data.")
    else:
        print_error("Error occurred while upgrading machines!")

def graceful_exit(signum, frame):
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}Goodbye! Thanks for using the LFG Mining Script.")
    exit(0)

def main():
    # Set up the signal handler for graceful exit
    signal.signal(signal.SIGINT, graceful_exit)

    try:
        while True:
            clear_console()
            query_ids = read_file_lines('data.txt')
            for i, query_id in enumerate(query_ids, 1):
                if i > 1:
                    print(f"{Fore.MAGENTA}{Style.BRIGHT}{'-' * 40}")
                print(f"{Fore.MAGENTA}{Style.BRIGHT}Processing Account {i}/{len(query_ids)}")

                fetch_account_data(query_id)
                fetch_mining_data(query_id)
                watch_tasks(query_id)
                upgrade_mining_machine(query_id)
            print(f"{Fore.MAGENTA}{Style.BRIGHT}{'-' * 40}")
            print_success("Completed all accounts! Waiting to start next cycle.")
            for i in tqdm(range(600, 0, -1), desc=f"{Fore.CYAN}{Style.BRIGHT}Countdown", unit="s", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"):
                time.sleep(1)
            print_info("Starting next cycle...")
    except KeyboardInterrupt:
        # This will catch any Ctrl+C that wasn't caught by the signal handler
        graceful_exit(None, None)

if __name__ == "__main__":
    main()
