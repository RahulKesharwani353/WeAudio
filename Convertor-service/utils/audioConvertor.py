from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio_from_video(video_path):
    try:
        # Create a VideoFileClip object - using direct import
        print(f"Processing video: {video_path}")
        video = VideoFileClip(video_path)
        
        # Get the audio from the video
        audio = video.audio
        
        if audio is None:
            print("No audio stream found in the video file.")
            return None, None
   
        return audio, video  # Return both audio and video so we can close video later
    except Exception as e:
        print(f"Error extracting audio: {str(e)}")
        return None, None