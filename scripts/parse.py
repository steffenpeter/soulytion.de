import re
import shutil
from bs4 import BeautifulSoup

with open('index.html.in', 'r', encoding='utf-8', errors='replace') as file:
    content = file.read()

fout = open('index.md', 'w', encoding='utf-8')

    #.encode('latin-1', errors='replace')

soup = BeautifulSoup(content, "html.parser")

for a_tag in soup.find_all('a'):
    if not a_tag.get_text(strip=True) and not a_tag.find('img'):
        a_tag.decompose()

fout.write("---"+"\n")

links = soup.find_all('h2')
for link in links:
    fout.write("title: '"+link.get_text()+"'\n")
    break

dd=None
m=re.search(r'/20\d{2}/\d{2}/', content)
if m:
    dd=re.findall(r'\d+',m[0])
if dd:
    fout.write("date: "+dd[0]+"-"+dd[1]+"-01"+"\n")
else:
    fout.write("date: 2000-01-01"+"\n")


fout.write("tags:"+"\n")
links = soup.find_all('a', rel='category tag')
for link in links:
    fout.write("  - "+link.get_text().lower()+"\n")

img_tags = soup.find_all('img')
for img_tag in img_tags:
    if img_tag and "soulytion.de/" in img_tag['src'] and img_tag['src'][-4:]==".png":
        path="\\\\wsl.localhost\\Debian\\home\\steffen\\soulytion.de\\"+"\\".join(img_tag['src'].split("/")[3:])
        try:
            shutil.copy2(path, "./")
            image_path = img_tag['src'].split("/")[-1]
            fout.write("image: "+image_path+"\n")
            break
        except:
            print("could not find ", path)
            continue

post = soup.find(class_=["entry","hentry"])
p_tags = post.find_all('p')
for link in p_tags:
    link_ = link.find('p')
    if link_:
        link = link_
    fout.write("excerpt: '"+link.get_text()[:500]+"'\n")
    break


fout.write("---"+"\n")


post = soup.find(class_=["entry","hentry"])

target_element = post.find(class_='meta_tags')
if target_element:
    for tag in target_element.find_all_next():
        tag.decompose()
    target_element.decompose()

a_tags = soup.find_all('a')
if a_tags:
    for a_tag in a_tags:
        if a_tag['href'][-4:]!=".png" or not "soulytion.de/" in a_tag['href']:
            continue
        path0="\\\\wsl.localhost\\Debian\\home\\steffen\\soulytion.de\\"+"\\".join(a_tag['href'].split("/")[3:])
        path=re.sub(r'-\d+x\d+', '', path0)
        path=re.sub(r'.thumbnail', '', path)
        try:
            #fout.write("try copy "+path)
            shutil.copy2(path, "./")
        except:
            #fout.write("try copy "+path0+" instead")
            try:
                shutil.copy2(path0, path)
                shutil.copy2(path, "./")
            except:
                a_tag["href"]=""
                continue
        image_path = path.split("\\")[-1]
        #image_path = img_tag['src'].split("/")[-1]
        #fout.write("use image "+image_path)
        new_format = f"{{% image \"{image_path}\", \"linkonly\" %}}"
        a_tag["href"]=new_format



img_tags = soup.find_all('img')
if img_tags:
    for img_tag in img_tags:
        path0="\\\\wsl.localhost\\Debian\\home\\steffen\\soulytion.de\\"+"\\".join(img_tag['src'].split("/")[3:])
        path=re.sub(r'-\d+x\d+', '', path0)
        path=re.sub(r'.thumbnail', '', path)
        print("IMG:"+path)
        #fout.write(path)
        if not "soulytion.de/" in img_tag['src']:
            print("no soulytion in ", img_tag['src'])
            continue
        try:
            #fout.write("try copy "+path)
            shutil.copy2(path, "./")
        except:
            print("try copy "+path0+" instead")
            try:
                shutil.copy2(path0, path)
                shutil.copy2(path, "./")
            except:
                print("copy failed")
                img_tag.replace_with("")
                continue
        image_path = path.split("\\")[-1]
        #image_path = img_tag['src'].split("/")[-1]
        print("use image "+image_path)
        new_format = f"{{% image \"{image_path}\", \".\" %}}"
        img_tag.replace_with(new_format)



post.extract()
post = post.find('p')
fout.write(post.decode_contents())

fout.close()
