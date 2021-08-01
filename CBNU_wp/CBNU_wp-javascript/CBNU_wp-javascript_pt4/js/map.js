const gbk = document.getElementById('gbk_map');
const bh = document.getElementById('bh_map');
const lt = document.getElementById('lt_map');

const gbk_location = {
    center: new kakao.maps.LatLng(37.57983009596175, 126.97703822416157),
    level: 3
};

const bh_location = {
    center: new kakao.maps.LatLng(37.584880178283996, 126.97503929746438),
    level: 3
};

const lt_location = {
    center: new kakao.maps.LatLng(37.51318565805038, 127.10277227814534),
    level: 3
};

const gbk_map = new kakao.maps.Map(gbk, gbk_location);
const bh_map = new kakao.maps.Map(bh, bh_location);
const lt_map = new kakao.maps.Map(lt, lt_location);

let gbk_mapTypeControl = new kakao.maps.MapTypeControl();
let bh_mapTypeControl = new kakao.maps.MapTypeControl();
let lt_mapTypeControl = new kakao.maps.MapTypeControl();

gbk_map.addControl(gbk_mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);
bh_map.addControl(bh_mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);
lt_map.addControl(lt_mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

let gbk_zoomControl = new kakao.maps.ZoomControl();
let bh_zoomControl = new kakao.maps.ZoomControl();
let lt_zoomControl = new kakao.maps.ZoomControl();

gbk_map.addControl(gbk_zoomControl, kakao.maps.ControlPosition.RIGHT);
bh_map.addControl(bh_zoomControl, kakao.maps.ControlPosition.RIGHT);
lt_map.addControl(lt_zoomControl, kakao.maps.ControlPosition.RIGHT);