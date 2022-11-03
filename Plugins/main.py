try:
    # importing prebuilt modules
    import os
    import logging
    import pyttsx3
    logging.disable(logging.WARNING)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # disabling warnings for gpu requirements
    from keras_preprocessing.sequence import pad_sequences
    import numpy as np
    from keras.models import load_model
    from pickle import load
    import speech_recognition as sr
    import sys
    #sys.path.insert(0, os.path.expanduser('~') + "/PycharmProjects/Virtual_Voice_Assistant")
    sys.path.insert(0, os.path.expanduser('~')+"/Virtual-Voice-Assistant") # adding voice assistant directory to system path
    # importing modules made for assistant
    from database import *
    from image_generation import generate_image
    from gmail import *
    from API_functionalities import *
    from system_operations import *
    from browsing_functionalities import *
except (ImportError, SystemError, Exception, KeyboardInterrupt) as e:
    print("ERROR OCCURRED WHILE IMPORTING THE MODULES")
    exit(0)

'''
import os
import logging
import pyttsx3
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # disabling warnings for gpu requirements
from keras_preprocessing.sequence import pad_sequences
import numpy as np
from keras.models import load_model
from pickle import load
import speech_re