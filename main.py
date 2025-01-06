# -*- coding: UTF-8 -*-
# author:      Liu Kun
# email:       liukunup@outlook.com
# timestamp:   2025/01/05 23:44:00
# description: 上传文件到七牛云

import argparse
from src.qiniu import QiniuHandler


def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ak', type=str, required=True)
    parser.add_argument('--sk', type=str, required=True)
    parser.add_argument('--bucket', type=str, required=True)
    parser.add_argument('--image', type=str, required=True)
    return parser.parse_args()


if __name__ == '__main__':
    # 解析命令行参数
    args = args_parser()
    # 上传镜像文件
    handler = QiniuHandler(args.ak, args.sk, args.bucket)
    handler.create()
    handler.upload(args.image)
