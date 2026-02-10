from pydub import AudioSegment
from tempfile import NamedTemporaryFile
import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def transcribe_audio(audio_bytes: bytes) -> str:
    # salvar ogg temporário
    with NamedTemporaryFile(suffix=".ogg") as ogg_file:
        ogg_file.write(audio_bytes)
        ogg_file.flush()

        # converter para wav
        audio = AudioSegment.from_ogg(ogg_file.name)

        with NamedTemporaryFile(suffix=".wav") as wav_file:
            audio.export(wav_file.name, format="wav")

            # Gemini Speech-to-Text
            model = genai.GenerativeModel("models/gemini-1.5-pro")

            response = model.generate_content([
                "Transcreva fielmente este áudio para texto. "
                "Se estiver em inglês, mantenha o inglês. "
                "Se estiver em português, mantenha o português. "
                "Não traduza.",
                genai.upload_file(wav_file.name)
            ])

    return response.text.strip()
