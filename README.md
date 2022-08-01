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
3. 使用 python mange.py makemigration sign 命令将模型创建成表（数据表迁移，迁移后会在sign/migration目录下生成数据表）