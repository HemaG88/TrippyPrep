from services.json_loader import JSONLoader


def main():

    print("=" * 50)
    print("        TrippyPrep JSON Loader Test")
    print("=" * 50)

    file_path = "data/aptitude/01_foundation/number_system.json"

    try:

        questions = JSONLoader.load(file_path)

        print(f"\n✅ Successfully loaded: {file_path}")
        print(f"📚 Total Questions : {len(questions)}")

        if len(questions) > 0:

            first = questions[0]

            print("\n-------------------------------")
            print("First Question")
            print("-------------------------------")

            print(f"ID         : {first['id']}")
            print(f"Question   : {first['question']}")

            print("\nOptions:")

            for option in first["options"]:
                print(f"  {option}")

            print(f"\nCorrect Option : {first['correct_option']}")
            print(f"Explanation    : {first['explanation']}")

        print("\n✅ JSON Loader Working Successfully!")

    except Exception as e:

        print("\n❌ Error")
        print(e)


if __name__ == "__main__":
    main()