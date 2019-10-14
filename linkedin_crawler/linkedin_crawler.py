from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import time as tm
import pandas as pd
import requests
import re
import random


df = pd.read_excel('ICE DANCING AND WRESTLING.xlsx')
a = list(df['url'])
b = a[1300:1450]
# b = ['https://www.linkedin.com/in/david-mayekawa-9284341/']
# b = ["https://www.linkedin.com/in/justyna-bednarek-17973aa8/"]


proxy = {'address': '23.106.244.56:29842',
         'username': 'cinc',
         'password': 'VLh6Q9Wt'}

capabilities = dict(DesiredCapabilities.CHROME)
capabilities['proxy'] = {'proxyType': 'MANUAL',
                         'httpProxy': proxy['address'],
                         'ftpProxy': proxy['address'],
                         'sslProxy': proxy['address'],
                         'noProxy': '',
                         'class': "org.openqa.selenium.Proxy",
                         'autodetect': False}

capabilities['socks_username'] = proxy['username']
capabilities['socks_password'] = proxy['password']


# chrome_options = Options()
# chrome_options.headless = False
# browser = webdriver.Chrome(desired_capabilities=capabilities, chrome_options=chrome_options)

chrome_options = Options()
chrome_options.headless = False
browser = webdriver.Chrome(executable_path = '/home/algoscale/Documents/Crawling/Linkedin/chromedriver',desired_capabilities=capabilities, chrome_options=chrome_options)

browser.get("http://www.linkedin.com/uas/login")
username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys("JULISSA_Angeles9923@hotmail.com")
password.send_keys("QwErTy10278!@#$")
login_attempt = browser.find_element_by_class_name("from__button--floating").click()


# ALTERNATE LOGIN


# try:
#     browser.get("https://www.linkedin.com")
# except Exception as e:
#     print("url get exception")
#     print(e)


# try:

#     username = browser.find_element_by_id("login-email")
#     password = browser.find_element_by_id("login-password")

#     username.send_keys("claytonolinger@mail.ru")
#     password.send_keys("4Uxu3ezlcu4R")

#     login_attempt = browser.find_element_by_id("login-submit").click()
#     # login_attempt = browser.find_element_by_class_name("from__button--floating").click()


# except Exception as e:
#     print("login exception")
#     print(e)


# contact_info = browser.find_element_by_css_selector(".pv-top-card-v2-section__entity-name.pv-top-card-v2-section__contact-info.ml2.t-14.t-black.t-bold")
# if contact_info:
#     contact_info.click()
#     time.sleep(5)
# x = 'artdeco-modal'
# soup = BeautifulSoup(browser.page_source, 'lxml')
# modal = soup.find('div', attrs={'id': 'artdeco-modal-outlet'})
# print(modal.prettify())
# data = str(modal)
# # for items_list in modal.find_all('header', class_="pv-contact-info__header"):
# #     item = (items_list.text).replace('\n', '').strip()
# #     print(item)

# # print('---------')
# # for items_list in modal.find_all('div', class_="pv-contact-info__ci-container"):
# #     item = (items_list.text).replace('\n', '').strip()
# #     print(item)
# tags = re.split("<.*>", data)
# print(tags)
# for i in tags:
#     if i != '\\n' and len(i) < 100:
#         print(i.replacesa('\n', '').strip())
# time.sleep(5)

ii = 100
# --------------------------------------------------------------------------------------    NEW CODE
for url in b:
    # tm.sleep(30)
    ii += 1
    print("------------------------>>>>>>>>>>>>>>>>>>>>>>> {}".format(ii))
    # if ii == 2:
    #     break
    browser.get(url)
    tm.sleep((random.randint(1, 5)) * 8)
    # tm.sleep(30)
    # soup = BeautifulSoup(browser.page_source, 'lxml')
    # print(soup.prettify(), file=open('full_page_source_server.html', 'w'))
    # f = open('skills_expanded1.html', 'w')
    # f.write(str(skills.prettify()))
    # f.close()

    try:
        contact_info = browser.find_element_by_css_selector(".pv-top-card-v2-section__entity-name.pv-top-card-v2-section__contact-info.ml2.t-14.t-black.t-bold")
        if contact_info:
            contact_info.click()
            tm.sleep(5)

        print(">>>>>>>>>>>------------ before headings")
        headings = browser.find_elements_by_css_selector('.t-16.t-black.t-bold')
        headings_values = browser.find_elements_by_css_selector('.t-14.t-black.t-normal')
        # for i in range(len(headings)):
        #     print(headings[i].text,headings_values[i].text)
    except Exception as e:
        print(e)

    each_profile = {}

    contact_info_dict = dict()
    try:
        contact_info_dict['Linkedin Profile'] = headings_values[1].text
    except:
        contact_info_dict['Linkedin Profile'] = ""

    try:
        contact_info_dict['Website'] = headings_values[2].text
    except:
        contact_info_dict['Website'] = 0

    try:
        contact_info_dict['birthday'] = headings_values[3].text
    except:
        contact_info_dict['birthday'] = ""

    print(contact_info_dict)

    each_profile.update({"contact_info": contact_info_dict})

    # for i in headings:
    #     print(i.text)

    # print()
    # for i in headings_values:
    #     print(i.text)

    # x = 'artdeco-modal'
    # soup = BeautifulSoup(browser.page_source, 'lxml')
    # modal = soup.find('div', attrs={'id': 'artdeco-modal-outlet'})
    # # print(modal.prettify())
    # print('before modal >>>>>>>>>>>')
    # for heading in modal.find_all('header', class_ = 't-16 t-black t-bold'):
    #     print(heading)

    # print('---------------')
    # for heading in modal.find_all('header', class_ = 't-14 t-black t-normal'):
    #     print(heading)

    try:
        browser.find_element_by_css_selector('#artdeco-modal-outlet button.artdeco-dismiss').click()
    except:
        pass

    firstName = ""
    lastName = ""
    full_name = ''
    try:
        full_name = browser.find_element_by_class_name("pv-top-card-section__name").text
    except:
        pass

    if full_name:
        each_profile.update({"fullName": full_name})
    else:
        each_profile.update({"fullName": ""})

    # each_profile.update({"profileId": memberID})
    # each_profile.update({"publicUrl": url})
    each_profile.update({"industry": ""})

    '''scroll down'''
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    tm.sleep(5)

    additional_info = {}

    each_profile.update({"original_linkedin_url": url})

    each_profile.update({"additional_info": {"email": "", "birthday": ""}})

    try:
        avatar_profile_img = browser.find_element_by_class_name('pv-top-card-section__image').get_attribute('src')
        if avatar_profile_img:
            each_profile.update({"avatar": avatar_profile_img})
    except:
        each_profile.update({"avatar": ""})

    try:
        location = browser.find_element_by_class_name('pv-top-card-section__location')
        if location:
            each_profile.update({"location": location.text})
            # print "location",location.txt
        else:
            each_profile.update({"location": ""})
            # print "location not extracted",location.txt
    except:
        each_profile.update({"location": ""})

    try:
        # connections = browser.find_element_by_class_name(
        #     'pv-top-card-section__connections').find_element_by_css_selector('span').text

        connections = browser.find_element_by_class_name(
            'pv-top-card-v2-section__connections').text
        each_profile.update({"connections": connections})

        print("-------------------->>>>>>>>>>>>>>> {}".format(connections))
        # print "connections",connections
    except Exception as e:
        # print e,"connections"
        each_profile.update({"connections": ""})

    try:
        description = browser.find_element_by_class_name('button-tertiary-small')
        description.click()
        browser.switch_to.window(browser.window_handles[0])
    except:
        try:
            description = browser.find_element_by_class_name('truncate-multiline--button')
            description.click()
            browser.switch_to.window(browser.window_handles[0])
        except Exception as e:
            pass

    tm.sleep(2)
    try:
        summary = browser.find_element_by_class_name('pv-top-card-section__summary-text').text
        # print("summary IS ------------->>>>>>>>>>>>>>>>>>>>>> {}".format(summary))
        # if summary == " " or not summary:
        #     summary = browser.find_element_by_class_name('truncate-multiline--truncation-target').text.encode(
        #         'utf-8')
        # elif "See less" in summary:
        #     summary = str(summary).replace("See less", "")

        print("summary IS ------------->>>>>>>>>>>>>>>>>>>>>> {}".format(summary))
        each_profile.update({"summary": summary})
        # print "summary",summary
    except:
        each_profile.update({"summary": ""})

    imax = 0
    try:
        certification = browser.find_element_by_xpath(
            "//button[@data-control-name='accomplishments_expand_certifications']")
        if certification:
            certification.click()
            browser.switch_to.window(browser.window_handles[0])
            tm.sleep(2)
            while imax < 10:
                if browser.find_element_by_xpath(
                        "//button[@aria-controls='certifications-accomplishment-list']").text != 'Show less certifications':
                    browser.find_element_by_xpath(
                        "//button[@aria-controls='certifications-accomplishment-list']").click()
                    browser.switch_to.window(browser.window_handles[0])
                    tm.sleep(2)
                else:
                    break
                imax += 1
    except:
        pass

    certificates = []

    # tm.sleep(3)
    try:
        certifications = browser.find_element_by_class_name('certifications')
        if not certifications:
            each_profile.update({"certifications": certificates})

        else:
            certifications = browser.find_element_by_class_name('certifications').find_elements_by_tag_name('li')
            for i in range(len(certifications)):
                try:
                    name = browser.find_element_by_class_name('certifications').find_elements_by_tag_name('li')[
                        i].find_element_by_tag_name('h4').text.encode(
                        'utf-8')
                    if name:
                        name = str(name).replace("Title", "").strip()
                    else:
                        name = ""
                except:
                    name = ""

                try:
                    date = browser.find_element_by_class_name('certifications').find_elements_by_tag_name('li')[
                        i].find_element_by_class_name('pv-accomplishment-entity__date').text
                    if date:
                        date = date.encode("utf-8").split("–")
                        if 'Certification Date' in date:
                            date = date.repalce("Certification Date", "")
                        date = "starting " + str(date[0]).strip()
                    else:
                        date = ""
                except:
                    date = ""

                try:
                    licence_name = \
                        browser.find_element_by_class_name('certifications').find_elements_by_tag_name('li')[
                            i].find_element_by_class_name('pv-accomplishment-entity__license')
                    source_name = \
                        browser.find_element_by_class_name('certifications').find_elements_by_tag_name('li')[
                            i].find_element_by_class_name('Sans-15px-black-55%')
                    if licence_name and source_name:
                        certification_authority = \
                            browser.find_element_by_class_name('certifications').find_elements_by_tag_name('li')[
                                i].find_element_by_class_name('Sans-15px-black-55%').text.replace(
                                "Certification authority", "").strip()
                        license_name = \
                            browser.find_element_by_class_name('certifications').find_elements_by_tag_name('li')[
                                i].find_element_by_class_name('pv-accomplishment-entity__license').text
                        source = certification_authority + "," + license_name
                    elif source_name:
                        source = \
                            browser.find_element_by_class_name('certifications').find_elements_by_tag_name('li')[
                                i].find_element_by_class_name('Sans-15px-black-55%').text.replace(
                                "Certification authority", "").strip()
                    else:
                        source = ""
                except:
                    source = ""

                if name or date or source:
                    each = {"name": name, "source": source, "date": date}
                else:
                    continue
                certificates.append(each)

    except:
        pass
    each_profile.update({"certifications": certificates})
    # print "certificates",certificates

    # print "looping back...3"
    # tm.sleep(3)
    imax = 0
    try:
        honor = browser.find_element_by_xpath(
            "//button[@data-control-name='accomplishments_expand_honors']")
        if honor:
            honor.click()
            browser.switch_to.window(browser.window_handles[0])
            tm.sleep(2)
            while imax < 10:
                if browser.find_element_by_xpath(
                        "//button[@aria-controls='honors-accomplishment-list']").text != 'Show less honors':
                    browser.find_element_by_xpath("//button[@aria-controls='honors-accomplishment-list']").click()
                    browser.switch_to.window(browser.window_handles[0])
                    tm.sleep(2)
                else:
                    break
                imax += 1
    except:
        pass

    # tm.sleep(1)
    honors = []
    try:
        honors_data = browser.find_element_by_class_name('honors')
        if not honors_data:
            each_profile.update({"honors": honors})
        else:
            all_honor = browser.find_element_by_class_name('honors').find_elements_by_tag_name('li')
            for i in range(len(all_honor)):
                try:
                    name = browser.find_element_by_class_name('honors').find_elements_by_tag_name('li')[
                        i].find_element_by_tag_name('h4').text.encode(
                        'utf-8')
                    if name:
                        name = str(name).replace("honor title", "").strip()
                    else:
                        name = ""
                except:
                    name = ""

                try:
                    issuer = browser.find_element_by_class_name('honors').find_elements_by_tag_name('li')[
                        i].find_element_by_class_name("pv-accomplishment-entity__issuer").text.encode(
                        'utf-8')
                    if issuer:
                        given_by = str(issuer).replace("honor issuer", "").strip()
                    else:
                        given_by = ""
                except:
                    given_by = ""

                try:
                    date = browser.find_element_by_class_name('honors').find_elements_by_tag_name('li')[
                        i].find_element_by_class_name("pv-accomplishment-entity__date").text.encode(
                        'utf-8')
                    if date:
                        date = str(date).replace("honor date", "").strip()
                    else:
                        date = ""
                except:
                    date = ""

                try:
                    honour_description = \
                        browser.find_element_by_class_name('honors').find_elements_by_tag_name('li')[
                            i].find_element_by_class_name("pv-accomplishment-entity__description").text.encode(
                            'utf-8')
                    if honour_description and "honor description" in honour_description:
                        description = str(honour_description).replace("honor description", "").strip()
                    else:
                        description = ""
                except:
                    description = ""
                if name or date or given_by or description:
                    each = {"name": name, "given_by": given_by, "description": description, 'date': date}
                    honors.append(each)

    except:
        pass
    each_profile.update({"honors": honors})
    # print "honors",honors

    # tm.sleep(3)
    imax = 0
    try:
        publication = browser.find_element_by_xpath(
            "//button[@data-control-name='accomplishments_expand_publications']")
        if publication:
            publication.click()
            browser.switch_to.window(browser.window_handles[0])
            tm.sleep(1)
            while imax < 10:
                if browser.find_element_by_xpath(
                        "//button[@aria-controls='publications-accomplishment-list']").text != 'Show less publications':
                    browser.find_element_by_xpath(
                        "//button[@aria-controls='publications-accomplishment-list']").click()
                    browser.switch_to.window(browser.window_handles[0])
                    tm.sleep(1)
                else:
                    break
                imax += 1
    except:
        pass

    publications = []
    try:
        publications_data = browser.find_element_by_class_name('publications')
        if not publications_data:
            each_profile.update({"publications": publications})
        else:
            all_publications = browser.find_element_by_class_name('publications').find_elements_by_tag_name('li')
            for i in range(len(all_publications)):
                try:
                    name = browser.find_element_by_class_name('publications').find_elements_by_tag_name('li')[
                        i].find_element_by_tag_name('h4').text.encode(
                        'utf-8')
                    if name:
                        name = str(name).replace("publication title", "").strip()
                    else:
                        name = ""
                except:
                    name = ""

                try:
                    date = browser.find_element_by_class_name('publications').find_elements_by_tag_name('li')[
                        i].find_element_by_class_name("pv-accomplishment-entity__date").text.encode(
                        'utf-8')
                    if date:
                        date = str(date).replace("publication date", "").strip()
                    else:
                        date = ""
                except:
                    date = ""

                try:
                    description = \
                        browser.find_element_by_class_name('publications').find_elements_by_tag_name('li')[
                            i].find_element_by_class_name("pv-accomplishment-entity__description").text.encode(
                            'utf-8')
                    if "publication description" in description:
                        description = str(description).replace("publication description", "").strip()
                    else:
                        description = ""
                except:
                    description = ""
                if name or date or description:
                    each = {"name": name, "description": description, 'date': date}
                    publications.append(each)

    except:
        pass
    each_profile.update({"publications": publications})
    # print "publications",publications

    imax = 0
    tm.sleep(1)
    try:
        project = browser.find_element_by_xpath(
            "//button[@data-control-name='accomplishments_expand_projects']")
        if project:
            project.click()
            browser.switch_to.window(browser.window_handles[0])
            tm.sleep(1)
            while imax < 10:
                if browser.find_element_by_xpath(
                        "//button[@aria-controls='projects-accomplishment-list']").text != 'Show less projects':
                    browser.find_element_by_xpath("//button[@aria-controls='projects-accomplishment-list']").click()
                    browser.switch_to.window(browser.window_handles[0])
                    tm.sleep(1)
                else:
                    break
                imax += 1
    except:
        pass

    projects = []
    try:
        projects_data = browser.find_element_by_class_name('projects')
        if not projects_data:
            each_profile.update({"projects": projects})
        else:
            all_projects = browser.find_element_by_class_name('projects').find_elements_by_tag_name('li')
            for i in range(len(all_projects)):
                try:
                    name = browser.find_element_by_class_name('projects').find_elements_by_tag_name('li')[
                        i].find_element_by_tag_name('h4').text.encode(
                        'utf-8')
                    if name:
                        name = str(name).replace("Project name", "").strip()
                    else:
                        name = ""
                except:
                    name = ""

                try:
                    date = browser.find_element_by_class_name('projects').find_elements_by_tag_name('li')[
                        i].find_element_by_class_name("pv-accomplishment-entity__date").text.encode(
                        'utf-8')
                    if date:
                        date = str(date).strip()
                    else:
                        date = ""
                except:
                    date = ""

                try:
                    description = browser.find_element_by_class_name('projects').find_elements_by_tag_name('li')[
                        i].find_element_by_class_name("pv-accomplishment-entity__description").text.encode(
                        'utf-8')
                    if "Project description" in description:
                        description = str(description).replace("Project description", "").strip()
                    else:
                        description = ""
                except:
                    description = ""
                if name or date or description:
                    each = {"name": name, "description": description, 'date': date}
                    projects.append(each)

    except:
        pass
    each_profile.update({"projects": projects})

    try:
        browser.find_element_by_class_name("pv-skills-section__additional-skills").click()
        browser.switch_to.window(browser.window_handles[0])
    except:
        pass

    tm.sleep(1)
    tag_votes = []
    try:
        tags = browser.find_elements_by_class_name("pv-skill-entity--featured")
        if not tags:
            each_profile.update({"tags_votes": tag_votes})
        else:
            for i in tags:
                key = i.find_element_by_class_name("pv-skill-entity__skill-name")
                try:
                    value = i.find_element_by_class_name("pv-skill-entity__endorsement-count")
                except:
                    value = None
                if key is not None and value is not None:
                    tag_votes.append({key.text: value.text})
                elif key and value is None:
                    tag_votes.append({key.text: 0})
                else:
                    tag_votes.append({"tags_votes": tag_votes})

            each_profile.update({"tags_votes": tag_votes})
      #      print "tag_votes",tag_votes
    except:
        each_profile.update({"tags_votes": tag_votes})

    # print each_profile
    try:
        recommendations = browser.find_elements_by_xpath("//button[@aria-controls='recommendation-list']")
        if recommendations:
            recommendations[0].click()
            browser.switch_to.window(browser.window_handles[0])
            while (len(browser.find_elements_by_xpath("//button[@aria-controls='recommendation-list']")) > 1):
                tm.sleep(1)
                if browser.find_elements_by_xpath("//button[@aria-controls='recommendation-list']")[
                        0].text == "Show less":
                    break
                else:
                    browser.find_elements_by_xpath("//button[@aria-controls='recommendation-list']")[0].click()
                    browser.switch_to.window(browser.window_handles[0])

    except Exception as e:
        pass

    recommendation_received = []
    try:
        recommendations = browser.find_element_by_id("recommendation-list")
        # browser.find_element_by_class_name("pv-recommendations-section")
        if not recommendations:
            each_profile.update({"recommendation_received": recommendation_received})
        else:
            all_recommendation = browser.find_element_by_id("recommendation-list").find_elements_by_tag_name('li')
            for i in range(len(all_recommendation)):
                try:
                    endorser_details = \
                        browser.find_element_by_id("recommendation-list").find_elements_by_tag_name('li')[
                            i].find_element_by_class_name("pv-recommendation-entity__headline").text
                    title = endorser_details.split(" ")
                    # sentence = nltk.word_tokenize(endorser_details)
                    # sent = pos_tag(sentence)
                    if "at" in title:
                        index = title.index("at")
                        endorser_title = title[:index]
                        endorser_title = " ".join(endorser_title)
                        endorser_companyname = title[index + 1:]
                        endorser_companyname = " ".join(endorser_companyname)
                    else:
                        endorser_title = endorser_details
                        endorser_companyname = ""
                except:
                    endorser_details = ""
                    endorser_title = ""
                    endorser_companyname = ""
                try:
                    description = browser.find_element_by_id("recommendation-list").find_elements_by_tag_name('li')[
                        i].find_element_by_class_name("pv-recommendation-entity__text").text.encode('utf-8').strip()
                except:
                    description = ""
                try:
                    date_additional = \
                        browser.find_element_by_id("recommendation-list").find_elements_by_tag_name('li')[
                            i].find_element_by_class_name("rec-extra").text.encode('utf-8').strip()
                    date_additional = str(date_additional).split(",")
                    additional = date_additional[2]
                    endorsement_date = str(date_additional[0] + date_additional[1]).strip()
                except:
                    additional = ""
                    endorsement_date = ""
                try:
                    name = browser.find_element_by_id("recommendation-list").find_elements_by_tag_name('li')[
                        i].find_element_by_class_name("pv-recommendation-entity__detail").find_element_by_tag_name(
                        "h3").text.encode('utf-8').strip()
                    endorser_name = name
                except:
                    endorser_name = ""
                if description or additional or endorsement_date or endorser_name or endorser_details or endorser_companyname or endorser_title:
                    each = {"description": description, "additional": additional,
                            "endorsementDate": endorsement_date,
                            "endorserName": endorser_name, "endorserDetails": endorser_details,
                            "endorserCompanyName": endorser_companyname, "endorserTitle": endorser_title}
                    recommendation_received.append(each)

    except:
        pass
    each_profile.update({"recommendation_received": recommendation_received})
    # print "recommendation_received",recommendation_received

    imax = 0
    '''this block is expanding education'''
    try:
        browser.find_element_by_class_name("education-section").find_element_by_class_name(
            "pv-profile-section__see-more-inline").click()
        browser.switch_to.window(browser.window_handles[0])
        while imax < 10:
            tm.sleep(1)
            if browser.find_element_by_class_name("education-section").find_element_by_class_name(
                    "pv-profile-section__see-more-inline"):
                browser.find_element_by_class_name("education-section").find_element_by_class_name(
                    "pv-profile-section__see-more-inline").click()
                browser.switch_to.window(browser.window_handles[0])
            else:
                break
            imax += 1
    except:
        pass

    # print "looping back..5"
    # tm.sleep(3)

    imax = 0
    '''this block is for expanding description of education'''
    try:
        while imax < 10:
            tm.sleep(1)
            data = browser.find_element_by_class_name('education-section').find_element_by_class_name(
                'pv-profile-section__show-more-detail')
            if data:
                data.click()
                browser.switch_to.window(browser.window_handles[0])
            else:
                break
            imax += 1
    except:
        pass

    tm.sleep(5)

    degree_data = []

    try:
        all_degree = browser.find_element_by_class_name("education-section").find_elements_by_tag_name("li")
        print('---------------------!!!!!!!!!!!!!!!!!!!!!! IN DEGREE')
        # webdriver.Chrome().get_screenshot_as_file('chal_gaya.png')
        for i in range(len(all_degree)):

            try:
                # tm.sleep(2)
                school_id = browser.find_element_by_class_name("education-section").find_elements_by_tag_name("li")[
                    i].find_element_by_tag_name("a").get_attribute("href")
                school_id = str(school_id).split("/")
                school_id = school_id[-2]
                if ":" in school_id:
                    school_id = school_id.split(":")[1]
            except:
                school_id = ""

            try:
                additional = \
                    browser.find_element_by_class_name("education-section").find_elements_by_tag_name("li")[
                        i].find_element_by_class_name("pv-entity__description").text.strip()
            except:
                additional = ""

            try:
                # tm.sleep(2)
                activities = \
                    browser.find_element_by_class_name("education-section").find_elements_by_tag_name("li")[
                        i].find_element_by_class_name("activities-societies").text.strip()
            except:
                activities = ""
            try:
                # tm.sleep(2)
                school = browser.find_element_by_class_name("education-section").find_elements_by_tag_name("li")[
                    i].find_element_by_tag_name("h3").text
            except:
                school = ""

            try:
                # tm.sleep(2)
                major = browser.find_element_by_class_name("education-section").find_elements_by_tag_name("li")[
                    i].find_element_by_class_name("pv-entity__fos").find_element_by_class_name(
                    "pv-entity__comma-item").text
            except:
                major = ""

            try:
                # tm.sleep(2)
                duration = browser.find_element_by_class_name("education-section").find_elements_by_tag_name("li")[
                    i].find_element_by_class_name("pv-entity__dates").find_elements_by_tag_name("time")
                start_date = end_date = ""
                if len(duration) == 2:
                    start_date = duration[0].text
                    end_date = duration[1].text
                elif len(duration) == 1:
                    start_date = duration[0].text
                    end_date = "Present"
                else:
                    start_date = ""
                    end_date = ""
            except:
                start_date = ""
                end_date = ""

            try:
                degree = browser.find_element_by_class_name("education-section").find_elements_by_tag_name("li")[
                    i].find_element_by_class_name("pv-entity__degree-name").find_element_by_class_name(
                    "pv-entity__comma-item").text
            except:
                degree = ""
            if school_id or additional or school or activities or major or start_date or end_date or degree:
                each = {"school_id": school_id, "additional": additional, "activities": activities,
                        "school": school, "major": major, "startDate": start_date, "endDate": end_date,
                        "degree": degree}
            else:
                continue
            degree_data.append(each)

    except Exception as e:
        # webdriver.Chrome().get_screenshot_as_file('fatt_gaya.png')
        print(e)
        # print e,"degree  exception",degree_data
        pass
    each_profile.update({"degree": degree_data})
    # print "degree",degree_data
    # print "looping back..6"
    '''this block is expanding experience'''
    imax = 0
    try:
        browser.find_element_by_class_name('background-details').find_element_by_class_name("experience-section").find_element_by_class_name(
            "pv-profile-section__see-more-inline").click()
        browser.switch_to.window(browser.window_handles[0])
        tm.sleep(2)
        while imax < 10:
            tm.sleep(2)
            if browser.find_element_by_class_name('background-details').find_element_by_class_name("experience-section").find_element_by_class_name(
                    "pv-profile-section__see-more-inline"):
                browser.find_element_by_class_name('background-details').find_element_by_class_name("experience-section").find_element_by_class_name(
                    "pv-profile-section__see-more-inline").click()
                browser.switch_to.window(browser.window_handles[0])
            else:
                break
            imax += 1
    except:
        pass
    imax = 0

    # print "looping back..6.05"
    tm.sleep(1)

    '''this block is for expanding description of experience'''
    try:
        while imax < 10:
            tm.sleep(2)
            data = browser.find_element_by_class_name('background-details').find_element_by_class_name('experience-section').find_element_by_class_name(
                'pv-profile-section__show-more-detail')
            if data:
                data.click()
                browser.switch_to.window(browser.window_handles[0])
            else:
                break
            imax += 1
    except:
        pass

    # print "looping back.6.1"
    tm.sleep(2)

    employements = []

    try:

        print('EXPERIENCE SECTION STARTS -????????????????????????????????????')
        # browser.find_element_by_class_name('pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle link').click()
        tm.sleep(2)
        button_output = browser.find_element_by_css_selector('button.pv-profile-section__see-more-inline.pv-profile-section__text-truncate-toggle.link').click()
        # tm.sleep(5)
        # button_output = browser.find_element_by_xpath("//*[@id='oc-background-section']")
        # button_output = browser.find_element_by_css_selector('pv-profile-section experience-section ember-view')
        button_output = browser.find_element_by_id('experience-section')
        print(button_output.text)
        # print('Show 5 more experiences' in browser.page_source)
        print('button clicked successfully')
    except:
        print('Button not clicked in employements')

    try:
        # print browser.find_element_by_class_name('experience-section'),"---------------------------------------------"
        all_employement = browser.find_element_by_class_name('background-details').find_element_by_class_name("experience-section").find_elements_by_tag_name("li")

        for i in range(len(all_employement)):

            try:
                tm.sleep(1)
                company_id = \
                    browser.find_element_by_class_name('experience-section').find_elements_by_tag_name("li")[
                        i].find_element_by_tag_name("a").get_attribute("href")
                company_id = str(company_id).split("/")
                company_id = company_id[-2]

                if ":" in company_id:
                    company_id = company_id.split(":")[1]

            except Exception as e:
                company_id = ""

            try:
                # tm.sleep(2)
                description = browser.find_element_by_class_name('experience-section').find_elements_by_tag_name("li")[i].find_element_by_class_name("pv-entity__description").text
            except:
                description = ""

            try:
                # tm.sleep(2)
                title = browser.find_element_by_class_name('experience-section').find_elements_by_tag_name("li")[
                    i].find_element_by_tag_name("h3").text
            except:
                title = ""

            try:
                # tm.sleep(2)
                company = browser.find_element_by_class_name('experience-section').find_elements_by_tag_name("li")[
                    i].find_element_by_class_name("pv-entity__secondary-title").text
                #print(company,"company name-------------------------")
            except Exception as e:
                #print(e,"compamny name excdprtiuon")
                company = ""

            try:
                # tm.sleep(2)
                time = browser.find_element_by_class_name('experience-section').find_elements_by_tag_name("li")[
                    i].find_element_by_class_name("pv-entity__date-range").find_elements_by_tag_name("span")[
                    1].text.encode("utf-8")
                # print("-------------------", type(time))
                # start_date = time.split("\xe2\x80\x93")[0]
                # end_date = time.split("\xe2\x80\x93")[1]
                time = time.decode('utf-8')
                start_date = time.split(time.split(' ')[2])[0]
                end_date = time.split(time.split(' ')[2])[1]

            except:
                start_date = ""
                end_date = ""

            try:
                # tm.sleep(2)
                locationData = \
                    browser.find_element_by_class_name('experience-section').find_elements_by_tag_name("li")[
                        i].find_elements_by_class_name("pv-entity__bullet-item")
                if len(locationData) >= 2:
                    location = locationData[1].text
                else:
                    location = ""
            except:
                location = ""

            if location == "":
                try:
                    locationData = \
                        browser.find_element_by_class_name('experience-section').find_elements_by_tag_name("li")[
                            i].find_element_by_class_name("pv-entity__location").text
                    location = locationData.replace("Location", "").strip()

                except:
                    location = ""

            if company_id or description or title or company or start_date or end_date or location:
                each = {"company_id": company_id, "description": description, "title": title, "company": company,
                        "start_date": start_date, "end_date": end_date, "location": location}
                employements.append(each)

    except Exception as e:
        print('Exception in employements')

    each_profile.update({"employements": employements})

    # SKILLS AND ENDORSEMENTS

    try:
        show_more = browser.find_element_by_css_selector('button.pv-profile-section__card-action-bar.pv-skills-section__additional-skills.artdeco-container-card-action-bar span.svg-icon-wrap').click()
        tm.sleep(5)
        print('%%%%%%%%% button clicked')
    except Exception as e:
        print(e)
        print('%%%%%%%%% button not clicked')

    try:

        skills_list = []
        soup = BeautifulSoup(browser.page_source, 'lxml')
        skills = soup.find('section', class_='pv-skill-categories-section')
        # f = open('skills_expanded1.html', 'w')
        # f.write(str(skills.prettify()))
        # f.close()
        # skk = browser.find_elements_by_css_selector('.pv-skill-category-entity__name-text.t-16.t-black.t-bold')
        # for skill in skk:
        for skill in skills.find_all('span', class_='pv-skill-category-entity__name-text t-16 t-black t-bold'):
            skills_list.append(skill.text)
            print(skill.text)

    except Exception as e:
        print(e)
        print('%%%%%%%%% ISSUES HERE')
        pass

    each_profile.update({"skills": skills_list})

    # INTERESTS
    print("interests -----------------------")
    interests = browser.find_elements_by_class_name('pv-interest-entity')
    interests_list = []
    for i in interests:
        interests_list.append(i.text)
        print(i.text)

    each_profile.update({"interests": interests_list})

    for i, j in each_profile.items():
        print("{} :\t{}".format(i, j))

    file_name = "_15feb4_" + str(ii) + '.csv'
    each_profile_updated = dict()
    ll = []
    for key, value in each_profile.items():
        ll.append(str(value))
        each_profile_updated[key] = ll
        ll = []
    # print(each_profile)

    # print(each_profile_updated)
    csv_df = pd.DataFrame.from_dict(each_profile_updated)
    csv_df.to_csv(file_name)

# return each_profile,url,memberID
# print "employements",employements

# ------------------------------------------------------------------------------------------- NEW CODE ENDS
browser.close()
