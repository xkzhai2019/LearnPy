with open("fileRead.txt","r+") as f:
    f.seek(0,2)
    text = ["我是中国人\n","我住在苏州\n"]
    f.writelines(text)


# with open("fileRead.txt","w") as f:
#    f.write("苏州是个宜居的城市\n")
#    f.write("但是苏州的就业机会不多\n")


with open("fileRead.txt","w") as f:
    f.write("苏州是个宜居的城市\n")
    f.write("但是苏州的就业机会不多\n")
