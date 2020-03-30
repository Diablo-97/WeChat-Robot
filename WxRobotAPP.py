from wxpy import *
import re
#bot = Bot(cache_path = True)
bot = Bot(cache_path = True)

# 打印所有*好友*对象中的*文本*消息
@bot.register(Friend,TEXT)
def auto_accept_friends(fdmsg):
    print("获取好友消息",fdmsg)
    print("获取好友消息",fdmsg.text)
    if fdmsg.text == "进群":
        fdmsg.chat.send("回复1进入荣耀战队")
    elif fdmsg.text == "1":
        group_select = bot.groups().search("XUan肉肉的小队")[0]
        group_select.add_members(fdmsg.chat,use_invitation=True)

# 打印所有*群聊*对象中的*文本*消息
#@bot.register(Group, TEXT)
#def print_group_msg(msg):
 #   print(msg)

#新人入群通知的匹配正则
rp_new_member_name = (
    re.compile(r'^"(.+)"通过'),
    re.compile(r'邀请"(.+)"加入'),
)

#获取新成员名称
def get_new_mumber_name(msg):
    from itchat.utils import msg_formatter
    msg_formatter(msg.raw,'Text')
    for rp in rp_new_member_name:
        match = rp.search(msg.text)
        if match:
            return match.group(1)

#新人进群欢迎语
welcome_text = '''🏂欢迎@{0} 的加入！⛷
JSKI.极四季是全日本官方注册的最大华人滑雪俱乐部，本群是JSKI中国西部滑雪俱乐部雪友群。本群宗旨为开心滑雪，安全滑雪，欢迎群友进行文明友好的技术讨论和滑雪活动交流。
俱乐部提供成都尖峰旱雪场67元/次/人的雪票福利。具体请联系群主预约，限本群雪友使用。
俱乐部提供日本SAJ认证，加拿大CASI认证的单板滑雪教学服务。
具体请联系俱乐部教练：天一 和 陈6岁
{1}'''

#Test_Robot = bot.groups().search("JSKI极四季.中国西部雪友群🏂 ⛷")[0]
Test_Robot = bot.groups().search("JSKI极四季.中国西部雪友群🏂 ⛷")[0]
# 设置新人进群自动@新人文本消息
@bot.register(Test_Robot, NOTE)
def print_group_msg(msg):
    print(msg)
    print("加入了群聊" in msg.text)
    if "加入了群聊" in msg.text:
        #获取新成员名称
        name = get_new_mumber_name(msg)
        #在群里回复文本
        msg.reply(welcome_text.format(name,""))

#获取微信好友
#wx_friends = bot.friends()
#print("微信好友总数",len(wx_friends))

#获取微信群
#wx_groups = bot.groups()
#print("微信群总数",len(wx_groups),wx_groups)

print("登录成功")
#堵塞线程
bot.join()