import struct


def get(fhandle):
    height = -1
    width = -1

    # with open(str(filepath), 'rb') as fhandle:
    head = fhandle.read(32)
    size = len(head)
    # handle GIFs
    if size >= 10 and head[:6] in (b'GIF87a', b'GIF89a'):
        # Check to see if content_type is correct
        try:
            width, height = struct.unpack("<hh", head[6:10])
        except struct.error:
            raise ValueError("Invalid GIF file")
    elif size >= 24 and head.startswith(b'RIFF') and head[8:12] == b'WEBP':
        try:
            chunks = split_webp(head)
        except:
            raise ValueError("invalid split")
        try:
            width, height = get_webp_size(chunks)
        except:
            raise ValueError("invalid get size")
    # see png edition spec bytes are below chunk length then and finally the
    elif size >= 24 and head.startswith(b'\211PNG\r\n\032\n') and head[12:16] == b'IHDR':
        try:
            width, height = struct.unpack(">LL", head[16:24])
        except struct.error:
            raise ValueError("Invalid PNG file")
    # Maybe this is for an older PNG version.
    elif size >= 16 and head.startswith(b'\211PNG\r\n\032\n'):
        # Check to see if we have the right content type
        try:
            width, height = struct.unpack(">LL", head[8:16])
        except struct.error:
            raise ValueError("Invalid PNG file")
    return width, height


def split_webp(data):
    start = 12
    pointer = start
    CHUNK_FOURCC_LENGTH = 4
    LENGTH_BYTES_LENGTH = 4

    chunks = []
    while pointer + CHUNK_FOURCC_LENGTH + LENGTH_BYTES_LENGTH < len(data):
        fourcc = data[pointer:pointer + CHUNK_FOURCC_LENGTH]
        pointer += CHUNK_FOURCC_LENGTH
        chunk_length_bytes = data[pointer:pointer + LENGTH_BYTES_LENGTH]
        chunk_length = struct.unpack("<L", chunk_length_bytes)[0]
        pointer += LENGTH_BYTES_LENGTH

        chunk_data = data[pointer:pointer + chunk_length]
        chunks.append({"fourcc": fourcc, "length_bytes": chunk_length_bytes, "data": chunk_data})

        padding = 1 if chunk_length % 2 else 0

        pointer += chunk_length + padding
    return chunks


def _get_size_from_vp8x(chunk):
    width_minus_one_bytes = chunk["data"][-6:-3] + b"\x00"
    width_minus_one = struct.unpack("<L", width_minus_one_bytes)[0]
    width = width_minus_one + 1
    height_minus_one_bytes = chunk["data"][-3:] + b"\x00"
    height_minus_one = struct.unpack("<L", height_minus_one_bytes)[0]
    height = height_minus_one + 1
    return width, height


def _get_size_from_vp8(chunk):
    BEGIN_CODE = b"\x9d\x01\x2a"
    begin_index = chunk["data"].find(BEGIN_CODE)
    if begin_index == -1:
        ValueError("wrong VP8")
    else:
        BEGIN_CODE_LENGTH = len(BEGIN_CODE)
        LENGTH_BYTES_LENGTH = 2
        length_start = begin_index + BEGIN_CODE_LENGTH
        width_bytes = chunk["data"][length_start:length_start + LENGTH_BYTES_LENGTH]
        width = struct.unpack("<H", width_bytes)[0]
        height_bytes = chunk["data"][length_start + LENGTH_BYTES_LENGTH:length_start + 2 * LENGTH_BYTES_LENGTH]
        height = struct.unpack("<H", height_bytes)[0]
        return width, height


def _get_size_from_vp8l(chunk):
    b1 = chunk["data"][1:2]
    b2 = chunk["data"][2:3]
    b3 = chunk["data"][3:4]
    b4 = chunk["data"][4:5]

    width_minus_one = (ord(b2) & ord(b"\x3F")) << 8 | ord(b1)
    width = width_minus_one + 1

    height_minus_one = (ord(b4) & ord(b"\x0F")) << 10 | ord(b3) << 2 | (ord(b2) & ord(b"\xC0")) >> 6
    height = height_minus_one + 1

    return width, height


def get_webp_size(chunks):
    width = None
    height = None

    for chunk in chunks:
        if chunk["fourcc"] == b"VP8X":
            width, height = _get_size_from_vp8x(chunk)
        elif chunk["fourcc"] == b"VP8 ":
            width, height = _get_size_from_vp8(chunk)
        elif chunk["fourcc"] == b"VP8L":
            width, height = _get_size_from_vp8l(chunk)
    return width, height
