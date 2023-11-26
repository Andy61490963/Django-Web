from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.html import format_html

#Import Database
from .models import homepost
from .models import Interest

from .models import wherefrom
from .models import introduction
from .models import autobiography

from .models import Licence
from .models import Licence1

from .models import Ability
from .models import Ability1

from .models import Experience
from .models import Experience1

from .models import Dream

from .models import information
from .models import article
from .models import paper
from .models import all_aboutus
from .models import Portfolio

#Import Form
from .forms import InformationForm
from .paperforms import paperForm
from .homepostforms import homepostForm

#Import Pagination
from django.core.paginator import Paginator



#用block content鑲嵌於base.html的home.html
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    post = homepost.objects.all()#.order_by('-name')
    name = "Sentimental1"

    p = homepost.objects.all().order_by('id')
    paginator = Paginator(p, 3)
    page = request.GET.get('page')
    post1 = paginator.get_page(page)
    nums = "a" * post1.paginator.num_pages

    #time
    now = datetime.now()
    time = now.strftime("%Y-%m-%d, %H:%M")
    return render(request,
        'home.html', {
        "post": post,
        "name": name,
        "year": year,
        "month": month,
        "time": time,
        "post1": post1,
        "nums": nums
        })

def add_homepost(request):
    submitted = False
    if request.method == "POST":
        form = homepostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_homepost?submitted=True')
    else:
        form = homepostForm
        if 'submitted' in request.GET:
            submitted =  True
        
    return render(request,'add_homepost.html',
        {'form': form, 'submitted': submitted})




#home/dropdown/About Me
def whereamifrom1(request):
    wherefroms = wherefrom.objects.all()
    return render(request, 'Fixed Dropdown menu/About Me/whereamifrom.html',
        {"wherefroms":wherefroms},)

def introduction1(request):
    introductions = introduction.objects.all()
    return render(request, 'Fixed Dropdown menu/About Me/Introduction.html',
        {"introductions":introductions},)

def autobiography1(request):
    autobiographys = autobiography.objects.all()
    
    p = autobiography.objects.all().order_by('id')
    paginator = Paginator(p, 1)
    page = request.GET.get('page')
    autobiographypage = paginator.get_page(page)
    nums = "a" * autobiographypage.paginator.num_pages
    
    return render(request, 'Fixed Dropdown menu/About Me/autobiography.html', {
        "autobiographys": autobiographys,
        "autobiographypage": autobiographypage,
        "nums": nums
    })

#home/dropdown/Licence
def Licence_(request):
    Licences = Licence.objects.all()
    return render(request, 'Fixed Dropdown menu/Licence/Licence.html',
        {"Licences":Licences},)

def Licence_1(request):
    Licences1 = Licence1.objects.all()
    return render(request, 'Fixed Dropdown menu/Licence/Licence1.html',
        {"Licences1":Licences1},)

#home/dropdown/Ability
def Ability_(request):
    Abilitys = Ability.objects.all()
    return render(request, 'Fixed Dropdown menu/Ability/ability.html',
        {"Abilitys":Abilitys},)

def Ability_1(request):
    Abilitys1 = Ability1.objects.all()
    return render(request, 'Fixed Dropdown menu/Ability/ability1.html',
        {"Abilitys1":Abilitys1},)

#home/dropdown/Experience
def Experience_(request):
    Experiences = Experience.objects.all()
    return render(request, 'Fixed Dropdown menu/Experience/Experience.html',
        {"Experiences":Experiences},)

def Experience_1(request):
    Experiences1 = Experience1.objects.all()
    return render(request, 'Fixed Dropdown menu/Experience/Experience1.html',
        {"Experiences1":Experiences1},)

#home/dropdown/Dream
def Dream_(request):
    Dreams = Dream.objects.all()
    return render(request, 'Fixed Dropdown menu/Dream/Dream.html',
        {"Dreams":Dreams},)

def all_info(request):
    #info = information.objects.all().order_by('-name')
    info = information.objects.all()

    #set up pagination
    p = information.objects.all().order_by('id')
    #Paginator(p, 1) 那個1代表每頁顯示幾個物件
    paginator = Paginator(p, 1)
    #從 HTTP 請求的 GET 參數中獲取當前頁碼
    page = request.GET.get('page')
    #傳遞給分頁對象
    info1 = paginator.get_page(page)
    nums = "a" * info1.paginator.num_pages
    
    return render(request,'Top Dropdown menu/info/info.html',
        {"info": info,
        "info1": info1,
        "nums": nums}
        )

def add_information(request):
    submitted = False
    #檢查 HTTP 請求的方法是否為 POST。如果是 POST 請求，則表示用戶提交了一個表單
    if request.method == "POST":
        #在 POST 請求的情況下，創建一個 InformationForm 表單對象，並將 request.POST 和 request.FILES 傳遞給表單，以接收用戶的輸入數據和上傳文件
        form = InformationForm(request.POST, request.FILES)
        #驗證表單的數據。如果表單數據有效（通過驗證），則創建一個 Information 物件，將表單的數據保存到該物件中
        if form.is_valid():
            #將 request.user.id 賦值給 information.owner，以將該物件與當前用戶關聯。最後，保存 information 物件
            information = form.save(commit=False)
            information.owner = request.user.id
            information.save()
            #form.save()
            #在 POST 請求的情況下，重定向到 /add_information?submitted=True，即重新加載頁面，並將 submitted 參數設置為 True
            return HttpResponseRedirect('/add_information?submitted=True')
        
    else:
        #檢查是否有名為 submitted 的 GET 參數。如果有，則將 submitted 設置為 True
        form = InformationForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request,'Top Dropdown menu/info/add_information.html',
        {'form': form, 'submitted': submitted, }) #add_information.html與views.add_information對應

def infoname_list(request):
    infoname_list = information.objects.all()
    return render(request,'Top Dropdown menu/info/information.html',
        {"infoname_list": infoname_list})

def update_information(request, information_id):
    update_information = information.objects.get(pk=information_id) #在model中找id
    form = InformationForm(request.POST or None, request.FILES or None, instance=update_information)
    if form.is_valid():
        form.save()
        return redirect('infoname-list')
        
    return render(request,'Top Dropdown menu/info/function/update_information.html',
        {"update_information": update_information,
        'form':form})

def delete_information(request, information_id):
    update_information = information.objects.get(pk=information_id)
    update_information.delete()
    return redirect('infoname-list')

def My_article(request):
    articles = article.objects.all()
    
    p = article.objects.all().order_by('id')
    paginator = Paginator(p, 1)
    page = request.GET.get('page')
    articlepage = paginator.get_page(page)
    nums = "a" * articlepage.paginator.num_pages
    
    return render(request, 'Top Dropdown menu/articles/articles.html', {
        "articles": articles,
        "articlepage": articlepage,
        "nums": nums
    })

def show_information(request, information_id):
    infodetail = information.objects.get(pk=information_id)
    return render(request,'Top Dropdown menu/info/function/show_information.html',
        {"infodetail": infodetail})

def all_paper(request):
    papers = paper.objects.all()
    
    #set up pagination
    p = paper.objects.all().order_by('id')
    paginator = Paginator(p, 1)
    page = request.GET.get('page')
    papers1 = paginator.get_page(page)
    nums = "a" * papers1.paginator.num_pages
    
    return render(request,'Top Dropdown menu/papers/paper.html',
        {"papers": papers,
        "papers1": papers1,
        "nums": nums}
        )

def add_paper(request):
    submitted = False
    if request.method == "POST":
        form = paperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_paper?submitted=True')
    else:
        form = paperForm
        if 'submitted' in request.GET:
            submitted =  True
        
    return render(request,'Top Dropdown menu/papers/add_paper.html',
        {'form': form, 'submitted': submitted})


def My_Portfolio(request):
    Portfolios = Portfolio.objects.all()
    return render(request,'Top Dropdown menu/my portfolio/Portfolio.html',
        {"Portfolios":Portfolios},)
        
def aboutus(request):
    aboutus1 = all_aboutus.objects.all()
    return render(request,'Top Dropdown menu/about me/aboutus.html',
        {"aboutus1": aboutus1},)

def search_information(request):
    if request.method == "POST":
        searched = request.POST['searched'] #受到來自使用者的請求
        informations = information.objects.filter(name__contains=searched)
        
        return render(request,
        'Top Dropdown menu/info/function/search_information.html',
        {'searched':searched,
        'informations':informations})
    else:
        return render(request,
        'Top Dropdown menu/info/function/search_information.html',
        {})


#API
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSeti(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
