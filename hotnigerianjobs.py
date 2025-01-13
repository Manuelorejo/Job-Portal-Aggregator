# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:33:41 2025

@author: Oreoluwa
"""

from bs4 import BeautifulSoup
import requests
import re
#search_term = input("What job are you looking for? ")



def hotnigerianjobs(search_term):
    base_url = "https://www.hotnigerianjobs.com/"
    #location = input("Where do you want to work? ")
    url = f"https://www.hotnigerianjobs.com/index.php?csrf=1736175830&qid={search_term}"
    
    response = requests.get(url)
    
    def extract_text(text):
    # Define the pattern
        pattern = r"is located in (.*?) State"
        
        # Search for the pattern in the text
        match = re.search(pattern, text)
        
        if match:
            #extracted_text = match.group(0)  # Extracts the entire match (including "State")
            extracted_location = match.group(1)  # Extracts only the location (excluding "State")
            return(f"{extracted_location} State")
        else:
            return("Location Not Available.")
    
    
    job_list = []
    if response:
        
    
        soup = BeautifulSoup(response.content,'html.parser')
        
        document = soup.find("div",class_ = "wrapper")
        jobs = document.find_all("div",class_ = "mycase")
        
        for job in jobs:
            job_post = {}
            
            try:
                job_title = job.h1.text.strip()
                job_post['Job Title'] = job_title
            except:
                continue
            
            
            try: 
                job_link  = job.find_all("span",class_="semibio")[1].a['href']
                job_post['Job Link'] = job_link
                
            except:
                continue
            
            try:
                
                job_desc = job.find("div",class_ = 'mycase4')
                job_location = extract_text(job_desc.text)
                job_post['Job Location'] = job_location
                job_post['Job Source'] = "hotnigerianjobs.com"
            except:
                continue
                
                
                
            #if type(job_title) != type(None) and type(job_link) != type(None) and type(job_location) != type(None):
              
                
                
               
                
                
            job_list.append(job_post)
        return job_list
        
    '''else:
        print("Couldn't fetch")
    
    counter = 1
    for job in job_list:
        if len(job) == 0:
            job_list.remove(job)
        else:
            print("Job " + str(counter))
            for k,v in job.items():
                print(k, ": ",v)
            print("\n")
            counter += 1'''
    
    
#hotnigerianjobs(search_term)
