import requests
from twilio.rest import Client


# 访问接口获取天气预报信息，返回消息
def get_weather(name, location):


    # 设置心知天气的apikey
    apikey = "--此处为私钥--"
    url = "https://api.thinkpage.cn/v3/weather/daily.json?key=%s&location=%s&language=zh-Hans&unit=c&start=0&days=5" % (apikey, location)
    res = requests.get(url)
    res_json = res.json()

    # 构造消息字符串
    location = res_json["results"][0]["location"]
    location_str = "早上好，%s，你现在在%s" % (name, location["name"])
    weather_today = res_json["results"][0]["daily"][0]
    weather_today_str = "\n今天是%s，白天%s，晚上%s，最高气温%s，最低气温%s" % (
    weather_today["date"], weather_today["text_day"], weather_today["text_night"], weather_today["high"], weather_today["low"])
    message = location_str + weather_today_str

    # 判断今天是否有雨
    code_day = int(weather_today["code_day"])
    if(code_day >= 10):
        text_care = "\n今天有雨，请不要忘记带上雨伞哦"
        message += text_care

    # 返回结果
    return message

# 发送短信
def send_sms(phone, message):

    # 设置twilio账户信息
    twilio_account_sid = "--twilio_account_sid--"
    twilio_auth_token = "--twilio_auth_token--"
    client = Client(twilio_account_sid, twilio_auth_token)

    # 发送短信的指令
    client.messages.create(to=phone, from_="--twilio_phone--", body=message)

# main函数
if __name__ == "__main__":
    name = "--你的名字--"
    phone = "--你的电话--"
    location = "shanghai"
    message = get_weather(name, location)
    send_sms(phone, message)
