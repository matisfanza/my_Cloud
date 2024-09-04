import streamlit as st
import cv2
import os
import ffmpeg

# 画像の自動再生機能
def display_images(folder_path, interval):
    images = [os.path.join(folder_path, img) for img in os.listdir(folder_path) if img.endswith(('png', 'jpg', 'jpeg'))]
    for img_path in images:
        img = cv2.imread(img_path)
        st.image(img, caption=os.path.basename(img_path))
        st.time.sleep(interval)

# 動画のアイコン表示機能
def display_videos(folder_path):
    videos = [os.path.join(folder_path, vid) for vid in os.listdir(folder_path) if vid.endswith(('mp4', 'avi', 'mov'))]
    for vid_path in videos:
        vidcap = cv2.VideoCapture(vid_path)
        success, image = vidcap.read()
        if success:
            st.image(image, caption=os.path.basename(vid_path))
        vidcap.release()

st.title("クラウドアプリ")
st.write("画像と動画をアップロードして表示します。")

uploaded_files = st.file_uploader("ファイルをアップロード", accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success("ファイルがアップロードされました。")

folder_path = "uploads"
interval = st.selectbox("自動再生の間隔（秒）", [5, 10, 15])
if st.button("画像を自動再生"):
    display_images(folder_path, interval)

if st.button("動画を表示"):
    display_videos(folder_path)
