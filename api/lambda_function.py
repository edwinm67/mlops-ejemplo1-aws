import pickle
import json

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("transformer.pkl", "rb") as f:
    transformer = pickle.load(f)

def lambda_handler(event, context):
    input_data = json.loads(event["body"])["input"]
    X_input = transformer.transform([input_data])
    prediction = model.predict(X_input)
    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": prediction.tolist()})
    }
