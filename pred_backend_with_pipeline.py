import pickle
import numpy as np

pipe = pickle.load(open('models/pipe.pkl','rb'))

def predict(Pclass, gender, age, SibSp, Parch, Fare, Embarked):
    user_input = np.array([Pclass, gender, age, SibSp, Parch, Fare, Embarked], dtype=object).reshape(1,7)
    print("user_input >", user_input, type(user_input))
    result = pipe.predict(user_input) 
    print('result >', result, type(result))

    if result[0] == 0:
        return "This person could NOT survive in the titanic."
    else:
        return "This person could survive in the titanic."