from PIL import Image, ImageDraw,ImageFont
import math

# User settings

lens_name = "Makro_symmar_180HM"

lens_efl_mm = 179.9
focusing_ring_extension_mm_per_deg = 4/45
focusing_ring_max_angle = 165
hpf_ring_diameter_mm = 86.7
hpf_ring_width_mm = 9.5
text_len = 4
output_dpi = 300
dash_length_mm = 1.0
dash_width_mm = 0.5
fontPath = "./Square721 Cn BT Bold.ttf"
show_efl = True
save_file_path = "./"


# System variables

output_angle = [1,2,3,4]+[(i+1)*5 for i in range(165//5)]


image_size_mm = hpf_ring_diameter_mm*3.1416
mm2inch_ratio = 25.4
image_h_pix = int(image_size_mm/mm2inch_ratio*output_dpi)
image_w_pix = int(hpf_ring_width_mm/mm2inch_ratio*output_dpi)
dash_len_pix = int(dash_length_mm/mm2inch_ratio*output_dpi)
dash_width_pix = int(dash_width_mm/mm2inch_ratio*output_dpi)
canvas_sizeX,canvas_sizeY = image_w_pix,image_h_pix
print("图片尺寸"+str(canvas_sizeX))



project_name = lens_name+"_"+str(lens_efl_mm) +"mm"+ "_M65_HPF_Sticker_"\
+ str(image_w_pix) +"x" +str(image_h_pix)+"mm_" + str(output_dpi) + "dpi"

print(project_name)


fnt = ImageFont.truetype(fontPath, image_w_pix/3)


print("Creating canvas")


# 创建600x600的黑色背景灰度图像
img = Image.new('L', (canvas_sizeX,canvas_sizeY), color=0)
draw = ImageDraw.Draw(img)

# draw.rectangle([(0,0),(canvas_sizeX,canvas_sizeY)], fill=0, outline=255, width=image_w_pix//100)




print("Canvas generated")


text_distance = hpf_ring_diameter_mm*output_dpi*3.1416/360/mm2inch_ratio


dash_start_y = image_w_pix/6+dash_width_pix//2
draw.line([(0,text_distance+dash_start_y),(dash_len_pix,text_distance+dash_start_y)], fill=255, width=dash_width_pix)
draw.text((dash_len_pix+10, text_distance), "INF", font=fnt, fill=255)



for i in output_angle:
    extension = focusing_ring_extension_mm_per_deg*i
    v = lens_efl_mm+extension
    u = 1/(1/lens_efl_mm- 1/ v)/1000
    if u > 999:
        print("please change your setting")
    hpf_sign = str(u+v/1000)

    if "." in hpf_sign and u<100:
        hpf_sign = hpf_sign[:text_len+1]
    elif u>=100 and "." in hpf_sign:
        hpf_sign = hpf_sign[:text_len+1]
    else:
        hpf_sign = hpf_sign[:text_len]

    # print(extension,u,hpf_sign)
    # print(i)
    if i < 5:
        draw.line([(0,text_distance*(i)*5+10+dash_start_y),(dash_len_pix,text_distance*(i)*5+10+dash_start_y)], fill=255, width=dash_width_pix)
        draw.text((dash_len_pix+10, text_distance*(i)*5+10), hpf_sign, font=fnt, fill=255)
    else:
        draw.line([(0,text_distance*(i+20)+10+dash_start_y),(dash_len_pix,text_distance*(i+20)+10+dash_start_y)], fill=255, width=dash_width_pix)
        draw.text((dash_len_pix+10, text_distance*(i+20)+10), hpf_sign, font=fnt, fill=255)

if show_efl:
    draw.text((10, text_distance*(output_angle[-1]+30)+10), "E.F.L.", font=fnt, fill=255)
    draw.text((10, text_distance*(output_angle[-1]+35)+10), str(lens_efl_mm), font=fnt, fill=255)
    draw.text((10, text_distance*(output_angle[-1]+39)+10), "   m/m", font=fnt, fill=255)


print("Saving Raw image")

# 保存图像
img.save(save_file_path+
    project_name+"_raw_PNG.png",
    dpi = (output_dpi,output_dpi)
    )

# print("Creating dithered image")


# dithered_img = img.convert('1', dither=Image.FLOYDSTEINBERG)
# dithered_img.save(
#     project_name+"_dithered_PNG.png",
#     dpi = (output_dpi,output_dpi)
# )    

print("Well done")
