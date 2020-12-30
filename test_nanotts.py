import unittest
import nanotts
import logging

class TestNanoTTS(unittest.TestCase):

  def setUp(self):
    self.ntts = nanotts.NanoTTS()
    self.ntts.loglevel = logging.CRITICAL

  def test_getVoices(self):
    self.assertCountEqual(self.ntts._getVoices(), ["de-DE", "en-GB", "en-US", "es-ES", "fr-FR", "it-IT"])

  def test_setVoiceSuccess(self):
    self.ntts.voice = "de-DE"
    self.assertEqual(self.ntts.voice, "de-DE")

  def test_setVoiceFailure(self):
    self.ntts.voice = "foo"
    self.assertEqual(self.ntts.voice, None)

  def test_setSpeed(self):
    self.ntts.speed = 2
    self.assertEqual(self.ntts.speed, 2)

  def test_setPitch(self):
    self.ntts.pitch = 2
    self.assertEqual(self.ntts.pitch, 2)

  def test_setVolume(self):
    self.ntts.volume = 2
    self.assertEqual(self.ntts.volume, 2)

  def test_setPlay(self):
    self.ntts.play = True
    self.assertEqual(self.ntts.play, True)

  def test_setOutputFile(self):
    self.ntts.outputFile = "test.wav"
    self.assertEqual(self.ntts.outputFile, "test.wav")

  def test_NoOutputMethod(self):
    self.ntts.play = False
    self.ntts.outputFile = None
    self.assertRaises(Exception, self.ntts._getCommand)

  def test_getCommand(self):
    self.ntts.play = True
    self.ntts.outputFile = "test.wav"
    self.ntts.voice = "en-GB"
    self.ntts.volume = 1
    self.ntts.pitch = 1
    self.ntts.speed = 1
    self.assertListEqual(self.ntts._getCommand(), ['nanotts', '--voice', 'en-GB', '-o', 'test.wav', '-p', '--speed', '1', '--pitch', '1', '--volume', '1']) 

if __name__ == "__main__":
  unittest.main()
