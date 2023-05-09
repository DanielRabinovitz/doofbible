

# Open the original file and read its contents
with open("episodeList.txt", "r") as f:
    episode_list = f.read()

# Replace spaces with underscores and question marks with "%3F" to match the wiki's formatting
episode_list = episode_list.replace(" ", "_").replace("?", "%3F")

# Write the new formatted episode list to a new file
with open("reformattedEpisodeList.txt", "w") as f:
    f.write(episode_list)