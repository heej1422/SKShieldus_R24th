from deep_translator import GoogleTranslator

# 입력
input_text = input("한글을 입력하세요: ")

# 번역
translated = GoogleTranslator(source='ko', target='en').translate(input_text)

# 출력
print(f"입력한 한글: {input_text}")
print(f"번역된 영어: {translated}")