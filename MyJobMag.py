# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:20:55 2025

@author: Oreoluwa
"""
import requests
from bs4 import BeautifulSoup
import re

search_term = "Data Scientist"
location = "Lagos"
#search_term = input('What role are you looking for? ')
#location = input('Which state do you want to work in? ')


def MyJobMag(search_term,location):
    base_url = 'https://www.myjobmag.com/'
    url = f'https://www.myjobmag.com/search/jobs?q={search_term}&location={location}&location-sinput={location}'
    
    response = requests.get(url)
    
    job_list = []
    if response:
        soup = BeautifulSoup(response.content,'html.parser')
        document = soup.find("div",class_ = 'content-wrap2' )
        jobs = document.find_all("li",class_='job-list-li')
        
        
        for job in jobs:
            job_post = {}
            try:
                job_title = job.h2.text.strip()
                job_post['Job Title'] = job_title
            except: 
                continue
            try:
                
                job_location = location + ' State'
                job_post['Job Location'] = job_location
            except:
                continue
            try:
                
                job_link =  base_url + job.h2.a['href']
                job_post['Job Link'] = job_link
            except:
                continue
            
            try:
                job_response = requests.get(job_link)
                job_doc = BeautifulSoup(job_response.content,"html.parser")
                job_doc = job_doc.find("div",class_ ="read-left-section")
                job_desc = job_doc.find("ul", class_ = "job-key-info")
                job_type = job_desc.find("li")
                job_type = job_type.find("span", class_ = "jkey-info")
                job_type = job_type.text
                
                
                job_post['Job Mode'] = job_type
                
            except:
                job_post['Job Mode'] = "Not Specified"
                job_post['Job Source'] = "MyJobMag.com"
            
            job_list.append(job_post)
        return job_list
        
       
        
    '''else:
        print("Could not scrape")
    
    if len(job_list) == 0:
        print("No jobs available")
    
    else:
        
        
        counter = 1    
        for job in job_list:
            print("JOB " + str(counter))
            counter += 1
            for k,v in job.items():
                print(k, ":", v)
                print("\n")'''
        
        
MyJobMag(search_term, location)        