import json
import os


def load_json_file(file_path):
    """
    Load a single JSON file
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except Exception as e:
        print("Error loading JSON:", e)
        return []


def load_folder_questions(folder_path):
    """
    Load all JSON files inside a folder
    """

    questions = []

    if not os.path.exists(folder_path):
        return questions


    for file_name in os.listdir(folder_path):

        if file_name.endswith(".json"):

            file_path = os.path.join(
                folder_path,
                file_name
            )

            data = load_json_file(file_path)

            questions.extend(data)


    return questions