from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # 词云，颜色生成器，停止词
import jieba  # 词语切割
import matplotlib.pyplot as plt # 数据可视化
from PIL import Image  # 处理图片
import numpy as np  # 科学计算


path_txt = 'C:/Users/local-hz23128870/Desktop/wordcloud'  # 文本路径
path_bg = 'C:/Users/local-hz23128870/Desktop/wordcloud/dive.jpg'  # 词云背景模板路径
font_path = 'C:/Windows/Fonts/Alibaba-PuHuiTi-Regular.otf'  # 设置字体，可以显示中文


file = open(r"C:\Users\local-hz23128870\Desktop\wordcloud\word.txt",encoding='UTF8')
text = file.read()  # 读入一个中文txt文件,gbk -> utf-8
words = jieba.lcut(text)  # 使用jieba库分词,生成字符串
string = ' '.join(words)  # 使用join()方法，将分词生成的字符串以空格进行分割,生成词云时，字符串之间需要为空格
print(len(string))  # 输出词量

img = Image.open(r'C:\Users\local-hz23128870\Desktop\wordcloud\dive.jpg')  # 打开图片
img_array = np.array(img)  # 将图片装换为数组

# 设置停止词 
stopwords = open(r"C:\Users\local-hz23128870\Desktop\wordcloud\baidu_stopwords.txt",encoding='UTF8').read().split("\n")

# 配置词云的背景，图片，字体大小等参数
wc = WordCloud(
    background_color='white',  # 设置显示内容在什么颜色内
    width=1920000111,  # 设置图片宽,默认为400
    height=1080000111,  # 设置图片高,默认为200
    mask=img_array,  # 设置词云背景模板
    font_path=font_path,  # 设置字体路径
    stopwords=stopwords,  # 设置需要屏蔽的词，如果为空，则使用内置的STOPWORDS
    scale=10,  # 图照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍
    max_words=100000,  # max_words图片上显示的最大词语的个数
    max_font_size=120,  # max_font_size为最大字体的大小
    min_font_size=4,  # min_font_size为最小字体大小,默认为4
    mode='RGB',  # ,默认值RGB,当参数为“RGBA”并且background_color不为空时，背景为透明
    relative_scaling=.3,  # 词频和字体大小的关联性,默认值
    collocations=0# 是否包括两个词的搭配
)

wc.generate_from_text(string)  # 根据文本生成词云
image_colors = ImageColorGenerator(img_array)  # 获取color
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")  # 按照给定的图片颜色布局生成字体颜色,当wordcloud尺寸比image大时，返回默认的颜色
plt.axis('off')  # 关闭坐标轴
plt.show()  # 显示图片
wc.to_file(r"C:\Users\local-hz23128870\Desktop\wordcloud\1.jpg")  # 保存图片
