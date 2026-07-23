import os

from extractors.image import extract_image_metadata
from extractors.pdf import extract_pdf_metadata
from extractors.document import extract_doc_metadata
from extractors.video import extract_video_metadata


def extract_metadata(file_path):

    extension = os.path.splitext(file_path)[1].lower()


    # Image files
    if extension in [".jpg", ".jpeg", ".png"]:

        return extract_image_metadata(file_path)


    # PDF files
    elif extension == ".pdf":

        return extract_pdf_metadata(file_path)


    # Word documents
    elif extension == ".docx":

        return extract_doc_metadata(file_path)


    # Video files
    elif extension in [".mp4", ".mkv", ".avi"]:

        return extract_video_metadata(file_path)


    # Unsupported files
    else:

        return {
            "Error": "Unsupported file type"
        }