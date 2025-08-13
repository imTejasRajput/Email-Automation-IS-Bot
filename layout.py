import streamlit as st
from processing import clean_data
from emailsender import send_mail
import markdown
import time
from emailcreator import basic_email_creator, ai_email_creator
st.title("Email Automation")
st.write("Created with 💖 By Tejas Rajput.")

auth, data_settings, settings = st.tabs(["Authentication", "Data Settings","Settings"])

with auth:
    auth_container=auth.columns(1)[0]
    with auth_container:
        auth_container.title("Login")
        username = auth_container.text_input("Username",key='person_name')
        password = auth_container.text_input("Password", type="password",key='person_password')
        id_verify=auth_container.button(label='Verify',key='person_verify')
        auth_container.title("Email Credential",)
        entered_email = auth_container.text_input("Email",key='person_email')
        app_password = auth_container.text_input("App Password", type="password",key='person_email_password')
        email_verify=auth_container.button(label='Verify',key='person_email_verify')


with data_settings :
    data_container=data_settings.columns(1)[0]
    with data_container:
        data_container.title("Settings For Data")
        uploaded_file = data_container.file_uploader("Upload an Excel file", type=["xls", "xlsx"])
        if uploaded_file is not None:
            df= clean_data(uploaded_file)
            st.write("Excel file content:")
            st.dataframe(df) 

with settings:
    settings_container=settings.columns(1)[0]
    with settings_container:
        settings_container.title("Settings For Email")
        subjects=[  'Invitation to Be Recognized in Our Upcoming Leadership Edition',
                    'Feature Opportunity in Mashriq Leaders Magazine – Next Edition',
                    'Highlighting Leaders Making a Real Difference in Business',
                    'Shaping the Next Edition of Mashriq Leaders – Your Story Matters',
                    'Curating Inspiring Leadership Journeys – We’d Like to Include Yours',
                    'Editorial Feature Consideration – Mashriq Leaders Magazine',
                    'Showcasing Meaningful Leadership Stories – Let’s Connect',
                    'Contributing to Our Next Business Publication – You’re Invited',
                    'Documenting Leadership That Drives Change – Let’s Begin',
                    'Your Professional Journey Stands Out – Let’s Explore a Feature',
                  'Inquiry About Your Mental Health'
                ]
        settings_container.title("Select Your Domain Provider")
        selected_domain_provider=settings_container.selectbox(label='email subjects',options=['gmail','outlook'])
        settings_container.title("Select Subject")
        selected_subject=settings_container.selectbox(label='email subjects',options=subjects)
        settings_container.title("Select Currency")
        selected_currency=settings_container.radio(label='choose currency',options=['USD','AED'])
        settings_container.title("Set Pricing")
        selected_price=settings_container.text_input(key="pricing",label='enter price')
        
        settings_container.title("Choose Template")
        selected_template=settings_container.radio(label='templates',key='template_options',options=['Basic','Ai','Test'])
        
        settings_container.title("Enter Magazine Title")
        selected_magazine_title=settings_container.text_input(label='Enter The Magazine Title')
        
        settings_container.title("Enter Edition Title")
        selected_edition_title=settings_container.text_input(label='Enter The Edition Title')

        settings_container.title("Run Program")
      

        if settings_container.button(label='run button',key='run'):
            # Basic Template 
            if selected_subject and selected_currency is not None and selected_price and selected_template=='Basic' and uploaded_file is not None and selected_magazine_title is not None and selected_edition_title is not None and app_password is not None and entered_email is not None and selected_domain_provider is not None:
                settings_container.warning("All options are correct")
                for lead in clean_data(uploaded_file).itertuples():
                    email=basic_email_creator(name=lead.FirstName[0],magazine_title=selected_magazine_title,edition_title=selected_edition_title,price=selected_currency+' '+selected_price)
                    html_content = markdown.markdown(email)
                    send_mail(
                         'gmail',app_password,entered_email,lead.Email,lead.Name+' '+selected_subject,html_content 
                        )
                    settings_container.warning('mail sent')
                    time.sleep(30)
            else:
                settings_container.warning("Please Select All Options")

            # Ai Template
            if selected_subject and selected_currency is not None and selected_price and selected_template=='Ai' and uploaded_file is not None and selected_magazine_title is not None and selected_edition_title is not None and app_password is not None and entered_email is not None and selected_domain_provider is not None:
                settings_container.warning("All options are correct") 
                df= clean_data(uploaded_file)
                if not ( df['About'].isna().any() and df['Experience'].isna().any() ) :
                    for lead in clean_data(uploaded_file).itertuples():
                        email=ai_email_creator(name=lead.FirstName[0],magazine_title=selected_magazine_title,edition_title=selected_edition_title,price=selected_currency+' '+selected_price,about=lead.About)
                        html_content = markdown.markdown(email)
                        send_mail(
                            'gmail',app_password,entered_email,lead.Email,lead.Name+' '+selected_subject,html_content 
                            )
                        settings_container.success(body='mail sent')
                        time.sleep(20)
                else :
                    settings_container.warning("Data Should Not Have About And Education Section Empty For AI Template")

            # Test Template
            if selected_subject and selected_currency is not None and selected_price and selected_template=='Test' and uploaded_file is not None and selected_magazine_title is not None and selected_edition_title is not None and app_password is not None and entered_email is not None and selected_domain_provider is not None:
                settings_container.warning("All options are correct")
                for lead in clean_data(uploaded_file).itertuples():
                    email=test_email_creator()
                    html_content = markdown.markdown(email)
                    send_mail(
                         'gmail',app_password,entered_email,lead.Email,lead.Name+' '+selected_subject,html_content 
                        )
                    settings_container.warning('mail sent')
                    time.sleep(30)
            else:
                settings_container.warning("Please Select All Options")


            
     
