#pyocrとTesseractをインストールしてください。
import re
from PIL import Image
import pyocr.builders
tools = pyocr.get_available_tools()
tool = tools[0]
image_name = input("画像の名前を教えてください。")
img_org = Image.open(image_name)
builder = pyocr.builders.TextBuilder()
result = tool.image_to_string(img_org, lang="jpn", builder=builder)
kougeki = None
kaisin_ritu = None
kaisin_dame = None
try:
    kougeki = re.search(r'攻撃力(.+)%', str(result)).group(1)
except Exception as e:
    pass
try:
    kaisin_ritu = re.search(r'会心率(.+)%', str(result)).group(1)
except Exception as e:
    pass
try:
    kaisin_dame = re.search(r'会心ダメージ(.+)%', str(result)).group(1)
except Exception as e:
    pass
try:
    kougeki = kougeki.replace('+', '')
except Exception as e:
    pass
try:
    kaisin_ritu = kaisin_ritu.replace('+', '')
except Exception as e:
    pass
try:
    kaisin_dame = kaisin_dame.replace('+', '')
except Exception as e:
    pass
if kougeki == None:kougeki=0.0
if kaisin_ritu == None:kaisin_ritu=0.0
if kaisin_dame == None:kaisin_dame=0.0
print(f"スコア {float(kougeki)+float(kaisin_ritu) * 2+float(kaisin_dame)}")
