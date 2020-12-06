# How to debug

- No checking code with printing statement
- We can just use debugging especially in vscode.
- special thanks to (https://www.youtube.com/watch?v=w8QHoVam1-I)

### vscode debug
- python debug의 debug 창을 activate 시켜서 사용
- 설정에 현재 보고 있는 파일을 디버깅하는 것으로 .vscode에 launch.json 파일에 {$file} 이런식으로 넣어준다.
- 본격적으로 시작

#### 활용
- 시작 (F5)
    - 디버깅을 시작한다. 파이썬 파일을 켜두어야한다.
- breaking point
    - editor창에의 line number 옆에 커서를 대면 빨간색 포인트를 찍을 수 있다.
    - 찍은 포인트에서 debug가 실행되서 멈추게 된다.
- check the value of variables
    - 왼쪽 디버그 창에서 vscode라면 값을 확인할 수 있다.
    - global과 local variable로 나누어진다.
- call stack
    - 코드 실행시 실행되는 라인의 상위 class와 func을 call stack으로 확인 할 수 있다.
- watch
    - 코드에서 원하는 variable이나 func이름을 블럭해서 마우스 오른쪽 키를 누르면 watch 창에서 현재 값 확인
    - breaking point에서 찍어둔 var이 아니여도 바로 확인가능하여 편하다

## 번외

### Shell 사용
- shell로 사용할려면 매우매우 귀찮다.
- python -m gdb file.py로 gdb창을 켜서 사용
- 쉘 조작으로 실시하는 디버깅이라 답답한 면이 조금 있다
### inline 활용 (import gdb)
- gdb를 import 해서 함수로 디버깅을 확인하는 방법
- 매번 변경해야해서 별로임