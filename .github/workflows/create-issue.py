import sys
import json

if __name__ == "__main__":
    request = sys.argv[1]
    sec = sys.argv[2]
    print(request)
    print(sec)
    
    try:
        # 解析 JSON 字符串
        data = json.loads(request)
        print("Parsed JSON:", data)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
        
        
    print(data["issue"]["title"])