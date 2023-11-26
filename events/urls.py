from django.urls import path
from . import views

urlpatterns = [
    #path 自定義網址
    #分別對應網址後綴、views函數、html內容的連結
    path('', views.home, name="home"), #主頁面
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('add_homepost', views.add_homepost,name="add-homepost"),

    #home/dropdown/About Me
    path('whereamifrom',views.whereamifrom1, name="dropdown_from_whereamifrom"),
    path('introduction',views.introduction1, name="dropdown_from_introduction"),
    path('autobiography',views.autobiography1, name="dropdown_from_autobiography"),

    #home/dropdown/Licence
    path('Licence',views.Licence_, name="dropdown_from_Licence"),
    path('Licence1',views.Licence_1, name="dropdown_from_Licence1"),

    #home/dropdown/Ability
    path('Ability',views.Ability_, name="dropdown_from_Ability"),
    path('Ability1',views.Ability_1, name="dropdown_from_Ability1"),

    #home/dropdown/Experience
    path('Experience',views.Experience_, name="dropdown_from_Experience"),
    path('Experience1',views.Experience_1, name="dropdown_from_Experience1"),

    #home/dropdown/Dream
    path('Dream',views.Dream_, name="dropdown_from_Dream"),

    path('info', views.all_info,name="all_infos"), #個人資料
    path('add_information', views.add_information,name="add-information"), #新增個人資料
    path('infoname_list', views.infoname_list,name="infoname-list"), #列舉個人資料

    path('show_information/<int:information_id>', views.show_information,name="show-information"), 
    path('update_information/<int:information_id>', views.update_information,name="update-information"),
    path('delete_information/<int:information_id>',views.delete_information, name="delete-information"),

    path('articles',views.My_article, name="My_article"),

    path('paper',views.all_paper, name="all_papers"),
    path('add_paper', views.add_paper,name="add-paper"),

    path('my_Portfolio',views.My_Portfolio, name="My-Portfolio"), #My portfolio

    path('aboutus',views.aboutus, name="about-us"), #About me

    path('search_information', views.search_information,name="search-inofrmation"),


]
