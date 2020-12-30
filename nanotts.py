import os
import shutil
import logging
import subprocess

class NanoTTS():
  def __init__(self, 
               voice=None, 
               outputFile=None, 
               play=False, 
               speed=None, 
               pitch=None, 
               volume=None,
               loglevel=logging.INFO):

    if not self._executableInPath():
      raise Exception("Can't find nanotts executable. Make sure to add it to the $PATH.")

    self._outputFile = outputFile
    self._play = play
    self._speed = speed
    self._pitch = pitch
    self._volume = volume
    self._voices = self._getVoices()
    self._voice = voice if self._voiceAvailable else None
    
    self._loglevel = loglevel
    self._logger = logging.getLogger()
    self._logger.setLevel(self._loglevel)

  def _executableInPath(self):
    return shutil.which("nanotts") is not None

  def _getCommand(self):
    cmd = ["nanotts"]
    
    if self._voice is not None: 
      cmd.append("--voice")
      cmd.append(self._voice)
    if self._outputFile is not None: 
      cmd.append("-o")
      cmd.append(self._outputFile)
    if self._play: cmd.append("-p")
    if self._speed is not None: 
      cmd.append("--speed")
      cmd.append(str(self._speed))
    if self._pitch is not None: 
      cmd.append("--pitch")
      cmd.append(str(self._pitch))
    if self._volume is not None:
      cmd.append("--volume")
      cmd.append(str(self._volume))

    if not self._play and self._outputFile is None:
      raise Exception("No output method specified. You need to set at least one of 'play' and 'output'.")
    return cmd

  def speak(self, input_file):
    cmd = self._getCommand()
    cmd.append("-f")
    cmd.append(input_file)

    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

  def speaks(self, text):
    cmd = self._getCommand()
    cmd.append("-i")
    cmd.append(text)

    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

  @property
  def voice(self):
    return self._voice

  @voice.setter
  def voice(self, voice):
    if voice is not None and not self._voiceAvailable(voice):
      warning = "Language '" + voice + "' is not available. Select voices from:\n"
      for v in self._voices: warning += "- " + v + "\n"
      old_voice = self._voice if self._voice is not None else "en-GB"
      warning += "Chosen voice is still " + old_voice + "."
      logging.warning(warning)
      return
    self._voice = voice

  @property
  def speed(self):
    return self._speed

  @speed.setter
  def speed(self, speed):
    self._speed = speed

  @property
  def pitch(self):
    return self._pitch

  @pitch.setter
  def pitch(self, pitch):
    self._pitch = pitch

  @property
  def volume(self):
    return self._volume

  @volume.setter
  def volume(self, volume):
    self._volume = volume
  
  @property
  def outputFile(self):
    return self._outputFile

  @outputFile.setter
  def outputFile(self, outputFile):
    self._outputFile = outputFile
  
  @property
  def play(self):
    return self._play

  @play.setter
  def play(self, play):
    self._play = play
  
  @property
  def loglevel(self):
    return self._loglevel

  @loglevel.setter
  def loglevel(self, loglevel):
    self._loglevel = loglevel
    self._logger.setLevel(self._loglevel)

  def _voiceAvailable(self, voice):
    return voice in self._voices

  def _getVoices(self):
    lang_dir = os.fsencode(shutil.which("nanotts")[:-7] + "lang")
    voices = []
    for f in os.listdir(lang_dir):
      filename = os.fsdecode(f)
      if filename.endswith("_ta.bin"):
        voices.append(filename[0:5])
    return voices

