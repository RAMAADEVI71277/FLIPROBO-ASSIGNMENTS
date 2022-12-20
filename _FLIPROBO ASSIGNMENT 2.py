#!/usr/bin/env python
# coding: utf-8

# # Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. Youhave to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10jobs data.

# In[1]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import warnings
warnings.filterwarnings("ignore")


# In[2]:


driver=webdriver.Chrome(r'C:\Users\S.Ramaa Devi\Downloads\chromedriver_win32 (2).zip\chromedriver.exe')


# In[3]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')
driver


# In[4]:


driver.get('https://www.naukri.com/')


# In[5]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys("Data Analyst")


# In[6]:


#location=driver.find_element(By.CLASS_NAME,"suggestor-input") 
# if we try this it joins with designations as the class name for both is the same
#location.send_keys("Bangalore")


# In[7]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
# full path for only one location
location.send_keys("Bangalore")


# In[8]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[9]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[17]:


job_tag=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
location_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 locWdth"]')
company_tag=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
exp_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 expwdth"]')


# In[18]:


for i in job_tag:
    job_title.append(i.text)
    
len(job_title)    


# In[19]:


for i in location_tag:
    job_location.append(i.text)
    
for i in company_tag:
    company_name.append(i.text)
    
for i in exp_tag:
    experience_required.append(i.text)


# In[20]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[21]:


df=pd.DataFrame(data={'JOB_TITLE':job_title[0:10],'JOB_LOCATION':job_location[0:10],'COMPANY_NAME':company_name[0:10],'EXP_NEEDED':experience_required[0:10]},index=range(1,11))
df


# # Q2:Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. Youhave to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.

# In[22]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')


# In[23]:


driver.get("https://www.naukri.com/")


# In[24]:


designation=driver.find_element(By.CLASS_NAME,'suggestor-input')
designation.send_keys("Data Scientist")


# In[25]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
location.send_keys("Bangalore")


# In[26]:


search=driver.find_element(By.CLASS_NAME,'qsbSummit')
search.click()


# In[27]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit") # double quotes
search.click()


# In[28]:


job_title=[]
job_location=[]
company_name=[]

job_tag=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
location_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 locWdth"]')
company_tag=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')

for i in job_tag[0:10]:
    job_title.append(i.text)
    
for i in location_tag[0:10]:
    job_location.append(i.text)
    
for i in company_tag[0:10]:
    company_name.append(i.text)
    
print(len(job_title),len(job_location),len(company_name))    


# In[29]:


df=pd.DataFrame(data={'JOB_TITLE':job_title,'JOB_LOCATION':job_location,'COMPANY_NAME':company_name},index=range(1,11))
df


# # Q3: In this question you have to scrape data using the filters available on the webpage as shown below:

# In[30]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')


# In[31]:


driver.get("https://www.naukri.com/")


# In[32]:


designation=driver.find_element(By.CLASS_NAME,'suggestor-input')
designation.send_keys("Data Scientist")


# In[33]:


location=driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input')
location.send_keys("Delhi/NCR")


# In[34]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit") # double quotes
search.click()


# In[35]:


salary_filter=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/p/span[1]')
salary_filter.click()


# In[36]:


location1=driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[13]/div[2]/div[3]/label/p/span[1]')
location1.click()


# In[37]:


j_title=[]
j_location=[]
c_name=[]
exp_req=[]

j_tag=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
loc_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 locWdth"]')
c_tag=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
exp_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft fs12 lh16 expwdth"]')

for i in j_tag[0:10]:
    j_title.append(i.text)
    
for i in loc_tag[0:10]:
    j_location.append(i.text)
    
for i in c_tag[0:10]:
    c_name.append(i.text)
    
for i in exp_tag[0:10]:
    exp_req.append(i.text)
    
    
print(len(j_title),len(j_location),len(c_name),len(exp_req))    
    


# In[38]:


df=pd.DataFrame(data={'JOB_TITLE':j_title,'JOB_LOCATION':j_location,'COMPANY_NAME':c_name,'EXPERIENCE_REQUIRED':exp_req},index=range(1,11))
df


# # Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 
# 2. ProductDescription
# 
# 3. Price

# In[39]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')
driver.get('https://www.flipkart.com/')


# In[41]:


products=driver.find_element(By.CLASS_NAME,"_3704LK")
products.send_keys("sunglasses")


# In[42]:


search=driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
search.click()


# In[43]:


sun_glasses=[]


# In[44]:


import time
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException


# In[45]:


for page in range(0,2):
    tag=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in tag: # indentation is very important --should be within
    sun_glasses.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')  
    next_button.click()
    time.sleep(5)
 


# In[47]:


for page in range(0,2):
    tag=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in tag:
        sun_glasses.append(i.text)
        next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]') # indentation is very important --should be within
        next_button.click()
        time.sleep(5)
 


# In[46]:


for page in range(0,3):
    tag=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in tag:
        sun_glasses.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]') # indentation is very important --should be within
    next_button.click()
    time.sleep(5)
 
 


# In[48]:


len(sun_glasses)


# In[49]:


df=pd.DataFrame(data=sun_glasses[0:100])
df


# # Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# 
# https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market
# 
# place=FLIPKART

# In[50]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')
driver.get('https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market')


# In[51]:


rating=[]
review_summary=[]
full_review=[]


# In[52]:


for page in range(0,10):
    rating_tag=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    sum_tag=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    full_tag=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in rating_tag:
        rating.append(i.text)
        
    for i in sum_tag:
        review_summary.append(i.text)
        
    for i in full_tag:
        full_review.append(i.text)
        
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(5)


# In[53]:


print(len(rating),len(review_summary),len(full_review))


# In[54]:


df=pd.DataFrame(data={'RATING':rating,'REVIEW_SUMMARY':review_summary,'FULL_REVIEW':full_review},index=range(1,101))
df


# # Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.
# You have to scrape 4 attributes of each sneaker:
#     
# 1. Brand
# 
# 2. ProductDescription
# 
# 3. Price

# In[55]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')
driver.get('https://www.flipkart.com/')


# In[56]:


products=driver.find_element(By.CLASS_NAME,"_3704LK")
products.send_keys("sneakers")


# In[57]:


search=driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
search.click()


# In[58]:


brand=[]
desc=[]
price=[]


# In[61]:


for page in range(0,3):
    b_tag=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    desc_tag=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    price_tag=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in b_tag:
        brand.append(i.text)
        
    for i in desc_tag:
        desc.append(i.text)
        
    for i in price_tag:
        price.append(i.text)
        
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(5)


# In[62]:


print(len(brand),len(desc),len(price))


# In[63]:


print(len(brand[0:100]),len(desc[0:100]),len(price[0:100]))


# In[64]:


df=pd.DataFrame(data={'SNEAKERS_BRAND':brand,'PRODUCT_DESCRIPTION':desc,'PRICE':price},index=range(1,101))
df


# In[65]:


df=pd.DataFrame(data={'SNEAKERS_BRAND':brand[0:100],'PRODUCT_DESCRIPTION':desc[0:100],'PRICE':price[0:100]},index=range(1,101))
df


# # Q7: Go to webpage https://www.amazon.in/
# Enter “Laptop” in the search field and then click the search icon.
# Then set CPU Type filter to “Intel Core i7” as shown in the below image:
#     
#     After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[66]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')
driver.get('https://www.amazon.in/')


# In[67]:


products=driver.find_element(By.CLASS_NAME,"nav-search-field ")
products.send_keys("laptop")


# In[68]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')
driver.get('https://www.amazon.in/s?k=laptop&crid=F8Q3EPG8P618&sprefix=laptop%2Caps%2C261&ref=nb_sb_ss_ts-doa-p_2_6')
# tried thr other way ,going straightly into laptop browser


# In[69]:


filter=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[6]/li[14]/span/a')
filter.click()


# In[70]:


title=[]
ratings=[]
price=[]


# In[71]:


title_tag=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')
rat_tag=driver.find_elements(By.XPATH,'//div[@class="a-row a-size-small"]')
price_tag=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')


# In[72]:


for i in title_tag:
    title.append(i.text)
    
 
    
for i in price_tag:
    price.append(i.text)


# In[73]:


for i in rat_tag:
    ratings.append(i.text.split())


# In[74]:


ratings


# In[75]:


print(len(title),len(ratings),len(price))


# In[76]:


df=pd.DataFrame(data={'TITLE':title[0:10],'RATINGS':ratings[0:10],'PRICE':price[0:10]},index=range(1,11))
df


# # Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
#     
# 1.First get the webpage https://www.azquotes.com/
#     
# 2. Click on Top Quotes
# 
# 3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[77]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')
driver.get('https://www.azquotes.com/')


# In[78]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
search.click()


# In[79]:


quote=[]
author=[]
type_of_quotes=[]


# In[80]:


for page in range(0,10):
    q_tag=driver.find_elements(By.XPATH,'//a[@class="title"]')
    a_tag=driver.find_elements(By.XPATH,'//div[@class="author"]')
    t_tag=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    
    for i in q_tag:
        quote.append(i.text)
        
    for i in a_tag:
        author.append(i.text)
        
    for i in t_tag:
        type_of_quotes.append(i.text)
        
    next_button=driver.find_element(By.XPATH,'//li[@class="next"]')
    next_button.click()
        


# In[81]:


print(len(quote),len(author),len(type_of_quotes))


# In[82]:


df=pd.DataFrame(data={'QUOTE':quote[0:50],'AUTHOR_NAME':author[0:50],'TYPE_OF_QUOTES':type_of_quotes[0:50]},index=range(1,51))
df


# # Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead,Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpage https://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make the DataFrame.

# In[103]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')
driver.get('https://www.jagranjosh.com/')


# In[99]:


search=driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[6]/div/div[1]/header/div[3]/ul/li[9]/a')
search.click()


# In[106]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a')
search.click()


# In[101]:


name=[]
born_dead=[]
term=[]
remarks=[]


# In[111]:


name_tag=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[4]/span/div[2]/table/tbody/tr[2]/td[2]/p/strong')
name_tag.text


# In[117]:


born_tag=driver.find_element(By.XPATH,'//*[@id="itemdiv"]/div[4]/span/div[2]/table/tbody/tr[2]/td[3]')
born_dead.append(born_tag.text)


# In[119]:


t_tag=driver.find_element(By.XPATH,'//*[@id="itemdiv"]/div[4]/span/div[2]/table/tbody/tr[2]/td[4]/p[2]')
term.append(t_tag.text)


# In[120]:


r_tag=driver.find_element(By.XPATH,'//*[@id="itemdiv"]/div[4]/span/div[2]/table/tbody/tr[2]/td[5]/p')
remarks.append(r_tag.text)


# In[121]:


print(len(name),len(born_dead),len(term),len(remarks))


# In[122]:


df=pd.DataFrame({'PM_NAME':name[0],'PM_LIFESPAN':born_dead,'RULETERM':term,'REMARKS':remarks})
df


# In[ ]:


# cant scrap more there is no class .


# # Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e.Car name ,Description and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to click on the List option from Dropdown menu on leftside.
# 3. Then click on 50 most expensive carsin the world..
# 4. Then scrap the mentioned data and make the

# In[102]:


driver=webdriver.Chrome(r'chromedriver_win32(2).zip')
driver.get('https://www.motor1.com/')


# In[88]:


search=driver.find_element(By.XPATH,'//div[@class="m1-hamburger-button"]')
search.click()


# In[89]:


search=driver.find_element(By.XPATH,'//li[@class="m1-navigation-main__animated-block grand left top mobile dropdown show"]')
search.click()


# In[90]:


search=driver.find_element(By.XPATH,'/html/body/div[3]/div[7]/div/div[1]/div[1]/div[2]/div/div[1]/h3/a')
search.click()


# In[91]:


name=[]
desc=[]
price=[]


# In[92]:


name_tag=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in name_tag:
    name.append(i.text)
    
len(name)    


# In[93]:


d_tag=driver.find_elements(By.XPATH,'//*[@id="article_box"]/div[1]/div[2]/div[1]/p[103]')
for i in d_tag:
    desc.append(i.text)
    
len(desc)    


# In[95]:


price_tag=driver.find_elements(By.XPATH,'//*[@id="article_box"]/div[1]/div[2]/div[1]/p[102]/strong')
for i in price_tag:
    price.append(i.text)
    
len(price)    


# In[96]:


df=pd.DataFrame({'CAR_NAME':name[0],'DESCRIPTION':desc,'CAR_PRICE':price})
df


# In[97]:


#cant scrap all as it does not contain a class


# In[ ]:




