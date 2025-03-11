import os, json, tempfile
from utils.audioConvertor import extract_audio_from_video
from client.rabbitMQClient import consume_messages
from utils.download import download
from utils.upload import upload

VIDEO_DB = "VIDEO_DB"
AUDIO_DB = "AUDIO_DB"

def callback(ch, method, properties, body):
    print(f" [>] Received message: {body[:100]}...")
    message = json.loads(body)
    v_file_id = message.get("video_fid")
    print(f" [>] Processing video file: {v_file_id}")
    tf = tempfile.NamedTemporaryFile(delete=False)
    video, status = download(v_file_id)
    tf.write(video.read())

    audio, vid = extract_audio_from_video(tf.name)
    tf.close()
    tf_path = tempfile.gettempdir() + f"/{v_file_id}.mp3"
    audio.write_audiofile(tf_path)
    audio.close()
    vid.close()
    

    f = open(tf_path, "rb")
    msg = upload(f)
    f.close()
    print(f" [✓] Processing completed successfully {msg}")

    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    """
    Main function that extracts audio from a video file.

    """
    
    consume_messages(callback)
    
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