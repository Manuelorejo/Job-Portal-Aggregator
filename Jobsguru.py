# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:23:02 2025

@author: Oreoluwa
"""

import requests
from bs4 import BeautifulSoup
#search_term = input('What role are you looking for? ')

def Jobsguru(search_term):

    base_url = 'https://www.jobgurus.com.ng/'
    url = f'https://www.jobgurus.com.ng/jobs?search_keyword={search_term}&specialization=&work_level='
    
    response = requests.get(url)
    
    job_list = []
    if response:
           soup = BeautifulSoup(response.content,'html.parser') 
           #document = soup.find("div", class_ = "main-content-section")
           jobs = soup.find_all("div", class_ = "panel-body")
           
          # print(job)
          
           for job in jobs:
               job_post = {}
               
               try:
                   job_title = job.h2.text.strip()
                   job_post['Job title'] = job_title
                   
                   job_link = job.a['href'] 
                   job_post['Job Link'] = job_link
                   
                   
               except:
                   continue
               
               job_response = requests.get(job_link)
               if job_response:
                   job_soup = BeautifulSoup(job_response.content, "html.parser")
                   job_doc = job_soup.find("div", class_ = "main-content-section")
                   job_desc = job_doc.find("div", class_ = 'clearfix')
                   job_meta = job_desc.find_all("p")[3].get_text(separator = '')
                   
                   try:
                       job_location = job_meta.split("\n")[0]
                       job_location = job_location.split(":")[-1].strip()
                       job_post['Job Location'] = job_location
                   except:
                       continue     
                   
                   try:
                       job_mode = job_meta.split("\n")[1]
                       job_mode = job_mode.split(":")[-1].strip()
                       job_post['Job Mode'] = job_mode
                       job_post['Job Source'] = "Jobsguru.com"
                       
                   
                   except:
                       continue
               
                 
               
               job_list.append(job_post)
           return job_list
               
    
    
               
    '''else:
        print("Could not scrape")
    
    counter = 1    
    for job in job_list:
        print("JOB " + str(counter))
        counter += 1
        
        for k,v in job.items():
            print(k, ": ",v)
            print("\n")'''
            


#Jobsguru(search_term)