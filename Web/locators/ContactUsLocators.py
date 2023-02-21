from selenium.webdriver.common.by import By


class ContactUsLocators:
    page_title = (By.XPATH, "//h3[contains(text(),'שירות לקוחות')]")
    indication_message_xpath = (By.XPATH, "//*[@id='contactForm']/div[1]/div[1]/div")
    option1 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[2]')
    option2 = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div[3]/div[1]')
    save = (By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/button')
    contact_us_xpath = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/a[1]")
    contact_us_header_color = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[1]/img")
    images_on_contact_us = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[3]/div/img")
    contact_us_header_text = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[1]/h4")
    contact_us_footer_existence = (By.XPATH, "//*[@id='root']/div/div[2]/div[3]/div")
    contact_us_form_image = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[2]/img")
    active_hours_text_title = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[3]/div/div/h3[1]")
    time_active_hours = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[3]/div/div/h3[2]")
    first_name_xpath = (By.XPATH, "//*[@id='contactForm']/div[1]/div[1]/span/input")
    last_name_xpath = (By.XPATH, "//*[@id='contactForm']/div[1]/div[2]/span/input")
    indication_message_last_name = (By.XPATH, "//*[@id='contactForm']/div[1]/div[2]/div")
    indication_message_xpath_first_name_xpath = (By.XPATH, "//*[@id='contactForm']/div[1]/div[1]/div")
    email_xpath = (By.XPATH, "//*[@id='contactForm']/div[1]/div[3]/span/input")
    indication_message_for_email_xpath = (By.XPATH, "//*[@id='contactForm']/div[1]/div[3]/div")
    phone_xpath = (By.XPATH, "//*[@id='contactForm']/div[1]/div[4]/span/input")
    validation_phone_number = (By.XPATH, "//*[@id='contactForm']/div[1]/div[4]/div")
    indication_message_for_phone_xpath = (By.XPATH,"//*[@id='contactForm']/div[1]/div[4]/div")
    content_referral_xpath = (By.XPATH, "//*[@id='contactForm']/div[1]/div[5]/textarea")
    indication_message_for_content_referral = (By.XPATH, "//*[@id='contactForm']/div[1]/div[5]/div")
    submit_xpath = (By.XPATH, "//*[@id='contactForm']/input")
    success_message_xpath = (By.XPATH, "//*[@id='contactForm']/div[3]")
    contact_us_phone_number_to_connect = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[3]/div/div/div/h3[2]")

    first_name_astrix = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/label[1]/span[1]")
    first_name_label = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/label[1]")
    last_name_astrix = (By.XPATH, "//*[@id='contactForm']/div[1]/div[2]/label/span")
    contact_us_page_bg_color = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[2]")
    contact_us_form_display = (By.XPATH, "//*[@id='contactForm']/div[1]")
    images_on_right_side_contact_us_form = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[1]/div')













