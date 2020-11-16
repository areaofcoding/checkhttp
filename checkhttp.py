#!/usr/bin/python3
import requests,sys
from multiprocessing import Pool
file = open(sys.argv[1])
urls = []
for url in file:
    url = url.splitlines()
    urls.append(url[0])
def banner():
    logo = '''
\t+-+-+-+-+-+-+-+-+-+ Author: CodingArea
\t|c|h|e|c|k|h|t|t|p|
\t+-+-+-+-+-+-+-+-+-+ Contact: fb.com/areaofcoding
\tUsage:python3 checkhttp.py list.txt
    '''
    print(logo)
banner()
def main(i):
    c = "\033[036m"
    w = "\033[037m"
    r = "\033[031m"
    g = "\033[032m"
    y = "\033[033m"
    p = "\033[035m" 
    try:
        # i = i.replace("https://","")
        # i = i.replace("http://","")
        # i = "http://"+i
        req = requests.get(i,allow_redirects = False,timeout = 3)
        if req.status_code in range(200,299):
            print(f"{i} [{g}{req.status_code}{w}] [{c}{req.headers['Server']}{w}]")
        elif req.status_code in range(300,399):
            reloca = req.headers["Location"]
            print(f"{i} [{y}{req.status_code}{w}] [{c}{req.headers['Server']}{w}] [{p}{reloca}{w}]")
        elif req.status_code in range(400,499):
                print(f"{i} [{r}{req.status_code}{w}] [{c}{req.headers['Server']}{w}]")
        elif req.status_code in range(500,599):
            print(f"{i} [{r}{req.status_code}{w}] [{c}{req.headers['Server']}{w}]")
        else:
            pass
    except KeyError:
        if req.status_code in range(200,299):
            print(f"{i} [{g}{req.status_code}{w}] []")
        elif req.status_code in range(300,399):
            print(f"{i} [{y}{req.status_code}{w}] [] []")
        elif req.status_code in range(400,499):
                print(f"{i} [{r}{req.status_code}{w}] []")
        elif req.status_code in range(500,599):
            print(f"{i} [{r}{req.status_code}{w}] []")
        else:
            pass
    except requests.RequestException:
        pass
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    p = Pool(50)
    final = p.map(main,urls)
    p.close()
    p.join()
