import hashlib


def generate_hash(file_path):

    md5 = hashlib.md5()

    sha256 = hashlib.sha256()


    with open(file_path, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break


            md5.update(data)

            sha256.update(data)


    return {

        "MD5": md5.hexdigest(),

        "SHA256": sha256.hexdigest()

    }