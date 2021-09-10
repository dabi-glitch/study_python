#pickle
#사용하고 있는 데이터를 파일 형태로 저장하고 전송, 수신

import pickle
# profile_file = open("profile.pickle","wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장한다. 
# profile_file.close()

#데이터를 pickle을 이용해서 불러오기
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) #파일에 있는 정보를 profile에 불러옴
print(profile)
profile_file.close()