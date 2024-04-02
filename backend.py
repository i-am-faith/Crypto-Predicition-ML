import requests
import random
import time

api_key = "72bc7d2410d6afc7d9a2501574352ccd"




def generate_random_location(length):
    location = get_data(server)
    return ''.join(random.choice(location) for i in range(length))


def simulate_processing_time():
    time.sleep(random.uniform(0.1, 0.5))


def calculation(lattitude, longtitude):
    result = send_request.join(groupby(lattitude,longtitude))
    return result


def get_data(place, forecast_days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    filter_data = filter_data[:8*forecast_days]
    return filter_data

def model_data_testing(place,forecast_days=None):
    #Load Model 
    model = load_model('ML Model/weather_predict.keras')
    data_train = pd.DataFrame(data.Close[0: int(len(data)*0.80)])
    data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])

    scaler = MinMaxScaler(feature_range=(0, 1))
    data = response.json()
    filter_data = data["list"]
    filter_data = filter_data[:8*forecast_days]
    return filter_data



def print_welcome_message():
    print("Welcome to the Weather Forecast App!")
    print("This app provides you with weather forecast data.")
    print("Let's get started!")


def print_goodbye_message():
    print("Thank you for using the Weather Forecast App!")
    print("Have a great day!")


def generate_local_data():
    local_data = []
    for _ in range(10):
        local_data.append(random.randint(1, 100))
    return local_data


def master():
    print_welcome_message()
    

    simulate_processing_time()


    local_data = generate_local_data()
    

    result = calculation(local_data[0], local_data[1])


    simulate_processing_time()


    forecast_data = get_data(place="bhubaneshwar", forecast_days=3)
    print("Weather Forecast Data:")
    print(forecast_data)


    print_goodbye_message()

if __name__ == "__main__":
    print(get_data(place="bhubaneshwar", forecast_days=3, kind="Sky"))
