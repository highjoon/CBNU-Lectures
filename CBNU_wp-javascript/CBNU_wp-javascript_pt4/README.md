# 1. 과제 내용 설명
9주차 강의를 통해 배우게 된 <br>
주소 검색 API 이용법을 응용하여 <br>
5주차 과제의 레이아웃을 업그레이드하는 과제입니다. <br>

<a href="#"><img src="./images/Example.png" width="400px" height="500px" alt="Original_Image"></a>

# 2. 주요 코드 설명
카카오맵 API를 적용하였고 <br>
전체적인 UI 디자인과 레이아웃 구성을 업그레이드 했습니다.<br><br>

1. **서울특별시 소개 및 홍보 사이트를 컨셉으로 업그레이드.**
    - 메인 배너 이미지 교체, 확장.
        - <a href="#"><img src="./images/main.png" width="400px" height="300px" alt="seoul_night"></a>
        - ```background-attachment: fixed;``` 적용하여 스크롤에 상관없이 고정되도록 설정.
    <br><br>
    - 관광명소 : 경복궁, 청와대, 롯데타워.
        - 각 이미지에 hover 시 이미지 확장 효과 부여.
        - 카카오맵 API를 적용하여 각 관광명소의 지도 추가.
    <br>
2. **전반적인 레이아웃 재조정 및 세부사항 수정.**
    - Grid 템플릿 재조정.
        - ``` header header .; ```
        - ``` main main main; ```
        - ``` section section section; ```
        - ``` aside aside aside; ```
        - ``` content content content; ```
        - ``` footer footer footer; ```
    - 시각 효과를 위해 폰트 교체.
        - Noto Sans KR
        - Exo 2
        - 구글폰트에서 import url 적용.
    - 가상요소 사용.
        - ``` main .mainTitle .view:after {content: ''; ...}  ```
3. **9주차 강의내용 반영.**
    - 카카오 Developers에서 Web Domain 추가 후 JavaScript 키를 부여받아 카카오맵 API 적용.
        - map.js 일부 내용
        - ```const gbk = document.getElementById('gbk_map');```
        - ``` const gbk_location = {center: new kakao.maps.LatLng(37. 57983009596175, 126.97703822416157),level: 3}; ```
        - ``` const gbk_map = new kakao.maps.Map(gbk, gbk_location);```
        - ``` let gbk_mapTypeControl = new kakao.maps.MapTypeControl(); ```
        - ``` gbk_map.addControl(gbk_mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT); ```
        - ``` let gbk_zoomControl = new kakao.maps.ZoomControl(); ```
        - ``` gbk_map.addControl(gbk_zoomControl, kakao.maps.ControlPosition.RIGHT); ```
    - 각 Grid 속의 사진이 마우스를 갖다대면 (hover) 크기가 커지는 효과 수정.
        - ``` transition-duration: 1s;  ```
        - ``` ~:hover { transform: scale(1.2); opacity: 1; z-index: 1;}```
# 3. 결과

<a href="#"><img src="./images/sample.png" width="500px" height="700px" alt="Final_Image"></a>
