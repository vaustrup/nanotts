import unittest

import nanotts
import logging
import os

class TestNanoTTS(unittest.TestCase):

  def setUp(self):
    self.ntts = nanotts.NanoTTS()
    self.ntts.loglevel = logging.CRITICAL

  def test_logLevel(self):
    self.assertEqual(self.ntts.loglevel, logging.CRITICAL)

  def test_getVoices(self):
    self.assertCountEqual(self.ntts._getVoices(), ["de-DE", "en-GB", "en-US", "es-ES", "fr-FR", "it-IT"])

  def test_setVoiceSuccess(self):
    self.ntts.voice = "de-DE"
    self.assertEqual(self.ntts.voice, "de-DE")

  def test_setVoiceFailure(self):
    self.ntts.voice = "foo"
    self.assertEqual(self.ntts.voice, None)

  def test_setVoiceFailureInit(self):
    ntts = nanotts.NanoTTS(voice="foo")
    self.assertEqual(ntts.voice, None)

  def test_setSpeedSuccess(self):
    self.ntts.speed = 2
    self.assertEqual(self.ntts.speed, 2)

  def test_setSpeedFailureMax(self):
    self.ntts.speed = 10
    self.assertEqual(self.ntts.speed, nanotts.MAX_SPEED)

  def test_setSpeedFailureMin(self):
    self.ntts.speed = 0.1
    self.assertEqual(self.ntts.speed, nanotts.MIN_SPEED)

  def test_setPitchSuccess(self):
    self.ntts.pitch = 2
    self.assertEqual(self.ntts.pitch, 2)

  def test_setPitchFailureMax(self):
    self.ntts.pitch = 10
    self.assertEqual(self.ntts.pitch, nanotts.MAX_PITCH)

  def test_setPitchFailureMin(self):
    self.ntts.pitch = 0.1
    self.assertEqual(self.ntts.pitch, nanotts.MIN_PITCH)

  def test_setVolumeSuccess(self):
    self.ntts.volume = 2
    self.assertEqual(self.ntts.volume, 2)

  def test_setVolumeFailureMax(self):
    self.ntts.volume = 10
    self.assertEqual(self.ntts.volume, nanotts.MAX_VOLUME)

  def test_setVolumeFailureMin(self):
    self.ntts.volume = -0.1
    self.assertEqual(self.ntts.volume, nanotts.MIN_VOLUME)

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
