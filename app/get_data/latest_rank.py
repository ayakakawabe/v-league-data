from selenium.webdriver.common.by import By

def latest(driver):
    article_section=driver.find_element(By.CLASS_NAME,"block_content_record_main")
    article_section_header=article_section.find_element(By.CLASS_NAME,"js_tab_head")
    # print(article_section_header.get_attribute('innerHTML'))
    a_tag_in_article_section_header=article_section_header.find_elements(By.TAG_NAME,"a")
    a_tag_in_article_section_header[1].click()
    url=driver.current_url
    print(url)
    driver.get(url)
    article_section=driver.find_element(By.CLASS_NAME,"block_content_record_main")
    # article_section_body=article_section.find_element(By.CLASS_NAME,"js_tab_body_item active col_men")
    article_section_title=article_section.find_element(By.TAG_NAME,"h2")
    article_section_tables=article_section.find_elements(By.TAG_NAME,"table")
    print(article_section_title.get_attribute("innerHTML"))
    table_titles=["team rank","player rank","player attack rank","player block rank"]
    for i in range(len(article_section_tables)):
        print(table_titles[i])
        rows=article_section_tables[i].find_elements(By.TAG_NAME,"tr")
        for j in range(len(rows)):
            print(rows[j].get_attribute("innerHTML"))