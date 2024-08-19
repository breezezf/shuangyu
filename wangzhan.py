import streamlit as st
from PIL import Image
import time
import base64

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )
page_bg('主页背景.jpg')

def music(name, time):
    with open(name, 'rb')as f:
        mp3 = f.read()
    st.audio(mp3, format='audio/mp3', start_time=time)
def pagea():
    #绘图
    st.title('欢迎进入网站')
    st.snow()
    
def pageb():
    #图片处理
    uploaded_file = st.file_uploader("请上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            col1 = st.slider('r：', 0, 2, 0)
        with col2:
            col2 = st.slider('g：', 0, 2, 0)
        with col3:
            col3 = st.slider('b：', 0, 2, 0)
        st.image(img_change(img, col1, col2, col3))
if 'users' not in st.session_state:
    st.session_state.users = 0
def pagec():
    #聊天
    st.write('聊天区')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if True:
            with st.chat_message('⚛️'):
                st.write(i[1], ':', i[2])
    dengluname = st.session_state.users
    new_message = st.text_input('想要说的话')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), dengluname, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            messages = ' '
            for i in messages_list:
                messages += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            messages = messages[:-1]
            f.write(messages)

# def paged(): 
#     st.write('请选择你的游戏')
#     if st.button('我的世界'):
#         st.write('1')
#     if st.button('王者荣耀'):
#         st.write('1')
#     if st.button('原神'):
#         st.write('1')
#     if st.button('蛋仔派对'):
#         st.write('1')

def pagee():
    #游戏
    tab1,tab2,tab3,tab4 = st.tabs(['周深的歌','英文歌','流行音乐','纯音乐'])
    with tab1:
        st.write('小美满')
        music('小美满.mp3', 0)
        st.write('大鱼')
        music('大鱼.mp3', 75)
        st.write('亲爱的旅人')
        music('亲爱的旅人.mp3', 0)
        st.write('浮光.mp3')    
        music('浮光.mp3', 0)
        st.write('化身孤岛的鲸.mp3')
        music('化身孤岛的鲸.mp3', 0)
        st.write('灯火里的中国.mp3')
        music('灯火里的中国.mp3', 0)
    with tab2:
        st.write('Tamada.mp3')
        music('Tamada.mp3', 0)
        st.write('All My People.mp3')
        music('All-My-People.mp3', 0)
        st.write('Lose Contru.mp3')
        music('Lose-Contru.mp3', 0)
        st.write('unstappeable.mp3')
        music('unstappeable.mp3', 0)
        st.write('We Never.mp3')
        music('We-Never.mp3', 0)
        st.write('Take Me Hand.mp3')
        music('Take-Me-Hand.mp3', 50)
        st.write('曼波.mp3')
        music('曼波.mp3', 0)
    with tab3:
        st.write('循迹.mp3')
        music('循迹.mp3', 0)
        st.write('Da Da Da.mp3')
        music('Da-Da-Da.mp3', 0)
    with tab4:
        st.write('Summer(菊次郎的夏天）.mp3')
        music('Summer(菊次郎的夏天).mp3', 0)

def pagef():
    st.write('智慧词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查的词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
    
def img_change(img, rc, gc, bc):
    #图片处理
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (b, g, r)
    return img

def main():
    is_login = True
    page = st.sidebar.radio('菜单栏', ['首页', '图片处理', '聊天'#, '寻找游戏搭子'
                                    ,'听音乐', '智慧词典'])
    if page == '首页':
        pagea()
    elif page == '图片处理':
        pageb()
    elif page == '聊天':
        pagec()
    # elif page == '寻找游戏搭子':
    #     paged()
    elif page == '听音乐':
        pagee()
    elif page == '智慧词典':
        pagef()

def welcome():
    st.title('登录')
    st.write('游客登录：游客，123')
    username = st.text_input("用户名")
    password = st.text_input("密码")
    is_login = False
    with open('users.txt','r',encoding='utf-8') as f:
        nameword_list = f.read().split('\n')
        for i in range(len(nameword_list)):
            nameword_list[i] = nameword_list[i].split('#')
        passwords = {}
        for i in range(len(nameword_list)):
            passwords[nameword_list[i][0]] = nameword_list[i][1]
    if st.button('登录'):
        try:
            if password == passwords[username]:
                st.session_state.users = username
                is_login = True  # 设置会话状态变量
        except:
            st.error("登录失败")
    return is_login,username

try:
    if st.session_state.count == 0:
        main()
except:
    is_login,user = welcome()
    if is_login:
        if 'count' not in st.session_state:
            st.session_state.count = 0
        if 'key' not in st.session_state:
            st.session_state.key = str(user)