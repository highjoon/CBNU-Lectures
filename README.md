# 1. 과제 내용 설명
5주차 강의를 통해 배우게 된 <br>
CSS의 transiton, transform, animation 속성을 적용하여 <br>
4주차 과제의 레이아웃을 재구성하는 과제입니다. <br>

<a href="#"><img src="./example/Example.png" width="400px" height="500px" alt="Original_Image"></a>

# 2. 주요 코드 설명
단순히 5주차 강의 내용을 반영하는 정도에 그치지 않고 <br>
전체적인 디자인과 구성을 수정했습니다.<br><br>

1. **서울특별시 홍보 사이트를 컨셉으로 지정.**
    - 서울특별시 로고 추가.
        - <a href="#"><img src="./images/seoul_logo.png" width="400px" height="100px" alt="seoul_logo"></a>
        - <a href="#"><img src="./images/seoul_title.png" width="200px" height="100px" alt="seoul_title"></a>
    <br>
    - 메인 배너 이미지 교체.
        - <a href="#"><img src="./images/seoulnight.png" width="400px" height="300px" alt="seoul_night"></a>
    <br>
    - 각 grid에 서울 관광명소 사진과 그 부연설명 작성 및 공식홈페이지 링크 부여.
        - 추가된 관광명소는 다음과 같습니다.
            - 경복궁
            - 명동
            - 청와대
            - N서울타워
    <br>
2. **전반적인 레이아웃 재조정 및 세부사항 수정.**
    - 전체 레이아웃 크기를 80%로 조정하고 가운데배치함으로써 가독성 향상.
        - ``` width : 80%; ```
        - ``` margin : 0 auto; ```
    <br>
    - 시각 효과를 위해 폰트 교체.
        - HanS_Calli.ttf
        - seoulhangang.ttf
        - <a> https://fonts.googleapis.com/earlyaccess/nanumbrushscript.css </a>
3. **5주차 강의내용 반영.**
    - 웹페이지 실행 시 메인 배너 사진이 이동.
        - ``` transform: translate(-50%, -50%);```
        - ``` top:50%; ```
        - ``` left:50%; ```
        - ``` transition-duration: 2s; ```
    - 메인 배너 속 문구에 시각적 효과를 부여.
        - 기울임 효과 부여.
            - ``` transform: translateX(-50%) rotate(-10deg); ```
        - 반짝거림 효과 부여.
            - ``` @keyframes banner-content { from { opacity: 0; } to { opacity: 1; } } ```
            - ``` animation: banner-content 2s infinite alternate; ```
                - count : infinite, direct : alternate 를 부여하여 애니메이션이 항상 지속되도록 설정.
    - 각 Grid 속의 사진이 마우스를 갖다대면 (hover) 크기가 커지는 효과 부여.
        - ``` transition-duration: 1s;  ```
        - ``` ~:hover { transform: scale(1.1); opacity: 1; z-index: 1;}```
        - 크기가 커지는 동시에 홍보 문구와 함께 새로운 div가 보이도록 설정. (0.5의 opacity를 갖는 반투명한 div)
            - ``` transition-duration: 1s;  ```
            - ``` section>a>.bar { width: 0; height: 0; transition-duration: 1s; overflow: hidden; opacity: 0.5; background: linear-gradient(#cb60b3 0%, #db36a4 100%);} ```
            - ``` section>a:hover:.bar { width: 90%; height: 90%; } ```

# 3. 결과

<a href="#"><img src="./example/Final.png" width="400px" height="500px" alt="Final_Image"></a>