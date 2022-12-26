# 라즈베리파이 vscode-server 개발기 #4

## 0. 개요

저번 시간에 ip 고정과 포트포워딩까지 마쳤다. 이제 보안 연결만 하면 언제 어디서나 쾌적하고 안전하게 코딩이 가능하다!! ~~ipad로 어떻게든 꿀빠려고 노력중~~

## 1. ~~nginx 설치~~

> 설치
```py
sudo apt install nginx

sudo systemctl start nginx.service

sudo systemctl start nginx.service
# code-server과 동일하다. stop도 가능
```
start한 이후 status로 확인했을 때 active 상태이면 전에 vscode-server 접속할 때 썼던 ip, 즉 라즈베리파이의 ip에다 80번 포트를 붙여서 접속하면 

<img width="963" alt="image" src="https://user-images.githubusercontent.com/68508521/205314760-b5942a3a-5b7c-4fe4-9214-0cd53334aeab.png">

이런식으로 연결이 원활함을 확인할 수 있다. 굳이 ip로 접속하지 않아도 `netstat -lntp` 를 통해서 80번 포트가 listen되고 있으면 원활하다는 것을 알 수 있다. 

** 수정
일반적으로 소개하는 방법은 다음과 같았다.  

> 외부 도메인 -> nginx(+ssl 암호화) -> 내 로컬 웹 서버

client가 내 웹 서버로 연결된 "도메인"에 접속할 경우, 이 접속 요청이 내 웹 서버에 직접 전달되는 것이 아니라 nginx를 거쳐서 전달되게 된다.

```py
server {
    listen 80;
    # client가 접속을 요청한 domain
    server_name www.example.com example.com;

    location /blog {
        # 내 local web 서버 주소
        # 내 경우는 http://ip주소:포트명 꼴로 생김
       proxy_pass http://node1.com:8000/wordpress/;
    }
}
```
https를 위한 암호화는 nginx에서 진행한다. 하지만 이 방법의 치명적인 단점은 바로 도메인이 필요하다는 것이다. 무료 도메인은 너무 쉽게 끊기거나 몇 달 주기로 손수 갱신해야한다는 문제점이 있었다. 그래서 도메인 없이, localhost 형태여도 인증서를 발급받을 수 있는 사설 인증서로 암호화하기로 했다. 

## 2. 암호화  




## Reference
- nginx 설치 : https://t-okk.tistory.com/154
- nginx 구조 : https://jjeongil.tistory.com/1490