from ast import arg
from utils import *
from controller import *


if __name__ == "__main__":
    file_name=read_file(args.file)
    time_frames=build_schedule(file_name)
    occurrencies=office_occurrency(time_frames)
    presentation(occurrencies)
