
import praw
import json
import time

# Credentials for Reddit API.
client_id = ''
client_secret = ''

# Create instance of Reddit.
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='testscript')

# Save submissions in a list.
# Each submission is stored in a dictionary.
data = []


# Current timestamp.
now = time.time()

# Check for submissions made within last 6 months.
time_6_months = 6 * 30 * 24 * 60 * 60


# Submission fields.
fields = ['id', 'title', 'url', 'score', 'created_utc', 'num_comments']

# Ireland subreddit.
subreddit = reddit.subreddit('ireland')

# Search for tweets related to Galway on the Ireland subreddit.
query_term = 'galway'
galway_submissions = subreddit.search(query=query_term, sort='new', time_filter='year', limit=None)

print('Getting submissions for query term: %s...\n' % query_term)

for submission in galway_submissions:

    # Submission made within last 6 months.
    if now - submission.created_utc >= time_6_months:
        continue

    # Get required fields to the dictionary.
    submission_dict = vars(submission)
    submission_dict = {field: submission_dict[field] for field in fields }

    # Get comments on the submission as list.
    submission.comments.replace_more(limit=None)    # limit=None to handle `More Comments` errors.
    comments = submission.comments.list()

    # Save text from comments.
    submission_dict['comments'] = [comment.body for comment in comments]

    
    # Save everything as a list of dicts.
    data.append(submission_dict)


# Save submissions and comments to a JSON file.
filename = query_term + '-' + time.strftime('%d-%m-%Y-%H-%M-%S', time.localtime(now)) + '.json'

with open(filename, 'w') as f:
    
    print('Writing %d submissions to JSON file.\n' % len(data))

    json.dump(data, f)

print('Done.')
