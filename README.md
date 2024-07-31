# ASCII字符串转换工具

这是一个简单的Python脚本，用于将字符串转换为ASCII码，或者将ASCII码转换回字符串。

## 功能

- 将ASCII码列表转换为对应的字符串。
- 将字符串转换为对应的ASCII码列表。
- 支持从文件读取ASCII码或字符串，并进行转换。

## 安装

确保您的系统上安装了Python 3。然后，您可以下载或克隆此项目。

```bash
git clone https://github.com/TiramisuPS/ASCII-to-String.git
cd ASCII-to-String
```
## 使用方法
```bash
# python ascii.py --help
usage: ascii.py [-h] (-to_string | -to_ascii) [-s S] [-r R]

ASCII字符串转换工具

options:
  -h, --help  show this help message and exit
  -to_string  将ASCII码转换为字符串
  -to_ascii   将字符串转换为ASCII码
  -s S        要转换的字符串
  -r R        从文件中读取内容进行转换
```

## 转换ASCII码为字符串
```bash
python ascii.py -to_string -s '72,101,108,108,111'
```
## 转换字符串为ASCII码
```bash
python ascii.py -to_ascii -s 'Hello'
```
## 从文件转换ASCII码为字符串
假设1.txt文件包含ASCII码列表：

```bash
python ascii.py -to_string -r 1.txt
```
## 从文件转换字符串为ASCII码
假设1.txt文件包含要转换的字符串：

```bash
python ascii.py -to_ascii -r 1.txt
```
## 贡献
如果您有任何建议或想要贡献代码，请提交Pull Request或创建Issue。
