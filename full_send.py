from get_news import *
from get_user_data import *
from send_email import send_email
from encryption import decrypt


users = get_users()

for i in users:
    email = (decrypt(i[1][5:]))
    name = i[2]

    kw1 = i[3]
    kw2 = i[4]
    kw3 = i[5]
    kw4 = i[6]
    kw5 = i[7]

    general = get_general_news()
    keyword1 = get_keyword_news_support(i[3])
    keyword2 = get_keyword_news_support(i[4])
    keyword3 = get_keyword_news_support(i[5])
    keyword4 = get_keyword_news_support(i[6])
    keyword5 = get_keyword_news_support(i[7])






    statements = ['generalarticle1titlesource = general[0][0].rsplit(" - ", 1)',
        'generalarticle2titlesource = general[1][0].rsplit(" - ", 1)',
        'generalarticle3titlesource = general[2][0].rsplit(" - ", 1)',
        'generalarticle4titlesource = general[3][0].rsplit(" - ", 1)',
        'generalarticle5titlesource = general[4][0].rsplit(" - ", 1)']

    for j in statements:
        try:
            exec(j)
        except Exception:
            exec(j[0:25]+' = ["",""]')
            try:
                exec('general'+j[14]+'.append(["",""])')
            except:
                pass









    statements = ['kw1article1titlesource = keyword1[0][0].rsplit(" - ", 1)', 'kw1article2titlesource = keyword1[1][0].rsplit(" - ", 1)', 'kw1article3titlesource = keyword1[2][0].rsplit(" - ", 1)', 'kw1article4titlesource = keyword1[3][0].rsplit(" - ", 1)',
    'kw2article1titlesource = keyword2[0][0].rsplit(" - ", 1)', 'kw2article2titlesource = keyword2[1][0].rsplit(" - ", 1)', 'kw2article3titlesource = keyword2[2][0].rsplit(" - ", 1)', 'kw2article4titlesource = keyword2[3][0].rsplit(" - ", 1)',
    'kw3article1titlesource = keyword3[0][0].rsplit(" - ", 1)', 'kw3article2titlesource = keyword3[1][0].rsplit(" - ", 1)', 'kw3article3titlesource = keyword3[2][0].rsplit(" - ", 1)', 'kw3article4titlesource = keyword3[3][0].rsplit(" - ", 1)',
        'kw4article1titlesource = keyword4[0][0].rsplit(" - ", 1)',
        'kw4article2titlesource = keyword4[1][0].rsplit(" - ", 1)',
        'kw4article3titlesource = keyword4[2][0].rsplit(" - ", 1)',
        'kw4article4titlesource = keyword4[3][0].rsplit(" - ", 1)',

        'kw5article1titlesource = keyword5[0][0].rsplit(" - ", 1)',
        'kw5article2titlesource = keyword5[1][0].rsplit(" - ", 1)',
        'kw5article3titlesource = keyword5[2][0].rsplit(" - ", 1)',
        'kw5article4titlesource = keyword5[3][0].rsplit(" - ", 1)']

    for u in statements:
        try:
            exec(u)
        except Exception:
            exec(u[:22]+' = ["No news found today for this keyword, click here to change keyword", ""]')
            try:
                exec('keyword'+u[2]+'['+str(count)+'][1] = "https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            except:
                exec('keyword'+u[2]+'.append(["","https://www.youtube.com/watch?v=dQw4w9WgXcQ"])')




    print(send_email(

        receiver_email=email,
        subject="wsAlpha Newsletter",

        # General news
        # 1
        generalNewsTitle1=generalarticle1titlesource[0],
        generalNewsLink1=general[0][1],
        generalNewsSource1=generalarticle1titlesource[1],
        # 2
        generalNewsTitle2=generalarticle2titlesource[0],
        generalNewsLink2=general[1][1],
        generalNewsSource2=generalarticle2titlesource[1],
        # 3
        generalNewsTitle3=generalarticle3titlesource[0],
        generalNewsLink3=general[2][1],
        generalNewsSource3=generalarticle3titlesource[1],
        # 4
        generalNewsTitle4=generalarticle4titlesource[0],
        generalNewsLink4=general[3][1],
        generalNewsSource4=generalarticle4titlesource[1],
        # 5
        generalNewsTitle5=generalarticle5titlesource[0],
        generalNewsLink5=general[4][1],
        generalNewsSource5=generalarticle5titlesource[1],


        # Keyword 1
        kw1=i[3],
        # 1
        kw1article1title=kw1article1titlesource[0],
        kw1article1link=keyword1[0][1],
        kw1article1source=kw1article1titlesource[1],
        # 2
        kw1article2title=kw1article2titlesource[0],
        kw1article2link=keyword1[1][1],
        kw1article2source=kw1article2titlesource[1],
        # 3
        kw1article3title=kw1article3titlesource[0],
        kw1article3link=keyword1[2][1],
        kw1article3source=kw1article3titlesource[1],
        # 2
        kw1article4title=kw1article4titlesource[0],
        kw1article4link=keyword1[3][1],
        kw1article4source=kw1article4titlesource[1],




        # Keyword 2
        kw2=i[4],
        # 1
        kw2article1title=kw2article1titlesource[0],
        kw2article1link=keyword2[0][1],
        kw2article1source=kw2article1titlesource[1],
        # 2
        kw2article2title=kw2article2titlesource[0],
        kw2article2link=keyword2[1][1],
        kw2article2source=kw2article2titlesource[1],
        # 3
        kw2article3title=kw2article3titlesource[0],
        kw2article3link=keyword2[2][1],
        kw2article3source=kw2article3titlesource[1],
        # 2
        kw2article4title=kw2article4titlesource[0],
        kw2article4link=keyword2[3][1],
        kw2article4source=kw2article4titlesource[1],




        # Keyword 3
        kw3=i[5],
        # 1
        kw3article1title=kw3article1titlesource[0],
        kw3article1link=keyword2[0][1],
        kw3article1source=kw3article1titlesource[1],
        # 2
        kw3article2title=kw3article2titlesource[0],
        kw3article2link=keyword3[1][1],
        kw3article2source=kw3article2titlesource[1],
        # 3
        kw3article3title=kw3article3titlesource[0],
        kw3article3link=keyword3[2][1],
        kw3article3source=kw3article3titlesource[1],
        # 2
        kw3article4title=kw3article4titlesource[0],
        kw3article4link=keyword3[3][1],
        kw3article4source=kw3article4titlesource[1],




        # Keyword 4
        kw4=i[6],
        # 1
        kw4article1title=kw4article1titlesource[0],
        kw4article1link=keyword4[0][1],
        kw4article1source=kw4article1titlesource[1],
        # 2
        kw4article2title=kw4article2titlesource[0],
        kw4article2link=keyword4[1][1],
        kw4article2source=kw4article2titlesource[1],
        # 3
        kw4article3title=kw4article3titlesource[0],
        kw4article3link=keyword4[2][1],
        kw4article3source=kw4article3titlesource[1],
        # 2
        kw4article4title=kw4article4titlesource[0],
        kw4article4link=keyword4[3][1],
        kw4article4source=kw4article4titlesource[1],




        # Keyword 5
        kw5=i[7],
        # 1
        kw5article1title=kw5article1titlesource[0],
        kw5article1link=keyword5[0][1],
        kw5article1source=kw5article1titlesource[1],
        # 2
        kw5article2title=kw5article2titlesource[0],
        kw5article2link=keyword5[1][1],
        kw5article2source=kw5article2titlesource[1],
        # 3
        kw5article3title=kw5article3titlesource[0],
        kw5article3link=keyword5[2][1],
        kw5article3source=kw5article3titlesource[1],
        # 2
        kw5article4title=kw5article4titlesource[0],
        kw5article4link=keyword5[3][1],
        kw5article4source=kw5article4titlesource[1],
    ))
