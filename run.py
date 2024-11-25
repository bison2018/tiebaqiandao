import time  
import subprocess  
import os  

# 获取当前文件夹的路径  
current_folder = os.path.dirname(os.path.abspath(__file__))  
# 拼接出 a.py 的完整路径  
script_path = os.path.join(current_folder, "tieba.py")  

if __name__ == "__main__":  
    while True:  
        # 执行指定的 a.py 文件  
        try:  
            subprocess.run(["python", script_path], check=True)  
            print(f"成功执行 {script_path}。")  
        except subprocess.CalledProcessError as e:  
            print(f"执行 {script_path} 失败，错误信息：{e}")  

        # 暂停程序 24 小时  
        time.sleep(86400)  # 86400 秒 = 24 小时