import praw
import random
import csv

client_id = 'pmeZOFB-mV2NkCYke8-9Dw'
client_secret = 'gKNCeEk9lhg4vGUtyfehIPk2HZ5X0A'
user_agent = 'user_analysis'  

# Xác thực với Reddit API
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

subreddits = ['announcements', 'funny', 'AskReddit', 'gaming', 'aww', 'Music', 'pics', 'science', 'worldnews','videos','todayilearned','movies','sports']

posts_collected = 0
max = 1200

with open('reddit_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ["Tiêu đề bài đăng",
    "Tác giả",
    "Điểm số (Lượt upvote - Lượt downvote)",
    "URL bài đăng",
    "Số lượng bình luận",
    "Nội dung tóm tắt (Selftext)",
    "Thời gian đăng bài",
    "Phụ đề (Caption)",
    "Loại bài đăng",]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()

    while posts_collected < max:
        subreddit_name = random.choice(subreddits)
        subreddit = reddit.subreddit(subreddit_name)
        try:
                for post in subreddit.hot(limit=10): 
                    if posts_collected >= max:
                        break
                    print("----------------------")
                    post_info = {
                        "Tiêu đề bài đăng": post.title,
                        "Tác giả": str(post.author),
                        "Điểm số (Lượt upvote - Lượt downvote)": post.score,
                        "URL bài đăng": post.url,
                        "Số lượng bình luận": post.num_comments,
                        "Nội dung tóm tắt (Selftext)": post.selftext,
                        "Thời gian đăng bài": post.created_utc,
                        "Tỷ lệ upvote": post.upvote_ratio if hasattr(post,'upvote_ratio') else "",
                    }
                    print(post_info)
                    print("--------" , posts_collected, "/" , max , "----------" )
                    posts_collected += 1
                    writer.writerow(post_info)                                        
        except Exception as e:
                print(f"Error in {subreddit.display_name}: {e}")

print(f"Đã thu thập {posts_collected} bài viết.")
