import requests

BASE="http://127.0.0.1:5000/"

def result(response):
    res = response.status_code
    if(res==200):
        print(response.text, "with status code ", res)
    elif(res==400):
        print(response.text, "Status code is ", res)
    else:
        print(response.text, "Status code is ", res)


#TESTING CREATION OF DATA IN DATABASE
response=requests.patch(BASE+"Song",{"id":1,"nameOfSong":"SONG1","durationOfSong":10,"uploadTime":"24/21/2021"})
result(response)
input()
response=requests.patch(BASE+"Podcast",{"id":1,"nameOfPodcast":"PODCAST1","durationOfPodcast":20,"uploadTime":"25/21/2021","host":"Host1"})
result(response)
input()
response=requests.patch(BASE+"Audiobook",{"id":1,"nameOfAudiobook":"AUDIOBOOK1","durationOfAudiobook":40,"uploadTime":"26/21/2021","narrator":"Narrator1","author":"Author1"})
result(response)
input()

response=requests.patch(BASE+"Song",{"id":2,"nameOfSong":"SONG2","durationOfSong":20,"uploadTime":"23/21/2021"})
result(response)
input()
response=requests.patch(BASE+"Podcast",{"id":2,"nameOfPodcast":"PODCAST2","durationOfPodcast":40,"uploadTime":"22/21/2021","host":"Host2","participants":"Participant1, Participant2"})
result(response)
input()
response=requests.patch(BASE+"Audiobook",{"id":2,"nameOfAudiobook":"AUDIOBOOK2","durationOfAudiobook":30,"uploadTime":"24/21/2021","narrator":"Narrator2","author":"Author2"})
result(response)
input()


#TESTING FETCHING OF DATA FROM DATABASE
response=requests.get(BASE+"Song/1")
result(response)
input()
response=requests.get(BASE+"Song")
result(response)
input()
response=requests.get(BASE+"Podcast/2")
result(response)
input()
response=requests.get(BASE+"Podcast")
result(response)
input()
response=requests.get(BASE+"Audiobook/1")
result(response)
input()
response=requests.get(BASE+"Audiobook")
result(response)
input()


#TESTING UPDATION OF DATA IN DATABASE
response=requests.put(BASE+"Song/2",{"nameOfSong":"SONG12","durationOfSong":110,"uploadTime":"24/21/2021"})
result(response)
input()
response=requests.put(BASE+"Podcast/1",{"nameOfPodcast":"PODCAST3","durationOfPodcast":40,"uploadTime":"25/21/2021","host":"Host3"})
result(response)
input()
response=requests.put(BASE+"Audiobook/2",{"nameOfAudiobook":"AUDIOBOOK21","durationOfAudiobook":80,"uploadTime":"26/21/2021","narrator":"Narrator21","author":"Author21"})
result(response)
input()


#TESTING DELETION OF DATA FROM DATABASE
response=requests.delete(BASE+"Song/2")
result(response)
input()
response=requests.delete(BASE+"Podcast/1")
result(response)
input()
response=requests.delete(BASE+"Audiobook/2")
result(response)
input()


#PERFORMING SOME NEGATIVE TEST SCENARIOS
response=requests.patch(BASE+"Songs",{"id":1,"nameOfSong":"SONG1","durationOfSong":10,"uploadTime":"24/21/2021"})
result(response)
input()
response=requests.get(BASE+"Podcast/5")
result(response)
input()
response=requests.get(BASE+"Pod/1")
result(response)
input()