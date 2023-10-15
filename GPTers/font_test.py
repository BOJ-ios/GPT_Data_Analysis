from matplotlib import pyplot as plt
from matplotlib import font_manager


def test_korean_font_direct_explicit(font_path):
    """Test Korean font by plotting a sample text with direct method."""
    font_properties = font_manager.FontProperties(fname=font_path)
    plt.figure(figsize=(5, 5))
    plt.text(0.5, 0.5, '한글 폰트 테스트', size=20, ha='center',
             va='center', fontproperties=font_properties)
    plt.axis('off')
    plt.show()


test_korean_font_direct_explicit(
    "C:/Users/LoewllZoe/Downloads/NanumGothicBold.ttf")
