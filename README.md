<h1>wpnuker</h1>  
<p>wpnuker is an assortment of tools in continual development that involve the assessment of a Wordpress blog.  

$ python3 wpnuker.py version --url https://cybertutorials.org  
WordPress 5.9.3  

$ python3 wpnuker.py brutelogin --username admin --wordlist wlist.txt --url "https://www.cybertutorials.org/wp-admin"  
admin:asdf - Bad Password  
admin:a - Bad Password  
 
$ python3 wpnuker.py comment --target "https://www.cybertutorials.org/2022/python-wpnuker-a-collection-of-wordpress-pentesting-tools" --advertise "google.com" --anchor "test"  
Comment is in the moderation queue.  

$ python3 wpnuker.py plugins --url https://cybertutorials.org  
simple-sitemap ver=3.5.5  
revslider ver=6.5.15  
fusion-builder  
litespeed-cache ver=4.6  

$ python3 wpnuker.py getip --url cybertutorials.org  
173.236.172.84  
