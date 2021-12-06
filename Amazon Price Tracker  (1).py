#!/usr/bin/env python
# coding: utf-8

# In[43]:


import requests
from bs4 import BeautifulSoup
import smtplib 
import time


# In[44]:


URL = 'https://www.amazon.in/Finest-Moments-Mohammed-Rafi-GB/dp/B07YR4DNZG/ref=zg-bs_music_2/260-2988806-1423167?pd_rd_w=iJ3vP&pf_rd_p=56cde3ad-3235-46d2-8a20-4773248e8b83&pf_rd_r=FBYXAG4YD143PNKPYEJF&pd_rd_r=e5485dcd-8ad1-4527-ab41-a38ee414639c&pd_rd_wg=jFG5v&pd_rd_i=B07YR4DNZG&psc=1'


# In[45]:


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}


# In[ ]:


def check_price():


# In[46]:


page = requests.get(URL, headers=headers)


# In[47]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[48]:


title = soup.find(id="productTitle").get_text()


# In[49]:


price = soup.find(id="priceblock_ourprice").get_text()
price=price.strip("₹")


# In[50]:


converted_price = float(price[0:5])


# In[21]:


if(converted_price<"170"):
    send_mail()


# In[ ]:


print(converted_price)


# In[11]:


print(title.strip())


# In[54]:


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server('husainrizvi55@gmail.com', 'mjutmyhdgtwjahshsgdg')
    subject = ' Price Fell Down'
    body = 'Check the amazon website https://www.amazon.in/Finest-Moments-Mohammed-Rafi-GB/dp/B07YR4DNZG/ref=zg-bs_music_2/260-2988806-1423167?pd_rd_w=iJ3vP&pf_rd_p=56cde3ad-3235-46d2-8a20-4773248e8b83&pf_rd_r=FBYXAG4YD143PNKPYEJF&pd_rd_r=e5485dcd-8ad1-4527-ab41-a38ee414639c&pd_rd_wg=jFG5v&pd_rd_i=B07 '
    
    msg = f"Subject: {subject}\n\n{body}""
    
    server.sendmail(
        'husainrizvi55@gmail.com',
        'owenwalsh314@gmail.com',
       msg
    )
    print('HEY EMAIL HAS BEEN SENT!')
    
    server.quit()
    


# In[53]:


while(True):
     check_price()
     time.sleep(60*60)


# In[ ]:




