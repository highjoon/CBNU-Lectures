def make_logger(tag):
    def log(msg):
        print(tag.upper() + ': ' + msg)
    return log  # 내부 함수 자체를 리턴

error_logger = make_logger('error')
info_logger = make_logger('info')
error_logger('hi~')
info_logger('Hello!!!')