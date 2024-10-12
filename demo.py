# 導入所需的庫
from yt_dlp import YoutubeDL
import pandas as pd


# 設定影片的URL
video_url = "https://www.youtube.com/watch?v=An37m2r1f2U"

# 設定選項來獲取評論
opts = {
    "getcomments": True
}

# 使用YoutubeDL來提取影片信息及評論
with YoutubeDL(opts) as yt:
    info = yt.extract_info(video_url, download=False)
    comments = info.get("comments", [])
    comment_count = info.get("comment_count", 0)

# 將評論轉換為DataFrame
comments_df = pd.DataFrame(comments)

# 將DataFrame保存為CSV文件
comments_df.to_csv('youtube_comments.csv', index=False, encoding='utf-8-sig')

print("評論已成功保存至 'youtube_comments.csv'")