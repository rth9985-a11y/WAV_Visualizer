import wave
import numpy as np
import matplotlib.pyplot as plt

""" DEFINE 
plotAudioWaveform creates a static plot of amplitude of a WAV file over time (sec)
:param: file (from user input)
:return: void 
"""
def plotAudioWaveform(file):
    try:
        file = wave.open(file, 'r')

        # retrieve data from the wave file and setup parameters
        numChannels = file.getnchannels()
        numSamps = file.getnframes()
        sampRate = file.getframerate()
        byteDepth = file.getsampwidth()
        bits = byteDepth * 8
        chunkSize = 1024
        chunkTime = chunkSize / sampRate    #
        rawAudioChunk = file.readframes(numSamps)


        '''

        '''
        def intType(byteDepth):
            bits = byteDepth * 8
            if bits == 8:
                return np.uint8
            elif bits == 16:
                return np.int16
            elif bits == 32:
                return np.int32
   
        ''' DEFINE
        :param a: binary PCM data (rawAudioChunk)
        :type a: byte
        :param b: byteDepth (byteDepth )
        :type a: int
        '''
        def bytesToInt(rawAudioChunk, byteDepth):
            return np.frombuffer(rawAudioChunk, dtype=intType(byteDepth))
            
        audio = bytesToInt(rawAudioChunk, byteDepth)
        if numChannels > 1:
            audio = np.reshape(audio, (-1, numChannels))
        audio = audio / np.max(np.abs(audio))

        duration = numSamps /sampRate
        time = np.linspace(0, duration, numSamps)

        #create the plot
        plt.figure(figsize=(10, 4))
        if numChannels == 1:
            plt.plot(time, audio, linewidth = 0.5)
            plt.title("Amplitude Over Time (mono)")

        else:
            for ch in range (numChannels):
                plt.plot(time, audio[:,ch], linewidth = 0.5, label = f"Channel {ch+1}")
            plt.title("Amplitude Over Time (stereo)")
            plt.legend()

        plt.xlabel("Time(s)")
        plt.ylabel("Amplitude")
        plt.tight_layout()
        plt.show()

    except:
        print("File doesn't exist or could not be opened")


file = input("What file would you like to open?: ")
plotAudioWaveform(file)