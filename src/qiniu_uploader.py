# -*- coding: UTF-8 -*-
# author:      Liu Kun
# email:       liukunup@outlook.com
# timestamp:   2025/01/05 23:44:00
# description: 上传文件到七牛云

import os
from src import AbstractUploader, args_parser
from qiniu import Auth, put_file, etag


class QiniuUploader(AbstractUploader):

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


if __name__ == '__main__':
    args = args_parser()
    inst = QiniuUploader(args.ak, args.sk, args.bucket)
    inst.create()
    inst.upload(args.image)