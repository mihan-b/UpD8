import requests


def get_stock(tag):
  link = "https://finance.yahoo.com/quote/" + tag.upper()
  print(link)
  raw = requests.get(link)
  rawtext = raw.text
  rawlist = rawtext.split("regularMarketPrice")
  rawtext2 = rawlist[7]
  rawlist2 = rawtext2.split("value")
  rawtext3 = rawlist2[1]
  rawlist3 = rawtext3.split("\"")
  return "The price of " + tag + " is $" + rawlist3[1]


def get_weather(city):
  link = "https://www.timeanddate.com/weather/canada/" + city
  print(link)
  raw = requests.get(link)
  rawtext = raw.text
  rawlist = rawtext.split("Now")
  rawtext2 = rawlist[1]
  rawlist2 = rawtext2.split("\"")
  rawtext3 = rawlist2[4]
  rawlist3 = rawtext3.split(">")
  rawtext4 = rawlist3[2]
  rawlist4 = rawtext4.split("&")
  fahr = int(rawlist4[0])
  cel = str(round((fahr - 32) / 1.8))
  return "The weather in " + city + " is " + cel + "\N{DEGREE SIGN}C and " + rawlist2[
    1]

def get_score(league, team):
  if (league == "nba" or league == "NBA"):
    link1 = "nba"
    if (team == "Celtics" or team == "celtics"):
      link2 = "1"
    if (team == "Nets" or team == "nets"):
      link2 = "2"
    if (team == "Knicks" or team == "knicks"):
      link2 = "3"
    if (team == "76ers"):
      link2 = "4"
    if (team == "Raptors" or team == "raptors"):
      link2 = "5"
    if (team == "Bulls" or team == "bulls"):
        link2 = "6"
    if (team == "Cavs" or team == "cavs"):
      link2 = "7"
    if (team == "Pistons" or team == "pistons"):
      link2 = "8"
    if (team == "Pacers" or team == "pacers"):
       link2 = "9"
    if (team == "Bucks" or team == "bucks"):
      link2 = "10"
    if (team == "Hawks" or team == "hawks"):
      link2 = "11"
    if (team == "Hornets" or team == "hornets"):
      link2 = "12"
    if (team == "Heat" or team == "heat"):
      link2 = "13"
    if (team == "Magic" or team == "magic"):
      link2 = "14"
    if (team == "Wizards" or team == "wizards"):
      link2 = "15"
    if (team == "Warriors" or team == "warriors"):
      link2 = "16"
    if (team == "Clippers" or team == "clippers"):
      link2 = "17"
    if (team == "Lakers" or team == "lakers"):
      link2 = "18"
    if (team == "Suns" or team == "suns"):
      link2 = "19"
    if (team == "Kings" or team == "kings"):
      link2 = "20"
    if (team == "Mavs" or team == "mavs" or team == "Mavericks"
          or team == "mavericks"):
      link2 = "21"
    if (team == "Rockets" or team == "rockets"):
      link2 = "22"
    if (team == "Grizzlies" or team == "grizzlies"):
      link2 = "23"
    if (team == "Pelicans" or team == "pelicans"):
      link2 = "24"
    if (team == "Spurs" or team == "spurs"):
      link2 = "25"
    if (team == "Nuggets" or team == "nuggets"):
      link2 = "26"
    if (team == "Timberwolves" or team == "timberwolves" or team == "Wolves"
          or team == "wolves"):
     link2 = "27"
    if (team == "Thunder" or team == "thunder"):
      link2 = "28"
    if (team == "Trailblazers" or team == "trailblazers" or team == "Blazers"
          or team == "blazers"):
      link2 = "29"
    if (team == "Jazz" or team == "jazz"):
        link2 = "30"

  if (league == "mlb" or league == "MLB"):
    link1 = "mlb"

  if (league == "nhl" or league == "NHL"):
    link1 = "nhl"

  if (league == "nfl" or league == "NFL"):
    link1 = "nfl"

  link = "https://www.thescore.com/" + link1 + "/teams/" + link2
  print(link)
  raw = requests.get(link)    
  rawtext = raw.text
  rawlist = rawtext.split("EventCard__teamName--JweK5")
  winningraw = rawlist[2]
  winninglist = winningraw.split("</")
  winningraw2 = winninglist[0]
  winninglist2 = winningraw2.split("v>")
  winningteam = winninglist2[1]
  
  losingraw = rawlist[3]
  losinglist = losingraw.split("</div>")
  losingraw2 = losinglist[0]
  losinglist2 = losingraw2.split("<div>")
  losingteam = losinglist2[1]

  rawlist = rawtext.split("EventCard__score--2C1-p")
  wscore = rawlist[2]
  wlist = wscore.split("<")
  wscore2 = wlist[0]
  wlist2 = wscore2.split(">")
  winningscore = wlist2

  lscore = rawlist[3]
  llist = lscore.split("</")
  lscore2 = llist[0]
  llist2 = lscore2.split(">")
  losingscore = llist2[1]

  return "The " + str(winningteam) + " beat the " + str(losingteam) + " by a score of " + str(winningscore[1]) + "-" + str(losingscore)
