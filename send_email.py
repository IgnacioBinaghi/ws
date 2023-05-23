import os
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

port = 465
email_server = 'smtp.gmail.com'

# load the environment variables (returns current folder of python file)
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir/ ".env"
load_dotenv(envars)

# read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_email(subject, receiver_email, 
               generalNewsLink1, generalNewsTitle1, generalNewsSource1,
               generalNewsLink2, generalNewsTitle2, generalNewsSource2,
               generalNewsLink3, generalNewsTitle3, generalNewsSource3,
               generalNewsLink4, generalNewsTitle4, generalNewsSource4,
               generalNewsLink5, generalNewsTitle5, generalNewsSource5,
               kw1, kw1article1link, kw1article1title, kw1article1source, kw1article2link, kw1article2title, kw1article2source,kw1article3link, kw1article3title, kw1article3source, kw1article4link, kw1article4title, kw1article4source,
               kw2, kw2article1link, kw2article1title, kw2article1source, kw2article2link, kw2article2title, kw2article2source,kw2article3link, kw2article3title, kw2article3source, kw2article4link, kw2article4title, kw2article4source,
               kw3, kw3article1link, kw3article1title, kw3article1source, kw3article2link, kw3article2title, kw3article2source,kw3article3link, kw3article3title, kw3article3source, kw3article4link, kw3article4title, kw3article4source,
               kw4, kw4article1link, kw4article1title, kw4article1source, kw4article2link, kw4article2title, kw4article2source,kw4article3link, kw4article3title, kw4article3source, kw4article4link, kw4article4title, kw4article4source,
               kw5, kw5article1link, kw5article1title, kw5article1source, kw5article2link, kw5article2title, kw5article2source,kw5article3link, kw5article3title, kw5article3source, kw5article4link, kw5article4title, kw5article4source,
               ):
    # create the base text message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("wsAlpha", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        """
    )
    # add the HTML version. This converts the message into a multipart/alternative 
    # container, with the original text message of the first part and the
    # new html message as the second part. 
    msg.add_alternative(
        f"""\
        <!DOCTYPE html>

    <html lang="en">
        <head>
            <link href="newsletter.css" rel="stylesheet">
            <title>Template</title>
        </head>
        <body style="position:absolute;
                        border-radius: 25px;
                        border: 2px solid #35852c;
                        background: #ffffff;
                        padding: 20px;
                        left:50%;
                        transform: translate(-50%);
                        margin:0;
                        overflow-x:hidden;">

            <table class="styled-table" style="border-collapse: collapse;
                                                margin: 25px 0;
                                                font-size: 0.9em;
                                                font-family: sans-serif;
                                                min-width: 400px;
                                                box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);">
                <thead>
                    <tr style="background-color: #35852c;
                                color: #ffffff;
                                text-align: left;">
                        <th style="padding: 12px 15px; color: #;"></th>
                        <th style="padding: 12px 15px;">Prior Day's Close</th>
                        <th style="padding: 12px 15px;">1-Day Change</th>
                        <th style="padding: 12px 15px;">YTD Change</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 12px 15px; color: #000000;">S&P 500</td>
                        <td style="padding: 12px 15px; color: #000000;">4,169.48</td>
                        <td style="padding: 12px 15px; color: #000000;">0.80%</td>
                        <td style="padding: 12px 15px; color: #000000;">8.60%</td>
                    </tr>
                    <tr class="active-row">
                        <td style="padding: 12px 15px; color: #000000;">NASDAQ</td>
                        <td style="padding: 12px 15px; color: #000000;">34,096.16</td>
                        <td style="padding: 12px 15px; color: #000000;">0.80%</td>
                        <td style="padding: 12px 15px; color: #000000;">2.90%</td>
                    </tr>
                    <tr>
                        <td style="padding: 12px 15px; color: #000000;">Bitcoin</td>
                        <td style="padding: 12px 15px; color: #000000;">1,897.31</td>
                        <td style="padding: 12px 15px; color: #000000;">-0.90%</td>
                        <td style="padding: 12px 15px; color: #000000;">8.60%</td>
                    </tr>
                    <tr class="active-row">
                        <td style="padding: 12px 15px; color: #000000;">10Y UST</td>
                        <td style="padding: 12px 15px; color: #000000;">3.452%</td>
                        <td style="padding: 12px 15px; color: #000000;">-7.6bps</td>
                        <td style="padding: 12px 15px; color: #000000;">-37.8bps</td>
                    </tr>
                </tbody>
            </table>

            <section>
                <h3 style="color: #35852c;">General</h3>
                <ul style="list-style: none;
                            padding: 0">
                    <li>
                        <a href={generalNewsLink1} style="color: #000000; text-decoration: none;">{generalNewsTitle1}, <em style="color: #000000;">{generalNewsSource1}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={generalNewsLink2} style="color: #000000; text-decoration: none;">{generalNewsTitle2}, <em style="color: #000000;">{generalNewsSource2}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={generalNewsLink3} style="color: #000000; text-decoration: none;">{generalNewsTitle3}, <em style="color: #000000;">{generalNewsSource3}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={generalNewsLink4} style="color: #000000; text-decoration: none;">{generalNewsTitle4}, <em style="color: #000000;">{generalNewsSource4}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={generalNewsLink5} style="color: #000000; text-decoration: none;">{generalNewsTitle5}, <em style="color: #000000;">{generalNewsSource5}</em></a>
                    </li>
                </ul> 
            </section>
            <section>
                <h3 style="color: #35852c;">{kw1} News</h3>
                <ul style="list-style: none;
                            padding: 0">
                    <li>
                        <a href={kw1article1link} style="color: #000000; text-decoration: none;">{kw1article1title}, <em style="color: #000000;">{kw1article1source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw1article2link} style="color: #000000; text-decoration: none;">{kw1article2title}, <em style="color: #000000;">{kw1article2source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw1article3link} style="color: #000000; text-decoration: none;">{kw1article3title}, <em style="color: #000000;">{kw1article3source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw1article4link} style="color: #000000; text-decoration: none;">{kw1article4title}, <em style="color: #000000;">{kw1article4source}</em></a>
                    </li>
                </ul> 
            </section>
            <section>
                <h3 style="color: #35852c;">{kw2} News</h3>
                <ul style="list-style: none;
                            padding: 0">
                    <li>
                        <a href={kw2article1link} style="color: #000000; text-decoration: none;">{kw2article1title}, <em style="color: #000000;">{kw2article1source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw2article2link} style="color: #000000; text-decoration: none;">{kw2article2title}, <em style="color: #000000;">{kw2article2source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw2article3link} style="color: #000000; text-decoration: none;">{kw2article3title}, <em style="color: #000000;">{kw2article3source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw2article4link} style="color: #000000; text-decoration: none;">{kw2article4title}, <em style="color: #000000;">{kw2article4source}</em></a>
                    </li>
                </ul> 
            </section>
            <section>
                <h3 style="color: #35852c;">{kw3} News</h3>
                <ul style="list-style: none;
                            padding: 0">
                    <li>
                        <a href={kw3article1link} style="color: #000000; text-decoration: none;">{kw3article1title}, <em style="color: #000000;">{kw3article1source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw3article2link} style="color: #000000; text-decoration: none;">{kw3article2title}, <em style="color: #000000;">{kw3article2source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw3article3link} style="color: #000000; text-decoration: none;">{kw3article3title}, <em style="color: #000000;">{kw3article3source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw3article4link} style="color: #000000; text-decoration: none;">{kw3article4title}, <em style="color: #000000;">{kw3article4source}</em></a>
                    </li>
                </ul> 
            </section>
            <section>
                <h3 style="color: #35852c;">{kw4} News</h3>
                <ul style="list-style: none;
                            padding: 0">
                    <li>
                        <a href={kw4article1link} style="color: #000000; text-decoration: none;">{kw4article1title}, <em style="color: #000000;">{kw4article1source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw4article2link} style="color: #000000; text-decoration: none; ">{kw4article2title}, <em style="color: #000000;">{kw4article2source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw4article3link} style="color: #000000; text-decoration: none;">{kw4article3title}, <em style="color: #000000;">{kw4article3source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw4article4link} style="color: #000000; text-decoration: none;">{kw4article4title}, <em style="color: #000000;">{kw4article4source}</em></a>
                    </li>
                </ul> 
            </section>
            <section>
                <h3 style="color: #35852c;">{kw5} News</h3>
                <ul style="list-style: none;
                            padding: 0">
                    <li>
                        <a href={kw5article1link} style="color: #000000; text-decoration: none;">{kw5article1title}, <em style="color: #000000;">{kw5article1source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw5article2link} style="color: #000000; text-decoration: none;">{kw5article2title}, <em style="color: #000000;">{kw5article2source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw5article3link} style="color: #000000; text-decoration: none;">{kw5article3title}, <em style="color: #000000;">{kw5article3source}</em></a>
                    </li>
                    <br>
                    <li>
                        <a href={kw5article4link} style="color: #000000; text-decoration: none;">{kw5article4title}, <em style="color: #000000;">{kw5article4source}</em></a>
                    </li>
                </ul> 
            </section>
        </body>
    </html>
    """,
        subtype="html"
    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(email_server, port, context=context) as server:
        server.login(sender_email, password_email)
        server.send_message(msg)

    return True

if __name__ == "__main__":
    send_email(
        receiver_email="thomasbinaghi@gmail.com",
        subject="wsAlpha Newsletter",        

        ## General news
        # 1
        generalNewsTitle1="Elon Musk Says He’s Stepping Down as Twitter’s CEO",
        generalNewsLink1="https://www.bloomberg.com/news/articles/2023-05-11/musk-to-name-new-twitter-ceo-will-shift-to-cto-executive-chair?srnd=premium",
        generalNewsSource1="Bloomberg",
        # 2
        generalNewsTitle2="Zelensky makes dramatic G-7 visit as Biden mobilizes allies over China",
        generalNewsLink2="https://www.washingtonpost.com/world/2023/05/20/biden-zelensky-g7-summit-hiroshima-japan/",
        generalNewsSource2="Washington Post",
        # 3
        generalNewsTitle3="Zelenskiy Meets With India’s Modi on Sidelines Of G-7 Summit",
        generalNewsLink3="https://www.bloomberg.com/news/articles/2023-05-20/zelenskiy-seeks-to-meet-lula-modi-at-g7-summit-in-hiroshima?srnd=premium#xj4y7vzkg",
        generalNewsSource3="Bloomberg",
        # 4
        generalNewsTitle4="Stocks slide after Republicans 'press pause' on debt ceiling talks: Stock market news today",
        generalNewsLink4="https://finance.yahoo.com/news/stock-market-news-today-live-updates-may-19-2023-120401938.html",
        generalNewsSource4="Yahoo Finance",
        # 5
        generalNewsTitle5="Debt-Limit Talks Resume After Optimism Curbed by GOP Walk-Out",
        generalNewsLink5="https://www.bloomberg.com/news/articles/2023-05-19/mccarthy-says-debt-negotiations-will-restart-friday-night?srnd=premium#xj4y7vzkg",
        generalNewsSource5="New York Times",


        ### KEYWORD Sections (Five per user, with two articles each)
        
        ## Keyword 1
        kw1="Soccer",
        # 1
        kw1article1title="Weekend stakes for Premier League, LaLiga, top European soccer leagues",
        kw1article1link="https://www.espn.com/soccer/story/_/id/37683440/europe-top-soccer-leagues-whats-stake-weekend-premier-league-laliga-bundesliga-serie-ligue-1",
        kw1article1source="ESPN",
        # 2
        kw1article2title="AC Milan vs. Sampdoria odds, picks, how to watch, stream, start time: May 20, 2023 Italian Serie A predictions",
        kw1article2link="https://www.cbssports.com/soccer/news/ac-milan-vs-sampdoria-odds-picks-how-to-watch-stream-start-time-may-20-2023-italian-serie-a-predictions/",
        kw1article2source="CBS Sports",
        
        ## Keyword 2
        kw2="Architecture",
        # 1
        kw2article1title="Overcoming Barriers: Social Justice in Latin American Architecture",
        kw2article1link="https://www.archdaily.com/997064/overcoming-barriers-social-justice-in-latin-american-architecture",
        kw2article1source="Arch Daily",
        # 2
        kw2article2title="Taliesyn draws on vernacular architecture for earth-toned Cabin House",
        kw2article2link="https://www.dezeen.com/2023/05/20/taliesyn-cabin-house-vernacular-architecture-earth-toned-residential-bangalore/",
        kw2article2source="Dezeen",
        
        ## Keyword 3
        kw3="Politics",
        # 1
        kw3article1title="Disney rocks DeSantis ahead of expected White House bid announcement",
        kw3article1link="https://www.cnn.com/2023/05/19/politics/desantis-disney-feud/index.html",
        kw3article1source="CNN",
        # 2
        kw3article2title="Debt talks resume after a snag as the country gets closer to a possible default",
        kw3article2link="https://www.npr.org/2023/05/19/1177092657/debt-ceiling-negotiations-pause-default-biden-mccarthy",
        kw3article2source="npr",
        
        ## Keyword 4
        kw4="Technology",
        # 1
        kw4article1title="The Underground History of Russia’s Most Ingenious Hacker Group",
        kw4article1link="https://www.wired.com/story/turla-history-russia-fsb-hackers/",
        kw4article1source="Wired",
        # 2
        kw4article2title="OpenAI launches free ChatGPT app for iOS",
        kw4article2link="https://www.theverge.com/2023/5/18/23728703/openai-chatgpt-app-ios",
        kw4article2source="The Verge",
        
        ## Keyword 5
        kw5="Arts",
        # 1
        kw5article1title="Ruling Against Warhol Shouldn’t Hurt Artists. But It Might.",
        kw5article1link="https://www.nytimes.com/2023/05/19/arts/design/warhol-prince-supreme-court-copyright.html",
        kw5article1source="New York Times",
        # 2
        kw5article2title="Giant Louise Bourgeois spider sculpture sells for record $32.8 million at auction",
        kw5article2link="https://www.cnn.com/style/article/louise-bourgeois-spider-sold-record-intl-scli/index.html",
        kw5article2source="CNN",


    )



