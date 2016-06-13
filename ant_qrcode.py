#!/usr/bin/python  
# -*- coding:utf8 -*-  

import os
import shutil
import qrcode

def generatorQrcode(inPath, outPath):
    BASE_DIR = os.path.dirname(__file__)
    IN_DIR = BASE_DIR + '/' + inPath
    OUT_DIR = BASE_DIR + '/' + outPath

    # 删除qrcode,并创建
    if os.path.exists(outPath):
        shutil.rmtree(outPath)
    os.mkdir(OUT_DIR)

    files = os.listdir(IN_DIR)
    for f in files:
        path = IN_DIR + '/' + f
        if (os.path.isfile(path)):
            name = os.path.splitext(f)[0]
            info = open(path).read()

            # 生成二维码
            img = qrcode.make(info)
            img.save(OUT_DIR + '/' + name + '.png')

if __name__ == '__main__':
    generatorQrcode('input', 'output')
    print 'ok! done!'