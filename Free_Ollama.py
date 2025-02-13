import requests
import json
import threading
from tqdm import tqdm

# 线程锁
lock = threading.Lock()

# 要过滤的关键词列表
exclude_keywords = [":7b", ":1.5b", ":3b", ":1.8b", ":14b", ":0.5b", ":11b", ":14b", ":8b", ":1b", ":4b", ":2b", ":3.8b", ":9b", ":1.1b", ":12b", ":1.3b", ":6.7b"]

# 检查URL是否包含排除的关键词
def should_exclude(url):
    for keyword in exclude_keywords:
        if keyword in url:
            return True
    return False

# 获取model
def fetch_model(url):
    # 确保url以http://开头
    if not url.startswith("http"):
        url = "http://" + url
    
    # 拼接API路径
    api_url = url + "/api/tags"
    
    try:
        # 发起GET请求
        response = requests.get(api_url, timeout=5)
        
        # 如果响应成功且返回json数据
        if response.status_code == 200:
            data = response.json()
            
            # 遍历models
            if "models" in data:
                models = data["models"]
                for model in models:
                    # 确保每个model有name字段
                    if "model" in model:
                        model_name = model["model"]
                        with lock:
                            # 输出url和model到文件
                            with open("output.csv", "a") as f:
                                f.write(f"{url} , {model_name}\n")
    except Exception as e:
        # 请求失败不做处理
        pass

# 读取txt文件并启动线程
def main():
    with open('./urls.txt', 'r') as f:
        lines = f.readlines()

    # 创建线程池
    threads = []
    for line in tqdm(lines, desc="Processing URLs"):
        url = line.strip()
        
        # 检查是否包含排除的关键词
        if should_exclude(url):
            continue
        
        # 启动线程处理该URL
        thread = threading.Thread(target=fetch_model, args=(url,))
        thread.start()
        threads.append(thread)
    
    # 等待所有线程结束
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
