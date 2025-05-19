
from utils import api_utils, audio_utils
import streamlit as st
import requests



st.set_page_config(page_title="SumarIA", page_icon="🤖")




st.title("Bem vind@ à :rainbow[SumarIA] :robot_face:", anchor=False)

st.subheader('Onde vídeos _muito_ chatos vêm para serem resumidos', anchor=False)

st.markdown('Basta colar o link do vídeo (ou shorts!) _chatão_ do :red-background[Youtube] e você vai receber de volta a transcrição e um resumo do que foi dito no vídeo.')

st.info('Vídeos longos demoram mais e, como o resumo é baseado na transcrição, os vídeos precisam conter áudio.')




# Sidebar (configurações)
with st.sidebar:
    st.header("Configurações adicionais :gear: :star2:")
    deepseek_key = st.text_input("Chave da OpenRouter API (opcional)", type="password")



# Campo para URL do YouTube
video_url = st.text_input("Cole a URL do YouTube:", key='url_input')




if video_url:
    try:
        # Baixar áudio do YouTube
        audio = audio_utils.download_youtube_audio(video_url)


        # Transcrição com Whisper
        with st.spinner("Transcrevendo áudio..."):
            transcribed = audio_utils.model.transcribe(audio, fp16=False)["text"]
        
        st.subheader("📝 Transcrição")
        st.text_area("Texto transcrito:", transcribed, height=200)


        # Resumo com DeepSeek
        with st.spinner("Gerando resumo..."):

            summary = api_utils.generate_summary(transcribed)
        

        st.subheader("🔍 Resumo")
        st.write(summary)
        
        st.balloons()


    except Exception as e:
        st.error(f"Erro: {e}")

else:
    st.info("Cole uma URL do YouTube para começar.")


