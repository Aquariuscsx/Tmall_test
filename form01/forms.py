"""
1.第一步  先定义对象
"""
from django import forms

from form01 import models


class TestForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=15, min_length=6,
                               widget=(forms.TextInput(attrs={'placeholder': '请输入用户名'})),
                               error_messages={'max_lenght': '输入过长', 'min_lenght': '最少输入6位'})
    password = forms.CharField(label='密码', widget=(forms.PasswordInput(attrs={'placeholder': '请输入密码'})))
    is_accept = forms.BooleanField(label='同意', error_messages={'required': '必须接收'})
    file = forms.FileField(label='请选择上传的文件', required=False)
    img = forms.ImageField(label='请选择要上传的图片', required=False)
    test_date = forms.DateField(label='请输入日期', input_formats=['%Y-%m-%d'])
    test_datetime = forms.DateTimeField(label='请输入日期', input_formats=['%Y-%m-%d %H%M%S'])
    sex = forms.ChoiceField(label='性别', choices=[(1, '女'), (2, '男')])
    email = forms.EmailField(label='邮箱', max_length=20)

    def __init__(self):
        super().__init__()
        self.fields['sex'].inital = {[(1, '女'), (2, '男')]}

    # 重写验证
    # 全局 局部
    def clean_username(self):
        if self.cleaned_data['username'].isalpha():
            return self.cleaned_data['username']
        else:
            raise EnvironmentError('用户名必须包含字母')


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.User

        # 所有的属性都生成form
        fields = '__all__'
        # 指定的特定的属性生成form
        # fields = ['username', 'password']
        # # 不包含
        # exclude = ['is_del']
