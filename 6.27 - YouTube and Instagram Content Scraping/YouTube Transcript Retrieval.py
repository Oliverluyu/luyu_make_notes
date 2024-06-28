#!/usr/bin/python
# -*- coding: utf-8 -*-
from youtube_transcript_api import YouTubeTranscriptApi


def fetch_video_transcript(video_url):

    # Extracting Video ID from URL

    if 'youtu.be' in video_url:
        video_id = video_url.split('/')[-1]
    else:
        video_id = video_url.split('v=')[-1].split('&')[0]

    # Attempt to fetch the video transcript

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        full_transcript = '\n'.join([item['text'] for item in
                                    transcript_list])
        return full_transcript
    except Exception as e:
        return 'Failed to fetch transcript: {}'.format(str(e))


# Main block to set the 'result' variable, as expected by the platform

video_url = '{{7.`Apify Dataset`[].pageUrl}}'
result = fetch_video_transcript(video_url)