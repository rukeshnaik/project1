from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def convert_to_degrees(value):

    try:
        d = float(value[0])
        m = float(value[1])
        s = float(value[2])

        return round(d + (m / 60.0) + (s / 3600.0), 6)

    except:
        return None



def extract_gps(exif):

    gps_result = {}

    if "GPSInfo" not in exif:
        return gps_result


    gps_info = exif.get_ifd(34853)


    gps = {}

    for key, value in gps_info.items():

        gps[GPSTAGS.get(key, key)] = value



    if "GPSLatitude" in gps:

        latitude = convert_to_degrees(
            gps["GPSLatitude"]
        )

        if gps.get("GPSLatitudeRef") == "S":
            latitude = -latitude

        gps_result["Latitude"] = latitude



    if "GPSLongitude" in gps:

        longitude = convert_to_degrees(
            gps["GPSLongitude"]
        )

        if gps.get("GPSLongitudeRef") == "W":
            longitude = -longitude

        gps_result["Longitude"] = longitude



    if "GPSAltitude" in gps:

        try:
            gps_result["Altitude"] = (
                str(gps["GPSAltitude"]) + " meters"
            )
        except:
            pass


    return gps_result



def extract_image_metadata(file_path):

    metadata = {}

    try:

        image = Image.open(file_path)


        # File Information

        metadata["FILE INFORMATION"] = ""

        metadata["Format"] = image.format

        metadata["Resolution"] = (
            f"{image.width} x {image.height}"
        )


        exif = image.getexif()


        if not exif:

            metadata["Info"] = "No EXIF metadata found"

            return metadata



        # Camera Information

        metadata[""] = ""

        metadata["CAMERA INFORMATION"] = ""


        for tag_id, value in exif.items():

            tag = TAGS.get(
                tag_id,
                tag_id
            )


            if tag == "Make":

                metadata["Camera Make"] = value


            elif tag == "Model":

                metadata["Camera Model"] = value


            elif tag == "Software":

                metadata["Software"] = value


            elif tag == "DateTime":

                metadata["Date Taken"] = value



            elif tag == "ISOSpeedRatings":

                metadata["ISO"] = value


            elif tag == "ExposureTime":

                metadata["Exposure Time"] = value


            elif tag == "FocalLength":

                metadata["Focal Length"] = value



        # GPS Information


        metadata[""] = ""

        metadata["LOCATION INFORMATION"] = ""


        gps = extract_gps(exif)


        if gps:

            metadata.update(gps)

        else:

            metadata["GPS"] = "No GPS data available"



    except Exception as e:

        metadata["Error"] = str(e)



    return metadata