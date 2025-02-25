from moviepy.video.io.VideoFileClip import VideoFileClip
import os

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

def main():
    """
    Main function that extracts audio from a video file.
    Usage example:
    
    # Extract audio from a video and save to a specific folder
    output = extract_audio_from_video("path/to/video.mp4", "path/to/output/folder", "wav")
    print(f"Audio saved to: {output}")
    
    # Extract audio and save in the same folder as the video
    output = extract_audio_from_video("path/to/video.mp4")
    print(f"Audio saved to: {output}")
    """
    # Example usage
    video_path = "./assets/video/maza_aya.mp4"  # Replace with actual video path
    output_folder = "./assets/audio"  # Replace with desired output folder
    
    audio, video = extract_audio_from_video(video_path)
    
    if audio is None:
        print("Error: No audio stream found in the video file.")
        return 1
        
    try:
        # Prepare output path
        video_filename = os.path.basename(video_path)
        base_name = os.path.splitext(video_filename)[0]
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, f"{base_name}.mp3")
        
        # Save audio to file
        print(f"Saving audio to {output_path}")
        audio.write_audiofile(output_path)
        
        print(f"Audio extraction complete: {output_path}")
        return 0
    
    except Exception as e:
        print(f"Error saving audio: {e}")
        return 1
    
    finally:
        # Close video file
        if video is not None:
            video.close()

if __name__ == "__main__":
    main()