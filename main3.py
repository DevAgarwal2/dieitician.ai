from elevenlabs import voices, generate,Voice, VoiceSettings, generate,play

voices = voices()
audio = generate(text="Hello there!", voice=voices[0])
print(voices)

audio2 = generate(
    text="Hello! My name is Bella.",
    voice=Voice(
        voice_id='EXAVITQu4vr4xnSDxMaL',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)

play(audio2)