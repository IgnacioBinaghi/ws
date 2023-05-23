from __future__ import print_function
import time
from datetime import date
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from constants import api_key
from newsletter_production import articles, date_today

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = api_key

api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
tag = "Newsletter"
sender = {"name": 'wsAlpha', "email": 'wsalpha.newsletter@gmail.com'}
name = 'Newsletter - ' + str(date.today())
template_id = 29
subject = 'Newsletter - ' + str(date_today)
recipients = {"listIds": [5]}

params = {"date":str(date_today),"headline1":articles["Article1"][2],"bodyText1":articles["Article1"][3][0:500]+"...","newspaper1":articles["Article1"][4], "image1":articles["Article1"][1], "newsURL1":articles["Article1"][0],
                                "headline2":articles["Article2"][2],"bodyText2":articles["Article2"][3][0:500]+"...","newspaper2":articles["Article2"][4], "image2":articles["Article2"][1], "newsURL2":articles["Article2"][0],
                                "headline3":articles["Article3"][2],"bodyText3":articles["Article3"][3][0:500]+"...","newspaper3":articles["Article3"][4], "image3":articles["Article3"][1], "newsURL3":articles["Article3"][0],
                                "headline4":articles["Article4"][2],"bodyText4":articles["Article4"][3][0:500]+"...","newspaper4":articles["Article4"][4], "image4":articles["Article4"][1], "newsURL4":articles["Article4"][0],
                                "headline5":articles["Article5"][2],"bodyText5":articles["Article5"][3][0:500]+"...","newspaper5":articles["Article5"][4], "image5":articles["Article5"][1], "newsURL5":articles["Article5"][0],
                                "headline6":articles["Article6"][2],"bodyText6":articles["Article6"][3][0:500]+"...","newspaper6":articles["Article6"][4], "image6":articles["Article6"][1], "newsURL6":articles["Article6"][0],
                                "headline7":articles["Article7"][2],"bodyText7":articles["Article7"][3][0:500]+"...","newspaper7":articles["Article7"][4], "image7":articles["Article7"][1], "newsURL7":articles["Article7"][0],
                                "headline8":articles["Article8"][2],"bodyText8":articles["Article8"][3][0:500]+"...","newspaper8":articles["Article8"][4], "image8":articles["Article8"][1], "newsURL8":articles["Article8"][0],
                                "headline9":articles["Article9"][2],"bodyText9":articles["Article9"][3][0:500]+"...","newspaper9":articles["Article9"][4], "image9":articles["Article9"][1], "newsURL9":articles["Article9"][0],
                                "headline10":articles["Article10"][2],"bodyText10":articles["Article10"][3][0:500]+"...","newspaper10":articles["Article10"][4], "image10":articles["Article10"][1], "newsURL10":articles["Article10"][0],
                                "headline11":articles["Article11"][2],"bodyText11":articles["Article11"][3][0:500]+"...","newspaper11":articles["Article11"][4], "image11":articles["Article11"][1], "newsURL11":articles["Article11"][0],
                                "headline12":articles["Article12"][2],"bodyText12":articles["Article12"][3][0:500]+"...","newspaper12":articles["Article12"][4], "image12":articles["Article12"][1], "newsURL12":articles["Article12"][0],
                                "headline13":articles["Article13"][2],"bodyText13":articles["Article13"][3][0:500]+"...","newspaper13":articles["Article13"][4], "image13":articles["Article13"][1], "newsURL13":articles["Article13"][0],
                                "headline14":articles["Article14"][2],"bodyText14":articles["Article14"][3][0:500]+"...","newspaper14":articles["Article14"][4], "image14":articles["Article14"][1], "newsURL14":articles["Article14"][0],
                                "headline15":articles["Article15"][2],"bodyText15":articles["Article15"][3][0:500]+"...","newspaper15":articles["Article15"][4], "image15":articles["Article15"][1], "newsURL15":articles["Article15"][0],
                                }


send_at_best_time = False
inline_image_activation = False
mirror_active = False
header = 'If you are not able to see this mail, click {here}'
footer = 'If you wish to unsubscribe from our newsletter, click {here}'
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(sender=sender, name=name, template_id=template_id, subject=subject, recipients=recipients, send_at_best_time=send_at_best_time, inline_image_activation=inline_image_activation, mirror_active=mirror_active, params=params) # CreateEmailCampaign | Values to create a campaign

try:
    api_response = api_instance.create_email_campaign(email_campaigns)
    pprint(api_response)
    #sendCampaign(api_response["id"])
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)
