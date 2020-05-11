import io
from PIL import Image
import sys
import urllib.request
import pyocr
import pyocr.builders

def screen_ocr(im_url):
 tools = pyocr.get_available_tools()
 if len(tools) == 0:
  print("No OCR tool found")
  sys.exit(1)
 # The tools are returned in the recommended order of usage
 tool = tools[0]
 print("Will use tool '%s'" % (tool.get_name()))
 # Ex: Will use tool 'libtesseract'

 langs = tool.get_available_languages()
 print("Available languages: %s" % ", ".join(langs))
 lang = langs[0]
 print("Will use lang '%s'" % (lang))
 # Ex: Will use lang 'fra'
 # Note that languages are NOT sorted in any way. Please refer
 # to the system locale settings for the default language
 # to use.

 f = io.BytesIO(urllib.request.urlopen(im_url).read())
 im = Image.open(f)
 im_crop = im.crop((im.width / 2, im.height / 4, im.width / 2 + 245, (im.height / 4) + 295))

 txt = tool.image_to_string(
  im_crop,
  lang=lang,
  builder=pyocr.builders.TextBuilder()
 )

 # txt is a Python string
 print(txt)
 txt = txt.split("\n")
 line_list = []
 for line in txt:
  if line != '' and ((('E' in line and 'C' in line) or 'REAT' in line) or ('Goo' in line or "GOO" in line)
                     or "BAD" in line or ("MISS" in line or "AAISS" in line)):
   line_list.append(line)

 score_list = []
 test_text = ["これくらい全然普通…じゃなかった。すごいね〜！", "うんうん、すごく普通だね〜", ""]
 reply_text = ""

 for line in line_list:
  try:
   score_list.append(int(line.split(" ")[-1]))
  except:
   score_list.append(0)

 try:
  if sum(score_list) == score_list[0]:
   reply_text = "これくらい普通…じゃなかった。Name先輩すごいですー！(広町リサーチ済)"
  elif score_list[2] >= 1:
   reply_text = "うんうん、すごく普通だよ〜(広町リサーチ済)"
  elif sum(score_list) == (score_list[0] + score_list[1]):
   reply_text = "これくらい全然普通…じゃなかった。すごいね〜！(広町リサーチ済)"
 except:
  pass
 print(line_list)
 print(score_list)