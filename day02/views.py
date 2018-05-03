from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.views import View

from Tmall_test import settings
from day02.models import UserInfo
from tamll.models import User


class UploadFile(View):
    """
    前端表单 必须是POST请求  类型必须是 ENCTYPE=multipart/form-data
    input type = 'file'
    如果发现 request.files 是为空 检查是否是post请求
    """

    def post(self, request):
        # request.FILES.get('')
        # 文件名称
        # 文件的内容
        # content_type 文件的类型
        upload_file = request.FILES.get('img')
        """
            # read()
            读取文件上传的数据<慎用>
            # multiple_chunks(size)
            判断文件是否足够大
            chunks() 返回一个生成器对象,把上传的文件切割
            可以指定size
            .name
            获取文件的名称
            size 获取文件的大小
            content_type 获取上传文件的类型
            charset  上传文件的编码
        """
        """
        客服端上传文件 
        服务端保存文件   二进制的数据
        保存文件的路径到数据库
        wb 写入二进制  没有就创建
        """
        """
        对客服端进行重命名
        对路径进行细分 对文件进行重命名(保证名字是唯一的)
        1.获取文件的后缀名  os.path.splittext() 
        str.split()
        str.slice()
        
        2.IMG_年月日时分秒
        
        """
        file_name_last = upload_file.name.split('.').pop()
        file_name = 'IMG_{}.{}'.format(datetime.now().strftime('%y%m%d%H%M%S'), file_name_last) + '.'
        with open(settings.MEDIA_ROOT + '/img/' + file_name, 'wb') as file:
            # 把二进制数据保存到服务器
            for chunk in upload_file.chunks():
                file.write(chunk)
        return render(request, 'day02.html')

    def upload_file(self, request):
        if request.method == 'POST':
            pass


def upload(request):
    if request.method == 'POST':

        upload_file = request.FILES.get('img')
        file_name_last = upload_file.name.split('.').pop()
        file_name = 'IMG_{}.{}'.format(datetime.now().strftime('%y%m%d%H%M%S'), file_name_last)
        with open(settings.MEDIA_ROOT + '/img/' + file_name, 'wb') as file:
            # 把二进制数据保存到服务器
            for chunk in upload_file.chunks():
                file.write(chunk)
    return render(request, 'day02.html')


def upload1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserInfo()
        user.head = request.FILES.get('file')
        user.username = username
        user.password = password
        user.save()
    return render(request, 'upload_error.html')