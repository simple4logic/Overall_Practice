# 라즈베리파이 개발 일지 day1

## 개요
아이패드가 가벼워서 자주 밖에 들고 다니는데, 코딩을 하고 싶어도 github이랑 자유자재로 동기화 되면서도 깔끔한 툴이 없어서 고민하고 있던 차에 vscode-server에 대해 알게 됐다. 근데 AWS로 계속 서버를 돌리기에는 아무리 개인 용도라서 비용이 거의 안든다지만 좀 신경쓰여서, 집에서 공짜로 놀고있는 라즈베리파이 두 대를 이참에 써먹어 보기로 하고 시작했다. 

## 과정

### 1. 초기화

기존에 라즈비안이 깔려있었는데, 와이파이로 연결이 참 편리하다는 점은 좋았는데 문제는 내부 패키지를 뭐 잘못건드린건지 apt-get update가 도저히 안된다. 이리저리 뜯어고쳐도 ping google.com 조차 안돼서 진짜 골치 아팠다. 경험상 리눅스 계열은 패키지 하나 잘못 건드려서 의존성이라던가 뭐가 꼬이면 도저히 고칠 수가 없어서 그냥 밀어버리고 새로 시작하기로 했다.  

OS 선택은 우분투 서버로 선택! 라즈베리파이로 서버를 상시 열고, 밖에서 접속하는 것이 목표이기 때문에 최대한 가벼운 OS를 선택했다. 라즈비안은 안좋은 기억밖에 없어서... 인터넷 상의 imager 툴 아무거나 집어서 sd카드에 리눅스 서버를 구웠다.

### 2. OS 설치 및 연결

OS를 밀고 설치한 것까진 좋은데 문제는 라즈베리파이와 모니터를 연결할 케이블이 없다는 거였다. 이전에는 어떻게 연결했는지 도저히 기억이 안나는데 어떻게 했지? 그래서 방법을 찾아본게 SSH였다. 근데 항상 불안한 예감은 들어맞았는데, 파일 설정에 와이파이 정보 몇개를 까딱해놓는다고 리눅스가 부팅하자마자 자동적으로 와이파이에 순순히 연결될 것 같지가 않았다. 혹시나 해서 시도해봤는데 당연히 실패.  

다음 방법은 그나마 가능성 있는 usb-uart, 즉 시리얼 통신. 오랜만에 옛날 기억 되살려서 tx-rx 교차로 연결하고, port 찾아서 putty로 연결했다. 여러번 시도했는데 계속 알수없는 usb 장치라고 뜨면서 인식을 못하길래, 예전에 플젝할 때 썼던 usb_uart 모듈 뒤적뒤적거리다가 새로 교체해서 연결했더니 어찌어찌 연결에 성공했다.  

마지막 난관은 기껏 시리얼 통신에 성공했는데 글자가 다 뭉개진다는 거였다. 이건 쉽게 해결했는데, 라즈비안과 우분투의 baud-rate이 좀 다른가보다. 분명 이전에는 11520으로 통신했는데 9600으로 통신해야 문제가 안 발생했다. 

### 3. wi-fi 연결

매번 시리얼 통신으로 할 수도 없는 노릇이다. 다행히 가장 큰 난관인 최초 연결에 성공했으니, 이제 시리얼 통신 없이도 ssh를 통해 접속할 수 있도록 wi-fi를 설정해주기로 했다. 다음과 같은 절차를 밟았다.  

> 무선랜 인터페이스 확인
```
iw dev
```
해당 명령어를 통해 Interface 옆에 뜨는 모듈 명을 확인하면 된다. 라즈베리파이 4에는 일반적으로 wlan0 모듈이 들어가있다고 보면 된다.  

> 무선랜 인터페이스 활성화  
```
sudo ip link show wlan0
```
현재 무선랜 카드의 상태를 확인한다. 상태가 비활성화 되어있으면 중간에 `state DOWN mode ~` 라고 뜬다. 그 경우 다음을 통해 활성화 한다.
```
sudo ip link set wlan0 up
```
다시 show를 통해 확인해보면, `state UP mode ~`으로 바뀐 것을 볼 수 있다. 이때 mode 뒤에 DEFAULT가 뜰 수도 있고 DORMANT가 뜰 수도 있는데 신경쓰지 않아도 된다.

> 연결 상태 확인
```
iw wlan0 link
```
현재 네트워크에 연결되어 있는지 확인할 수 있다. 연결되어 있지 않으면 `Not connected.`라고 뜬다. 연결되어 있으면 `Connected to '연결된 네트워크 정보'`가 뜬다.

> 와이파이 스캔
```py
# 공개된 경우 (비번 없는 와이파이)
iw wlan0 scan
sudo iw dev wlan0 connect "공개된 네트워크 명"
```
```py
# 공개되어 있지 않은 경우 (비번 있는 와이파이)
iw wlan0 scan
sudo wpa_passphrase "SSID" > wpa_supplicant.conf
"wifi-password" # 개행하고 바로 입력하면 된다
```
이때 모든 입력 시에 ""는 생략하고 입력해야한다. 그리고 SSID는 와이파이 이름이다.  

연결되는데는 잠깐 시간이 걸린다. 이후 다시 iw wlan0 link를 통해서 연결이 되었는지 확인할 수 있다. 

> reference  

- https://meyouus.tistory.com/138
- https://hiseon.me/linux/command/linux-wifi-command-line/

### 4. 최초 설정

이제 wifi에 무사히 연결했으니 기본적인 패키지 업데이트를 해주고, code-server를 설치한다.

```py
#기본적인 패키지 업데이트
sudo apt-get update
sudo apt-get upgrade

#code-server 설치
curl -fsSL https://code-server.dev/install.sh | sh
```