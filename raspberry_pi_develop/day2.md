# 라즈베리파이 vscode-server 개발기 #2

## 0. 개요
1일 차에 OS 설치 및 wi-fi 연결까지 진행했고, 이제 본격적인 code-server 설치를 진행하려 한다.

## 1. 최초 설정

기본적인 패키지 업데이트를 해주고, code-server를 설치한다.

```py
#기본적인 패키지 업데이트
sudo apt-get update
sudo apt-get upgrade

#code-server 설치
curl -fsSL https://code-server.dev/install.sh | sh
```

## 2. 방화벽 설정

로컬 환경뿐만이 아니라 외부에서도 접속을 허용하려면, 방화벽 설정을 허락해야할 필요가 있다. 그전에!! 먼저 방화벽을 활성화 해야한다. 

방화벽을 설정 안하면 외부에서의 접속 시도에 노출되기 때문에 시리얼 통신으로만 진행하는게 아닌 이상 방화벽 설정을 꼭 해줘야한다. 특히 22번 포트는 ssh의 기본 포트로, 해외에서 brute-force로 무자비하게 진입을 시도한다고 하니 가급적이면 막아주고 다른 포트를 이용해서 통신하다.

***주의점 -> wi-fi로 연결 중이면 방화벽 기본 rule이 모든 포트를 차단하는 것이라서 끊길 수 있다. 만약 연결 수단이 wi-fi 밖에 없다면 주의해야한다. 방화벽 설정에서 미리 ssh 통신을 위한 포트를 허용해놓고, 그 다음 enable 시키면 된다.

> 방화벽 활성화/비활성화
```py
#활성화
sudo ufw enable

#비활성화
sudo ufw disable

#상태 확인
sudo ufw status
```
> 일부 포트 허용
```py
#22번 포트 허용 - tcp, udp 둘 다 허용
sudo ufw allow 22
```

라즈베리파이와의 통신을 제외하고도, 라즈베리파이에서 띄우는 서버에 접속하기 위해서는 포트가 열려있어야 하므로 다른 서버를 위한 포트를 할당할 때 방화벽에서도 잊지말고 포트를 허가해줘야 한다.

## 3. 접속 포트 변경

모든 ssh 접속의 default 포트는 22이기 때문에 광범위하게 접속 시도가 가장 많고 위험한 포트가 22이다. 따라서 ssh 접속 포트를 다른 것으로 바꾸는 것이 좋다. 

```py
>> sudo vi /etc/ssh/sshd_config

# port 1234, 5678로 변경
Port 1234
Port 5678
```

접속 포트를 바꾸고, 방화벽에 새로 추가한 두 포트를 allow 시키면 된다. 한 개만 추가해도 무방.


## 4. code-server 실행

이제 실행만 하면 된다.

> systemd에 의한 상시 실행
```py
# 리부팅해도 자동 실행 **ubuntu에는 username이 들어가야함 이하동문
sudo systemctl enable --now code-server@ubuntu

# 1회만 실행 -> ctrl+z 시에 즉시 정지
code-server
```
해당 명령어를 실행하면 code-server을 위한 서버가 실행된다.

> 기타 명령어
```py
#현재 실행 중인 서버 확인
netstat -lntp

#변경사항 있을 경우 재시작
sudo systemctl restart --now code-server@ubuntu

#프로세스 정지
sudo systemctl stop --now code-server@ubuntu

#현재 프로세스 상태
sudo systemctl status --now code-server@ubuntu
```

![image](https://user-images.githubusercontent.com/68508521/205282297-a4924c05-97f1-436a-b8e3-8d712991e49c.png)

이 상태는 active라고 불이 들어왔긴 한데 제대로 실행이 안되는 상태다. 

![image](https://user-images.githubusercontent.com/68508521/205282429-f13bc013-aaa7-4025-8163-cae28d1003b7.png)

이 상태가 되어야 제대로 서버가 실행되고 있는 상태이다. 서버에 접속은 할 수 있지만 비밀번호를 먼저 확인해야한다.

> 비밀번호 확인 및 포트 설정
```py
vi ~/.config/code-server/config.yaml
```
해당 설정에서 기본적으로 bind-addr는 127.0.0.1:8080이 기본값인데 이를 0.0.0.0:(원하는 포트값)으로 설정해주면 된다. 그리고 비밀번호도 추가로 바꾸어 주면 기본적인 설정은 모두 끝난다. 이제 웹 주소창에

> (현재 라즈베리파이가 접속 중인 wifi의 ip):포트번호  

를 치면 vscode-server에 연결할 수 있다.

### 주의점

직접 삽질하면서 알아낸 것들이다.  

1. username 주의  
`sudo systemctl restart --now code-server@ubuntu` 명령어에서, ubuntu는 현재 라즈베리파이에 접속한 user명이다. user명이 ABC이면 `@ABC`로 바뀌어야 한다. 이 때문에 다른 블로그에서 코드를 참고할 때는` @$USER` 처럼 되어있는 경우가 있는데, 만약 내가 root에 접속해있을 경우에는 username이 root으로 바뀐다(whoami로 질문 시)... 그래서 ubuntu로 server을 run하고, root로 또 서버를 돌리려고 하면 충돌이 생긴다. 따라서 $USER말고 그냥 자기 계정 이름 넣어두거나 root 진입한 상태로 돌리지 말자.

2. config.yaml 설정 시 종료  
서버는 상시로 돌아가고 있기 때문에, config.yaml을 서버를 내리지 않고 수정하면 제대로 저장이 되지 않아서 swp파일이 생길 수도 있다. 따라서 수정하기 전에 stop으로 서버를 잠깐 멈추고, 수정이 끝나면 다시 실행시키도록 하자.
