from to_midi import Midi

def main():
    mid = Midi(1, 100)

    mid.push_notes([54, 63, 74, 45], [1, 2, 1, 1])

    mid.write_mid("test")

if __name__ == "__main__":
    main()
