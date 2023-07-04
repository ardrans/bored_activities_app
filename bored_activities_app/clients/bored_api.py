import requests
BOARD_URL = 'https://www.boredapi.com/api/activity'
class BoardedApi:

    @staticmethod
    def get_random_activity(activity_type:str):
        params = {
            "type":activity_type
        }
        response = requests.get(BOARD_URL,params = params)
        if response.ok:
            return response.json()

    @staticmethod
    def get_activities(activity_type:str,limit:int = 10)->list:
        activities =  []
        for i in range(0,limit):
            activities.append(BoardedApi.get_random_activity(activity_type))
        return activities

if __name__ == '__main__':
    activities_ = BoardedApi.get_activities('education')



