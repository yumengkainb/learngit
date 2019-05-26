from urllib.robotparser import  RobotFileParser

rp=RobotFileParser()
rp.set_url('https://github.com//robots.txt')
rp.read()
print(rp.can_fetch('*','https://github.com/yumengkainb/learngit'))
