from selenium.webdriver.common.by import By

man_v1:dict={
    "team":{},
    "player":{},
    "player_attak":{},
    "player_blok":{}
    }

man_v2:dict={
    "team":{},
    "player":{},
    "player_attak":{},
    "player_blok":{}
    }

man_v3:dict={
    "team":{},
    "player":{},
    "player_attak":{},
    "player_blok":{}
    }

women_v1:dict={
    "team":{},
    "player":{},
    "player_attak":{},
    "player_blok":{}
    }

women_v2:dict={
    "team":{},
    "player":{},
    "player_attak":{},
    "player_blok":{}
    }

women_v3:dict={
    "team":{},
    "player":{},
    "player_attak":{},
    "player_blok":{}
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
    print(team_rank_dict)

            

    

def get_player_attak_rank():
    pass

def get_player_blok_rank():
    pass

def get_man_v1_rank(driver):
    url=get_url(driver,0)
    driver.get(url)
    page_title=driver.find_element(By.TAG_NAME,"h2").get_attribute("innerHTML")
    get_team_rank(driver)
    

def latest(driver):
    get_man_v1_rank(driver)