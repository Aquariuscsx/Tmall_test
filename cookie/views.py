from django.http import HttpResponse
from django.shortcuts import render, redirect


def test_cookie(request):
    # 获取cookie信息
    # request.COOKIES['username']如果key不存在 会抛异常

    # 响应
    resp = render(request, 'index.html')
    # resp = HttpResponse('')
    # resp = redirect()
    username = request.COOKIES.get('username')
    if not username:
        resp.set_cookie('username', 'zhangsan')
    return resp


def test_cookie2(request):
    resp = render(request, 'index.html')
    username = request.get_signed_cookie('username', default='', salt='test')
    if not username:
        # path/限制访问的路径
        # /cookie/test02/ 表示 http://ip:端口//cookie/test02/ 或者 /xxx 能够获取这个cookie
        resp.set_signed_cookie('username', 'xiaohong', salt='test', max_age=7 * 24 * 60 * 60,
                               domain=None, path='/cookie/test02', httpoly=False)
        # 删除cookie
        # resp.delete_cookie('username')
    return resp


# 不要存中文
# 缺点 安全性不高 而且客服端可以禁用
# 数据存在客服端  减轻服务器的压力

"""
在settings.py 中要开启, 默认已经开启 如果你用会话追踪技术可以去关闭
django 对 session 的处理方式
1.存在在数据库中(默认)
2.缓存
3.文件中
4.缓存 + 数据库
5.加密cookie
6.django-redis-session(第三方 需要单独安装)

"""


def test_session(request):
    # request.session['username']
    username = request.session.get('username', default=None)
    # 设置值  如果存在就修改 不存在就设置
    request.session.setdefault('username', '12313234')
    # request.session['user'] = '122342'
    # 获取所有的key
    # request.session.keys()
    # 获取所有的值
    request.session.iteritems()
    # 设置session 的过期时间
    request.session.set_expiry(2 * 24 * 60 * 60)
    """
    如果设置的值是个整数  多少秒之后失效
    如果是一个datetime 对象 在指定的日期失效
    如果是0  表示浏览器关闭失效
    荣国是None  表示参照全局的设置
    """
    pass


def test_session2(request):
    count = request.session.get('count', default=0)
    if count == 0:
        count = 1
        request.session.setdefault('count', count)
    else:
        count += 1
        request.session.setdefault('count', count)
        return HttpResponse('次数--->{}'.format(1))

    sessionid = request.COOKIES.get('sessionid')
    request.session.setdefault('username', '123')

    return render(request, 'day02.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.filter

