from pymediainfo import MediaInfo


def extract_video_metadata(file_path):

    metadata = {}

    try:

        media_info = MediaInfo.parse(file_path)


        for track in media_info.tracks:

            if track.track_type == "Video":

                metadata["Format"] = track.format
                metadata["Codec"] = track.codec_id
                metadata["Duration"] = track.duration
                metadata["Width"] = track.width
                metadata["Height"] = track.height
                metadata["Frame Rate"] = track.frame_rate
                metadata["Bit Rate"] = track.bit_rate


            elif track.track_type == "Audio":

                metadata["Audio Format"] = track.format
                metadata["Audio Channels"] = track.channel_s
                metadata["Audio Sampling Rate"] = track.sampling_rate


    except Exception as error:

        metadata["Error"] = str(error)


    return metadata