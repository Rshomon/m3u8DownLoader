import os
import requests
from requests.exceptions import Timeout
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


class downloader:
    """多线程下载
    """
    def __init__(self) -> None:
        self.headers = {
            'authority': 'c1v-h.phncdn.com',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
            'accept': '*/*',
            'origin': 'https://cn.pornhub.com',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://cn.pornhub.com/',
            'accept-language': 'zh-CN,zh;q=0.9',
        }
        self.proxies = {'http': f"http://{self.get_proxy()}"}

    # 获取代理地址
    def get_proxy(self):
        response = requests.get("http://www.rashomon.top:5555/random")
        return response.text

    # 检查代理 TODO:应改为协程方式
    def check_proxy(self):
        while True:
            try:
                response = requests.get("http://httpbin.org/ip",
                                        proxies=self.proxies,
                                        timeout=3)
                if response.status_code == 200:
                    print(response.text)
                    return True
                else:
                    print("代理不同")
                    self.proxies['http'] = self.get_proxy()
            except:
                self.proxies['http'] = self.get_proxy()
                print("异常")

    def show_progress(self, url):
        response = requests.get(url)
        with tqdm.wrapattr(open("video/" + url.split('?')[0].split('/')[-1],
                                "wb"),
                           "write",
                           miniters=1,
                           desc=url.split('?')[0].split('/')[-1],
                           total=int(response.headers.get('content-length',
                                                          0))) as fout:
            for chunk in response.iter_content():
                fout.write(chunk)

    def get_url_lit(self):
        with open("video_url.txt", 'r') as f:
            url_list = f.readlines()
            return url_list[:5]

    def downloader(self, url_list=""):
        if url_list == "":
            url_list = self.get_url_lit()
        else:
            url_list = url_list
        url_list = self.get_url_lit()
        with ThreadPoolExecutor(max_workers=20) as pool:
            for url_item in url_list:
                pool.submit(self.show_progress, url_item)


if __name__ == "__main__":
    if not os.path.isdir("video"):
        os.mkdir("video")
    d = downloader()
    # d.downloader()
    d.check_proxy()
    # print(d.proxies)