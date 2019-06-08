from urllib.robotparser import  RobotFileParser

rp=RobotFileParser()
rp.set_url('https://maoyan.com//robots.txt')
rp.read()
print(rp.can_fetch('*','https://maoyan.com/board/4'))
