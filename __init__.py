# streamlit_app.py
import streamlit as st
from Linkedln import linkedln
from Jobsguru import Jobsguru
from MyJobMag import MyJobMag
from hotnigerianjobs import hotnigerianjobs

# Streamlit app
def main():
    st.title("Job Aggregator")
    st.markdown(
        "Welcome to the Job Aggregator! Search for jobs across multiple websites with ease."
    )
    
    # Inputs for search term and location
    search_term = st.text_input("Enter the job title or keyword:", "")
    location = st.text_input("Enter the location (optional):", "")
    
    # Search button
    if st.button("Search"):
        if not search_term:
            st.error("Please enter a job title or keyword to search.")
        else:
            # Gather job listings
            with st.spinner("Fetching job listings..."):
                job_list = []

                try:
                    linkedln_results = linkedln(search_term, location)
                    job_list.extend(linkedln_results)
                except Exception as e:
                    st.warning(f"Error fetching LinkedIn jobs: {e}")

                try:
                    Jobsguru_results = Jobsguru(search_term)
                    job_list.extend(Jobsguru_results)
                except Exception as e:
                    st.warning(f"Error fetching Jobsguru jobs: {e}")

                try:
                    MyJobMag_results = MyJobMag(search_term, location)
                    job_list.extend(MyJobMag_results)
                except Exception as e:
                    st.warning(f"Error fetching MyJobMag jobs: {e}")

                try:
                    hotnigerianjobs_results = hotnigerianjobs(search_term)
                    job_list.extend(hotnigerianjobs_results)
                except Exception as e:
                    st.warning(f"Error fetching HotNigerianJobs jobs: {e}")

            # Display job listings
            if job_list:
                st.success(f"Found {len(job_list)} jobs for '{search_term}' in '{location}'.")
                for idx, job in enumerate(job_list, 1):
                    st.markdown(f"### Job {idx}")
                    for key, value in job.items():
                        st.markdown(f"**{key}:** {value}")
                    st.markdown("---")
            else:
                st.info("No jobs found. Try refining your search term or location.")

if __name__ == "__main__":
    main()
