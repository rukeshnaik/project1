from PyPDF2 import PdfReader


def extract_pdf_metadata(file_path):

    metadata = {}

    try:

        pdf = PdfReader(file_path)

        info = pdf.metadata

        if info:

            for key, value in info.items():

                metadata[key] = value

        else:

            metadata["Info"] = "No PDF metadata found"


    except Exception as error:

        metadata["Error"] = str(error)


    return metadata