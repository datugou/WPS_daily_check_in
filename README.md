# WPS_daily_~~check_in~~_invite

配合 WPS 打卡活动，完成每日 10 人邀请任务。

***该项目不是全自动的，需要配合微信小程序，每天在手机上进行打卡。***

---
WPS 有一个免费领会员的活动，关注微信小程序“我的WPS会员”，进入首页就可以看到。

每天 6:00-13:00 在小程序上打卡就会送 1 天 WPS 会员。
参与活动后，同时关注微信公众号“WPS会员”，该公众号会每天发微信提醒你打卡。
完成邀请任务可额外获得会员天数，每邀请一位好友可多得 1 天，每天最多邀请 10 个好友。
以防该活动结束，尽可能多嫖几天会员。

本项目的作用是**自动完成邀请好友的任务**。

# 执行步骤：
1. 添加微信小程序‘我的WPS会员’，首页参加打卡活动，进入个人中心记录数字 ID
2. 右上角 Fork 该项目
3. Fork 完后会直接跳转到你的项目页面中，点击上方 Actions，开启workflow
4. 点击文件 WPS_accept_invitation.py。将第一行 'invite_userids = [ID1, ID2]' 括号中的数字改成自己的会员 ID，多个账号用英文的逗号隔开，保存修改即可

# 手机接收邀请结果：
## SERVER 酱
1. 微信关注“server 酱”，访问 http://sc.ftqq.com/?c=code ，微信登录后，在“发送消息”页面获取 SCKEY 的值。
2. 在本页面上方 Settings → Secrets 中点击 New repository secret ，Name 填写 “**SERVER_KEY**”（不带引号），Value 中填写上一步获取的 SCKEY 值。

## Bark
1. 手机下载 Bark APP（我用的 ios，Android 不知道有没有），获取推送链接（类似这个 https://api.day.app/xxxxxxxxxxxxx ）；
2. 在本页面上方 Settings → Secrets 中点击 New repository secret ，Name 填写 “**BARK_URL**”（不带引号），Value 中填写上一步获取的链接。

# 每 60 天需要重新激活一下
![](https://user-images.githubusercontent.com/30107520/108630795-9f885200-74a1-11eb-85b3-7e9386f7fa05.jpg)  

60 天不改动这个项目的文件，就会停掉 Action 的 workflow。

需要每 60 天随便改动一下 README.md 里的内容，随便改几个字然后保存。

# 其它
- 该项目基于 GitHub Action 功能实现

- 该项目每天早上 9 点自动运行，可能会晚个十几分钟；每次修改该项目中的任何文件也会自动执行一次
- 接受邀请有时会不成功，可能同一时间有很多人使用备用账号，可以在 .github/workflows/wps_dci.yml 修改每天自动运行的时间，避免拥挤，
```
# 第 8 行代码
- cron: '0 1 * * *'
# 第一个数表示分钟（范围 0 - 59）
# 第二个数表示国际标准时间 1 点（北京时间上午 9 点）（范围 0 - 23）
# 改动前两个二个数即可，不要动后面的三个 *
```
- 如果邀请数不够 10，可以尝试在 WPS_accept_invitation.py 中增加重复请求次数和等待时间
```python
# 第 23 行代码
def request_re(sid, invite_userid, rep = 30):
# rep 值代表重复次数，可以增加次数
    invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'
    r = requests.post(invite_url, headers={'sid': sid}, data={'invite_userid': invite_userid})
    js = json.loads(r.content)
    if js['msg'] == 'tryLater' and rep > 0:
        rep -= 1
        time.sleep(2)
        # 这里表示每次重复等候 2 s，可以适当加大
        r = request_re(sid, invite_userid, rep)
    return r
```
- 可在微信小程序“我的WPS会员”，‘任务’菜单->‘邀请好友’栏查看是否邀请成功（9 点以后）

---
#### 本来想做全自动打卡，但是查了 github 上其它项目后，发现打卡需要一个验证 code ，获取该 code 要调用微信内部方法 wx.login()。没办法破解，有没有大佬提供其它思路。
