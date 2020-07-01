# pythonanywhere.com only

1.  create account on pythonanywhere beginer
2.  start django web app django2.2.7
3.  git clone https://github.com/Umidrifkatov/mysite.git
4.  cd mysite
5.  pip3 install -r requirements.txt --user
6.  python3 manage.py makemigrations telegram jet
7.  pyhton3 manage.py migrate 
8.  python3 manage.py collectstatic
9.  python3 manage.py createsuperuser set login default and password is login1
10. check is it work
11. set webhook example: https://api.telegram.org/bottoken/setWebhook?url=https://username.pythonanywhere.com/token/
12. set force https in webapp settings pythonanywhere
13. change token in mysite.settings.py
14. change photo fileid
15. set Debug = false
16. change about and about links
17. set group id
18. check if all working

# ready
