from docx import Document


def extract_doc_metadata(file_path):

    metadata = {}

    try:

        doc = Document(file_path)

        properties = doc.core_properties


        metadata["Title"] = properties.title
        metadata["Author"] = properties.author
        metadata["Subject"] = properties.subject
        metadata["Keywords"] = properties.keywords
        metadata["Created"] = properties.created
        metadata["Modified"] = properties.modified
        metadata["Last Modified By"] = properties.last_modified_by


    except Exception as error:

        metadata["Error"] = str(error)


    return metadata