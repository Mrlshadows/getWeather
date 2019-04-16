# getWeather
> Python环境为 python3

## 两个API
注册后即可使用免费版本的服务
- 心知天气
> https://www.seniverse.com/

- twilio
> https://www.twilio.com/

twilio记得要在控制台获得一个手机号才能设置相应的信息。

## 安装twilio
终端执行如下指令：
```
pip3 install twilio
```
## 运行脚本
编辑脚本更改将值对应修改：
```
# 设置心知天气的apikey
apikey = "--此处为私钥--"

# 设置twilio账户信息
twilio_account_sid = "--twilio_account_sid--"
twilio_auth_token = "--twilio_auth_token--"

# 发送短信的指令
client.messages.create(to=phone, from_="--twilio_phone--", body=message)

# 编辑接收人的信息，国内电话记得加 +86
name = "--你的名字--"
phone = "--你的手机号--"
location = "shanghai"
```
修改后终端运行该脚本：
```
python3 get_weather.py
```
运行成功后片刻你的手机便收到短信了。
## 定时执行脚本
MacOS和linux都可以使用crontab达到此效果。
终端运行指令：
```
crontab -e
```
此时进入了vim编辑器的界面。
举个例子，我想要每天早上6点钟收到天气的消息，编辑器内输入内容为：
```
# 第一列为执行脚本的分钟数
# 第二列为执行脚本的小时数
# 第三列为执行脚本的日，* 为通配符，表示全部
# 第四列为执行脚本的月，* 为通配符，表示全部
# 第五列为执行脚本的星期，* 为通配符，表示全部
# 第六列为到达条件后要执行的命令
0 6 * * * python3 脚本的路径/get_weather.py
```
保存后退出，提示terminal要获得全部权限，是
terminal显示已经安装
## 检验定时器是否添加成功
终端输入如下指令：
```
crontab -l
```
若是终端输出显示了你编辑的命令即添加成功
## 提示
#### 给非注册twilio的手机号发短信
需要进入控制台设置。
> 点击网页右边蓝色的链接  verified numbers。
> 添加相应的手机号
> 手机号语音认证或手机验证码认证
#### 睡眠状态后crontab失效
睡眠状态后crontab不再定时执行脚本。
## 总结
写代码也可以进行资源整合，实现相应的功能，达到预期的目标即可。代码改变世界。
## 参考
https://zhuanlan.zhihu.com/p/22273281
https://www.linuxidc.com/Linux/2014-01/95612.htm