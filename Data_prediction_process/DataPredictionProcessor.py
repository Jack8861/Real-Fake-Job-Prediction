import joblib
from os import listdir


class PredictionProcess:
    """
    This class handles the whole prediction process
    - it finds the probability prediction of output by each value or feature
    - uses those values to predict the class or final output

    by: syed rahim saqib
    version: 1
    """

    def __init__(self, data):
        self.proba_model_path = "Probability_finding_models"
        self.clf_model_path = "Classifier_model/classifier.joblib"
        self.data = {}
        self.data['title'] = data['title']
        self.data['location'] = data['location']
        self.data['department'] = data['department']
        self.data['salary_range'] = data['salary_range']
        self.data['company_profile'] = data['company_profile']
        self.probability_list = []

    def find_probabilities(self):
        """
        This method
        - loads the models (pipeline -[CountVectorizer, LogisticRegression])
        - uses them to get the probability prediction of each of the values/features
        returns: probabilities

        by: syed rahim saqib
        version: 1
        """
        try:
            proba_model_files = [f for f in listdir(self.proba_model_path)]
            for filename in proba_model_files:
                # get feature name from filename
                featureName = filename.split(" ")[0]
                # load the vector
                prob_predictor = joblib.load(self.proba_model_path + "/" + filename)
                exec("self.probability_list.append( list(prob_predictor.predict_proba([self.data['%s']]))[0][1] )" % featureName)

            return
        except Exception as e:
            print(e)

    def get_prediction(self):
        """
        This method
        - loads the final classifier model(knn)
        - predicts the output/class

        returns: prediction

        by: syed rahim saqib
        version: 1
        """
        try:
            clf = joblib.load(self.clf_model_path)
            prediction = clf.predict([self.probability_list])[0]

            return prediction
        except Exception as e:
            print(e)

