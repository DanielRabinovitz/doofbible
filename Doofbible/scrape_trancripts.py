import requests
from bs4 import BeautifulSoup

with open("reformattedEpisodeList.txt", "r", encoding="utf-8") as f:
    episode_list = f.read()

with open("episodeList.txt", "r", encoding="utf-8") as f:
    episode_list_unformatted = f.read()

episode_list = episode_list.split('\n')
episode_list_unformatted = episode_list_unformatted.split('\n')

urls = [f"https://phineasandferb.fandom.com/wiki/{episode}/Transcript"for episode in episode_list]

#scrapes the script of an episode for exclusivley sections that either 
#mention or contain Dr. Doofenshmirtz
def scrape_episode(url):

    # Send a GET request to the URL
    response = requests.get(url)

    # Use Beautiful Soup to parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the transcript section of the page by searching for the "div" tag with class "mw-content-ltr"
    transcript_div = soup.find("div", {"class": "mw-parser-output"})

    # Extract the transcript text by concatenating all the paragraph elements within the transcript section
    transcript_text = ""
    raw_text = transcript_div.find_all('p')
    for p in raw_text:
        if "Doofenshmirtz" in p.text or "Darthenshmirtz" in p.text:
            transcript_text += p.text + "\n"
    
    return transcript_text

#empty variables
doofelations = ""
season = 0

#iterate over episode_list and urls to create doofelations
for ep_index in range(len(episode_list)):

    ep_name = episode_list_unformatted[ep_index]

    if ep_name == "Rollercoaster":
        season = "Season 1"
    elif ep_name == "The Lake Nose Monster":
        season = "Season 2"
    elif ep_name == "The Great Indoors":
        season = "Season 3"
    elif ep_name == "For Your Ice Only":
        season = "Season 4"

    #adds header to chapter of doofelations, with special cases outlined
    if "Phineas and Ferb the Movie" in ep_name:
        doofelations += f"Doofelations Special:{ep_index+1} | {ep_name}\n\n"
    elif "O.W.C.A. Files" in ep_name:
        doofelations += f"Doofelations Special:{ep_index+1} | {ep_name}\n\n"
    elif "Mission Marvel" in ep_name:
        doofelations += f"Doofelations Special:{ep_index+1} | {ep_name}\n\n"
    elif "Star Wars" in ep_name:
        doofelations += f"Doofelations Special:{ep_index+1} | {ep_name}\n\n"
    elif "Save Summer" in ep_name:
        doofelations += f"Doofelations Special:{ep_index+1} | {ep_name}\n\n"    
    else: 
         doofelations += f"Doofelations {season}:{ep_index+1} | {ep_name}\n\n"
    
    #adds text to doofelations
    doofelations += scrape_episode(urls[ep_index])

with open("Doofelations.txt", "w", encoding="utf-8") as f:
    f.write(doofelations)
print('DONE')
