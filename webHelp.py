# coding:utf-8
import urllib
import http.cookiejar
import json

class MyWeb(object):
    def httpSendUrl(self, url, params, headers):
        if params:
            _params = urllib.parse.urlencode(params).encode(encoding='UTF8')
        else:
            _params = None
        req = urllib.request.Request(url, _params, headers)
        r = urllib.request.urlopen(req)
        html = r.read()
        return html.decode("utf-8")

    def httpGetUrl(self, url, headers):
        return self.httpSendUrl(url, None, headers)

    def httpPostUrl(self, url, paras, headers):
        return self.httpSendUrl(url, paras, headers)


if __name__ == "__main__":
    web = MyWeb()

    url = "https://search.damai.cn/search.html?tn=%E5%84%BF%E7%AB%A5%E4%BA%B2%E5%AD%90&cty=%E5%8D%97%E4%BA%AC&order=1"
    hearders = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                }
    xxx = web.httpGetUrl(url,  hearders)
    print (xxx)
