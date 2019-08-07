import time
import win32gui
import win32con


def windows_upload(filename):
    # 与windows交互
    dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口
    time.sleep(1)

    # 找到窗口
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
    edit = win32gui.FindWindowEx(comboBox, 0, "Edit", None)  # 四级
    button = win32gui.FindWindowEx(dialog, 0, "Button", None)  # 四级
    time.sleep(1)

    # 操作
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filename)  # 发送文件路径
    time.sleep(1)

    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
