# Django Web server
學習Django framework時寫的小程式

# 使用規則
* 可以複製此檔案至自己要開發個人形象網站
* 部署伺服器時，其內容請注意智慧財產權問題
* 可以參考以下使用範例懶人包，與該專案維護與運行時注意事項
* 主要是我重新佈署的時候可以懶人作業~


## 雲端部署

### 雲端環境

* 主機: AWS EC2 (Ubuntu Server)


## 部屬指令

### 更新套件
```
sudo apt-get update
```
### 安裝nginx server
```
sudo apt-get install nginx
```
### 查看server狀態
```
sudo systemctl start nginx
sudo systemctl status nginx
```
### 裝python和虛擬環境
```
sudo apt install python3-pip
-----------------python3.10-venv
```
### 創建虛擬環境
```
python3 -m venv env(name)
```
### 啟用虛擬環境
```
source env/bin/activate
```
### 專案用git複製到server
```
git clone https://github.com/Andy61490963/Django-Web.git
```
### 安裝server環境
```
pip install -r requirements.txt
```
### 設定nginx
```
cd /etc/nginx/sites-enabled
sudo nano default
```
```javascript
location
{ 
    proxy_pass http://0.0.0.0:9090;
}
location /static/
{ 
    autoindex on;
    alias /home/ubuntu/yourpathto/Django-Web/staticfiles
}
```
### 設定staticfiles的權限，然後重啟
```
sudo usermod -a -G ubuntu www-data
sudo chown -R :www-data staticfiles
sudo service nginx restart
```
### 安裝gunicorn和啟動伺服器
```
pip install gunicorn
gunicorn --bind 0.0.0.0:9090 Web.wsgi
```
