from sample_madlibs import philosophy, resolutions, spiritual
import random

if __name__ == "__main__":
    m = random.choice([philosophy,resolutions,spiritual])
    m.madlib()