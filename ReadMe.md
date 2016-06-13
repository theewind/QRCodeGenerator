使用说明
===
主要是依赖qrcode，具体参考[https://pypi.python.org/pypi/qrcode/5.1](https://pypi.python.org/pypi/qrcode/5.1)，qrcode又依赖Pillow。

目前比较简单，就是针对输入的input目录，将二维码生成到output目录中。

安装
----
1. pip install Pillow
2. pip install qrcode
3. python  ./ant_qrcode.py

如果安装出现权限的问题，可以通过暴力添加sudo pip ....执行。


