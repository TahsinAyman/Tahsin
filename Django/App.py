import json
from threading import Thread
import requests
from manage import thread, main

def other():
    response = requests.get('http://127.0.0.1:6969/resturant/customer')
    data = json.loads(response.text)
    print(data)
    print(type(data))
    
if __name__ == '__main__':
    t1 = Thread(target=other)
    main()
    other()
    t1.start()