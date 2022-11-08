from googleapiclient.discovery import build

youtube = build(serviceName='youtube', version='v3', developerKey='API_KEY')

if __name__ == '__main__':
    api_request = youtube.channels().list(part='id,snippet,statistics,status', id='UCfiwzLy-8yKzIbsmZTzxDgw')
    api_response = api_request.execute()
    print(api_response)

    api_request = youtube.videos().list(part='id,snippet,statistics,status', id='C_tb3AOj2qg')
    api_response = api_request.execute()
    print(api_response)
