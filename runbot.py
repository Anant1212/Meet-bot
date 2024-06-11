from audio import record_audio
from playback import play_audio
from request import send_audio
from selenium import join_meeting


def run_bot(meeting_link, email, password):
    driver = join_meeting(meeting_link, email, password)
    while True:
        if is_muted(driver):
            filename = 'recorded_audio.wav'
            record_audio(filename)
            processed_audio = send_audio(filename)
            play_audio(processed_audio)
            unmute(driver)

def is_muted(driver):
    # Logic to detect if the bot is muted
    pass

def unmute(driver):
    # Logic to unmute the bot
    pass
