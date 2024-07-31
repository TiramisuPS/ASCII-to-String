#!/usr/bin/env python3
import argparse

def string_to_ascii(input_string):
    return ','.join(str(ord(c)) for c in input_string)

def ascii_to_string(ascii_list):
    return ''.join(chr(int(a)) for a in ascii_list.split(','))

def process_file(file_path, to_string):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if to_string:
                print(ascii_to_string(content))
            else:
                print(string_to_ascii(content))
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='ASCII字符串转换工具')
    
    # 创建互斥参数组
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-to_string', action='store_true', help='将ASCII码转换为字符串')
    group.add_argument('-to_ascii', action='store_true', help='将字符串转换为ASCII码')

    # 添加其他参数
    parser.add_argument('-s', type=str, help='要转换的字符串')
    parser.add_argument('-r', type=str, help='从文件中读取内容进行转换')

    args = parser.parse_args()

    # 检查参数组合是否有效
    if args.s and args.r:
        print("错误：只能指定-s或-r中的一个。")
        sys.exit(1)
    if not args.s and not args.r and not (args.to_string or args.to_ascii):
        print("错误：必须指定-s或-r，并且指定转换类型。")
        sys.exit(1)

    # 执行转换操作
    if args.s:
        if args.to_string:
            print(ascii_to_string(args.s))
        else:
            print(string_to_ascii(args.s))
    elif args.r:
        process_file(args.r, args.to_string)

if __name__ == '__main__':
    main()
