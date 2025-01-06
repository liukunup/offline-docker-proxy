# -*- coding: UTF-8 -*-
# author:      Liu Kun
# email:       liukunup@outlook.com
# timestamp:   2025/01/05 12:00:00
# description: __init__.py


class AbstractObjectStorageHandler:

    def __init__(self, access_key, secret_key, bucket):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket = bucket

    def create(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in the subclass.")

    def upload(self, localfile):
        raise NotImplementedError("This is an abstract method and needs to be implemented in the subclass.")

    def download(self, key):
        raise NotImplementedError("This is an abstract method and needs to be implemented in the subclass.")
