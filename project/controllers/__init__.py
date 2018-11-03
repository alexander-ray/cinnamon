import os
import glob

# Example from https://github.com/salimane/flask-mvc/
# Defines * for directory
__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
