from selenium.webdriver.common.by import By

men_v1:dict={
    "team":{},
    "player":{},
    "player_attack":{},
    "player_block":{}
    }

men_v2:dict={
    "team":{},
    "player":{},
    "player_attack":{},
    "player_block":{}
    }

men_v3:dict={
    "team":{},
    "player":{},
    "player_attack":{},
    "player_block":{}
    }

women_v1:dict={
    "team":{},
    "player":{},
    "player_attack":{},
    "player_block":{}
    }

women_v2:dict={
    "team":{},
    "player":{},
    "player_attack":{},
    "player_block":{}
    }

women_v3:dict={
    "team":{},
    "player":{},
    "player_attack":{},
    "player_block":{}
    }

def get_url(driver,league:int):
    article_section=driver.find_element(By.CLASS_NAME,"block_content_record_main")
    article_section_header=article_section.find_element(By.CLASS_NAME,"js_tab_head")
    a_tag_in_article_section_header=article_section_header.find_elements(By.TAG_NAME,"a")
    a_tag_in_article_section_header[league].click()
    url=driver.current_url
    return url

def get_team_rank(driver):
    team_rank_dict:dict={}
    table=driver.find_element(By.TAG_NAME,"table")
    tbody=table.find_element(By.TAG_NAME,"tbody")
    trs=tbody.find_elements(By.TAG_NAME,"tr")
    for tr in trs:
        tds=tr.find_elements(By.TAG_NAME,"td")
        rank=tds[0].get_attribute("innerHTML")
        team_logo_img=tds[1].find_element(By.TAG_NAME,"img").get_attribute("src")
        team_name=tds[1].find_element(By.TAG_NAME,"a").get_attribute("innerHTML")
        win=tds[2].get_attribute("innerHTML")
        loss=tds[3].get_attribute("innerHTML")
        win_ratio=tds[4].get_attribute("innerHTML")
        team_dict_per_rank={str(rank):
                   {
                       "team_logo_url":team_logo_img,
                       "team_name":team_name,
                       "win":win,
                       "loss":loss,
                       "win_ratio":win_ratio
                    }}
        team_rank_dict=dict(**team_rank_dict,**team_dict_per_rank)
    return team_rank_dict
            

    

def get_player_attack_rank(driver):
    button_parents=driver.find_elements(By.CLASS_NAME,"cmn_btn")
    button=button_parents[0].find_element(By.TAG_NAME,"a")
    button.click()
    player_attack_rank_url=driver.current_url
    driver.get(player_attack_rank_url)
    tbody=driver.find_element(By.TAG_NAME,"tbody")
    print(tbody.get_attribute("innerHTML"))
    pass

def get_player_block_rank():
    pass

def set_data_to_men_v1(driver):
    url=get_url(driver,0)
    driver.get(url)
    page_title=driver.find_element(By.TAG_NAME,"h2").get_attribute("innerHTML")
    men_v1["team"]=get_team_rank(driver)
    print(men_v1)
    get_player_attack_rank(driver)
    

def latest(driver):
    set_data_to_men_v1(driver)