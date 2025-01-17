# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 16:33:41 2025

@author: Oreoluwa
"""

from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

search_term = "Data Scientist"
format_str = "%d/%m/%Y"   

def month_mapping(month):
    if month == "january":
        return "01"
        
    elif month == "february":
        return "02"
    
    elif month == "march":
        return "03"
    
    elif month == "april":
        return "04"
    
    elif month == "may":
        return "05"
    
    elif month == "june":
        return "06"
    
    elif month == "july":
        return "07"
    
    elif month == "august":
        return "08"
    
    elif month == "september":
        return "09"
    
    elif month == "october":
        return "10"
    
    elif month == "november":
        return "11"
    
    elif month == "december":
        return "12"

def date_conversion(date):
    try:
        
        day = date.split(" ")[0][:-2]
        month = date.split(" ")[1].lower()[:-1]
        year = date.split(" ")[2][:-1]
    

        month = month_mapping(month)
        
        date_str = (day + "/" + month + "/" + year)
        new_date = datetime.strptime(date_str, format_str)
        return new_date
    
    except:
        return "Wrong"






def hotnigerianjobs(search_term):
    #base_url = "https://www.hotnigerianjobs.com/"
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
            except:
                continue
                
            
            job_response = requests.get(job_link)
            job_soup = BeautifulSoup(job_response.content, 'html.parser')
            job_document = job_soup.find_all("div",class_ = "mycase4")[-2]
            
            job_desc  = job_document.find_all("div")[1]
            job_desc = job_desc.find_all("div")[1].text
            
            match = re.search(r"Employment Type:\s*(.+)", job_desc)
            if match:
                employment_type = match.group(1).strip()
                
            else:
                employment_type = "Not Specified"
            
            job_post['Job Mode'] = employment_type
            
            
            
            '''The following block of code parses the application closing date listed on the website and
            compares it with the current date, if the job is outdated, then it will be removed from the job list'''
            
            application_closing_date = job_document.find_all("div")[-2].text.split("\n")[1]
            if application_closing_date == "Not Specified":

                pass
            
            else:
                
                if date_conversion(application_closing_date) == "Wrong":
                    pass
                
                elif date_conversion(application_closing_date) < datetime.now(): 
                    continue
                
                else:
                    job_post['Application Closing Date'] = application_closing_date
                    pass
                
            
                
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
    
    
hotnigerianjobs(search_term)
