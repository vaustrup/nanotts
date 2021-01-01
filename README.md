# NanoTTS python wrapper

This package is a python wrapper for the NanoTTS speech synthesizer utility as described here: https://github.com/gmn/nanotts.

## Installation

You can install this package with `pip install nanotts`.
Make sure you have the NanoTTS synthesizer installed and added to your $PATH.

## Usage

The NanoTTS python wrapper provides two methods to generate speech, one from a string input, the other from a text file.

```python
import nanotts

ntts = nanotts.NanoTTS()

# Generate speech from a string
ntts.speaks("Hello World!")

# Generate speech from a text file
ntts.speak("input.txt")
```

The attributes that can be set are described below:

* `loglevel` [default: `logging.INFO`): set loglevel for the logging module (i.e. `logging.*`)
* `outputFile` [default: `None`: set name of the output .wav file (at least one of `outputFile` and `play` has to be set)
* `pitch` [default: `1.0`]: set pitch in range [0.5, 2.0]
* `play` [default: `False`]: toggle whether to directly play the created speech (at least one of `outputFile` and `play` has to be set)
* `speed` [default: `1.0`]: set speed in range [0.2, 5.0]
* `voice` [default: `"en-GB"`]: choose language from "de-DE", "en-GB", "en-US", "es-ES", "fr-FR", "it-IT"
* `volume` [default: `1.0`]: set volume in range [0.0, 5.0]

