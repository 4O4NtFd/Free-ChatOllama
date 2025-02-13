# Free Ollama

Free Ollama 是一个基于 Python 的工具，读取文本文件中的 URL 列表，向这些 URL 发送 GET 请求，并处理响应以提取模型名称。该程序会过滤掉匹配指定排除关键词的模型，并以结构化格式输出有效的模型。该工具利用多线程和进度条来提高性能和用户体验。

Free Ollama is a Python-based tool that reads a list of URLs from a text file, sends GET requests to these URLs, and processes the responses to extract model names. The program filters out models that match specified exclusion keywords and outputs the valid models in a structured format. The tool utilizes multi-threading and a progress bar to enhance performance and user experience.

## 特性 / Features

- **高效的多线程处理**：同时处理多个请求以提高性能。  
  **Efficient multi-threading**: Handles multiple requests simultaneously to improve performance.
- **排除过滤**：根据预定义的排除关键词列表自动过滤掉特定模型。  
  **Exclusion filtering**: Automatically filters out models based on a predefined list of exclusion keywords.
- **进度追踪**：使用 `tqdm` 显示进度条，跟踪处理的 URL 数量。  
  **Progress tracking**: Uses `tqdm` to display a progress bar, keeping track of the URLs processed.
- **输出到文件**：将过滤后的 URL 和模型名称写入输出文件，便于参考。  
  **Output to file**: Writes the filtered URLs and model names to an output file for easy reference.

## 安装依赖 / Requirements

- Python 3.x  
- `requests` library  
- `tqdm` library

You can install the required libraries with:

```bash
pip install requests tqdm
```
## 使用方法 / Usage
 1. 准备一个名为 urls.txt 的文件，文件中每行包含一个 URL。
Prepare a file named urls.txt containing a list of URLs, one per line.
 2. 运行脚本：
Run the script:
```bash
python free_ollama.py
```
 3. 过滤后的 URL 和其对应的模型将被保存到 `output.txt` 文件中。
The filtered URLs and their associated models will be saved in `output.txt`.
