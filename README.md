# dgu_pc_room_management
동국대학교 컴퓨터 실습실을 관리하기 편하도록 연구한 과정을 모아놨습니다.

ubuntu-downloader.py : requests 모듈을 이용하여 인터넷에서 설치파일을 자동으로 내려받습니다.
실습실 컴퓨터 100대에 실습실 컴퓨터를 하나하나 켠 후, 브라우저를 열어서 ubuntu 홈페이지를 검색한 후, ubuntu 설치파일을 내려받는 것이 귀찮아서 만들었습니다. 설치파일이 크기 때문에 usb 를 이용하면 usb 가 많이 필요하기 때문에
google drive 를 이용하려고 했으나 컴퓨터를 기기 인증하는 절차가 복잡하여서 코드로 동작하는 매크로를 고안했습니다. embeded python 과 ubuntu-downloader.py 를  usb 에 넣은 뒤, usb 를 설치하고자 하는 실습실 pc 에 꼽고 실행시키면 자동으로 설치파일을 다운로드 받기 때문에 빠르게 작업할 수 있습니다.
get 요청으로 파일을 다운로드하는 모든 웹사이트에 적용할 수 있기 때문에 url을 수정하면 다른 파일도 다운로드 받을 수 있습니다.

레퍼런스 : r-test.py

pywin32_draw.py : win32api.py 모듈로 모니터의 특정 위치에 빨간색을 그리는 코드입니다. 설치파일 진행을 이미지 매크로로 하기 위해서 고안되었습니다.

wsl-install-test.py : 실습실 컴퓨터 100대에 wsl(윈도우 하위 리눅스 시스템)을 설치하기 귀찮아서 만든 코드입니다. os.system 모듈로 wsl install을 수행합니다.

