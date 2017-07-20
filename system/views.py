#_*_coding:utf-8_*_
from django.shortcuts import render,HttpResponse,render_to_response
from django.contrib.auth.models import User,Group,Permission
from system.models import UserProfile

import json
def userIndex(request):



    return render(request,'user.html')

def userEdit(request):


    return render(request, 'useredit.html')
def addUser(request):

    g=Group.objects.get(name='测试组')
    print g.id    #获取组ID
    #u=User.objects.get(id=58)

    #u.groups.add(1)   #组ID




    '''
    u = User(username='ke4444445111222', email='kk22152@dsjka.com', first_name='来依2法5', last_name='再来2依法5',
             is_active=1)
    u.set_password('123456')
    u.groups.add(name="测试组")
    u.save()
    p = UserProfile(user=u, phone="18158100022")

    p.save()
    return HttpResponse("qqqq")
    '''
    return HttpResponse("qqqq")
def userAdd(request):
    if request.method == 'POST':


        u = User(username='ke4444445111222', email='kk22152@dsjka.com', first_name='来依2法5', last_name='再来2依法5',
                 is_active=1)
        u.set_password('123456')
        u.groups.add(name="测试组")
        u.save()
        p = UserProfile(user=u, phone="18158100022")

        p.save()
        return HttpResponse("qqqq")

    return render(request,'useradd.html')
def userData(request):
    #user_list=User.objects.all()
    #for line in user_list:
    #   print line.username,line.last_name,line.first_name,line.is_active,line.tel
    #print request.GET
    user_list=UserProfile.objects.all()
    print user_list
    for line in user_list:
        print line.user.username,line.user.first_name,line.user.last_name,line.phone

    data={
        "draw": 1,
        "recordsTotal": 57,
        "recordsFiltered": 57,
        "data":[
            {
                "id":1,
                "username":"kebinzhi",
                "name":u"柯斌志",
                "role":"技术中心",
                "tel":"1223343423432424",
                "status":1,
                "last_login":"2017-07-08 13:00:00"
             },
            {
                "id": 2,
                "username": "kebinzhi2",
                "name": u"柯斌志2",
                "role": "技术中心2",
                "tel": "1223343423432424",
                "status": 0,
                "last_login": "2017-07-08 13:00:00"
            },
            {
                "id": 3,
                "username": "kebinzhi3",
                "name": u"柯斌志3",
                "role": "技术中心3",
                "tel": "1223343423432424",
                "status": 1,
                "last_login": "2017-07-08 13:00:00"
            }
        ]
    }



    return HttpResponse(json.dumps(data))

def groupIndex(request):
    return render(request,'group.html')

def groupData(request):
    data = {
        "draw": 1,
        "recordsTotal": 57,
        "recordsFiltered": 57,
        "data": [
            {
                "id": 1,
                "name": u"测试组",
                "des": "技术中心",

            },
            {
                "id": 2,
                "name": u"测试组2",
                "des": "描述信息",

            },
            {
                "id": 3,
                "name": u"柯斌志3",
                "des": "技术中心3",
            }
        ]
    }

    return HttpResponse(json.dumps(data))

def groupAdd(request):

    perms=Permission.objects.all()

    #for line in perms:
    #    print(line.id)

    #新增组的时候是没有已授权权限的
    try:
        group=Group.objects.get(name='测试组')

        group_perms=group.permissions.all()

        for line in group_perms:
            print line
    except:
        group_perms=[]
    return render(request,'groupadd.html',{"perm_all":perms,"group_perms":group_perms})