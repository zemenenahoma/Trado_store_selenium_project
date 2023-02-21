from selenium.webdriver.common.by import By


class AdminProductsLocators:
    page_title_products = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/h4/span")
    page_title_pro = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/nav/div[2]/a[2]/span[2]")
    phone_code = (By.XPATH, "//*[@id='root']/div[1]/div[2]/div/span/form/div[1]/div/span/div/input")
    form_submit_button = (By.XPATH, "//*[@id='root']/div[1]/div[2]/div/span/form/input")
    code_admin = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/span[1]/div[1]")
    form_login = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/span/form/input")
    remember_click = (By.XPATH, "//*[@id='root']/div[1]/div[2]/div/span/form/div[1]/div[2]/span/span")
    # **************************************************************************************************#
    page_titles = (By.XPATH, "//*[@id='root']/div[1]/div[2]/div/nav/div[2]/a[2]/span[2]")
    click_Products = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/nav/div[2]/a[2]")
    selection_point = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div[2]/div/div[1]/div/span/i")
    add_products = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div[2]/div/div[1]/div[2]/div/div[1]/span[1]/i")
    products_form = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/h4")

    product_search = (
    By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[1]/div[1]/span/span/div/input")

    bar_code = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/span/div/input")
    bar_code_error_message = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div")
    product_name = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[4]/span/div/input")
    product_error_message = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[4]/div")
    price = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[5]/span/div/input")
    price_error_message = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[5]/div")
    date = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[7]/span/div/input")
    description = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[8]/span/div/input")

    next_button = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[4]/input")
    products_more_info = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[1]/div[2]/span[1]")
    select_priority = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[1]/div[1]")

    priority1 = (
    By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[1]/div[1]/span[1]/div[2]/div/div[3]")

    sectionId = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div[1]/span[1]/div")
    exx_id = (
    By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div[1]/span[1]/div[2]/div/div[1]")
    product_tag = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[4]/div[1]/span[1]/div/input")
    short_tag = (
    By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[4]/div[1]/span[1]/div[2]/div/div[2]")
    departmentId = (
    By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[3]/div[1]/span[1]/div/input")
    department_list = (
    By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[3]/div[1]/span[1]/div[2]/div/div")
    store_id = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[5]/div[1]/span[1]/div")
    store_list = (
    By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[5]/div[1]/span[1]/div[2]/div/div[2]")
    parrall_importer = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[7]/span/span")

    more_page_next_button = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[4]/input[2]")
    unit_page = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[1]/div[3]/span[1]")

    select_list_symbol = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[1]/div[1]/span[2]")

    average_per_unit = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div[1]/div/span/span")
    value_avg_per_unit = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div[1]/div[2]/span/div/input")
    click_weight_unit = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div[1]/div[3]/div[1]/span[1]/div/input")
    weights_unit = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div[1]/div[3]/div[1]/span[1]/div[2]/div/div[1]")
    units_in_carton = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[3]/div[1]/div[1]/span/div/input")
    amount = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[3]/div[1]/div[2]/span/div/input")
    minimum_order_carton_count = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[3]/div[1]/div[3]/span/div/input")
    unit_next_button = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[4]/input[2]")
    unit_title = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/label")
    city = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div[1]/div[1]/span/div/input")
    street = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div[1]/div[2]/span/div/input")
    number = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[2]/div[1]/div[3]/span/div/input")
    contact_num = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[2]/div[3]/div[1]/div/span/div/input")
    ends_button = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/span/form/div[1]/div[5]/span[1]")


