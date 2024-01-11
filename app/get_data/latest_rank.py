from selenium.webdriver.common.by import By

men_v1:dict={
    "team":{},
    "player":{},
    "player_attack":{},
    "player_block":{},
    "player_green_card":{}
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
    driver.execute_script("window.scrollTo(0, 0);")
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


def get_player_rank(driver):
    player_rank_dict:dict={}
    button_parents=driver.find_elements(By.CLASS_NAME,"cmn_btn")
    button=button_parents[0].find_element(By.TAG_NAME,"a")
    button.click()
    player_rank_url=driver.current_url
    driver.get(player_rank_url)
    tbody=driver.find_element(By.TAG_NAME,"tbody")
    trs=tbody.find_elements(By.TAG_NAME,"tr")
    trs_data=trs[1:len(trs)]
    for tr in trs_data:
        tds=tr.find_elements(By.TAG_NAME,"td")
        rank=tds[0].get_attribute("innerHTML")
        name=tds[1].get_attribute("innerHTML").replace("&nbsp;","")
        team_name=tds[2].get_attribute("innerHTML")
        point=tds[3].get_attribute("innerHTML")
        game=tds[4].get_attribute("innerHTML")
        set=tds[5].get_attribute("innerHTML")
        attack=tds[6].get_attribute("innerHTML")
        block=tds[7].get_attribute("innerHTML")
        serve=tds[8].get_attribute("innerHTML")
        player_rank_dict_per_rank={
            "name":name,
            "team_name":team_name,
            "point":point,
            "game":game,
            "set":set,
            "attack":attack,
            "block":block,
            "serve":serve
        }
        if str(rank) in player_rank_dict:
            player_rank_dict[str(rank)].append(player_rank_dict_per_rank)
        else:
            player_rank_dict[str(rank)]=[player_rank_dict_per_rank]
    return player_rank_dict

def get_player_attack_rank(driver):
    player_attack_rank_dict:dict={}
    button_parents=driver.find_elements(By.CLASS_NAME,"cmn_btn")
    button=button_parents[1].find_element(By.TAG_NAME,"a")
    button.click()
    player_attack_rank_url=driver.current_url
    driver.get(player_attack_rank_url)
    tbody=driver.find_element(By.TAG_NAME,"tbody")
    trs=tbody.find_elements(By.TAG_NAME,"tr")
    trs_data=trs[1:len(trs)]
    for tr in trs_data:
        tds=tr.find_elements(By.TAG_NAME,"td")
        rank=tds[0].get_attribute("innerHTML")
        name=tds[1].get_attribute("innerHTML").replace("&nbsp;","")
        team_name=tds[2].get_attribute("innerHTML")
        shooting_rate=tds[3].get_attribute("innerHTML")
        game=tds[4].get_attribute("innerHTML")
        set=tds[5].get_attribute("innerHTML")
        success=tds[6].get_attribute("innerHTML")
        failure=tds[7].get_attribute("innerHTML")
        player_attack_rank_dict_per_rank={
            "name":name,
            "team_name":team_name,
            "shooting_rate":shooting_rate,
            "game":game,
            "set":set,
            "success":success,
            "failure":failure
        }
        if str(rank) in player_attack_rank_dict:
            player_attack_rank_dict[str(rank)].append(player_attack_rank_dict_per_rank)
        else:
            player_attack_rank_dict[str(rank)]=[player_attack_rank_dict_per_rank]
    return player_attack_rank_dict

def get_player_block_rank(driver):
    player_block_rank_dict:dict={}
    button_parents=driver.find_elements(By.CLASS_NAME,"cmn_btn")
    button=button_parents[2].find_element(By.TAG_NAME,"a")
    button.click()
    player_block_rank_url=driver.current_url
    driver.get(player_block_rank_url)
    tbody=driver.find_element(By.TAG_NAME,"tbody")
    trs=tbody.find_elements(By.TAG_NAME,"tr")
    trs_data=trs[1:len(trs)]
    for tr in trs_data:
        tds=tr.find_elements(By.TAG_NAME,"td")
        rank=tds[0].get_attribute("innerHTML")
        name=tds[1].get_attribute("innerHTML").replace("&nbsp;","")
        team_name=tds[2].get_attribute("innerHTML")
        average_per_set=tds[3].get_attribute("innerHTML")
        game=tds[4].get_attribute("innerHTML")
        set=tds[5].get_attribute("innerHTML")
        point=tds[6].get_attribute("innerHTML")
        player_block_rank_dict_per_rank={
            "name":name,
            "team_name":team_name,
            "average_per_set":average_per_set,
            "game":game,
            "set":set,
            "point":point
        }
        if str(rank) in player_block_rank_dict:
            player_block_rank_dict[str(rank)].append(player_block_rank_dict_per_rank)
        else:
            player_block_rank_dict[str(rank)]=[player_block_rank_dict_per_rank]
    return player_block_rank_dict

def get_player_green_card_rank(driver):
    player_green_card_rank_dict:dict={}
    button_parents=driver.find_elements(By.CLASS_NAME,"cmn_btn")
    button=button_parents[3].find_element(By.TAG_NAME,"a")
    button.click()
    player_green_card_rank_url=driver.current_url
    driver.get(player_green_card_rank_url)
    tbody=driver.find_element(By.TAG_NAME,"tbody")
    trs=tbody.find_elements(By.TAG_NAME,"tr")
    trs_data=trs[1:len(trs)]
    for tr in trs_data:
        tds=tr.find_elements(By.TAG_NAME,"td")
        rank=tds[0].get_attribute("innerHTML")
        name=tds[1].get_attribute("innerHTML").replace("&nbsp;","")
        team_name=tds[2].get_attribute("innerHTML")
        quantity=tds[3].get_attribute("innerHTML")
        game=tds[4].get_attribute("innerHTML")
        set=tds[5].get_attribute("innerHTML")
        player_green_card_rank_dict_per_rank={
            "name":name,
            "team_name":team_name,
            "quantity":quantity,
            "game":game,
            "set":set
        }
        if str(rank) in player_green_card_rank_dict:
            player_green_card_rank_dict[str(rank)].append(player_green_card_rank_dict_per_rank)
        else:
            player_green_card_rank_dict[str(rank)]=[player_green_card_rank_dict_per_rank]
    return player_green_card_rank_dict
        

def set_data_to_men_v1(driver):
    url=get_url(driver,0)
    driver.get(url)
    page_title=driver.find_element(By.TAG_NAME,"h2").get_attribute("innerHTML")
    print(page_title)
    men_v1["team"]=get_team_rank(driver)
    men_v1["player"]=get_player_rank(driver)
    driver.back()
    men_v1["player_attack"]=get_player_attack_rank(driver)
    driver.back()
    men_v1["player_block"]=get_player_block_rank(driver)
    driver.back()
    men_v1["player_green_card"]=get_player_green_card_rank(driver)
    print(men_v1)

def set_data_to_men_v2(driver):
    url=get_url(driver,1)
    driver.get(url)
    page_title=driver.find_element(By.TAG_NAME,"h2").get_attribute("innerHTML")
    print(page_title)
    men_v2["team"]=get_team_rank(driver)
    men_v2["player"]=get_player_rank(driver)
    driver.back()
    men_v2["player_attack"]=get_player_attack_rank(driver)
    driver.back()
    men_v2["player_block"]=get_player_block_rank(driver)
    driver.back()
    men_v2["player_green_card"]=get_player_green_card_rank(driver)
    print(men_v2)

def set_data_to_men_v3(driver):
    url=get_url(driver,2)
    driver.get(url)
    page_title=driver.find_element(By.TAG_NAME,"h2").get_attribute("innerHTML")
    print(page_title)
    men_v3["team"]=get_team_rank(driver)
    men_v3["player"]=get_player_rank(driver)
    driver.back()
    men_v3["player_attack"]=get_player_attack_rank(driver)
    driver.back()
    men_v3["player_block"]=get_player_block_rank(driver)
    driver.back()
    men_v3["player_green_card"]=get_player_green_card_rank(driver)
    print(men_v3)

def latest(driver):
    set_data_to_men_v1(driver)
    driver.back()
    set_data_to_men_v2(driver)
    driver.back()
    set_data_to_men_v3(driver)