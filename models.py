from groq import Groq
import streamlit as st
import os
def summarise(about=None,experience=None):
    client = Groq(api_key= st.secrets["API_KEY"]
)

    if (not about) and (not experience ):
        return None
    else:
        if about and experience :
            response = client.chat.completions.create(
            model="llama3-8b-8192",  # Available models: llama3-8b-8192, mixtral-8x7b-32768, etc.
            messages=[
                    {"role": "system", "content": "You are a summary creator,you just give the output ,you do not add any of your own words like, here is the output or similar."},
                    {"role": "user", "content": f"About : {about} , Experience : {experience} \n give the summarise form of the above information , summarise output should not  exceed  300 word limit " }
                        ],
            temperature=0.7,
            max_tokens=200 )
            return response.choices[0].message.content
        elif about :
            response = client.chat.completions.create(
            model="llama3-8b-8192",  # Available models: llama3-8b-8192, mixtral-8x7b-32768, etc.
            messages=[
                    {"role": "system", "content": "You are a summary creator,you just give the output ,you do not add any of your own words like, here is the output or similar."},
                    {"role": "user", "content": f"About : {about} \n give the summarise form of the above information , summarise output should not  exceed  300 word limit " }
                        ],
            temperature=0.7,
            max_tokens=200 )
            return response.choices[0].message.content
        else:
            response = client.chat.completions.create(
            model="llama3-8b-8192",  # Available models: llama3-8b-8192, mixtral-8x7b-32768, etc.
            messages=[
                    {"role": "system", "content": "You are a summary creator,you just give the output ,you do not add any of your own words like, here is the output or similar."},
                    {"role": "user", "content": f"Experience : {experience} \n give the summarise form of the above information , summarise output should not  exceed  300 word limit " }
                        ],
            temperature=0.7,
            max_tokens=200 )
            return response.choices[0].message.content
            
        
        


# Create Groq client

client = Groq(api_key="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")

def create_response(about=None,experience=None) :
    summarise_info=summarise(about,experience)
    prompt= f"""
            Instruction :Using the information given in the following 'About the lead' section, create the output which has the same tone and structure as given in the following 'Example' section, you just give the output ,you do not add any of your own words like, here is the output or similar.

            About the lead :{summarise_info} 

            Example :  Your leadership in sustainability has been instrumental in advancing projects focused on strategic insights that advance sustainable energy solutions  and delivering measurable, impactful results. and Energy Management,and shaping the future of environmentally responsible development."""
    response = client.chat.completions.create(
    model="llama3-8b-8192",  # Available models: llama3-8b-8192, mixtral-8x7b-32768, etc.
    messages=[
        {"role": "system", "content": "You are an email creator."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=200
            )
    return response.choices[0].message.content


