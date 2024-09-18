import argparse
import utility as ut 


def main():

    # Check if the database should be cleared (using the --clear flag).
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        ut.clear_database()

    # Create (or update) the data store.
    documents = ut.load_documents()
    chunks = ut.split_documents(documents)
    ut.add_to_chroma(chunks)


if __name__ == "__main__":
    main()