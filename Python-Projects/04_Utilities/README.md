# 🔧 04 — Utilities

Real-world automation and productivity tools.

## Scripts

| File | Description |
|------|-------------|
| `pdf_reader_tts.py` | Reads a PDF page aloud using text-to-speech |
| `qr_code_generator.py` | Generates a QR code SVG from any URL |
| `video_to_audio.py` | Extracts audio track from a video as MP3 |
| `whatsapp_auto_message.py` | Sends a WhatsApp message at a scheduled time |
| `youtube_playlist_downloader.py` | Downloads all videos from a YouTube playlist |
| `phone_camera_stream.py` | Streams your phone's camera to PC over Wi-Fi |

## Run

```bash
pip install pypdf pyttsx3 pyqrcode pypng moviepy pywhatkit pytube opencv-python
```

## Setup Notes

### `pdf_reader_tts.py`
- Update the PDF file path on line 4 to your local PDF.

### `whatsapp_auto_message.py`
- Update the phone number, message, hour, and minute.
- WhatsApp Web must be open in your browser.

### `phone_camera_stream.py`
- Install **IP Webcam** app on your Android phone.
- Connect phone and PC to the same Wi-Fi.
- Update the IP address in the script to your phone's IP.

### `youtube_playlist_downloader.py`
- Replace the `playlist_url` with your desired playlist link.
