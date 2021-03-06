# Example for using the parse_midi.py library usage.
import save_to_file


def main():
    output_folder = "./output/"
    midi_folder = "./midi/elder/"

    #print("1. Converting a single file:")
    #save_to_file.convertSingleFile("./midi/country/sweet-home-alabama.mid", output_folder + "out.jsonl")

    print("\n\n2. Converting all files of a folder:")
    save_to_file.convertMultipleFiles(midi_folder, output_folder + "all_files/", multi=True)


if __name__ == '__main__':
    main()
