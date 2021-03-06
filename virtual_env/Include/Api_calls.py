from flask import Blueprint,jsonify,g
from flask_restful import Api, Resource, reqparse
from Include.db import *
import sqlite3



api_calls_create = Blueprint('api_calls_create', __name__)
api_calls_delete = Blueprint('api_calls_delete', __name__)
api_calls_get = Blueprint('api_calls_get', __name__)
api_calls_put = Blueprint('api_calls_put', __name__)




class Api_calls_create(Resource):
    def patch(self,filetype):
        if(filetype=="Song"):
            audio_update_args = reqparse.RequestParser()
            audio_update_args.add_argument("id", type=int, help="ID of the Song is mandatory", required=True)
            audio_update_args.add_argument("nameOfSong", type=str, help="Name of Song is mandatory", required=True)
            audio_update_args.add_argument("durationOfSong", type=int, help="Duration of song is mandatory", required=True)
            audio_update_args.add_argument("uploadTime", type=str, help="Upload Time of song is mandatory",required=True)
            args = audio_update_args.parse_args()
            cmd="INSERT INTO Song VALUES( {id}, '{song}', {duration}, '{uploadtime}' );".format(id=args['id'],song=args['nameOfSong'],duration=args['durationOfSong'], uploadtime=args['uploadTime'])
            res = executeQuery(cmd)
            if(res):
                data = "Query is successfully executed"
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        elif(filetype=="Podcast"):
            audio_update_args = reqparse.RequestParser()
            audio_update_args.add_argument("id", type=int, help="ID of the Song is mandatory", required=True)
            audio_update_args.add_argument("nameOfPodcast", type=str, help="Name of Podcast is mandatory", required=True)
            audio_update_args.add_argument("durationOfPodcast", type=int, help="Duration of podcast is mandatory",
                                           required=True)
            audio_update_args.add_argument("uploadTime", type=str, help="Upload Time of podcast is mandatory",
                                           required=True)
            audio_update_args.add_argument("host", type=str, help="Host name is mandatory",
                                           required=True)
            audio_update_args.add_argument("participants", type=str)

            args = audio_update_args.parse_args()

            cmd = "INSERT INTO Podcast VALUES( {id}, '{podcastName}', {duration}, '{uploadtime}', '{host}', '{participants}' );".format(id=args['id'],podcastName=args['nameOfPodcast'],duration=args['durationOfPodcast'],uploadtime=args['uploadTime'],host=args['host'],participants=args['participants'])
            res = executeQuery(cmd)
            if (res):
                data = "Query is successfully executed"
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        elif(filetype=="Audiobook"):
            audio_update_args = reqparse.RequestParser()
            audio_update_args.add_argument("id", type=int, help="ID of the Audiobook is mandatory", required=True)
            audio_update_args.add_argument("nameOfAudiobook", type=str, help="Title of the Audiobook is mandatory",
                                           required=True)
            audio_update_args.add_argument("durationOfAudiobook", type=int, help="Duration of the Audiobook is mandatory",
                                           required=True)
            audio_update_args.add_argument("uploadTime", type=str, help="Upload Time of the Audiobook is mandatory",
                                           required=True)
            audio_update_args.add_argument("author", type=str, help="Author's name is mandatory",
                                           required=True)
            audio_update_args.add_argument("narrator", type=str, help="Narrator's name is mandatory",
                                           required=True)

            args = audio_update_args.parse_args()

            cmd = "INSERT INTO Audiobook VALUES( {id}, '{nameOfAudiobook}', '{author}', '{narrator}',  {duration}, '{uploadtime}' );".format(
                id=args['id'], nameOfAudiobook=args['nameOfAudiobook'], duration=args['durationOfAudiobook'],
                uploadtime=args['uploadTime'], author=args['author'], narrator=args['narrator'])

            res = executeQuery(cmd)
            if (res):
                data = "Query is successfully executed"
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        else:
            data="Invalid request/Server error"
            response = jsonify(data)
            response.status_code = 500
            return response




class Api_calls_delete(Resource):

    def delete(self, filetype, id):
        if (filetype == "Song"):
            cmd = "DELETE FROM Song WHERE ID is {id};".format(id=id)
            res = executeQuery(cmd)
            if (res):
                data = "Query is successfully executed"
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        elif (filetype == "Podcast"):
            cmd = "DELETE FROM Podcast WHERE ID is {id};".format(id=id)
            res = executeQuery(cmd)
            if (res):
                data = "Query is successfully executed"
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        elif (filetype == "Audiobook"):
            cmd = "DELETE FROM Audiobook WHERE ID is {id};".format(id=id)
            res = executeQuery(cmd)
            if (res):
                data = "Query is successfully executed"
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        else:
            data = "Invalid request/Server error"
            response = jsonify(data)
            response.status_code = 500
            return response




class Api_calls_get(Resource):
    def get(self, filetype, id=None):
        if (filetype == "Song"):
            if id:
                cmd = "SELECT * FROM Song WHERE ID is {id};".format(id=id)
            else:
                cmd = "SELECT * FROM Song;"
            res = getQueryDate(cmd)
            if (res):
                data = res
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        elif (filetype == "Podcast"):
            if id:
                cmd = "SELECT * FROM Podcast WHERE ID is {id};".format(id=id)
            else:
                cmd = "SELECT * FROM Podcast;"
            res = getQueryDate(cmd)
            if (res):
                data = res
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        elif (filetype == "Audiobook"):
            if id:
                cmd = "SELECT * FROM Audiobook WHERE ID is {id};".format(id=id)
            else:
                cmd = "SELECT * FROM Audiobook;"
            res = getQueryDate(cmd)
            if (res):
                data = res
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        else:
            data = "Invalid request/Server error"
            response = jsonify(data)
            response.status_code = 500
            return response





class Api_calls_put(Resource):
    def put(self, filetype, id):
        if (filetype == "Song"):
            audio_update_args = reqparse.RequestParser()
            audio_update_args.add_argument("nameOfSong", type=str, help="Name of Song is mandatory", required=True)
            audio_update_args.add_argument("durationOfSong", type=int, help="Duration of song is mandatory",
                                           required=True)
            audio_update_args.add_argument("uploadTime", type=str, help="Upload Time of song is mandatory",
                                           required=True)
            args = audio_update_args.parse_args()
            cmd = "UPDATE Song SET SONG_NAME='{song}', DURATION_IN_SEC={duration}, UPLOADED_TIME='{uploadtime}' WHERE ID={id};".format(id=id,
                                                                                                  song=args[
                                                                                                      'nameOfSong'],
                                                                                                  duration=args[
                                                                                                      'durationOfSong'],
                                                                                                  uploadtime=args[
                                                                                                      'uploadTime'])
            res = executeQuery(cmd)
            if (res):
                data = "Query is successfully executed"
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        elif (filetype == "Podcast"):
            audio_update_args = reqparse.RequestParser()
            audio_update_args.add_argument("nameOfPodcast", type=str, help="Name of Podcast is mandatory",
                                           required=True)
            audio_update_args.add_argument("durationOfPodcast", type=int, help="Duration of podcast is mandatory",
                                           required=True)
            audio_update_args.add_argument("uploadTime", type=str, help="Upload Time of podcast is mandatory",
                                           required=True)
            audio_update_args.add_argument("host", type=str, help="Host name is mandatory",
                                           required=True)
            audio_update_args.add_argument("participants", type=str)

            args = audio_update_args.parse_args()

            cmd = "UPDATE Podcast SET PODCAST_NAME = '{podcastName}', DURATION_IN_SEC = {duration}, UPLOADED_TIME = '{uploadtime}', HOST='{host}', PARTICIPANTS='{participants}' WHERE ID={id};".format(
                id=id, podcastName=args['nameOfPodcast'], duration=args['durationOfPodcast'],
                uploadtime=args['uploadTime'], host=args['host'], participants=args['participants'])
            res = executeQuery(cmd)
            if (res):
                data = "Query is successfully executed"
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        elif (filetype == "Audiobook"):
            audio_update_args = reqparse.RequestParser()
            audio_update_args.add_argument("nameOfAudiobook", type=str, help="Title of the Audiobook is mandatory",
                                           required=True)
            audio_update_args.add_argument("durationOfAudiobook", type=int,
                                           help="Duration of the Audiobook is mandatory",
                                           required=True)
            audio_update_args.add_argument("uploadTime", type=str, help="Upload Time of the Audiobook is mandatory",
                                           required=True)
            audio_update_args.add_argument("author", type=str, help="Author's name is mandatory",
                                           required=True)
            audio_update_args.add_argument("narrator", type=str, help="Narrator's name is mandatory",
                                           required=True)

            args = audio_update_args.parse_args()

            cmd = "UPDATE Audiobook SET AUDIOBOOK_TITLE='{nameOfAudiobook}', AUDIOBOOK_AUTHOR='{author}', AUDIOBOOK_NARRATOR='{narrator}',  DURATION_IN_SEC={duration}, UPLOADED_TIME='{uploadtime}' WHERE ID={id}".format(
                id=id, nameOfAudiobook=args['nameOfAudiobook'], duration=args['durationOfAudiobook'],
                uploadtime=args['uploadTime'], author=args['author'], narrator=args['narrator'])

            res = executeQuery(cmd)
            if (res):
                data = "Query is successfully executed"
                response = jsonify(data)
                response.status_code = 200
                return response
            else:
                data = "Query is not executed successfully"
                response = jsonify(data)
                response.status_code = 400
                return response

        else:
            data = "Invalid request/Server error"
            response = jsonify(data)
            response.status_code = 500
            return response