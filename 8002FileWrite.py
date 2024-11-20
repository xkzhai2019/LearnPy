with open("fileRead.txt","w") as f:
    f.write("我是中国人\n")
    f.write("我住在苏州\n")


# with open("fileRead.txt","w") as f:
#    f.write("苏州是个宜居的城市\n")
#    f.write("但是苏州的就业机会不多\n")


# "a": 追加模式写入
with open("fileRead.txt","a") as f:
    f.write("苏州是个宜居的城市\n")
    f.write("但是苏州的就业机会不多\n")
