# flask로 https구성하기

pyopenssl을 통해서 파이썬에서 ssl을 구성할 수 있도록한다.

openssl을 이용해서 개인키, 인증서를 생성해서 flask 서버에 삽입해준다.



https://www.pyopenssl.org/en/stable/api/ssl.html#OpenSSL.SSL.Connection

pyopenssl설명서



- pyopenssl 이용코드

```
from OpenSSL import SSL
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('future.key')
context.use_certificate_file('future.crt')

##########################################################################################
if __name__ == '__main__':
    logger.info("Start RestAPI : listen %s:%s" % ('127.0.0.1', 8443))
    app.run(
        host='127.0.0.1',
        port=8443,
        debug = True,
        ssl_context=context,
    )
```



https://blusky10.tistory.com/352 인증서, 비밀키 생성



req명령어 오류 해결법

https://community.cisco.com/t5/wireless/fix-csr-generation-openssl-error-quot-unable-to-load-config-info/td-p/1881861



key, csr, crt파일 생성 명령어

```
openssl

genrsa -out future.pem 2048

req -new -key future.key -out future.csr -config openssl.cnf

req -x509 -days 365 -key future.pem -in future.csr -out future.pem -days 365 -config openssl.cnf
```



https://m.blog.naver.com/espeniel/221845133507

openssl 개인키 발금 ssl 인증서 생성

****

일단 돌아가긴함

- https 코드

```
from flask import Flask
from OpenSSL import SSL
# import ssl
from flask import Response, jsonify, request, render_template, redirect, url_for, make_response
app = Flask(__name__)

context = SSL.Context(SSL.SSLv23_METHOD)
cert = 'crt.pem'
pkey = 'future.pem'
context.use_privatekey_file(pkey)
context.use_certificate_file(cert)

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
# ssl_context.load_cert_chain(certfile='crt.pem', keyfile='future.pem', password='test')
# app.run(host="0.0.0.0", port=15000, ssl_context=ssl_context)



@app.route('/')
def main_page():
    
    return render_template('index.html')


app.run(host='0.0.0.0', port=443, ssl_context=(cert,pkey))
```

