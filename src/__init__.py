# -*- coding: UTF-8 -*-
# author:      Liu Kun
# email:       liukunup@outlook.com
# timestamp:   2025/01/05 12:00:00
# description: __init__.py

import argparse


def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ak', type=str, required=True)
    parser.add_argument('--sk', type=str, required=True)
    parser.add_argument('--bucket', type=str, required=True)
    parser.add_argument('--image', type=str, required=True)
    return parser.parse_args()


class AbstractUploader:

    def __init__(self, access_key, secret_key, bucket):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket = bucket

    def create(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in the subclass.")

    def upload(self, localfile):
        raise NotImplementedError("This is an abstract method and needs to be implemented in the subclass.")