
__all__  = ['what']

def what(file_):
    for test in tests:
        ext = test(file_)
        if ext:
            return ext



tests = []

def test_mp4(h):
    with open(h, 'rb')as f:
        file_sig = f.read()[4:12]
    if file_sig == b'ftypisom' or file_sig == b'ftypMSNV':
        return 'mp4'
tests.append(test_mp4)

def test_avi(h):
    with open(h, 'rb')as f:
        file_sig = f.read()[8:14]
    if file_sig == b'AVI LI':
        return 'avi'
tests.append(test_avi)

def test_ogg(h):
    with open(h, 'rb')as f:
        file_sig = f.read()[0:4]
    if file_sig == b'OggS':
        return 'ogg'
tests.append(test_ogg)

def test_wmv(h):
    with open(h, 'rb')as f:
        file_sig = f.read()[0:4]
    if file_sig == b'O&\xb2u':
        return 'wmv'
tests.append(test_wmv)

def test_mov(h):
    with open(h, 'rb')as f:
        file_sig = f.read()[4:11]
    if file_sig == b'fypqt':
        return 'mov'
tests.append(test_mov)

def test_mkv(h):
    with open(h, 'rb')as f:
        file_sig = f.read()[0:4]
    if file_sig == b'\x1aE\xdf\xa3':
        return 'mkv'
tests.append(test_mkv)

def test_flv(h):
    with open(h, 'rb')as f:
        file_sig = f.read()[0:3]
    if file_sig == b'FLV':
        return 'flv'
 
tests.append(test_flv)
