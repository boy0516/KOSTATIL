# https구성하기

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

