import requests, time, os, threading, json
os.system('title AutoVoteVN - All Code By nxhdev2002')
Lock = threading.Lock()
def work(num):
    Lock.acquire()
    print ('Starting thread #{0}'.format(str(num)))
    Lock.release()
    while True:
        headers = {
            'Content-Type': 'application/json',
            'referer': 'https://www.riddle.com/a/269406',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51',
            'x-requested-with': 'XMLHttpRequest'
        }
        payload = {
            'riddleId': 269406,
            'data': '269406.start',
            'event': 'start',
            'isFreetextAnswer': False,
            'dataV2': 'scope=1~fwd=riddleId=269406#messageType=1#commandId=1#category=core_metrics#label=start'
        }
        r = requests.post("https://www.riddle.com/embed/stats/enqueue", data=json.dumps(payload), headers=headers)


        payload = {
                'riddleId': 269406,
                'data': '269406.finish',
                'event': 'finish',
                'isFreetextAnswer': False,
                'dataV2': 'scope=1~fwd=riddleId=269406#messageType=1#commandId=1#category=core_metrics#label=finish'
            }
        r = requests.post("https://www.riddle.com/embed/stats/enqueue", data=json.dumps(payload), headers=headers)


        payload = {
                'riddleId': 269406,
                'data': '269406.36',
                'event': 'answer',
                'isFreetextAnswer': False,
                'dataV2': 'scope=1~fwd=riddleId=269406#messageType=1#commandId=1#category=answer#label=36'
            }
        r = requests.post("https://www.riddle.com/embed/stats/enqueue", data=json.dumps(payload), headers=headers)
        Lock.acquire()
        print("+1 LCV")
        Lock.release()
if __name__ == '__main__':
    thread_num = int(input("Số Thread? "))
    for i in range(thread_num):
        threading.Thread(target=work, args=(i+1,)).start()
