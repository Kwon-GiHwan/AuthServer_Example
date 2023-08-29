import re
def separate(ch):
    """한글 자모 분리. 주어진 한글 한 글자의 초성, 중성 초성을 반환함."""
    uindex = ord(ch) - 0xAC00
    jongseong = uindex % 28
    # NOTE: Force integer-divisions
    joongseong = ((uindex - jongseong) // 28) % 21
    choseong = ((uindex - jongseong) // 28) // 21

    return choseong

def build(choseong, joongseong, jongseong):
    """초성, 중성, 종성을 조합하여 완성형 한 글자를 만듦. 'choseong',
    'joongseong', 'jongseong' are offsets. For example, 'ㄱ' is 0, 'ㄲ' is 1,
    'ㄴ' is 2, and so on and so fourth."""
    code = int(((((choseong) * 21) + joongseong) * 28) + jongseong + 0xAC00)
        # Python 3.x
    return chr(code)

def is_hangul(ch):
    if ch is None:
        return False
    else:
        return ord(ch) >= 0xAC00 and ord(ch) <= 0xD7A3

def has_chosung(val: str) -> bool:
    """
    초성만 포함되었는지 여부
    :param val:
    :return: bool
    """
    regex = re.compile(r"[ㄱ-ㅎ]")
    if regex.match(val):
        return True
    return False

def get_hangul(val: str) -> str:
    """
    한글만 가져오기
    :param val:
    :return: str
    """
    regex_only_hangul = re.compile('[ㄱ-ㅎㅏ-ㅣ가-힣]')
    return "".join(regex_only_hangul.findall(val))
