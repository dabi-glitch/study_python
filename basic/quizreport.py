
for i in range(1,3):
    with open(str(i)+"주차.txt","w",encoding="utf8") as study_file:
        study_file.write("{} 주차 업무 보고-".format(i))
        study_file.write("\n부서 : ")
        study_file.write("\n이름 : ")
        study_file.write("\n업무 요약 : ")
