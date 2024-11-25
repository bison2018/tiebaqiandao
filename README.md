# tieba

百度贴吧签到脚本,每隔24小时循环运行,Python环境

## 使用方法

1. 登录 [网页版贴吧](https://tieba.baidu.com/),按F12->网络->页面刷新->选个链接,在cookie中找到找到名为 `BDUSS` 的值
2. 下载所有文件,，文件'tieba.py'中'此处填入cookie'替换为`BDUSS` 的值
3. 安装Python
4. 安装依赖: `pip install -r requirements.txt`
5. cd到文件目录python ./run.py运行, win系统可以直接点击脚本: `运行.cmd`


## 示例配置

```python

if __name__ == "__main__":
    cli = Tieba("此处填入cookie", [
        LarkChannel("<飞书 webhook>"),
```

## 支持的运行结果通知

- 飞书自定义机器人
- 企业微信机器人

