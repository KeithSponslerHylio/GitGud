import re

# Select which story to publish (Comment out the unused stories)
# story_genre = 'fantasy'
story_genre = 'scifi'

# Ingest nouns into a list
with open('words/nouns.txt', 'r') as f:
    nouns = f.read().splitlines()

# Ingest verbs into a list
with open('words/verbs.txt', 'r') as f:
    verbs = f.read().splitlines()

# Ingest the story template
with open('stories/' + story_genre + '.txt', 'r') as f:
    story_template = f.read()

# This function will replace the (n1) and (v2)'s with real words
def replace_placeholder(match):
    word_type = match.group(1)
    index = int(match.group(2)) - 1
    
    if word_type == 'n':
        return nouns[index]
    elif word_type == 'v':
        return verbs[index]

completed_story = re.sub(r'\((n|v)(\d+)\)', replace_placeholder, story_template)

with open('stories/PUBLISH_THIS.txt', 'w') as f:
    f.write(completed_story)