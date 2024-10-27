import pickle
import numpy as np

ohe_sex = pickle.load(open('models/ohe_sex.pkl','rb'))
ohe_embarked = pickle.load(open('models/ohe_embarked.pkl','rb'))
clf = pickle.load(open('models/clf.pkl','rb'))

def predict(Pclass, gender, age, SibSp, Parch, Fare, Embarked):
    # print('received from frontend >', Pclass, gender, age, SibSp, Parch, Fare, Embarked)
    user_input = np.array([Pclass, gender, age, SibSp, Parch, Fare, Embarked], dtype=object).reshape(1,7)
    # np.array([...], dtype=object): Creates a 1-dimensional NumPy array with mixed data types. Using dtype=object allows the array to contain elements of different types, such as integers, strings, and floats, within the same array.
    # .reshape(1,7): Reshapes the array into a 2-dimensional array with 1 row and 7 columns, making it suitable for feeding into a model that expects this shape for a single sample input.
    print("user_input >", user_input, type(user_input))
    user_input_sex = ohe_sex.transform(user_input[:,1].reshape(1,1))
    print("user_input_sex >", user_input_sex, type(user_input_sex))
    user_input_embarked = ohe_embarked.transform(user_input[:,-1].reshape(1,1))
    print("user_input_embarked >", user_input_embarked, type(user_input_embarked))
    user_input_age = user_input[:,2].reshape(1,1)
    print("user_input_age >", user_input_age, type(user_input_age))
    user_input_transformed = np.concatenate((user_input[:,[0,3,4,5]], user_input_age, user_input_sex.toarray(), user_input_embarked.toarray()), axis=1)
    print('user_input_transformed shape >', user_input_transformed.shape)
    result = clf.predict(user_input_transformed)
    print('result >', result, type(result))

    if result[0] == 0:
        return "This person could NOT survive in the titanic."
    else:
        return "This person could survive in the titanic."
