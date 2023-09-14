import json
import requests
import wordcloud
import random
import time
import re
import jieba

# 随机产生请求头
# ua = UserAgent(verify_ssl=False, path='D:/Pycharm/fake_useragent.json')
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36",
    "Cookie": "i-wanna-go-back=-1; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; LIVE_BUVID=AUTO5216539051785441; buvid4=BF640363-932C-9859-2DEB-9D5332BED8BA14521-022050118-RBQaCti2N%2FgbXXvSImVESA%3D%3D; buvid3=EA6B6EE5-CF42-44F0-8BF1-0E035F5182C9167646infoc; DedeUserID=506881997; DedeUserID__ckMd5=6816981dbd4223e9; CURRENT_FNVAL=4048; rpdid=|(u))kRlJJ)u0J'uYY)l~u)~J; CURRENT_QUALITY=80; hit-new-style-dyn=1; CURRENT_PID=150df130-cdea-11ed-9e61-390f799e5bb1; _uuid=68159E9C-3BA8-49EE-A1C6-D7E510610D865E40530infoc; nostalgia_conf=-1; b_ut=5; FEED_LIVE_VERSION=V8; hit-dyn-v2=1; home_feed_column=5; browser_resolution=1530-712; header_theme_version=CLOSE; fingerprint=93340026c1ba350713aeadf8766000e1; SESSDATA=5c25a608%2C1709466512%2Cc7e4b%2A92gDhsEFKTVzRobJkJtk9Sk1ph71ufczEtnhZVk3UyXcKE4ChKGDta46HuRUO_g-u_Rbl2OgAAYQA; bili_jct=37f8d40c6076352e8e44a85bbbeb65a4; sid=7px9659x; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQxODU3MzksImlhdCI6MTY5MzkyNjUzOSwicGx0IjotMX0.ek0FRkjhs25UswbCHtI0R25Otecvf_5FppkCkYoDMCE; bili_ticket_expires=1694185739; PVID=3; b_nut=100; buvid_fp=93340026c1ba350713aeadf8766000e1; b_lsid=109D53E510_18A6AC7C071; bp_video_offset_506881997=838254238965432390",
}
cvids = []
count_danmu = []
bvid = []
dm = []
dm_1 = []
count = []
client = requests.Session()
client.headers.update(headers)
result = []
file_1 = "弹幕字符串06.txt"
file_2 = "弹幕出现次数06.txt"
file_3 = "弹幕字符串（不去重）06.txt"
word_count = {}
def search_bvid(num, search_key):  ##获取bvid号
    url = "https://search.bilibili.com/all?vt=77103137&keyword=%E6%97%A5%E6%9C%AC%E6%A0%B8%E6%B1%A1%E6%9F%93%E6%B0%B4%E6%8E%92%E6%B5%B7%E3%80%81&from_source=webtop_search&spm_id_from=333.1007&search_source=3"
    headers = {
        "Cookie":"i-wanna-go-back=-1; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; LIVE_BUVID=AUTO5216539051785441; buvid4=BF640363-932C-9859-2DEB-9D5332BED8BA14521-022050118-RBQaCti2N%2FgbXXvSImVESA%3D%3D; buvid3=EA6B6EE5-CF42-44F0-8BF1-0E035F5182C9167646infoc; DedeUserID=506881997; DedeUserID__ckMd5=6816981dbd4223e9; CURRENT_FNVAL=4048; rpdid=|(u))kRlJJ)u0J'uYY)l~u)~J; CURRENT_QUALITY=80; hit-new-style-dyn=1; CURRENT_PID=150df130-cdea-11ed-9e61-390f799e5bb1; _uuid=68159E9C-3BA8-49EE-A1C6-D7E510610D865E40530infoc; nostalgia_conf=-1; b_ut=5; FEED_LIVE_VERSION=V8; hit-dyn-v2=1; header_theme_version=CLOSE; fingerprint=93340026c1ba350713aeadf8766000e1; b_nut=100; home_feed_column=5; browser_resolution=1530-712; PVID=1; SESSDATA=0302114b%2C1710070909%2Cb193f%2A92CjB_PBkiT4qt2bVCPgOFx-spTe7wzMMBKJ-PclyFB-jSaj-RdMS_MjtOcpzk5wqcglYSVm0wTUdYUkRrWjZzc1BvS2ozdU52eHpoNkRNRjgxMGZEWnM1a1hMREpNcklydUU0UDJUQjBIM25lcEY3Ukx4Sjk3ekxWSllrSXh6bWg2NEt3UTlwUGt3IIEC; bili_jct=8c8645cb335cdab6c06cff3de9ae4770; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ4Njc0MjMsImlhdCI6MTY5NDYwODIyMywicGx0IjotMX0.EpWXcudGBzl-QJe3dUHPrpneXEWBfKwKJbaGtZWI2nY; bili_ticket_expires=1694867423; buvid_fp=93340026c1ba350713aeadf8766000e1; b_lsid=3628D4101_18A926F3922; bp_video_offset_506881997=841105590435446823; sid=85fb88rc",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36",
    }
    all_video_list = []
    for i in range(1, 100):
        sleep_time = random.randint(0, 2) + random.random()
        time.sleep(sleep_time)
        search_result = client.get(
            url="https://api.bilibili.com/x/web-interface/search/type",
            headers=headers,
            params={"search_type": "video", "keyword": search_key, "page": i},
        )
        # print(search_result.text)
        search_result = search_result.json()
        result = search_result["data"]["result"]
        for i in range(0, len(result)):
            if result[i]["bvid"] not in bvid:
                bvid.append(result[i]["bvid"])
        if len(bvid) > num:
            break


def video_cid(bvid):  # 通过已有的bvid号解析cid号
    # print(bvid[i])
    url = (
            "https://api.bilibili.com/x/player/pagelist?bvid=" + str(bvid) + "&jsonp=jsonp"
    )
    video_logo = requests.get(url=url, headers=headers)
    # print(video_logo.text)
    video_name = video_logo.text
    name = json.loads(video_name)
    cid = name["data"][0]["cid"]
    return cid


def words(content_list):
    for j in content_list:
        if j not in dm:
            dm.append(j)
        idx = dm.index(j)
        if idx > len(count) - 1:
            count.append(1)
        else:
            count[idx] += 1
        for i in range(0, len(dm)):
            with open("弹幕字符串_1.txt", mode="a", encoding="utf-8") as f:
                f.write(dm[i])
                f.write("\n")
        for i in range(0, len(count)):
            with open("弹幕出现次数_1.txt", mode="a", encoding="utf-8") as f:
                f.write(str(count[i]))
                f.write("\n")


def create_Word_cloud_diagram(content_list):  # 做词云图
    f = open(file_2, encoding="utf-8")
    txt = f.read()
    txt_list = jieba.lcut(txt)
    string = " ".join(txt_list)
    wc = wordcloud.WordCloud(
        width=500, height=500, background_color="white", font_path="msyh.ttc", scale=15
    )
    wc.generate(string)
    wc.to_file("最终章_1.png")
    # print(count)
    # print(dm)


def get_words(n):  # 通过cid号来爬取弹幕
    for i in range(0, n):
        sleep_time = random.randint(0, 2) + random.random()
        time.sleep(sleep_time)
        cvids.append(video_cid(bvid[i]))
        print(len(cvids))
        url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=' + str(cvids[i])
        headers = {
            "user-agent": "Mozilla/5.0 .(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.289 Safari/537.36",
            "Cookie": "i-wanna-go-back=-1; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=0; LIVE_BUVID=AUTO5216539051785441; buvid4=BF640363-932C-9859-2DEB-9D5332BED8BA14521-022050118-RBQaCti2N%2FgbXXvSImVESA%3D%3D; buvid3=EA6B6EE5-CF42-44F0-8BF1-0E035F5182C9167646infoc; DedeUserID=506881997; DedeUserID__ckMd5=6816981dbd4223e9; CURRENT_FNVAL=4048; rpdid=|(u))kRlJJ)u0J'uYY)l~u)~J; CURRENT_QUALITY=80; hit-new-style-dyn=1; CURRENT_PID=150df130-cdea-11ed-9e61-390f799e5bb1; _uuid=68159E9C-3BA8-49EE-A1C6-D7E510610D865E40530infoc; nostalgia_conf=-1; b_ut=5; FEED_LIVE_VERSION=V8; hit-dyn-v2=1; home_feed_column=5; browser_resolution=1530-712; header_theme_version=CLOSE; fingerprint=93340026c1ba350713aeadf8766000e1; SESSDATA=5c25a608%2C1709466512%2Cc7e4b%2A92gDhsEFKTVzRobJkJtk9Sk1ph71ufczEtnhZVk3UyXcKE4ChKGDta46HuRUO_g-u_Rbl2OgAAYQA; bili_jct=37f8d40c6076352e8e44a85bbbeb65a4; sid=7px9659x; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQxODU3MzksImlhdCI6MTY5MzkyNjUzOSwicGx0IjotMX0.ek0FRkjhs25UswbCHtI0R25Otecvf_5FppkCkYoDMCE; bili_ticket_expires=1694185739; PVID=3; b_nut=100; buvid_fp=93340026c1ba350713aeadf8766000e1; b_lsid=109D53E510_18A6AC7C071; bp_video_offset_506881997=838254238965432390",
        }
        response = requests.get(url, headers)
        response.encoding = "utf-8"
        content_list = re.findall('<d p=".*?">(.*?)</d>', response.text)
        for j in content_list:
            if j not in word_count.keys():
                word_count[j]=1
            else:
                word_count[j]+=1
            with open(file_3,mode="a", encoding="utf-8") as f:
                f.write(j)
                f.write("\n")
    for i in word_count.keys():
        with open(file_1, mode="a", encoding="utf-8") as f:
            f.write(i)
            f.write("\n")
    for i in word_count.values():
        with open(file_2, mode="a", encoding="utf-8") as f:
            f.write(str(i))
            f.write("\n")
    with open(file_3, mode="a", encoding="utf-8") as f:
        f = open(file_3, encoding='utf-8')
        txt = f.read()
        txt_list = jieba.lcut(txt)
        string = ' '.join(txt_list)
        wc = wordcloud.WordCloud(
            width=500,
            height=500,
            background_color='white',
            font_path='msyh.ttc',
            scale=15
        )
        wc.generate(string)
        wc.to_file('最终章.png')
search_bvid(300, "日本核污染水排海")
get_words(300)
word_count=sorted(word_count.items(),key=lambda x: x[1],reverse=True)

cnt = 0
for i in word_count:
    print(i[0])
    cnt += 1
    if cnt >20:
        break
