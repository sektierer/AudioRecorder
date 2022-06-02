import pyaudio
import wave

print('Welcome to AudioRecorder v0.1\n')
lenrecord = int(input('How long to record audio (in seconds): '))
rate = int(input('Set audio rate (ex. 44100): '))
channels = int(input('How many channels (ex. 2): '))
filename = input('Set filename (ex. test.wav): ')
chunk = 1024
format = pyaudio.paInt16

p = pyaudio.PyAudio()

stream = p.open(format=format,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=chunk)

input('Press enter for start recording...')
print("* recording")

frames = []

for i in range(0, int(rate / chunk * lenrecord)):
    data = stream.read(chunk)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()
print(f'* audio saved as "{filename}"')

input('Press enter for exit...')