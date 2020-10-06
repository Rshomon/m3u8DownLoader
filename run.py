import requests
import re
import sys, time


# pornhub的m3u8下载器
class m3u8DownLoader:
    def __init__(self, url: str) -> None:
        self.url = url
        # 基础地址
        self.baseurl = self.base_url()
        self.num = 0

    def base_url(self) -> str:
        """获取传入链接的主拼接地址
        """
        baseurl = re.findall(r'http.*urlset/', self.url)[0]
        return baseurl

    def readfile(self) -> object:
        """第一次读取地址内容
        """
        response = requests.get(self.url)
        # 将读出来的文本进行分段
        response_body = response.text.split("\n")
        for item in response_body:
            # 获取开头为index的字符串
            if item.startswith("index"):
                # 拼接字符串继续发送请求
                response = requests.get(self.baseurl + item)
                # print(response.text)
                # 返回响应对象
                if response.status_code == 200:
                    yield response
                else:
                    print("request error")
                    return

    def get_source_url(self, response: object) -> list:
        """

        """
        response_list = response.text.split('\n')
        # 存放目标元素
        new_response_list = []
        for index, response_list_item in enumerate(response_list):
            if not response_list_item.startswith(
                    "#") and response_list_item != "":
                new_response_list.append(response_list_item)
        return new_response_list

    def get_download_addr(self, addr_list: list):
        with open(f"{str(self.num)}.txt", 'w', encoding='utf-8') as f:
            for addr_item in addr_list:
                f.write(self.baseurl + addr_item + "\n")
        print("写入完成")
        self.num += 1

    def main(self):
        for read in self.readfile():
            addr_list = self.get_source_url(read)
            self.get_download_addr(addr_list)


if __name__ == "__main__":
    m3u8 = m3u8DownLoader(
        "https://d1v-h.phncdn.com/hls/videos/202009/16/352343302/,1080P_4000K,720P_4000K,480P_2000K,240P_400K,_352343302.mp4.urlset/master.m3u8?ttl=1601987761&l=0&clientip=149.129.43.133&hash=103dfea3188dd9e8781e1f5337b23f0c"
    )
    m3u8.main()
