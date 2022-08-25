# Django Web 接口开发与自动化测试

# Django 常用命令

    django-admin    显示所有提供的命令
    django-admin startproject guest     # 创建 guest 项目
    python manage.py                    # 查看 manage 所提供的命令
    python manage.py startapp sign      # 创建 sign 应用
    python manage.py runserver          # 运行 mange.py 所在文件夹的项目
    python manage.py runserver 127.0.0.1:8001       # 指定运行端口号
    python manage.py migrate            # 创建 django_session 表
    python manage.py createsuperuser    # 创建 admin 后台管理员账号
    python manage.py makemigrations sign    # 当模型创建好以后，执行数据库迁移
    python manage.py shell              # Django 提供的高级 Python API，用于操作数据库表

# 添加发布会个角色步骤

1. 创建发布会和用户模型
2. 使用 python manage.py migrate 命令生成表
3. 使用 python mange.py makemigration sign 命令将模型创建成表（数据表迁移，迁移后会在 sign/migration 目录下生成数据表）

---

# 运行测试命令 Run test case

## 运行整个项目内的测试文件

```powershell
python manage.py test sign
```

## 运行指定测试文件 tests

```powershell
python manage.py test sign.tests
```

## 运行测试类

示例： 运行 tests.py 文件下的 ModeTest 测试类

```powershell
python manage.py test sign.tests.ModeTest
```

## 运行测试方法

示例： 运行 tests.py 文件下的 ModeTest 测试类中测试方法 test_event_models

```powershell
python manage.py test sign.tests.ModeTest.test_event_models
```

## 模糊匹配测试文件

指定匹配运行的测试文件 ---> test\*.py, 匹配以 “test” 开头， 以“.py” 结尾的测试文件。

```powershell
python manage.py test -p test*.py
```

# Robot Framework 测试框架

## 环境搭建

1. 安装 python 依赖 robotframework、requests 和 robotframework-requests 依赖

   ```powershell
   pip install robotframework
   pip install requests
   pip install robotframework-requests
   ```

2. 添加 robot 的环境变量
   将 python 安装包下的 Scripts 文件夹的据对路径添加到 用户或系统 Path 内<br>我的 Scripts 路径 ：D:\Program Files\Python\Python38\Scripts
