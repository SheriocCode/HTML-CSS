import os
import json
import time
import requests
from pathlib import Path

json_file = Path('frontend_1.json')
if not json_file.exists():
    raise SystemExit('videos.json 不存在！')
with json_file.open(encoding='utf-8') as f:
    data = json.load(f)

def extract_url(raw):
    """从 <url>...</url> 里抠出真正的 http 地址"""
    # try:
    #     return raw.split('>')[1].split('<')[0].strip()
    # except Exception:
    #     return None
    return raw

def download(url, path, timeout=10, retries=3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://www.bilibili.com'
    }
    for i in range(retries):
        try:
            r = requests.get(url, headers=headers, stream=True, timeout=timeout)
            r.raise_for_status()
            with open(path, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            return True
        except Exception as e:
            print(f"[{i+1}/{retries}] 下载失败：{e}，{url}")
            time.sleep(2)
    return False

# 初始化
out_dir = Path('pics')
out_dir.mkdir(exist_ok=True)
index = {}

for item in data:
    aid = item['aid']
    raw_pic = item['pic']
    url = extract_url(raw_pic)
    if not url:
        print(f"⚠️ 无法解析 {aid} 的图片地址")
        continue
    suffix = Path(url).suffix or '.jpg'
    file_name = f"{aid}{suffix}"
    file_path = out_dir / file_name
    print(f"→ 下载 {aid} ...")
    ok = download(url, file_path)
    if ok:
        index[str(aid)] = url
    else:
        print(f"❌ 跳过 {aid}")

# 保存索引
with open(out_dir / 'index.json', 'w', encoding='utf-8') as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print("全部完成，索引已保存到 pics/index.json")