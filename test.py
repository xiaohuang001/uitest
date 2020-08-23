from selenium import webdriver
import time
import sys
import os


p=os.path.join(os.getcwd(),'mm\\')
print(p)
path=os.environ['path']
print(type(path))
path=path+';'+p
os.environ['path']=path



driver = webdriver.Chrome()
#browser = webdriver.Ie()
#browser = webdriver.Firefox()
driver.get("https://www.baidu.com")
time.sleep(5)
driver.close()
driver.switch_to.default_content()
import weakref

weakref.WeakKeyDictionary()
import warnings
w=warnings.catch_warnings()
warnings.simplefilter()
f=open(r'C:\Users\Administrator\Desktop\123.txt','w')
f.close()
f=open(r'C:\Users\Administrator\Desktop\123.txt','wb')
import sys
s=sys.stdout
import contextlib
AssertionError
hash()
import HtmlTestRunner

from jinja2 import Template
import webbrowser