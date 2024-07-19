

import gradio as gr
from barcode import EAN13
from barcode.writer import ImageWriter
def do(num):
  cd=EAN13(num,writer=ImageWriter())
  cd.save('code.png')
  return 'code.png'
iface=gr.Interface(
    fn=do
    ,title='barcode產生器'
    ,description='這是可以產生barcode的工具，請先輸入號碼(12位數)，我們就會幫您產出，點擊右上方即可下載圖片。'
    ,inputs='text'
    ,outputs='image'
)
iface.launch(share='True')