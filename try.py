# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# ISBN书号查询 Python示例代码
if __name__ == '__main__':
    url = 'https://jmisbn.api.bdymkt.com/isbn/query'
    params = {}
    params['isbn'] = '9787115439789'

    headers = {

        'Content-Type': 'application/json;charset=UTF-8',
        'X-Bce-Signature': 'AppCode/5b984b94620f4f54be18215c8685f402'
    }
    r = requests.request("POST", url, params=params, headers=headers)
    print(r.content)
