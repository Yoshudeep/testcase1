import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("Real-time Webcam Feed")

def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    # Convert frame to numpy array
    img = frame.to_ndarray(format="bgr24")
    
    # Optional: do some processing here (currently just passes frame)
    
    # Convert back to VideoFrame
    return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
