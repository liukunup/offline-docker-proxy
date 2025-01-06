# -*- coding: UTF-8 -*-
# author:      Liu Kun
# email:       liukunup@outlook.com
# timestamp:   2025/01/06 22:07:00
# description: 七牛云对象存储处理类

import os
import requests
from src import AbstractObjectStorageHandler
# 导入七牛云的相关库
from qiniu import Auth, put_file, etag


class QiniuHandler(AbstractObjectStorageHandler):

    domain = 's3.cn-east-1.qiniucs.com'

    def create(self):
        self.client = Auth(self.access_key, self.secret_key)

    def upload(self, localfile):
        if not os.path.exists(localfile):
            raise FileNotFoundError(f'File not found: {localfile}')
        if self.client:
            # 提取文件名
            key = os.path.basename(localfile)
            # 生成上传 Token，可以指定过期时间等
            token = self.client.upload_token(self.bucket, key, 3600)
            ret, info = put_file(token, key, localfile, version='v2')
            assert ret['key'] == key
            assert ret['hash'] == etag(localfile)
            return info
        else:
            raise Exception("You need to create a client first!")

    def download(self, key):
        base_url = 'https://%s.%s/%s' % (self.bucket, self.domain, key)
        private_url = self.client.private_download_url(base_url, expires=3600)
        r = requests.get(private_url)
        assert r.status_code == 200
