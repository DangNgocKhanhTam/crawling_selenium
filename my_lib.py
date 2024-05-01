import requests
def write_txt(filename, list_data): 
    with open ( filename, 'w', encoding='utf-8') as f: 
        f.writelines(list_data)


def read_txt(file_name): 
    with open(file_name, 'r', encoding='utf-8') as f: 
        list_data = f.readlines()
        return list_data
        
def dowload_image( image_link, image_name): 
    with open(image_name, 'wb') as f: 
        image_content = requests.get(image_link, verify= False).content
        f.write(image_content)
        print('---> Wrote:',image_name )