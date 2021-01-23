import os
import shutil
import tkinter as tk
from tkinter import filedialog


class Encry:
    def __init__(self):
        self.input_name = \
            '1、jpg加密\n' \
            '2、jpg解密\n' \
            '3、mp4加密\n' \
            '4、mp4解密\n' \
            '5、删除操作\n' \
            '请输入指令：'

    def jpg2bit(self, filepath, datapath):
        filename_list = os.listdir(filepath)

        for f in filename_list:
            if (f.split('.'))[1] == 'jpg':
                img = filepath + f
                dataname = (f.split('.'))[0]

                with open(img, "rb") as f1, open('%s/%s.bin' % (datapath, dataname), 'wb')as f2:
                    img_bit = f1.read()
                    f2.write(img_bit)
            else: pass

        return 0 if len(os.listdir(datapath)) > 0 else 1

    def mp42bit(self, filepath, datapath):

        filename_list = os.listdir(filepath)

        for f in filename_list:

            img = filepath + f
            dataname = (f.split('.'))[0]

            with open(img, "rb") as f1, open('%s/%s.bin' % (datapath, dataname), 'wb')as f2:
                img_bit = f1.read()
                f2.write(img_bit)

        return 0 if len(os.listdir(datapath)) > 0 else 1

    def bit2jpg(self, datapath, savepath):
        dataname_list = os.listdir(datapath)

        for dataname in dataname_list:
            data = datapath + dataname
            savename = (dataname.split('.'))[0]
            # print(data)
            with open(data, "rb") as f1, open('%s/%s.jpg' % (savepath, savename), 'wb')as f2:
                img_bit = f1.read()
                f2.write(img_bit)

        return 0 if len(os.listdir(savepath)) > 0 else 1

    def bit2mp4(self, datapath, savepath):

        dataname_list = os.listdir(datapath)

        for dataname in dataname_list:
            data = datapath + dataname
            savename = (dataname.split('.'))[0]
            # print(data)
            with open(data, "rb") as f1, open('%s/%s.mp4' % (savepath, savename), 'wb')as f2:
                img_bit = f1.read()
                f2.write(img_bit)

        return 0 if len(os.listdir(savepath)) > 0 else 1

    def del_file(self, filepath):

        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    def window(self):
        root = tk.Tk()
        root.withdraw()
        Folderpath = filedialog.askdirectory()

        return Folderpath

    def main_do(self):

        instruction = input(self.input_name)

        if instruction == '1':
            print('请选择加密对象所在文件夹')
            img_path = self.window()
            if self.jpg2bit('%s/' % img_path, 'data/img/') == 0:
                print('完成加密')
        elif instruction == '2':
            print('请选择解密对象所在文件夹')
            save_path = self.window()
            if self.bit2jpg('data/img/', '%s/'%save_path) == 0:
                print('完成解密')
        elif instruction == '3':
            print('请选择加密对象所在文件夹')
            video_path = self.window()
            if self.mp42bit('%s/'%video_path, 'data/video/') == 0:
                print('完成加密')
        elif instruction == '4':
            print('请选择解密对象所在文件夹')
            save_path = self.window()
            if self.bit2mp4('data/video/', '%s/'%save_path) == 0:
                print('完成解密')
        elif instruction == '5':
            print('请选择删除对象所在文件夹')
            delete_path = self.window()
            self.del_file(delete_path)
            print('删除完成')


if __name__ == '__main__':
    try:
        a = Encry()
        a.main_do()
    except Exception as e:
        print(e)