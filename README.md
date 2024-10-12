# YouTube Video Comment Extractor

This Python script extracts comments from a specified YouTube video and saves them to a CSV file for further analysis.

📺 [Watch the tutorial on YouTube](https://www.youtube.com/watch?v=K-yvdE6SY6M) 🎥

---

### 🛠️ Requirements

- `yt-dlp`: A powerful tool for downloading and extracting information from YouTube.
- `pandas`: A data analysis library used to store the extracted comments in a structured format.

---

### How it Works

1. **Video URL**: Specify the YouTube video URL from which you want to extract comments.
2. **Comment Extraction**: Using the `yt-dlp` library with the `getcomments` option enabled, the script fetches the video information and its comments.
3. **Save to CSV**: The extracted comments are stored in a `pandas` DataFrame, and then saved to a CSV file for further use.

---

### Output

The script generates a CSV file named youtube_comments.csv containing all the comments extracted from the video.

### Disclaimer

This script is for educational purposes only. Always ensure that you comply with YouTube’s API and Terms of Service when extracting or processing data.
