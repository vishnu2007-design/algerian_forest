import pickle

ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

print("Ridge Model:", type(ridge_model))
print("Scaler:", type(scaler))