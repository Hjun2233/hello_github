import openpyxl

class readExcel:
    def read_excel(self):
        # 通过文件得到一个工作薄，参数是文件名，如果有路径要写绝对路径
        wb = openpyxl.load_workbook("../excel/exc.xlsx", data_only=True)
        # 获取sheet表格
        sheet = wb['tl']
        # 获取sheet中所有的数据
        data = list(sheet.values)[1:]
#         # 将列表还转化为字典
#         dict_list = []
#         for i in range(1, len(data)):
#             dict_list.append(list(zip(data[0], data[i])))#zip函数，合并两个元组
        return data
    
# if __name__ == '__main__':
#     print(readExcel().read_excel())